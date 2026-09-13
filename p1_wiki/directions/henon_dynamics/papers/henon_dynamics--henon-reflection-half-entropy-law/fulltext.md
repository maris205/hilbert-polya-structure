---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-reflection-half-entropy-law"
canonical_tex: "henon_dynamics/henon_reflection_half_entropy_law/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_reflection_half_entropy_law/paper/paper.pdf"
source_sha256: "21ef7bd52e1d14babf49835b4a70964059591de24fff78042cd81aee286d742e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Half-Entropy Law for Primitive Reflection Orbits in the Hénon H6 Survivor

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_reflection_half_entropy_law>)
- [规范 TeX](<../../../../../henon_dynamics/henon_reflection_half_entropy_law/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_reflection_half_entropy_law/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_reflection_half_entropy_law/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_reflection_half_entropy_law/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine every primitive reflection-symmetric orbit in the frozen four-state symbolic survivor associated with the H6 Hénon model. Its adjacency matrix has a unique symbol involution implementing time reversal. Half-word transfer then gives one Fibonacci formula at odd periods and two Fibonacci--Lucas formulas for the parity classes at even periods. A divisor-sensitive Möbius inversion converts these fixed-word identities into exact primitive-necklace formulas. If $C_n$ is the number of all primitive cycles and $R_n$ the number admitting a reflection, then $$C_n\sim \frac{\varphi^n}{n},\qquad
   R_n=\Theta(\varphi^{n/2}),$$ where $\varphi=(1+\sqrt5)/2$. Thus the reflection subsystem has entropy exactly one half of the full survivor entropy and its primitive-cycle density is $O(n\varphi^{-n/2})$. Exact enumeration through period sixteen and an implementation-independent census through period twelve validate all parity and multiplicity conventions. The theorem concerns physical symbolic necklaces. It does not count roots or embeddings of the associated reflection closure polynomials; that algebraic population is a separate interface required by any Galois-height pressure theorem.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  A Half-Entropy Law for Primitive Reflection Orbits\
  in the Hénon H6 Survivor
```

## Markdown 正文

# Introduction

Time reversal often turns a periodic-orbit problem into a half-orbit problem. The reduction is geometrically attractive but combinatorially treacherous: odd and even periods have different reflection conjugacy classes, periodic words must be separated from primitive necklaces, and an even necklace is represented twice on a fixed parity axis. We resolve all three issues for a four-state survivor arising in the frozen H6 Hénon programme.

The immediate motivation is an interface obstruction. Earlier exact trace fields showed that the stable tail of one selected physical reflection orbit does not control a height summed over all nonphysical Galois embeddings. A natural next question is therefore whether the physical reflection family itself is sufficiently abundant to support a pressure construction. The answer obtained here is exact: the family is infinite and admits closed all-period formulas, but its entropy is only half that of the ambient survivor.

Our contributions are as follows.

1.  We identify the reversal permutation $\rho=(1\ 2)$ and prove the matrix identity $A=P A^{\mathsf T}P$.

2.  We derive transfer formulas for odd reflections and for both even axis-parity classes.

3.  We prove Möbius formulas for primitive reversible necklaces, including the factor $1/2$ forced at even periods.

4.  We prove the half-entropy law and exponential sparsity of reflection cycles among all primitive cycles.

5.  We independently enumerate the system and lock the physical axis labels of the period-eight families used by the predecessor trace-field analysis.

The symbolic and periodic-orbit context is standard [@Bowen1975; @ParryPollicott1990]; periodic data also play their familiar cohomological role [@Livshits1972]. The contribution here is the exact specialization, parity resolution and interface statement for the frozen H6 object. No prime table, zeta-zero table or fitted entropy is used.

Sections 2--4 derive the exact formulas. Section 5 proves the entropy theorem. Sections 6--8 give the finite audit, the Galois claim boundary and the reproducibility contract.

# The survivor and its reversal

Let $\Sigma_A$ be the edge shift on the alphabet $\{0,1,2,3\}$ with $$\label{eq:adjacency}
A=
\begin{pmatrix}
1&0&1&0\\
1&0&0&0\\
0&1&0&1\\
0&1&0&0
\end{pmatrix}.$$ Write $\rho=(0)(1\ 2)(3)$ and let $P$ be its permutation matrix.

[\[prop:reversal\]]{#prop:reversal label="prop:reversal"} The involution $\rho$ is the unique symbol permutation satisfying $$\label{eq:reversal}
A=P A^{\mathsf T}P.$$ Consequently, for every cyclic admissible word $w=(w_j)_{j\in\mathbb Z/n}$, $$\label{eq:Rk}
(R_k w)_j=\rho(w_{-j-k})$$ is again admissible, and $R_k^2=1$.

Direct multiplication proves [\[eq:reversal\]](#eq:reversal){reference-type="eqref" reference="eq:reversal"}. Exhaustion of the $4!$ symbol permutations proves uniqueness. In entry form the identity is $A_{ij}=A_{\rho(j),\rho(i)}$, which reverses every admissible edge; applying $\rho$ twice proves the involution statement.

The characteristic polynomial factors as $$\label{eq:charpoly}
\det(zI-A)=(z^2+1)(z^2-z-1).$$ Let $F_m$ and $L_m$ denote the Fibonacci and Lucas sequences with $F_0=0,F_1=1$ and $L_0=2,L_1=1$. Taking powers in [\[eq:charpoly\]](#eq:charpoly){reference-type="eqref" reference="eq:charpoly"} gives the closed-word identity $$\label{eq:closed}
N_n:=\operatorname{tr}(A^n)=L_n+2\cos(\pi n/2).$$

For even periods we name the two classes *edge--edge* ($\mathrm{EE}$) and *vertex--vertex* ($\mathrm{VV}$) according to the physical Hénon closure used in the predecessor project. These names should not be inferred merely from which vertices of an abstract $n$-gon are fixed by [\[eq:Rk\]](#eq:Rk){reference-type="eqref" reference="eq:Rk"}. The exact word locks in Section 6 remove that possible convention ambiguity.

# Half-word transfer formulas

Define the column vectors $$u=(1,0,0,1)^{\mathsf T},\qquad
v=(1,0,1,0)^{\mathsf T},\qquad
\ell=(1,1,0,0)^{\mathsf T}.$$ Here $u$ selects symbols fixed by $\rho$, while $v_i=A_{i,\rho(i)}$ and $\ell_i=A_{\rho(i),i}$ encode the two possible axis-edge conditions.

[\[thm:fixed\]]{#thm:fixed label="thm:fixed"} For $n=2m+1$, every $R_k$ is conjugate under cyclic rotation and $$\label{eq:odd-fixed}
|\operatorname{Fix}(R_k)|=u^{\mathsf T}A^m v=F_{m+2}.$$ For $n=2m$, the even and odd values of $k$ form two conjugacy classes. With the physical labels fixed above, their cardinalities are $$\begin{aligned}
G_m&:=|\operatorname{Fix}(R_k)|_{\mathrm{EE}}=u^{\mathsf T}A^m u=L_m,
\label{eq:edge-fixed}\\
H_m&:=|\operatorname{Fix}(R_k)|_{\mathrm{VV}}=\ell^{\mathsf T}A^{m-1}v \notag\\
&=F_m+\frac25L_m-\frac45\cos(\pi m/2)
       -\frac25\sin(\pi m/2).
\label{eq:vertex-fixed}\end{aligned}$$

For odd $n$, multiplication by two is invertible modulo $n$, hence all reflections are rotationally conjugate. A fixed word consists of a free half-path, one $\rho$-fixed central symbol and one closing axis edge. Reading that path gives $u^{\mathsf T}A^m v$.

For even $n$, the parity of $k$ is invariant under rotational conjugacy. One class has two $\rho$-fixed boundary symbols and gives $u^{\mathsf T}A^m u$; the other has two axis-edge constraints and gives $\ell^{\mathsf T}A^{m-1}v$. Diagonalizing $A$ using [\[eq:charpoly\]](#eq:charpoly){reference-type="eqref" reference="eq:charpoly"}, or checking the induced fourth-order recurrence and four initial values, yields the displayed Fibonacci--Lucas expressions.

The trigonometric terms in [\[eq:vertex-fixed\]](#eq:vertex-fixed){reference-type="eqref" reference="eq:vertex-fixed"} are integral-periodic corrections arising from the eigenvalues $\pm i$. In particular, although the formula contains fifths, its numerator is divisible by five for every integer $m$.

# Primitive necklaces and divisor-sensitive inversion

Let $C_n$ be the number of primitive cyclic necklaces in $\Sigma_A$. Since $N_n$ counts periodic points rather than necklaces, ordinary Möbius inversion gives $$\label{eq:primitive-all}
C_n=\frac1n\sum_{d\mid n}\mu(n/d)N_d.$$

For a divisor $d$, set $$f(d)=F_{(d+3)/2}\quad(d\text{ odd}),$$ and define $$f_{\mathrm{EE}}(d)=
\begin{cases}f(d),&d\text{ odd},\\G_{d/2},&d\text{ even},\end{cases}
\qquad
f_{\mathrm{VV}}(d)=
\begin{cases}f(d),&d\text{ odd},\\H_{d/2},&d\text{ even}.
\end{cases}$$

[\[thm:primitive\]]{#thm:primitive label="thm:primitive"} If $n$ is odd, the number of primitive reversible necklaces is $$\label{eq:primitive-odd}
R_n=\sum_{d\mid n}\mu(n/d)F_{(d+3)/2}.$$ If $n$ is even, the two physical axis counts are $$\label{eq:primitive-even}
R_n^{\mathrm{EE}}=\frac12\sum_{d\mid n}\mu(n/d)f_{\mathrm{EE}}(d),
\qquad
R_n^{\mathrm{VV}}=\frac12\sum_{d\mid n}\mu(n/d)f_{\mathrm{VV}}(d),$$ and $R_n=R_n^{\mathrm{EE}}+R_n^{\mathrm{VV}}$.

First subtract all words of proper period by Möbius inversion while keeping the reflection operator fixed. A primitive necklace cannot be stabilized by two distinct reflections: their product would be a nontrivial stabilizing rotation. At odd period, multiplication by two is invertible modulo $n$, so the $n$ rotated representatives distribute one-to-one across the $n$ reflection axes. Thus the primitive fixed-word count for one axis already equals the number of reversible necklaces, proving [\[eq:primitive-odd\]](#eq:primitive-odd){reference-type="eqref" reference="eq:primitive-odd"}.

At even period, rotation preserves axis parity. There are $n/2$ axes of each parity, and a primitive reversible necklace of a fixed parity contributes two rotated representatives to every compatible fixed-axis census. Dividing the Möbius-inverted fixed-word count by two proves [\[eq:primitive-even\]](#eq:primitive-even){reference-type="eqref" reference="eq:primitive-even"}. The definition of $f_{\mathrm{EE}},f_{\mathrm{VV}}$ is essential: an even-period word inherited from an odd proper divisor belongs to the single odd-period reflection class before it is lifted.

This proof also explains why a parity-blind necklace formula is wrong. The factor $1/2$ and the odd-divisor branch are geometric multiplicities, not normalization choices.

# The half-entropy law

Put $\varphi=(1+\sqrt5)/2$. The bounded $\pm i$ contribution in [\[eq:closed\]](#eq:closed){reference-type="eqref" reference="eq:closed"} and the Binet formulas imply $N_n=\varphi^n+O(1)$. Every proper divisor of $n$ is at most $n/2$, so [\[eq:primitive-all\]](#eq:primitive-all){reference-type="eqref" reference="eq:primitive-all"} yields $$\label{eq:full-asymptotic}
C_n=\frac{\varphi^n}{n}+O(\varphi^{n/2}).$$

[\[thm:entropy\]]{#thm:entropy label="thm:entropy"} The primitive reflection population satisfies $$\label{eq:reflection-growth}
R_n=\Theta(\varphi^{n/2}).$$ Consequently, $$\label{eq:entropy}
\lim_{n\to\infty}\frac1n\log C_n=\log\varphi,
\qquad
\lim_{n\to\infty}\frac1n\log R_n=\frac12\log\varphi,$$ and $$\label{eq:density}
\frac{R_n}{C_n}=O\!\left(n\varphi^{-n/2}\right).$$

For odd $n$, the leading term in [\[eq:primitive-odd\]](#eq:primitive-odd){reference-type="eqref" reference="eq:primitive-odd"} is $F_{(n+3)/2}=\Theta(\varphi^{n/2})$, while every proper odd divisor is at most $n/3$. For even $n$, both $G_{n/2}$ and $H_{n/2}$ have positive leading constant times $\varphi^{n/2}$; all proper-divisor terms in [\[eq:primitive-even\]](#eq:primitive-even){reference-type="eqref" reference="eq:primitive-even"} are $O(\varphi^{n/4})$. This proves [\[eq:reflection-growth\]](#eq:reflection-growth){reference-type="eqref" reference="eq:reflection-growth"}. Equations [\[eq:entropy\]](#eq:entropy){reference-type="eqref" reference="eq:entropy"} and [\[eq:density\]](#eq:density){reference-type="eqref" reference="eq:density"} follow from [\[eq:full-asymptotic\]](#eq:full-asymptotic){reference-type="eqref" reference="eq:full-asymptotic"}.

The result is an all-period theorem. Finite counts are used below only to audit conventions, not to infer either exponential rate.

# Exact census and axis locks

Table [1](#tab:census){reference-type="ref" reference="tab:census"} records representative exact values. Dashes denote the single reflection class at odd period.

::: {#tab:census}
    $n$   $C_n$   $R_n$   $R_n^{\mathrm{EE}}$   $R_n^{\mathrm{VV}}$
  ----- ------- ------- --------------------- ---------------------
      7       4       4                    --                    --
      8       5       3                     2                     1
     12      25      11                     6                     5
     16     135      37                    20                    17
     20     750     102                    55                    47

  : Selected primitive-cycle counts from the exact formulas.
:::

The period-eight words connecting this theorem to the trace-field families are $$A_8=00000021,\qquad B_8=00000231.$$ Direct application of [\[eq:Rk\]](#eq:Rk){reference-type="eqref" reference="eq:Rk"} gives reflection shifts $3$ and $4$, respectively. The frozen physical convention therefore locks $A_8$ to the $\mathrm{VV}$ family and $B_8$ to the $\mathrm{EE}$ family.

The primary implementation computes all formula rows through $n=32$ and generates primitive necklaces by adjacency-guided depth-first search through $n=16$. A second implementation enumerates the Cartesian word space through $n=12$ and reconstructs the transfer formulas from matrix powers. Both agree exactly. These checks catch a swapped axis label, omission of the even factor $1/2$, deletion of odd proper divisors and replacement of the bounded $\pm i$ spectral contribution.

# What the theorem does and does not bridge

Theorem [\[thm:entropy\]](#thm:entropy){reference-type="ref" reference="thm:entropy"} supplies a complete physical reflection census. It shows that a reflection-only pressure built with uniformly subexponential weights cannot reproduce the full survivor pressure: the missing exponential rate is $(1/2)\log\varphi$. Any successful compilation must therefore add an exponentially compensating algebraic multiplicity or weight.

That statement is not a Galois theorem. A physical symbolic necklace is one dynamical orbit. A reflection closure polynomial may have many roots, and its trace field may have many real embeddings. Neither its degree nor the height of those embeddings is counted by $R_n$. In particular, $$\text{physical reflection entropy}
\quad\not\Rightarrow\quad
\text{algebraic-conjugate entropy or Galois pressure}.$$

The next legitimate bridge is consequently a reflection dynatomic theorem: factor the algebraic closure by exact primitive period, determine the reduced degree and compare its exponential rate with $(1/2)\log\varphi$. This is a new algebraic object, not a rephrasing of the present symbolic count.

For the Route-A evaluation, the result is an analytic $A1$ theorem for the reflection subsystem and inherits the predecessor's physical determinant structure. It does not identify rational primes, produce a completed determinant or authorize Route B.

# Reproducibility and hostile controls

The primary checker verifies six predecessor hashes, the reversal matrix identity, the characteristic polynomial, every formula row through period $32$, direct primitive-necklace agreement through period $16$, both physical axis locks and eighteen claim mutations. The independent checker imports no primary functions and performs a Cartesian enumeration through period $12$. Seven unit tests lock the formulas, selected census rows, entropy labels and claim firewall. The complete command is

    bash code/run_c59.sh

All counting arithmetic is integral. The displayed decimal value of $\varphi$ is diagnostic only. The two hostile-review passes specifically tested axis swapping, period/nonprimitive conflation, the even multiplicity factor and an attempted promotion from symbolic cycles to Galois embeddings. No cross-model upload was used for this unpublished draft.

# Conclusion

The H6 survivor admits an exact reflection compiler: one reversal involution, three half-word transfer formulas and a parity-sensitive primitive inversion. Its reversible primitive cycles have entropy $(1/2)\log\varphi$, exactly half the ambient value, and hence exponentially vanishing density.

This closes the physical counting question exposed by the preceding Galois interface obstruction. It also makes the next question sharper. The only possible exponential compensation must come from algebraic multiplicity or height, so the next object is the primitive reflection dynatomic quotient and not another finite physical census.

# Machine-checked formula ledger

The certificate freezes the following identities: $$\begin{aligned}
\operatorname{tr}(A^n)&=L_n+2\cos(\pi n/2),\\
|\operatorname{Fix}(R_k)|_{n=2m+1}&=F_{m+2},\\
|\operatorname{Fix}(R_k)|_{n=2m,\mathrm{EE}}&=L_m,\\
|\operatorname{Fix}(R_k)|_{n=2m,\mathrm{VV}}
 &=F_m+\frac25L_m-\frac45\cos(\pi m/2)
   -\frac25\sin(\pi m/2),\\
C_n&=\frac1n\sum_{d\mid n}\mu(n/d)\operatorname{tr}(A^d),\\
R_n\ (n\text{ odd})&=\sum_{d\mid n}\mu(n/d)F_{(d+3)/2},\\
R_n^\star\ (n\text{ even})
 &=\frac12\sum_{d\mid n}\mu(n/d)f_\star(d),
 \qquad \star\in\{\mathrm{EE},\mathrm{VV}\}.\end{aligned}$$ The canonical core SHA-256 is

68ba84a039ca5eaf774ce669975af7fe65df9246e9f8f8deca23ac4c10a5f39d.

The independent result SHA-256 is

d7afd772d072b490a4c72f9c6a3f4e7a614a4117bee6e6b3caf2a20be9c7739c.
