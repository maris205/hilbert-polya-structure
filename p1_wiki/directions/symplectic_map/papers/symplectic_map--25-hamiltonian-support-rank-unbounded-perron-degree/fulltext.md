---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--25-hamiltonian-support-rank-unbounded-perron-degree"
canonical_tex: "symplectic_map/papers/25-hamiltonian-support-rank-unbounded-perron-degree/paper/main.tex"
canonical_pdf: "symplectic_map/papers/25-hamiltonian-support-rank-unbounded-perron-degree/paper/main.pdf"
source_sha256: "4d8ac64803ecae76809461e183c72349e7bcab1ad1fac3e4167fe9735860eea2"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Sharp Support-Rank Bounds and Unbounded Perron Degree in Hamiltonian Product Shears

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/25-hamiltonian-support-rank-unbounded-perron-degree>)
- [规范 TeX](<../../../../../symplectic_map/papers/25-hamiltonian-support-rank-unbounded-perron-degree/paper/main.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/25-hamiltonian-support-rank-unbounded-perron-degree/paper/main.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/25-hamiltonian-support-rank-unbounded-perron-degree/notes/CLAIMS_EVIDENCE_MATRIX.md>)
- [BibTeX](<../../../../../symplectic_map/papers/25-hamiltonian-support-rank-unbounded-perron-degree/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every integer $d\geq2$ and every field of characteristic zero, we construct an explicit Hamiltonian product shear $F$ in $2d$ variables whose ordinary iterate degrees satisfy the exact fixed-coordinate identity $\deg(F^n)=e_1^{\mathsf{T}}C^n\mathbf{1}$ for all $n\geq0$. Literal polynomial iteration contains mixed support faces and two carried coordinate blocks, so a selected matrix recursion alone would give only an upper bound. Two nested strict chambers, together with survival of leading forms in the nonnegative coefficient semiring, prove that the selected recursion is the actual polynomial recursion and that $q_1$ is uniquely degree-maximal precisely at positive iterates. The matrix $C$ has an irreducible degree-$d$ characteristic polynomial, its Perron root is the first dynamical degree and has algebraic degree $d$, and the visible scalar degree sequence has minimal rational constant-coefficient recurrence order $d$ both from the start and eventually. More generally, a support-row factorization bounds the nonunit characteristic degree by the stacked selected row rank; the constructed family has rank $d$ and attains this bound for every $d\geq2$.
author:
- Anonymous
bibliography:
- references.bib
title: 'Sharp Support-Rank Bounds and Unbounded Perron Degree in Hamiltonian Product Shears'
```

## Markdown 正文

# Introduction and theorem map {#sec:introduction}

## Problem anchor and obstruction

A degree matrix extracted from selected monomials can be informative without yet describing the ordinary degree of a polynomial iterate. Three assertions must be separated. First, a max-plus or linear selection calculation may propose a matrix upper recursion. Second, the literal composition must select the proposed face in every component, defeat coordinates carried from earlier half-steps, and retain a nonzero leading form. Third, even when a matrix formula is exact, the scalar sequence visible in one coordinate can have smaller recurrence order than the matrix size if the initial state or observation covector misses part of the spectrum. The present construction resolves these three issues separately.

There is also a structural question. Selected gradient rows may span a space much smaller than the ambient one. A common kernel then produces a unit sector in the complete-step matrix, suggesting that the row-span rank should bound the nonunit characteristic degree. Such a ceiling becomes informative here only after a gradient-compatible Hamiltonian family attains it while preserving exact ordinary degrees. The central result is therefore a conjunction: a rank law, a sharp all-$d$ family, exact polynomial visibility, arithmetic irreducibility, and scalar minimality.

## Bounded context and gap

Affine-triangular polynomial automorphisms provide a broad setting in which dynamical degrees, matrix or valuation descriptions, and weak-Perron realization are studied; dimension four has also received a dedicated algebraic-degree analysis [@BvS; @SS]. Spectral interpretations place dynamical degrees in a wider algebraic framework, while work on twisted rational maps develops a related relative setting [@DF; @AX]. These results motivate the distinction between a spectral prediction and a degree sequence but do not provide the support-face verification needed below.

Hamiltonian position and momentum shears arise naturally in work on generation and approximation of Hamiltonian maps, and straight-line Hamiltonian flows supply another geometric shear context [@BT; @KL]. Higher-dimensional polynomial and birational examples show how varied degree growth can be outside the present support grammar [@Des]. Finally, the finite-field binomial criterion used for arithmetic provenance is recorded by Heyman and Shparlinski [@HS]. These references provide context and standard arithmetic provenance only: invertibility, symplecticity, chamber invariance, carry control, noncancellation, exact degree visibility, irreducibility in the chosen parameters, scalar minimality, and support-rank sharpness are all established directly here.

## Headline theorem and reader promise

Let $K$ be a field of characteristic zero. For each $d\geq2$, Section [4](#sec:parameters){reference-type="ref" reference="sec:parameters"} chooses data in the order $$d\longrightarrow p,c\longrightarrow a_1<\cdots<a_d\longrightarrow b,R_0.$$ Here $p\equiv1\pmod d$ is prime, $c$ generates $\mathbb{F}_{p}^\times$, the residues of the $a_i$ are exactly the $d$th roots of unity, and, with $S_a=\sum_i a_i$ and $M=a_d$, $$a_1+1>4d,\qquad bd\equiv1-(-1)^dc\pmod p,\qquad
R_0=1+\frac{2M}{bS_a},$$ $$b\geq2,\qquad R_0^2<2,\qquad
b(a_i-a_1)S_a>a_i^2R_0-a_1^2\quad(2\leq i\leq d).$$ Define $$V(q)=\prod_{j=1}^d q_j^2+\sum_{i=1}^d q_i^{a_i+1},
\qquad W(p)=\prod_{j=1}^d p_j^b,$$ $$S_V(q,p)=(q,p+\nabla V(q)),\qquad
T_W(q,p)=(q+\nabla W(p),p),\qquad F=T_W\circ S_V,$$ and put $$D=\mathop{\mathrm{diag}}(a_1,\ldots,a_d),\quad J=\mathbf{1}\mathbf{1}^{\mathsf{T}},\quad
B_0=bJ-I_d,\quad C=B_0D=b\mathbf{1}a^{\mathsf{T}}-D.$$

For every $d\geq2$, the parameters above can be chosen so that all of the following statements hold.

1.  $F$ is a positive integer-coefficient polynomial symplectomorphism of $K^{2d}$.

2.  For every $n\geq0$, $$\deg(F^n)=e_1^{\mathsf{T}}C^n\mathbf{1}.$$ All $2d$ coordinate degrees tie at $n=0$, whereas $q_1$ is the unique degree-maximal coordinate for every $n\geq1$.

3.  The characteristic polynomial $$\chi_C(t)=t^d+\sum_{k=1}^d(1-bk)e_k(a_1,\ldots,a_d)t^{d-k}$$ is irreducible over $\mathbb Q$, and its reduction modulo $p$ is $t^d-c$.

4.  The forward first dynamical degree is $\lambda_1(F)=\rho(C)$, and this Perron algebraic integer has algebraic degree exactly $d$.

5.  The visible sequence $s_n=e_1^{\mathsf{T}}C^n\mathbf{1}$ has minimal rational constant-coefficient recurrence order exactly $d$, both for recurrences valid from $n=0$ and for recurrences valid only eventually.

6.  The selected stacked row rank is $r=d$, and the structural bound in Structural Theorem S is attained.

The structural statement is independent of positivity and of the particular family. Let $$A=-I_N+\mathsf P\mathsf Q,\qquad
B=-I_N+\mathsf R\mathsf S,\qquad C=BA,$$ where $\mathsf P\in K^{N\times\alpha}$, $\mathsf Q\in K^{\alpha\times N}$, $\mathsf R\in K^{N\times\beta}$, and $\mathsf S\in K^{\beta\times N}$. Set $Y=[\mathsf Q^{\mathsf{T}}\ \mathsf S^{\mathsf{T}}]^{\mathsf{T}}$ and $r=\mathop{\mathrm{rank}}Y$. Choose $T_0\in K^{r\times N}$ whose rows form a basis of $\mathop{\mathrm{row}}Y$, write $Y=LT_0$, and define $$U=\begin{bmatrix}\mathsf R\mathsf S\mathsf P-\mathsf P&-\mathsf R\end{bmatrix},
\qquad X=UL.$$

With the preceding compatible dimensions, $$\chi_C(t)=(t-1)^{N-r}\det\bigl((t-1)I_r-T_0X\bigr).$$ The reduced determinant is monic of degree $r$. Consequently, the algebraic multiplicity of $1$ is at least $N-r$ and the nonunit characteristic degree is at most $r$. The reduced determinant may itself vanish at $t=1$, so neither exact unit multiplicity nor a complete rank-only spectral profile is asserted.

For the family of Theorem H, the presentations $$D=-I_d+I_d(D+I_d),\qquad B_0=-I_d+(b\mathbf{1})\mathbf{1}^{\mathsf{T}}$$ have stacked selected row rank $d$. The irreducible degree-$d$ characteristic polynomial has no factor $t-1$. Thus the structural bound is attained existentially for every constructed rank $r=d\geq2$.

## Contributions and non-contributions

The four verifiable outputs are:

1.  an exact ordinary-degree formula for an explicit Hamiltonian product shear in every half-dimension $d\geq2$;

2.  a uniform arithmetic construction for which the visible Perron root has algebraic degree $d$;

3.  exact rational recurrence order $d$ for the scalar degree sequence, both from the start and on every tail; and

4.  a support-row upper law that is attained for every rank occurring in the construction.

The result is not a realization theorem for all Perron or weak-Perron numbers, a classification of polynomial symplectomorphisms, a minimal-dimension or optimal-sparsity statement, or a priority statement. It concerns the displayed positive supports, forward ordinary degree, and characteristic-zero base fields.

## Proof map and organization

Table [1](#tab:proof-map){reference-type="ref" reference="tab:proof-map"} is explanatory: it records where the four proof branches meet and is not mathematical evidence.

::: {#tab:proof-map}
  Branch                 Proof units                                            Output
  ---------------------- ------------------------------------------------------ --------------------------------------------
  Structural             L1 $\rightarrow$ L2, retained through L15              support-row factor and boundary cases
  Construction           L3+L4 $\rightarrow$ L5+L6+L7+L8+L9 $\rightarrow$ L10   exact fixed-$q_1$ ordinary degrees
  Arithmetic--spectral   L3+L11 $\rightarrow$ L12 $\rightarrow$ L13+L14         irreducible Perron degree and scalar order
  Sharpness              L1+L2+L4+L12 $\rightarrow$ L15                         existential rank-$d$ attainment

  : Main-text dependency map.
:::

Section [2](#sec:shears){reference-type="ref" reference="sec:shears"} derives the literal gradient rows. Section [3](#sec:rank){reference-type="ref" reference="sec:rank"} proves the structural factorization, Sections [4](#sec:parameters){reference-type="ref" reference="sec:parameters"}--[5](#sec:degrees){reference-type="ref" reference="sec:degrees"} construct and verify the exact degree orbit, Sections [6](#sec:arithmetic){reference-type="ref" reference="sec:arithmetic"}--[7](#sec:perron){reference-type="ref" reference="sec:perron"} prove arithmetic and scalar minimality, and Section [8](#sec:sharpness){reference-type="ref" reference="sec:sharpness"} joins the branches and states the limitations.

# Hamiltonian product shears, degree profiles, and context {#sec:shears}

## Field, degree, and phase notation

Throughout the family theorem, $K$ is a field of characteristic zero and $$K[q,p]=K[q_1,\ldots,q_d,p_1,\ldots,p_d].$$ For a nonzero polynomial $G$, $\deg G$ denotes ordinary total degree and $\operatorname{LF}(G)$ its top homogeneous form. For a polynomial tuple $G=(G_1,\ldots,G_m)$, set $\deg G=\max_i\deg G_i$. We take $F^0$ to be the identity, hence $\deg(F^0)=1$.

The $q$- and $p$-coordinate tuples of $F^n$ will be denoted $Q^{(n)}$ and $P^{(n)}$. The vector $u_n$ will eventually be proved to equal the degrees of $Q^{(n)}$ at the start of the next $V$-phase. At this point it is only a proposed phase label. After the $V$-half-step the proposed fresh momentum vector is $Du_n$, and after the $W$-half-step the proposed fresh position vector is $B_0Du_n=Cu_n$. Section [5](#sec:degrees){reference-type="ref" reference="sec:degrees"} checks all competing faces and both carried blocks before turning these proposed vectors into equalities.

For a nonzero coordinate tuple with degree vector $u$, an exponent row $\nu=(\nu_1,\ldots,\nu_d)$ assigns the substituted monomial the degree $$\deg\!\left(\prod_j G_j^{\nu_j}\right)=\sum_j\nu_j\deg G_j=\nu^{\mathsf{T}}u.$$ Thus row multiplication records the weight of one literal support monomial. Taking the largest row weight records only a candidate for a sum: a carried coordinate is an additional competitor, and equal top-degree contributions could still interact. The roles of the chambers and leading-form argument are precisely to discharge these two obligations before the row action is treated as an ordinary-degree equality.

The literal composition has an intermediate momentum state. For $n\geq0$, write $\widehat P^{(n)}$ for the momentum tuple after applying $S_V$ to $(Q^{(n)},P^{(n)})$. Direct substitution, before any degree comparison, gives $$\begin{aligned}
\widehat P_i^{(n)}
&=P_i^{(n)}
  +2Q_i^{(n)}\prod_{j\ne i}\bigl(Q_j^{(n)}\bigr)^2
  +(a_i+1)\bigl(Q_i^{(n)}\bigr)^{a_i},\\
Q_i^{(n+1)}
&=Q_i^{(n)}
  +b\bigl(\widehat P_i^{(n)}\bigr)^{b-1}
     \prod_{j\ne i}\bigl(\widehat P_j^{(n)}\bigr)^b,\\
P_i^{(n+1)}&=\widehat P_i^{(n)}.\end{aligned}$$ These are identities in the polynomial ring. They expose the two retained coordinates and the two fresh terms that must be compared later; they do not yet replace those comparisons by a matrix recursion.

We define the forward first dynamical degree by $$\lambda_1(F)=\limsup_{n\to\infty}\deg(F^n)^{1/n}.$$ The exact formula and Perron asymptotics below show that the limsup is a limit for this family.

## Literal gradients and symplecticity

The maps $S_V$ and $T_W$ are polynomial symplectomorphisms. Their literal selected degree matrices are $D$ and $B_0=bJ-I_d$, and their complete selected matrix is $C=B_0D=b\mathbf{1}a^{\mathsf{T}}-D$, which is strictly positive.

Direct differentiation gives $$\frac{\partial V}{\partial q_i}
=2q_i\prod_{j\ne i}q_j^2+(a_i+1)q_i^{a_i},
\qquad
\frac{\partial W}{\partial p_i}
=b p_i^{b-1}\prod_{j\ne i}p_j^b.$$ In the corresponding $d$-dimensional exponent lattices, the literal supports are $$\operatorname{supp}\!\left(\frac{\partial V}{\partial q_i}\right)
=\{\,2\mathbf{1}-e_i,\ a_i e_i\,\},
\qquad
\operatorname{supp}\!\left(\frac{\partial W}{\partial p_i}\right)
=\{\,b\mathbf{1}-e_i\,\}.$$ Taking the dot product with a positive weight vector gives the weighted degree of each displayed monomial. Thus the matrices below record actual exponent rows: derivative coefficients affect the leading forms but not these row weights.

Thus, when a positive weight vector $u$ is assigned to the position coordinates, component $i$ of $\nabla V$ has exactly two support competitors, of weights $$2\sum_{j=1}^d u_j-u_i
\quad\hbox{and}\quad a_i u_i.$$ Selection of the pure spike in every component gives the diagonal matrix $D$. If a positive vector $v$ is assigned to the momentum coordinates, component $i$ of $\nabla W$ has the single monomial weight $$b\sum_{j=1}^d v_j-v_i,$$ whose row matrix is $B_0=bJ-I_d$. Hence the proposed complete-step matrix is $$C=B_0D=b\mathbf{1}a^{\mathsf{T}}-D.$$ Its diagonal and off-diagonal entries are respectively $$C_{ii}=(b-1)a_i>0,\qquad C_{ij}=ba_j>0\quad(i\ne j),$$ so $C$ is strictly positive.

The inverses are subtraction shears, $$S_V^{-1}(q,p)=(q,p-\nabla V(q)),\qquad
T_W^{-1}(q,p)=(q-\nabla W(p),p),$$ and are polynomial. For the standard symplectic form $\omega=\sum_i dq_i\wedge dp_i$, $$\Omega=
\begin{bmatrix}
0&I_d\\
-I_d&0
\end{bmatrix}$$ is its matrix in the ordered coordinates $(q,p)$. Set $H_V=\operatorname{Hess}V$ and $H_W=\operatorname{Hess}W$. The two Jacobians have the lower- and upper-shear forms $$DS_V=
\begin{bmatrix}
I_d&0\\
H_V&I_d
\end{bmatrix},
\qquad
DT_W=
\begin{bmatrix}
I_d&H_W\\
0&I_d
\end{bmatrix}.$$ A direct block multiplication keeps track of the different signs in the two cases: $$DS_V^{\mathsf{T}}\Omega DS_V
=
\begin{bmatrix}
H_V-H_V^{\mathsf{T}}&I_d\\
-I_d&0
\end{bmatrix}
=\Omega,$$ $$DT_W^{\mathsf{T}}\Omega DT_W
=
\begin{bmatrix}
0&I_d\\
-I_d&H_W^{\mathsf{T}}-H_W
\end{bmatrix}
=\Omega.$$ Both equalities use the symmetry of the corresponding Hessian. Equivalently, the additional $dq_i\wedge dq_j$ or $dp_i\wedge dp_j$ contributions cancel in pairs because the coefficient matrix is symmetric while the wedge product is alternating. Thus both shears and their composition are polynomial symplectomorphisms. Their forward coordinate formulas use only variables, addition, multiplication, and positive integer coefficients, so $F$ has positive integer coefficients.

Symplecticity and coefficient positivity enter the later arguments differently. The Hessian calculation proves preservation of $\omega$ from symmetry, independently of coefficient signs. Positivity instead belongs to the displayed forward formulas and supports survival of the selected leading forms. The subtraction formulas establish polynomial invertibility, but their negative terms never enter the forward positive-semiring induction. Thus nothing here asserts that inverse iterates have positive coefficients, use the same selectors, or obey the forward degree recursion. The inverse formulas certify only polynomial automorphism, while symplecticity and forward positivity retain separate proof roles.

## Context without theorem transfer

The maps above are literal position-only and momentum-only Hamiltonian shears. Generation and approximation results for Hamiltonian maps explain why such elementary factors are geometrically natural [@BT]; straight-line Hamiltonian flows give a related affine-integrable setting [@KL]. Neither context establishes which support face controls repeated polynomial composition, and neither is used to infer an ordinary-degree formula.

Likewise, affine-triangular dynamical degrees and their dimension-four specialization [@BvS; @SS], spectral interpretations of dynamical degrees [@DF], higher-dimensional polynomial and birational examples [@Des], and twisted rational-map degrees [@AX] organize neighboring phenomena at different levels of generality. Our argument does not transfer conclusions among those classes. The selected rows above motivate only the abstract rank statement in the next section; the exact orbit remains to be proved from the displayed polynomials.

# Support-row factorization {#sec:rank}

## Dimensions and stacked row space

Let $K$ now be any field. Fix $N\geq0$ and factor widths $\alpha,\beta\geq0$, with $$\mathsf P\in K^{N\times\alpha},\quad
\mathsf Q\in K^{\alpha\times N},\quad
\mathsf R\in K^{N\times\beta},\quad
\mathsf S\in K^{\beta\times N}.$$ For $A=-I_N+\mathsf P\mathsf Q$ and $B=-I_N+\mathsf R\mathsf S$, form $$Y=\begin{bmatrix}\mathsf Q\\ \mathsf S\end{bmatrix}
\in K^{(\alpha+\beta)\times N},\qquad r=\mathop{\mathrm{rank}}Y.$$ Choose $T_0\in K^{r\times N}$ with full row rank and $\mathop{\mathrm{row}}T_0=\mathop{\mathrm{row}}Y$. Then $Y=LT_0$ for some $L\in K^{(\alpha+\beta)\times r}$.

The row basis is only a coordinate system for this factor-through space. Indeed, if $G_0\in\operatorname{GL}_r(K)$ and $T_0'=G_0T_0$, then the same stacked matrix is $Y=L'T_0'$ with $L'=LG_0^{-1}$. Consequently $X'=UL'=XG_0^{-1}$ and $$T_0'X'=G_0(T_0X)G_0^{-1}.$$ The reduced matrices are similar, so their characteristic determinants agree. This check makes the reduced factor independent of the chosen basis of the fixed row space, while neither selecting a preferred presentation nor changing the presentation-dependent value of the stacked rank.

## Factorization and determinant identity

With $C=BA$, set $$U=\begin{bmatrix}\mathsf R\mathsf S\mathsf P-\mathsf P&-\mathsf R\end{bmatrix},
\qquad X=UL.$$ Then $C=I_N+XT_0$ and $$\chi_C(t)=(t-1)^{N-r}\det\bigl((t-1)I_r-T_0X\bigr).$$ The reduced determinant is monic of degree $r$.

The compatible dimensions make the reduction literal: $$U\in K^{N\times(\alpha+\beta)},\qquad
L\in K^{(\alpha+\beta)\times r},\qquad
X=UL\in K^{N\times r},$$ $$XT_0\in K^{N\times N},\qquad
T_0X\in K^{r\times r}.$$ Since $T_0$ has $r$ independent rows, necessarily $0\leq r\leq N$. On column spaces the nonidentity part factors through an $r$-dimensional space: $$K^N\xrightarrow{\ T_0\ }K^r\xrightarrow{\ X\ }K^N.$$ This dimension ledger is also why the two determinants in Lemma L1 have sizes $N$ and $r$, rather than two copies of the ambient size.

Multiplying the two factors gives $$\begin{aligned}
C-I_N
&=(-I_N+\mathsf R\mathsf S)(-I_N+\mathsf P\mathsf Q)-I_N\\
&=-\mathsf P\mathsf Q-\mathsf R\mathsf S
  +\mathsf R\mathsf S\mathsf P\mathsf Q\\
&=\begin{bmatrix}\mathsf R\mathsf S\mathsf P-\mathsf P&-\mathsf R\end{bmatrix}
  \begin{bmatrix}\mathsf Q\\ \mathsf S\end{bmatrix}=UY.\end{aligned}$$ Since $Y=LT_0$, this is $C-I_N=UL T_0=XT_0$.

Put $z=t-1$. The rectangular determinant identity says that $$\det(I_N+GH)=\det(I_r+HG)$$ for $G\in K(z)^{N\times r}$ and $H\in K(z)^{r\times N}$; the compatible-dimension form is recorded in [@StdKailath1980LinearSystems Appendix A.12, p. 651]. Apply it to $G=-z^{-1}X$ and $H=T_0$ over $K(z)$: $$\begin{aligned}
\det(zI_N-XT_0)
&=z^N\det(I_N-z^{-1}XT_0)\\
&=z^N\det(I_r-z^{-1}T_0X)\\
&=z^{N-r}\det(zI_r-T_0X).\end{aligned}$$ The use of $z^{-1}$ occurs only in the middle calculation over $K(z)$. To close the value $z=0$, consider the polynomial $$\Delta(z)=
\det(zI_N-XT_0)
-z^{N-r}\det(zI_r-T_0X)\in K[z].$$ Its image in $K(z)$ is zero by the preceding identity. Since the natural map $K[z]\hookrightarrow K(z)$ is injective, $\Delta$ is the zero polynomial. The identity therefore holds at $z=0$ as well; no expression containing $z^{-1}$ is being evaluated there. Substituting $z=t-1$ proves the characteristic factorization.

The explicit power $z^{N-r}$ records the forced contribution at $t=1$. The second factor can also vanish at $z=0$, in which case it contributes additional unit roots beyond that forced power. Finally, the unique degree-$r$ term in the reduced determinant is $\det(zI_r)=z^r$, so the reduced determinant is monic of degree $r$.

## Kernel interpretation and boundary cases

The space $\ker\mathsf Q\cap\ker\mathsf S$ has dimension $N-r$ and is fixed pointwise by $C$. The factorization forces unit algebraic multiplicity at least $N-r$, with the usual empty-determinant interpretation at $r=0$ and exponent zero at $r=N$; additional unit roots may lie in the reduced determinant.

Because $T_0$ and $Y$ have the same row space, $$\ker T_0=\ker Y=\ker\mathsf Q\cap\ker\mathsf S,
\qquad \dim\ker T_0=N-r.$$ If $v$ lies in this space, then $Av=-v$, $Bv=-v$, and hence $Cv=B(-v)=v$. Thus the geometric, and therefore algebraic, multiplicity of $1$ is at least $N-r$. Lemma L1 gives the same algebraic lower bound.

If $r=0$, then $Y=0$, so $\mathsf Q=0$ and $\mathsf S=0$. Consequently $A=B=-I_N$, $C=I_N$, and the formula reads $\chi_C(t)=(t-1)^N$ with the determinant of the empty matrix equal to one. If $r=N$, the forced exponent is zero and no unit factor is imposed. For intermediate or full rank, the reduced determinant may vanish at $t=1$; the argument gives no equality statement for unit multiplicity.

The completely empty ambient case is consistent with the same convention: if $N=0$, then $r=0$, both relevant determinants are empty, and $\chi_C(t)=1$. More generally, $$\mathop{\mathrm{rank}}(C-I_N)=\mathop{\mathrm{rank}}(XT_0)\leq r,$$ but this rank inequality is not a substitute for the characteristic identity. It explains the geometric factor-through constraint, whereas the polynomial factorization controls algebraic multiplicity and leaves room for further copies of $t-1$ in the reduced factor.

The rank inequality and the characteristic factorization answer different questions. The former bounds $\mathop{\mathrm{rank}}(C-I_N)$ and therefore bounds $\dim\ker(C-I_N)$ from below, which concerns geometric multiplicity. Divisibility of $\chi_C(t)$ by $(t-1)^{N-r}$ concerns algebraic multiplicity. Neither computation makes the two multiplicities equal. Extra factors $t-1$ in the reduced determinant are not certified as matching new fixed directions, and the proof does not determine the generalized eigenspace or Jordan blocks at $1$. This separation explains the lower-bound wording and leaves the exact unit profile outside the theorem.

Lemmas L1 and L2 prove Structural Theorem S, including both rank boundaries. Notice that the result depends on the chosen compatible row presentation. It gives a universal upper bound from that presentation, not uniqueness of a support representation.

## Structural meaning and limits

The factor $C-I_N=UY$ shows that every nontrivial direction of the complete-step matrix passes through the stacked selected row space. Factoring through a row basis removes repeated or dependent selected covectors automatically. The characteristic quotient left after the forced unit factor has degree $r$, and the actual nonunit part has degree at most $r$ because the quotient may contain further copies of $t-1$.

Rank alone does not determine the quotient polynomial, its roots, the exact unit multiplicity, or whether a given presentation is smallest. These are deliberate limits of Structural Theorem S. Section [8](#sec:sharpness){reference-type="ref" reference="sec:sharpness"} returns to the specific matrices $D$ and $B_0$, where a full-rank selected presentation and irreducibility make the bound an equality.

# Uniform parameter construction {#sec:parameters}

## Quantifier order and target inequalities

The construction makes no choice in response to a later iterate. Starting from a fixed integer $d\geq2$, we first choose $p$ and $c$, then all ordered lifts $a_i$, and only then $b$ and $R_0$. Once the lifts are fixed, write $$S_a=\sum_{i=1}^d a_i,\qquad M=a_d.$$ The target is one congruence and finitely many strict inequalities: $$\begin{aligned}
bd&\equiv1-(-1)^dc\pmod p,\\
R_0&=1+\frac{2M}{bS_a},\\
b&\geq2,\qquad R_0^2<2,\\
b(a_i-a_1)S_a&>a_i^2R_0-a_1^2\qquad(2\leq i\leq d).\end{aligned}$$ The next lemma proves simultaneous existence rather than treating these conditions as independent assumptions.

The quantifier order is part of that assertion. All existential choices occur before the degree orbit: $$d\longrightarrow(p,c)\longrightarrow
(a_1,\ldots,a_d)\longrightarrow(b,R_0)
\longrightarrow\{u_n\}_{n\geq0}.$$ Thus $p$ and $c$ are fixed before the integer lifts, the lifts are frozen before the final scalar choice, and the same $b,R_0$ must serve every later $n$. No iterate, chamber point, or observed degree is an input to the parameter selection.

## Prime and primitive element

For every $d\geq2$, parameters $p,c,a_1<\cdots<a_d,b,R_0$ exist in the stated order and satisfy every congruence and strict inequality above, as well as $a_1+1>4d$.

Dirichlet's theorem for the coprime pair $(1,d)$ gives a prime $$p\equiv1\pmod d;$$ we use only existence, not density or an effective bound [@StdIreland1990ModernNumberTheory Chapter 16, Section 1, Theorem 1, p. 251]. Hence $d\mid p-1$ and $p\nmid d$. The group $\mathbb{F}_{p}^\times$ is cyclic of order $p-1$, so choose a generator $c$ with $$\mathop{\mathrm{ord}}_{\mathbb{F}_{p}^\times}(c)=p-1.$$ Cyclicity, and the fact that $x^d=1$ has exactly $d$ roots when $d\mid p-1$, are recorded in [@StdIreland1990ModernNumberTheory Chapter 4, Section 1, pp. 39--41]. The exact order of $c$, rather than mere nonvanishing, will be essential in Section [6](#sec:arithmetic){reference-type="ref" reference="sec:arithmetic"}.

Let $$1\leq r_1<r_2<\cdots<r_d\leq p-1$$ be the sorted least positive representatives of all solutions to $x^d=1$ in $\mathbb{F}_{p}$. Choose a single integer $m\geq0$ large enough that $mp+r_1+1>4d$, and set $$a_i=mp+r_i\qquad(1\leq i\leq d).$$ A common shift preserves the strict integer order, positivity, and the complete residue multiset. It also gives $a_1+1>4d$. The ordering is an ordering of the chosen integer lifts and makes no claim about an order on the finite field.

Since $p\nmid d$, multiplication by $d$ is invertible modulo $p$. Therefore $$bd\equiv1-(-1)^dc\pmod p$$ defines one residue class modulo $p$. Choose an integer representative $b_0$ of that class. After the $a_i$, $S_a$, and $M$ have been frozen, define the finite threshold $$\begin{aligned}
B_{\mathrm{thr}}=\max\Biggl\{
&2,\,
\frac{2M}{(\sqrt{2}-1)S_a},\\
&\max_{2\leq i\leq d}
\frac{\sqrt{2}\,a_i^2-a_1^2}
{(a_i-a_1)S_a}
\Biggr\}.
\end{aligned}$$ Every denominator is positive: $S_a>0$ and $a_i-a_1>0$ for $i>1$. The integers $b_0+\ell p$ are arbitrarily large, so choose $\ell$ such that $$b=b_0+\ell p>B_{\mathrm{thr}}.$$ This preserves the required congruence and gives $b\geq2$. Moreover, $$R_0=1+\frac{2M}{bS_a}<\sqrt{2},
\qquad R_0^2<2.$$ For each $i>1$, the last group in the threshold gives $$\begin{aligned}
b(a_i-a_1)S_a
&>\sqrt{2}\,a_i^2-a_1^2\\
&>a_i^2R_0-a_1^2.\end{aligned}$$ Thus one member of the already fixed congruence class satisfies all $d-1$ visibility inequalities together with the ratio condition. Defining $R_0$ from this $b$ completes the required sequence of choices without a limiting or orbit-dependent choice.

No positivity of the initial representative $b_0$ is required. Since $p>0$, choosing $\ell$ sufficiently large makes $b_0+\ell p$ exceed the entire finite threshold while leaving its residue unchanged. Each entry in that threshold is already a fixed real number after the ordered lifts are chosen; even a negative numerator would create no obstruction. The strict choice $b>B_{\mathrm{thr}}$, rather than a limiting argument, supplies all ratio and visibility inequalities at once. Hence the resulting $b$ and $R_0$ are fixed before $u_0$ or any later orbit vector is considered.

## Ordered positive lifts

The proof of Lemma L3 chooses all roots before shifting them. This matters twice: coefficient comparison modulo $p$ later uses the complete multiset, whereas visibility uses the strict integer order. One common multiple of $p$ changes neither residue and gives the uniform selection margin $a_1+1>4d$ without altering the order.

The common shift has both invariants and noninvariants that fix the choice order. It preserves every residue $a_i\bmod p$, the strict order, and every difference $a_i-a_j$. It changes the absolute magnitudes of the lifts, hence $S_a$, $M$, and the quantities entering $B_{\mathrm{thr}}$. The roots are therefore collected and sorted first, the common shift is finalized second, and only afterward are the threshold and the congruence-class representative for $b$ chosen. Choosing $b$ before a later shift would preserve the modular identities but change the analytic quantities used to justify the inequalities. Freezing the lifts first removes that circularity.

## Congruence class and simultaneous large-$b$ closure

The final choice of $b$ is made inside one already determined residue class. The ratio $R_0$ decreases to one along that class, while each left side in the visibility inequalities grows linearly. Thus the ratio, selection, and visibility conditions are simultaneous consequences of one choice; no later degree orbit enters the parameter selection.

The three entries in $B_{\mathrm{thr}}$ have separate roles. The first enforces the elementary lower bound on $b$, the second places $R_0$ below $\sqrt{2}$, and the finite inner maximum closes every weighted visibility wall. At $d=2$ that inner maximum contains exactly one term. When $4\mid d$, no new analytic threshold is needed; the resulting congruence $p\equiv1\pmod4$ is used only in the arithmetic criterion of the arithmetic section.

## Arithmetic boundaries

The construction includes $d=2$. In that case $p\equiv1\pmod2$ is odd, the congruence for $b$ is soluble because $p\nmid2$, and there is exactly one visibility inequality to absorb in the large-$b$ choice. The requirement $a_1+1>8$ is obtained by the same common shift.

If $4\mid d$, then the same progression already gives $p\equiv1\pmod4$. This observation will discharge the separate $4\mid d$ clause in the irreducible-binomial criterion. Every parameter used later has now been fixed uniformly for the chosen $d$.

# Two-level chambers and exact polynomial-degree induction {#sec:degrees}

## Phase-labelled recursion target

Set $u_0=\mathbf{1}$. At the start of the $(n+1)$st application of $F$, suppose provisionally that the position-degree vector is $u_n$. The $V$-half-step leaves the position block unchanged and proposes the fresh momentum vector $Du_n$; it must compete with the old momentum block. The $W$-half-step leaves that momentum block unchanged and proposes the fresh position vector $$B_0Du_n=Cu_n;$$ it must compete with the old position block. Lemma L4 identified these rows from the literal gradients, but did not prove their repeated selection. We now establish strict selection in a broad cone, fixed-coordinate visibility in a finer chamber, both temporal carry comparisons, and leading-form survival.

The full phase ledger to be proved is $$\bigl(\deg Q_i^{(n)}\bigr)_{i=1}^d=u_n,
\qquad
\bigl(\deg P_i^{(n)}\bigr)_{i=1}^d=
\begin{cases}
\mathbf{1},&n=0,\\
Du_{n-1},&n\geq1,
\end{cases}$$ together with the half-step identities $$\bigl(\deg\widehat P_i^{(n)}\bigr)_{i=1}^d=Du_n,
\qquad
\bigl(\deg Q_i^{(n+1)}\bigr)_{i=1}^d=Cu_n.$$ This ledger is the induction assertion, not an additional hypothesis. The broad cone supplies the componentwise face and carry comparisons, the fine chamber identifies the fixed visible coordinate, and the coefficient argument later certifies that the selected top forms are nonzero.

The bookkeeping separates three logically different tests. A support row first has to beat every other row in the same gradient component. Its resulting degree must then beat the coordinate carried through that half-step. Finally, the corresponding top homogeneous polynomial must be nonzero after all substitutions. The matrices $D$ and $B_0$ encode only the first row weights; they do not encode the carried terms or certify survival. The induction below therefore uses the two chambers for the first two tests and the coefficient-semiring argument for the third before identifying the successive phase vectors with $Du_n$ and $Cu_n$.

## Broad cone and strict spike selection

Define $$\mathcal{K}_{\mathrm{ratio}}(R_0)=\{u\in\mathbb R_{>0}^d:\max_i u_i\leq R_0\min_i u_i\}.$$ The ordinary seed $\mathbf{1}$ belongs to this cone because $R_0>1$.

For every $u\in\mathcal{K}_{\mathrm{ratio}}(R_0)$ and every $i$, the pure spike weight $a_i u_i$ is strictly larger than the mixed-product weight $2\sum_j u_j-u_i$.

Put $m=\min_i u_i$. Then $u_j\leq R_0m$ for every $j$, and hence $$2\sum_{j=1}^d u_j-u_i\leq(2dR_0-1)m.$$ On the other hand, $a_i u_i\geq a_1m$. From $a_1+1>4d$ and $R_0^2<2$ we have $R_0<\sqrt2<2$ and $$a_1>4d-1>2dR_0-1.$$ Multiplication by $m>0$ gives the required strict inequality in every component. Thus no tie between the two literal $V$-faces occurs anywhere in the broad cone.

The proof also records a uniform positive margin at each $u$: $$\begin{aligned}
a_i u_i-\left(2\sum_j u_j-u_i\right)
&\geq
\bigl(a_1-(2dR_0-1)\bigr)m\\
&>0.
\end{aligned}$$ Only the minimum coordinate $m$ varies along the cone; the coefficient in parentheses is fixed once the parameters are chosen. This is the strict separation used at every $V$-phase, not an equality that could be altered by a carried coordinate.

## Strict broad-cone invariance and block domination

The matrix $C$ maps $\mathcal{K}_{\mathrm{ratio}}(R_0)$ into its strict interior. Moreover, for every $u\in\mathcal{K}_{\mathrm{ratio}}(R_0)$, $$(Cu)_i>\max_j a_j u_j>u_i\qquad(1\leq i\leq d).$$

For $u\in\mathcal{K}_{\mathrm{ratio}}(R_0)$, put $m=\min_i u_i$, $H=a^{\mathsf{T}}u$, and $z=Cu$. Then $$z_i=bH-a_i u_i,\qquad H\geq S_am,\qquad a_i u_i\leq MR_0m.$$ Strict positivity of $C$ gives $z_i>0$. Before dividing, note that $$\frac{MR_0}{bS_a}=\frac{R_0(R_0-1)}{2}<\frac12,$$ because $R_0(R_0-1)=R_0^2-R_0<2-R_0<1$. In particular, $bS_a-MR_0>0$. Now $$\begin{aligned}
\frac{\max_i z_i}{\min_i z_i}
&\leq\frac{bH}{bH-MR_0m}
\leq\frac{bS_a}{bS_a-MR_0}\\
&=\frac{1}{1-MR_0/(bS_a)}.\end{aligned}$$ The middle inequality uses that $x/(x-k)$ decreases for $x>k>0$. The final bound is strictly below $R_0$, since, after multiplication by the positive denominator, this is equivalent to $$(R_0-1)\left(1-\frac{R_0^2}{2}\right)>0.$$ Both factors are positive. Thus $C\mathcal{K}_{\mathrm{ratio}}(R_0)$ lies in the strict interior.

The first ratio estimate uses different one-sided bounds deliberately: $bH$ bounds every numerator from above, whereas $bH-MR_0m$ bounds every denominator from below. Its positivity is established before the quotient is compared. Replacing $bH/m$ by its lower bound $bS_a$ is then legitimate because $x/(x-MR_0)$ decreases on $x>MR_0$. The resulting upper ratio is a fixed number strictly below $R_0$, so every iterate starting at $\mathbf{1}$ re-enters the same cone with slack. This normalized cone statement is distinct from, and does not by itself imply, the global domination of the opposite coordinate block.

For the stronger block comparison, $$(Cu)_i\geq(bS_a-MR_0)m,\qquad \max_j a_j u_j\leq MR_0m.$$ The identity $bS_a=2M/(R_0-1)$ and $R_0(R_0-1)<1$ imply $bS_a>2MR_0$. Hence $bS_a-MR_0>MR_0$, proving $(Cu)_i>\max_j a_j u_j$. Finally, $a_i>1$ gives $\max_j a_j u_j\geq a_i u_i>u_i$. This is a comparison with the entire opposite block, stronger than coordinatewise growth alone.

## Fine visibility chamber

Define $$\mathcal{K}_{\mathrm{vis}}(R_0)=\left\{u\in\mathbb R_{>0}^d:
u_i\leq u_1<R_0u_i\ \text{for all }i,\quad
a_1u_1<a_i u_i\ \text{for }i>1\right\}.$$ The equality walls $u_i=u_1$ are permitted. Since $R_0>1$ and $a_1<a_i$ for $i>1$, the seed $\mathbf{1}$ belongs to $\mathcal{K}_{\mathrm{vis}}(R_0)$. Every $u$ in the fine chamber has largest coordinate $u_1$ and $u_i>u_1/R_0$ for all $i$, so $\mathcal{K}_{\mathrm{vis}}(R_0)\subset\mathcal{K}_{\mathrm{ratio}}(R_0)$.

If $u\in\mathcal{K}_{\mathrm{vis}}(R_0)$ and $w=Cu$, then $w\in\mathcal{K}_{\mathrm{vis}}(R_0)$ and $w_1>w_i$ for every $i>1$.

Put $s=u_1$ and $H=a^{\mathsf{T}}u$. The fine chamber gives $u_j\leq s$ and $u_j>s/R_0$ for all $j$, whence $$H>\frac{S_a}{R_0}s.$$ For $i>1$, the weighted wall directly yields $$w_1-w_i=(bH-a_1s)-(bH-a_i u_i)=a_i u_i-a_1s>0.$$ Thus $w_i<w_1$. For the ratio wall, $$\begin{aligned}
R_0w_i-w_1
&=(R_0-1)bH-R_0a_i u_i+a_1s\\
&>\left(\frac{(R_0-1)bS_a}{R_0}-R_0M+a_1\right)s\\
&=\left(\frac{M(2-R_0^2)}{R_0}+a_1\right)s>0.\end{aligned}$$ Here $(R_0-1)bS_a=2M$ and $R_0^2<2$. Therefore $w_1<R_0w_i$.

For the weighted wall, $$\begin{aligned}
a_iw_i-a_1w_1
&=b(a_i-a_1)H-a_i^2u_i+a_1^2s\\
&>\left(\frac{b(a_i-a_1)S_a}{R_0}-a_i^2+a_1^2\right)s.\end{aligned}$$ The parameter inequality implies $$\frac{b(a_i-a_1)S_a}{R_0}>a_i^2-\frac{a_1^2}{R_0}.$$ Substitution leaves the positive lower bound $$a_1^2\left(1-\frac1{R_0}\right)s.$$ All coordinate, ratio, and weighted walls are preserved in the required direction.

The signs in these estimates use all parts of the fine chamber. The strict lower bound for $H$ comes from $u_j>s/R_0$ for every $j$. In the ratio wall, the negative term is controlled by $a_i u_i\leq Ms$; in the weighted wall, the inequality $u_i\leq s$ changes $-a_i^2u_i$ into the required lower bound rather than an upper bound. The parameter inequality leaves the explicit positive remainder $a_1^2(1-1/R_0)s$. Thus the coordinate, ratio, and weighted walls are checked separately: the seed may lie on coordinate-equality walls, but its first image lies strictly on the visible side.

## Both temporal carries

Along the orbit from the ordinary seed, every fresh $V$-spike strictly defeats the carried momentum coordinate, and every fresh $W$-monomial strictly defeats every carried position or momentum degree.

We verify the two carries in the same order as the phase ledger. At $n=0$, the position vector is $u_0=\mathbf{1}$ and every momentum coordinate has degree one. Lemma L5 makes the pure spike in component $i$ strictly larger than the mixed $V$-term, while its degree $a_i>1$ also defeats the carried variable $p_i$. Thus the first post-$V$ momentum vector is $Du_0$.

The unique fresh $W$-monomial in component $i$ then has degree $$(B_0Du_0)_i=(Cu_0)_i.$$ Lemma L6 makes every entry of $Cu_0$ larger than every entry of $Du_0$ and larger than the retained position vector $u_0$. The first complete step therefore establishes the proposed next vector $u_1=Cu_0$ and the momentum part of the ledger.

Now suppose the ledger has been established through the start of a later step. The old momentum coordinate was created at the preceding $V$-phase and has degree $a_i u_{n-1,i}$, whereas the fresh pure spike has degree $a_i u_{n,i}$. From the already established preceding step and Lemma L6, $$u_n=Cu_{n-1}>u_{n-1}$$ componentwise. The fresh spike therefore defeats the old momentum coordinate strictly; Lemma L5 separately makes it defeat the mixed support face. Hence the post-$V$ momentum vector is $Du_n$.

At the following $W$-phase the sole fresh gradient monomial has degree $$(B_0Du_n)_i=(Cu_n)_i.$$ The two comparisons in Lemma L6 give $$(Cu_n)_i>\max_j a_j u_{n,j}>u_{n,i}$$ for every $i$. Thus the fresh position term defeats the entire momentum block $Du_n$ and the entire carried position block $u_n$, not merely the coordinate with the same index. The new position vector is $u_{n+1}=Cu_n$, while the $W$-shear leaves the new momentum vector $Du_n$ unchanged. This closes both parts of the ledger without using a conclusion from a future step.

For $n\geq1$, the temporal indices can be displayed without suppressing either retained block: $$\begin{aligned}
\deg P_i^{(n)}&=a_i u_{n-1,i},
&\deg(\text{fresh }V\text{-spike})&=a_i u_{n,i},\\
\deg\widehat P_i^{(n)}&=a_i u_{n,i},
&\deg(\text{fresh }W\text{-term})&=(Cu_n)_i.
\end{aligned}$$ Here $u_n=Cu_{n-1}$ is available from the preceding completed step, so its use in the first comparison is not circular. The second comparison uses the current post-$V$ block $Du_n$ and the retained position block $u_n$, both of which are already known at that point. Lemma L8 supplies these strict numerical comparisons, while Lemma L9 below verifies that the winning expressions really have nonzero top forms. The two lemmas therefore close one induction step jointly rather than borrowing its conclusion in advance.

## Positive-semiring leading-form survival

Strict degree comparison rules out cancellation between sources of different degrees, but it remains necessary to know that a selected top form is nonzero.

Every selected leading form in the induction is nonzero after base change to $K$, and no maximal-degree contribution cancels.

Begin over $$\mathbb Z_{\geq0}[q_1,\ldots,q_d,p_1,\ldots,p_d].$$ The coordinate variables have coefficient one, and the forward formulas for both shears use only addition, multiplication, positive powers, and positive integer derivative coefficients. Every coordinate of every forward iterate therefore remains in this nonnegative coefficient semiring. A strictly larger-degree summand cannot be canceled by a smaller one, while equally graded nonnegative summands can only add.

The strict comparisons of Lemma L8 make the surviving top forms explicit. Put $$A_i^{(n)}=\operatorname{LF}\bigl(Q_i^{(n)}\bigr),
\qquad
G_i^{(n)}=\operatorname{LF}\bigl(\widehat P_i^{(n)}\bigr).$$ The mixed $V$-face and the carried momentum term both have smaller degree than the pure spike, so $$G_i^{(n)}
=(a_i+1)\bigl(A_i^{(n)}\bigr)^{a_i},
\qquad
\deg G_i^{(n)}=a_i u_{n,i}.$$ At the $W$-phase the retained $Q_i^{(n)}$ has smaller degree than the fresh product. Therefore $$A_i^{(n+1)}
=b\bigl(G_i^{(n)}\bigr)^{b-1}
  \prod_{j\ne i}\bigl(G_j^{(n)}\bigr)^b,$$ and its degree is $$\begin{aligned}
\deg A_i^{(n+1)}
&=(b-1)a_i u_{n,i}
  +\sum_{j\ne i}ba_j u_{n,j}\\
&=b\,a^{\mathsf{T}}u_n-a_i u_{n,i}
=(Cu_n)_i.\end{aligned}$$ The leading form of a product or positive power of nonzero polynomials is the corresponding product or power of their leading forms. The ambient polynomial ring over $\mathbb Z$ is a domain, so the displayed products do not vanish. Positive coefficients also prevent equal monomials inside an expanded product from canceling.

The forms $A_i^{(n)}$ need not be monomials. What matters is that the strict face and carry comparisons isolate one source of the maximal degree, so the displayed power or product is exactly the top homogeneous component of the new coordinate. A power of a nonzero form and a product of nonzero forms remain nonzero in the integral polynomial ring, even when their expansions contain many monomials. If two expansion terms produce the same monomial, their nonnegative coefficients add instead of canceling. Establishing these identities over $\mathbb Z_{\geq0}$ before base change separates the domain argument from the later use of characteristic zero.

Finally, characteristic zero makes the map $\mathbb Z\to K$ injective. In particular, neither $a_i+1$ nor $b$ becomes zero under base change, and every nonzero positive coefficient in the displayed leading forms survives. Hence the entire top-form recursion remains valid in $K[q,p]$ without a genericity assumption.

## Exact fixed-$q_1$ visibility

For every $n\geq0$, the position-degree vector is $u_n=C^n\mathbf{1}$ and $$\deg(F^n)=e_1^{\mathsf{T}}C^n\mathbf{1}.$$ All coordinates have degree one at $n=0$, while $q_1$ is uniquely degree-maximal for every $n\geq1$.

The seed has position vector $u_0=\mathbf{1}$ and lies in both chambers. Lemmas L5--L9 show inductively that the literal $V$-phase has exact momentum vector $Du_n$, that the literal $W$-phase has exact new position vector $Cu_n$, and that the selected top forms survive. Thus $$u_{n+1}=Cu_n,\qquad u_n=C^n\mathbf{1}.$$ Lemma L7 keeps the orbit in $\mathcal{K}_{\mathrm{vis}}(R_0)$ and makes the first position coordinate strictly larger than all other position coordinates for $n\geq1$. The momentum block of $F^n$ for $n\geq1$ has vector $Du_{n-1}$. Applying the global cross-block comparison in Lemma L6 to $u_{n-1}$ shows that every entry of $u_n$ is strictly larger than every entry of $Du_{n-1}$. Hence $q_1$ is the unique maximal coordinate of the complete tuple at every positive iterate.

More explicitly, for $n\geq1$ the two block maxima satisfy $$\begin{aligned}
\max_i\deg P_i^{(n)}
&=\max_i a_i u_{n-1,i}\\
&<\min_i u_{n,i}
\leq u_{n,1}
=\max_i\deg Q_i^{(n)}.
\end{aligned}$$ The first strict inequality is the global block comparison, while Lemma L7 gives $u_{n,1}>u_{n,i}$ for every $i>1$. Thus the conclusion concerns the maximum over all $2d$ coordinates and not only the position block.

At $n=0$, all $2d$ coordinates of the identity have degree one, so uniqueness is neither claimed nor true; nevertheless $e_1^{\mathsf{T}}\mathbf{1}=1$. It follows for all $n\geq0$ that $$\boxed{\deg(F^n)=e_1^{\mathsf{T}}C^n\mathbf{1}.}$$ This is an equality of ordinary polynomial degrees, not a tropical or matrix upper bound.

# Characteristic polynomial and irreducibility {#sec:arithmetic}

## Rank-one determinant and coefficient count

For $C=b\mathbf{1}a^{\mathsf{T}}-D$, $$\chi_C(t)=t^d+\sum_{k=1}^d(1-bk)e_k(a_1,\ldots,a_d)t^{d-k}.$$

Over $\mathbb Q(t)$ the diagonal matrix $tI_d+D$ is invertible. The rank-one determinant formula is an immediate corollary of the compatible determinant identities in [@StdKailath1980LinearSystems Appendix A.12 and A.26(2), pp. 651, 658]; applying the corollary here gives $$\begin{aligned}
\chi_C(t)
&=\det(tI_d+D-b\mathbf{1}a^{\mathsf{T}})\\
&=\det(tI_d+D)\left(1-ba^{\mathsf{T}}(tI_d+D)^{-1}\mathbf{1}\right)\\
&=\prod_{i=1}^d(t+a_i)-b\sum_{i=1}^d a_i\prod_{j\ne i}(t+a_j).\end{aligned}$$ The last line is a polynomial identity, so no exceptional value $t=-a_i$ remains.

The two polynomial expansions can be compared uniformly: $$\prod_{i=1}^d(t+a_i)
=\sum_{k=0}^d e_k(a)t^{d-k},$$ $$\sum_{i=1}^d a_i\prod_{j\ne i}(t+a_j)
=\sum_{k=1}^d k\,e_k(a)t^{d-k}.$$ Indeed, fix a subset of $k$ distinct entries of $a$. Its squarefree product occurs once in $e_k(a)$. In the second expression, the same product is obtained once for each of the $k$ choices of its distinguished factor $a_i$, and for no other index. Thus it occurs exactly $k$ times. Subtracting $b$ times the second expansion from the first gives coefficient $(1-bk)e_k(a)$ for $t^{d-k}$, including the constant case $k=d$.

## Roots-of-unity reduction

The reduction of $\chi_C$ modulo $p$ is $t^d-c$. This binomial is irreducible over $\mathbb{F}_{p}$, and $\chi_C$ is irreducible over $\mathbb Q$.

The residues of $a_1,\ldots,a_d$ are exactly the $d$ roots of $x^d-1$ in $\mathbb{F}_{p}$. Since $p\nmid d$, the roots are distinct, and equality of monic split polynomials gives $$\prod_{i=1}^d(x-a_i)\equiv x^d-1\pmod p.$$ The sign pattern on the left is $$\prod_{i=1}^d(x-a_i)
=x^d-e_1(a)x^{d-1}+\cdots+(-1)^de_d(a).$$ For $1\leq k<d$, comparison with $x^d-1$ gives $(-1)^ke_k(a)\equiv0$, hence $e_k(a)\equiv0$. The constant coefficient instead gives $$(-1)^de_d(a)\equiv-1\pmod p,$$ and therefore $$e_k(a)\equiv0\pmod p\quad(1\leq k<d),
\qquad e_d(a)\equiv(-1)^{d+1}\pmod p.$$ The defining congruence for $b$ is equivalently $$1-bd\equiv(-1)^dc\pmod p.$$ Lemma L11 therefore gives $$\begin{aligned}
\chi_C(t)
&\equiv t^d+(1-bd)e_d(a)\\
&\equiv t^d+(-1)^dc(-1)^{d+1}
\equiv t^d-c\pmod p.\end{aligned}$$ In particular, the reduction remains monic of degree $d$.

The equality of split polynomials uses the complete residue multiset, not merely the congruence $a_i^d\equiv1$. Because $p\nmid d$, the derivative $d x^{d-1}$ is nonzero at every nonzero root of $x^d-1$; hence those roots are simple. Cyclicity and $d\mid p-1$ give exactly $d$ of them, so the $d$ lifted residues exhaust the roots with no repetition. The common integer shift and their ordering do not alter that multiset. The argument therefore depends on the full root set, not on checking the power congruence for each lift independently. Coefficient comparison can therefore kill every intermediate $e_k(a)$ while retaining the signed constant coefficient, and the separate congruence for $b$ changes precisely that surviving coefficient to $-c$.

## Full finite-field binomial criterion

For $x^m-\gamma\in\mathbb F_q[x]$ with $m\geq2$ and $\gamma\ne0$, the irreducible-binomial criterion requires all three conditions

1.  every prime divisor of $m$ divides $\mathop{\mathrm{ord}}_{\mathbb F_q^\times}(\gamma)$;

2.  $\gcd\bigl(m,(q-1)/\mathop{\mathrm{ord}}_{\mathbb F_q^\times}(\gamma)\bigr)=1$; and

3.  if $4\mid m$, then $q\equiv1\pmod4$.

This is the form recorded in [@HS Section 2.1, Lemma 6, p. 4]. We now check rather than delegate every condition. Here $m=d$, $q=p$, and $\gamma=c$. Because $c$ is a generator, $$\mathop{\mathrm{ord}}_{\mathbb{F}_{p}^\times}(c)=p-1.$$ The three numerical checks can be kept separate: $$d\mid p-1=\mathop{\mathrm{ord}}(c),\qquad
\frac{p-1}{\mathop{\mathrm{ord}}(c)}=1,\qquad
4\mid d\Longrightarrow4\mid p-1.$$ The first relation implies that every prime divisor of $d$ divides $\mathop{\mathrm{ord}}(c)$. The second makes the required greatest common divisor equal to $\gcd(d,1)=1$. Under the hypothesis $4\mid d$, the final relation is equivalent to $p\equiv1\pmod4$. Thus no clause is absorbed into another, and all three conditions hold. Consequently $t^d-c$ is irreducible in $\mathbb{F}_{p}[t]$.

## Boundary cases and rational lifting

When $d=2$, the prime $p$ is odd and $\mathbb{F}_{p}^\times$ has even order. Its squares form the index-two subgroup, while a generator $c$ has order $p-1$ and is therefore not a square. Thus the quadratic $t^2-c$ has no root, agreeing with the three-condition argument. When $4\mid d$, the separate congruence condition was established above rather than absorbed silently into the other two conditions.

The polynomial $\chi_C$ is monic in $\mathbb Z[t]$, and reduction modulo $p$ preserves its degree. Gauss's lemma and the monic reduction criterion are recorded in [@StdDummit2004AbstractAlgebra Chapter 9, Sections 9.3--9.4, pp. 303--308]. For completeness, suppose $\chi_C$ factored over $\mathbb Q$. Gauss's lemma and a change of signs if necessary would give $$\chi_C(t)=g(t)h(t),
\qquad
g,h\in\mathbb Z[t]\ \hbox{monic},
\qquad
1\leq\deg g,\deg h\leq d-1.$$ The reductions $\overline g,\overline h\in\mathbb{F}_{p}[t]$ retain the same positive degrees because their leading coefficients remain one. Reducing the equality would therefore produce the nontrivial factorization $$t^d-c=\overline g\,\overline h$$ over $\mathbb{F}_{p}$, contradicting the binomial irreducibility just proved. Hence $\chi_C$ is irreducible over $\mathbb Q$. This completes the proof of Lemma L12.

Monicity performs two jobs in the lift. It makes $\chi_C$ primitive, so a rational factorization yields integral monic factors, and it prevents either factor from losing degree after reduction because its leading coefficient remains one modulo $p$. Thus the reduced product would be genuinely nontrivial; no factor can disappear through coefficient reduction.

## Arithmetic output

The matrix $C$ has integer entries and monic irreducible characteristic polynomial of degree $d$. Consequently, the minimal polynomial over $\mathbb Q$ of every eigenvalue of $C$ is $\chi_C$. In particular, this holds for the positive eigenvalue selected by Perron--Frobenius theory in the next section. The standard binomial criterion is used only for provenance; the residue calculation, its three hypotheses, and the rational lift have all been checked explicitly.

Two minimal-polynomial assertions are distinct. The matrix minimal polynomial $m_C$ is a nonconstant divisor of $\chi_C$ by Cayley--Hamilton, so irreducibility forces $m_C=\chi_C$. For an eigenvalue $\lambda$, its scalar minimal polynomial $m_\lambda$ divides $\chi_C$ because $\chi_C(\lambda)=0$, and irreducibility again forces equality. The first statement rules out a lower-degree polynomial annihilating the matrix; the second rules out one annihilating the algebraic number. Their arithmetic source is the same, but their uses differ: the matrix statement supports cyclicity and recurrence, whereas the scalar statement supplies algebraic degree and the eventual-tail contradiction.

# Perron degree and exact scalar recurrence {#sec:perron}

## Perron projection and dynamical-degree limit

The first dynamical degree is $\lambda_1(F)=\rho(C)$. This number is a Perron algebraic integer of algebraic degree exactly $d$.

Every entry of $C$ is strictly positive. Perron's theorem for positive matrices gives a simple positive eigenvalue $\rho=\rho(C)$, positive right and left eigenvectors, and no other eigenvalue on the spectral circle [@StdMeyer2000MatrixAnalysis Section 8.2, p. 667]. The positive left vector follows by applying the same theorem to $C^{\mathsf{T}}$, and uniqueness on the spectral circle gives the strict gap. Choose $v_\rho,\ell>0$ with $$Cv_\rho=\rho v_\rho,\qquad \ell^{\mathsf{T}}C=\rho\ell^{\mathsf{T}},
\qquad \ell^{\mathsf{T}}v_\rho=1.$$ Define the rank-one Perron projector $$\Pi_\rho=v_\rho\ell^{\mathsf{T}}.$$ The normalization gives $$\Pi_\rho^2=\Pi_\rho,\qquad
C\Pi_\rho=\Pi_\rho C=\rho\Pi_\rho.$$ Choose $\theta$ strictly between the largest modulus of a non-Perron eigenvalue and $\rho$. On the complementary generalized eigenspaces, Jordan powers contribute a fixed polynomial in $n$ times an exponential of smaller modulus; enlarging to $\theta$ absorbs every such polynomial factor. Thus $$C^n=\rho^n\Pi_\rho+E_n,
\qquad
\lVert E_n\rVert=O(\theta^n).$$ Multiplication by the fixed covector and state gives $$e_1^{\mathsf{T}}C^n\mathbf{1}
=\gamma\rho^n+O(\theta^n),
\qquad
\gamma=e_1^{\mathsf{T}}\Pi_\rho\mathbf{1}
=(e_1^{\mathsf{T}}v_\rho)(\ell^{\mathsf{T}}\mathbf{1})>0.$$ Both factors in the last product are positive. Hence the fixed observation and state see the Perron projection with a nonzero coefficient; no cancellation among subdominant terms can remove this leading contribution.

The asymptotic can be normalized as $$e_1^{\mathsf{T}}C^n\mathbf{1}
=\gamma\rho^n\left(1+O\!\left((\theta/\rho)^n\right)\right).$$ The parenthetical factor is positive for all sufficiently large $n$ and tends to one, while $\gamma^{1/n}\to1$. Taking $n$th roots therefore yields $\rho$, rather than only a limsup upper bound. This reasoning does not require diagonalizability: the polynomial factors contributed by non-Perron Jordan blocks have already been absorbed by choosing $\theta$ strictly above their eigenvalue moduli. Positivity of both the state and observation projections is what prevents the Perron term itself from disappearing.

Lemma L10 identifies the left side with $\deg(F^n)$. Taking $n$th roots therefore gives an actual limit and proves $$\lambda_1(F)=\lim_{n\to\infty}\deg(F^n)^{1/n}=\rho(C).$$ The positive coefficient $\gamma$ is the needed visibility statement: the fixed state and covector do not annihilate the leading spectral projection.

## Exact Perron algebraic degree

By Lemma L12, $\rho$ is a root of the irreducible monic polynomial $\chi_C\in\mathbb Z[t]$ of degree $d$. Its minimal polynomial over $\mathbb Q$ is therefore $\chi_C$, so $\rho$ is an algebraic integer of degree exactly $d$. All other roots of $\chi_C$ are the remaining eigenvalues of $C$, and the strict spectral gap makes their moduli smaller than $\rho$. Thus $\rho$ is a Perron algebraic integer. Together with the preceding subsection, this proves Lemma L13.

Because $\chi_C$ is both the characteristic polynomial of $C$ and the minimal polynomial of $\rho$, the $\mathbb Q$-conjugates of $\rho$ are exactly the roots of $\chi_C$, hence exactly the spectrum over an algebraic closure. Characteristic zero and irreducibility make those roots distinct. Irreducibility supplies this coincidence and the degree count; Perron--Frobenius theory instead identifies the positive conjugate seen by the fixed state and covector and makes every other conjugate smaller in modulus. Positivity is therefore not being used as an algebraic-degree argument, nor irreducibility as a visibility argument.

## Cayley--Hamilton upper bound

A rational constant-coefficient recurrence of order $k\geq1$ for a sequence $(s_n)$ means an identity $$s_{n+k}+\xi_{k-1}s_{n+k-1}+\cdots+\xi_0s_n=0,
\qquad \xi_j\in\mathbb Q,$$ on the specified range of $n$. From-start means every $n\geq0$; eventual means every $n$ above some threshold.

The sequence $s_n=e_1^{\mathsf{T}}C^n\mathbf{1}$ has minimal rational constant-coefficient recurrence order $d$ from the start and eventually.

Write $$\chi_C(t)=t^d+\eta_1t^{d-1}+\cdots+\eta_d.$$ Cayley--Hamilton, in the form that a square matrix satisfies its characteristic polynomial [@StdKailath1980LinearSystems Appendix, Section 8, pp. 658--659], gives $$C^d+\eta_1C^{d-1}+\cdots+\eta_dI_d=0.$$ Multiplication by $e_1^{\mathsf{T}}C^n$ on the left and $\mathbf{1}$ on the right supplies an order-$d$ recurrence for every $n\geq0$. This proves only the upper bound.

Monicity of $\chi_C$ makes the recurrence normalized: the coefficient of $s_{n+d}$ is one and the remaining coefficients are rational. This proves only that the sequence has an annihilating relation of order at most $d$. A scalar state--observation pair could still satisfy a shorter relation even for a $d\times d$ matrix. The next subsection excludes that possibility for $(\mathbf{1},e_1^{\mathsf{T}})$ by proving both Krylov families cyclic and the Hankel matrix full rank. Eventual minimality needs the separate Perron-root contradiction, because the Hankel argument uses a recurrence starting at $n=0$.

## Reachability, observability, and Hankel rank

Suppose the vectors $\mathbf{1},C\mathbf{1},\ldots,C^{d-1}\mathbf{1}$ were dependent over $\mathbb Q$. Then a nonzero polynomial $f$ of degree below $d$ would satisfy $f(C)\mathbf{1}=0$. Irreducibility of $\chi_C$ gives $\gcd(f,\chi_C)=1$, so there are $g,h\in\mathbb Q[t]$ with $$g(t)f(t)+h(t)\chi_C(t)=1.$$ Evaluation at $C$ and application to $\mathbf{1}$, using $\chi_C(C)=0$, would give $\mathbf{1}=0$, a contradiction. Hence the reachability matrix $$\mathcal R_C=\begin{bmatrix}\mathbf{1}&C\mathbf{1}&\cdots&C^{d-1}\mathbf{1}\end{bmatrix}$$ is invertible.

This argument is an annihilator test for the particular state $\mathbf{1}$. A dependence among its first $d$ Krylov vectors would produce an annihilating polynomial below the irreducible degree $d$, and the Bezout identity would force that nonzero state to vanish. No positivity assertion is used in this step.

Apply the same argument to $C^{\mathsf{T}}$ and the nonzero vector $e_1$. Its characteristic polynomial is again the irreducible $\chi_C$, so $e_1,C^{\mathsf{T}}e_1,\ldots,(C^{\mathsf{T}})^{d-1}e_1$ is a basis. Equivalently, $$\mathcal O_C=
\begin{bmatrix}
e_1^{\mathsf{T}}\\ e_1^{\mathsf{T}}C\\ \vdots\\ e_1^{\mathsf{T}}C^{d-1}
\end{bmatrix}$$ is invertible. These are direct cyclicity proofs for the chosen state and covector, not consequences of positivity alone.

On the observation side the same annihilator test applies specifically to $e_1$. Transposition turns its Krylov basis into the rows of $\mathcal O_C$, so the reachability and observability conclusions have identical algebraic input but concern the two fixed ends of the scalar sequence.

Their product is the $d\times d$ Hankel matrix $$\mathcal H_d=\mathcal O_C\mathcal R_C
=\bigl(e_1^{\mathsf{T}}C^{i+j}\mathbf{1}\bigr)_{0\leq i,j<d}
=(s_{i+j})_{0\leq i,j<d}.$$ Thus $\mathop{\mathrm{rank}}\mathcal H_d=d$. The standard reachability, observability, realization, and Hankel-rank correspondences are recorded with the same factorization in [@StdKailath1980LinearSystems Sections 2.2--2.4, 5.1, and 6.5]; the matrices needed here have just been proved invertible directly.

For the recurrence implication, denote the $j$th Hankel column by $$h_j=(s_j,s_{j+1},\ldots,s_{j+d-1})^{\mathsf{T}}.$$ If an order $k<d$ recurrence held from $n=0$, its first $d$ shifted instances would give $$h_k=-\xi_0h_0-\xi_1h_1-\cdots-\xi_{k-1}h_{k-1}.$$ Applying the same recurrence at successive shifts expresses every later column $h_{k+1},\ldots,h_{d-1}$ in the span of $h_0,\ldots,h_{k-1}$. Hence every column of $\mathcal H_d$ would lie in a space of dimension at most $k$, forcing $$\mathop{\mathrm{rank}}\mathcal H_d\leq k<d,$$ a contradiction. The from-start order is therefore at least $d$, and the Cayley--Hamilton upper bound makes it exactly $d$.

There are two independent rank steps in this argument. Entrywise multiplication gives $$(\mathcal O_C\mathcal R_C)_{ij}
=e_1^{\mathsf{T}}C^iC^j\mathbf{1}=s_{i+j},$$ and the two cyclicity tests make both square factors invertible, so the Hankel matrix has full rank. Equivalently, $$\det\mathcal H_d=(\det\mathcal O_C)(\det\mathcal R_C)\ne0;$$ this is the exact point at which the fixed state and fixed covector meet. For the recurrence contradiction, the first $d$ shifted equations are exactly the $d$ components of the relation for $h_k$. Shifting once more gives the analogous relation for $h_{k+1}$, and repetition places every column through $h_{d-1}$ in the span of the first $k$. Thus the rank loss follows from the assumed from-start range itself; it is not imported from positivity or from a general realization-minimality assertion.

## Eventual recurrence order

Suppose instead that a nonzero relation of order $k<d$ held for every $n\geq n_0$: $$\sum_{j=0}^k f_j s_{n+j}=0,\qquad f_k\ne0.$$ Set $f(t)=\sum_{j=0}^k f_jt^j$. Lemma L13 gives $$s_{n+j}
=\gamma\rho^{n+j}+O(\theta^{n+j})
=\gamma\rho^n\rho^j+O(\theta^n)$$ for each fixed $0\leq j\leq k$; the constant implicit in the final error may depend on $j$, but the set of shifts is finite. Summing with the fixed coefficients gives $$\sum_{j=0}^k f_js_{n+j}
=\gamma\rho^nf(\rho)+O(\theta^n).$$ This identity is used only for $n\geq n_0$, where the assumed relation makes its left side zero. Divide by $\rho^n$ and let $n\to\infty$. Since $\theta/\rho<1$ and $\gamma>0$, we obtain $f(\rho)=0$. The polynomial $f$ is nonzero and has degree $k<d$, which is impossible because the minimal polynomial of $\rho$ has degree $d$. No smaller recurrence can hold even on a tail. This completes the proof of Lemma L14.

The leading coefficient $f_k$ could be normalized to one, but only its nonvanishing is needed to ensure $\deg f=k<d$. Because the number of shifts $j$ is finite, their error constants combine into one $O(\theta^n)$ term. The threshold $n_0$ is immaterial when the normalized identity is sent to infinity along its valid tail. If $f(\rho)$ were nonzero, that identity would converge to the nonzero value $\gamma f(\rho)$, contradicting its identically zero left side.

## Conceptual distinction

Matrix size $d$, algebraic degree $d$, and scalar recurrence order $d$ are therefore three separately proved conclusions: irreducibility connects the first two, while cyclic reachability and observability connect the matrix to the scalar sequence.

The dependency audit has four separate chains. Literal gradients, chambers, carry comparisons, and positive-semiring survival establish the exact degree identity; the selected matrix alone does not. Roots-of-unity residues, the congruence for $b$, the binomial audit, and the rational lift establish irreducibility and algebraic degree. Strict positivity and the visible Perron projection then give the dynamical-degree limit. Finally, cyclic reachability and observability, Hankel rank, and the tail asymptotic exclude shorter recurrences. All four conclusions use the same $d$, but numerical agreement replaces none of these links; matrix size alone proves neither algebraic degree nor scalar minimality.

# Sharpness, positioning, limitations, and conclusion {#sec:sharpness}

## Rank-$d$ attainment

For every constructed $d\geq2$, the selected stacked row rank equals $d$ and the nonunit characteristic degree equals $d$. Thus Structural Theorem S is attained existentially at rank $r=d$.

Use the selected presentations $$D=-I_d+I_d(D+I_d),\qquad
B_0=-I_d+(b\mathbf{1})\mathbf{1}^{\mathsf{T}}.$$ In the notation of Structural Theorem S, one may take $$\mathsf P=I_d,\quad \mathsf Q=D+I_d,\qquad
\mathsf R=b\mathbf{1},\quad \mathsf S=\mathbf{1}^{\mathsf{T}}.$$ The matrix $D+I_d$ is diagonal with nonzero diagonal entries $a_i+1$, hence invertible. Therefore $$\mathop{\mathrm{rank}}\begin{bmatrix}D+I_d\\ \mathbf{1}^{\mathsf{T}}\end{bmatrix}=d.$$ The first $d$ rows already have rank $d$, and stacking the additional row $\mathbf{1}^{\mathsf{T}}$ cannot raise the rank beyond the number of columns. Thus $r=d=N$. This rank equality alone only removes the unit factor forced by Structural Theorem S; it does not rule out a unit root in the reduced degree-$d$ determinant. Lemma L12 supplies that separate obligation: $\chi_C$ is irreducible of degree $d\geq2$, so it cannot contain the linear factor $t-1$. Its entire degree is therefore nonunit, and the upper bound $r=d$ is attained.

Here attainment compares two quantities attached to the displayed selected presentation. Invertibility of $D+I_d$ proves that its stacked row rank is $r=d$; it is not a computation of $\mathop{\mathrm{rank}}(C-I_d)$ or a minimization over presentations. Irreducibility separately proves that the nonunit part has degree $d$. Neither fact alone supplies the asserted equality.

Lemma L15 proves Corollary C and the sixth conjunct of Theorem H. The statement is existential for the displayed selected family. It does not assert sharpness for every presentation, and it supplies no rank-zero or rank-one Hamiltonian sharpness construction. Nor does it establish minimal ambient dimension or optimal support sparsity.

## Positioning after subtraction

The complete contribution is narrower than broad affine-triangular realization. Affine-triangular work permits a much larger range of maps and dynamical degrees [@BvS], while the dimension-four analysis isolates questions special to that ambient dimension [@SS]. Spectral and twisted-map frameworks address algebraicity through different geometric structures [@DF; @AX]. Our statement is instead about one explicit Hamiltonian product-shear grammar and the simultaneous validity of a support-rank ceiling, exact ordinary-degree visibility, irreducible Perron degree, and scalar minimality.

The Hamiltonian literature explains why position and momentum shears are useful building blocks [@BT; @KL], but the present iterate proof depends on the particular product and spike supports and on strict chamber inequalities. Examples of polynomial and birational degree growth illustrate the breadth of possible behavior beyond those supports [@Des]. The finite-field binomial result supplies a standard criterion whose hypotheses were checked here [@HS]; it is not a novelty claim. None of these contextual works is used as a substitute for a theorem-critical step.

The contribution is restricted to this joint interface, not presented as a priority claim for one ingredient. It concerns the displayed Hamiltonian gradient supports together with strict face control, exact forward ordinary-degree visibility, irreducible Perron degree, scalar minimality, and the support-row ceiling. Shear generation, the finite-field criterion, Perron theory, and realization tools retain their standard roles. The public citations locate those ingredients and neighboring map classes; they neither enlarge the family nor make the bounded screen exhaustive. The comparison is package-level and assumption-specific, with no component-firstness or additional literature claim.

## Limitations and open directions

Several boundaries are intrinsic to the statement. The family theorem uses a characteristic-zero field so that positive integer derivative coefficients remain nonzero. It treats the forward ordinary total degree of the displayed positive supports; arbitrary signs, coefficients, additional monomials, exponent profiles, or longer shear words are not covered. The structural theorem gives a lower bound on unit multiplicity, not an exact unit profile, because its reduced determinant can contain additional unit roots.

The construction is existential. It does not realize every Perron algebraic integer or every weak-Perron number, classify Hamiltonian polynomial automorphisms, or prove minimal dimension, optimal sparsity, genericity, nonconjugacy, or uniqueness. It makes no assertion about inverse degree, higher dynamical degrees, compactifications, entropy, integrability, or arithmetic orbits. It also gives no positive-characteristic version of the Hamiltonian family theorem; reduction modulo $p$ is an arithmetic irreducibility device, not a base-field extension of the dynamics.

It remains natural to ask which other gradient-compatible supports admit stationary strict chambers, whether comparable rank sharpness can occur with fewer monomials, and how inverse or higher dynamical degrees behave for related families. These are questions rather than conclusions of this article. The scalar result is limited to rational constant-coefficient recurrences; variable-coefficient and nonlinear recurrences are outside its scope.

The hypotheses used above have separate proof roles. Characteristic zero keeps the positive derivative coefficients nonzero after base change. The ordered lifts and strict chamber inequalities control support selection and fixed-coordinate visibility, while coefficient positivity prevents cancellation of the selected top forms. Strict positivity of $C$ supplies both cross-block domination and the Perron projection. The residue multiset and the congruence for $b$ enter only the modular irreducibility argument. Finally, the row-space factorization gives the structural ceiling independently of this arithmetic, whereas irreducibility and the two cyclicity arguments show that the constructed scalar sequence reaches the full algebraic complexity allowed by that ceiling.

This division of hypotheses is a failure map for the present proof, not a list of necessary conditions or counterexamples. Without characteristic zero, the positive-semiring step no longer certifies nonvanishing derivative coefficients. With changed signs, supports, or exponents, the chamber and noncancellation arguments no longer establish the literal recursion. Without the residue multiset and congruence for $b$, the arithmetic calculation no longer gives the binomial reduction used here. Without strict positivity, the stated Perron argument no longer supplies the visible dominant term; without both cyclicity tests, the Hankel proof no longer certifies scalar minimality. These are limits of the present derivation, not claims that the conclusions fail or that another proof under broader hypotheses is impossible.

## Conclusion

For every $d\geq2$, the displayed potentials produce a polynomial Hamiltonian product shear whose literal iterates are governed exactly by the positive matrix $C=b\mathbf{1}a^{\mathsf{T}}-D$. The two-level chamber proof separates support selection from fixed-coordinate visibility, defeats both temporal carries, and uses positivity in the coefficient semiring to turn the proposed matrix evolution into exact ordinary degrees from the identity seed.

The roots-of-unity residues and the congruence for $b$ reduce the characteristic polynomial to an irreducible binomial without dropping the $d=2$ or $4\mid d$ boundaries. Consequently the first dynamical degree is a Perron algebraic integer of degree $d$. Independent reachability and observability arguments make the visible degree sequence have exact recurrence order $d$ from the start and on every tail.

Finally, the support-row factorization bounds the nonunit characteristic degree by the stacked row rank while allowing extra unit roots in general. The constructed selected presentation has rank $d$ and an irreducible nonunit characteristic polynomial of degree $d$, so it attains that ceiling at every constructed rank. Exact support control and scalar observability are both necessary: the former validates the polynomial orbit, and the latter ensures that its full algebraic complexity remains visible in one fixed coordinate.
