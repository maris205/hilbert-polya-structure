---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--26-pure-power-selector-atom-collapse"
canonical_tex: "symbolic_dynamics/papers/26-pure-power-selector-atom-collapse/main.tex"
canonical_pdf: "symbolic_dynamics/papers/26-pure-power-selector-atom-collapse/main.pdf"
source_sha256: "6722011e691f5323f40ae8ef801143b05d865438fd3abbae545afa75e229223c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Pure-Power Cyclic Selectors over Holomorphic Renewal: Exact Incidence Cancellation and Semisimple Atom-Block Collapse

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/26-pure-power-selector-atom-collapse>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/26-pure-power-selector-atom-collapse/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/26-pure-power-selector-atom-collapse/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/26-pure-power-selector-atom-collapse/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/26-pure-power-selector-atom-collapse/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Paper25 removed the fixed-point denominator of each logarithmic-code return with a canonical holomorphic zero-/one-form grading, but every mixed return necklace survived on a shared renewal component. We test the remaining loophole: a cyclic selector with coefficient one on every nonempty monochromatic word and zero on every mixed word, at all repetitions. Two exact constructions exist. A reduced-support exterior fiber gives the coefficient orbitwise, and coordinate projectors give a stationary trace realization. We then prove the cost of stationarity. For $m$ supplied colors, the selector has Hankel rank $m$, or $m+1$ under the literal language empty-word convention, and observable syntactic algebra $\mathbb C^m$, respectively $\mathbb C^{m+1}$. Every finite ordinary trace realization semisimplifies to one active character per color plus dormant modules; every even graded realization has the same virtual class, up to matched parity sectors and trace-invisible radical extensions. Hence its full graded determinant is exactly the product of color factors. Tensoring with the holomorphic de Rham sector yields an honest countable trace-class family on $\Re s>1$, but it is unitarily the disjoint supplied atom inventory. A deterministic audit passes 58/58 tests over 51,734 exact rows and shows why aggregate commuting power traces are insufficient. The selector problem is solved; arithmetic source selection, continuation, and a spectral mechanism are not. Route A is therefore rejected.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  Pure-Power Cyclic Selectors over Holomorphic Renewal:\
  Exact Incidence Cancellation and Semisimple Atom-Block Collapse
```

## Markdown 正文

# Introduction {#sec:introduction}

A shared renewal system has an economical state space and an expensive orbit ledger. Once two completed returns are legal from the same recurrent state, their alternating concatenations produce mixed primitive necklaces. The holomorphic exterior grading studied in the preceding step cancels local tangent stability exactly, but it does not alter this symbolic fact. The remaining question is therefore concrete: can a source-derived cyclic coefficient delete every mixed return word, including all repetitions, while retaining the pure returns with coefficient one?

Fix a finite alphabet $A_m=\{a_1,\ldots,a_m\}$. For a nonempty word $w$, write $$\chi_m(w)=
 \begin{cases}
  1,&|\operatorname{supp}(w)|=1,\\
  0,&|\operatorname{supp}(w)|\ge2.
 \end{cases}
 \label{eq:intro-selector}$$ This coefficient is cyclic and satisfies $\chi_m(w^r)=\chi_m(w)$ for every $r\ge1$. It is exactly the ledger needed to turn a shared full-return trace expansion into pure color factors. The positive part of our answer is immediate but nontrivial: $\chi_m$ has both a support-incidence exterior realization and a stationary positive projector realization. The negative part is the paper's main content: every finite stationary trace realization has the same observable color memory as those projectors.

The conclusion is not that the matrices must literally be diagonal. They may contain noncommuting upper-triangular extensions, and an even/odd realization may contain arbitrary matched sectors. Cyclic traces cannot see these additions. What is rigid is the semisimplified virtual character and the determinant it controls: one net one-dimensional color character per supplied label. This distinction lets us state a strong collapse theorem without turning character data into an unsupported operator-conjugacy claim.

The main contributions are four falsifiable statements.

1.  We give two exact all-repetition selectors. For the completed support $S=\operatorname{supp}(w)$, the reduced exterior space has superdimension $(1-1)^{|S|-1}$. On a fixed $m$-dimensional space, orthogonal coordinate projectors have word trace $\chi_m(w)$.

2.  We compute the full recognizable memory. The Hankel rank is $m$ when $\chi_m(\varepsilon)=m$, the completion natural for a matrix character, and $m+1$ when $\chi_m(\varepsilon)=0$, the characteristic series of the nonempty language. The corresponding syntactic algebras are $\mathbb C^m$ and $\mathbb C^{m+1}$. Thus no fixed finite recognizer works while the number of supplied colors grows.

3.  We prove ordinary and graded character-rigidity theorems. Every ordinary realization contains one active simple per color after semisimplification. Every even $\mathbb Z/2$-graded realization has that same net class; dormant modules, parity-matched modules, and radicals exhaust the trace-invisible freedom. The full multivariable graded determinant is therefore $\prod_i(1-zx_i)$.

4.  We tensor this selector with the logarithmic-code holomorphic de Rham sector. The degreewise operator sums are trace class when the supplied weights are in $\ell^1$, hence for $u=1$ and $\Re s>1$. Their graded determinant is $\prod_n(1-zu^{\ell(n)}n^{-s})$, but the coordinate fiber makes the operator unitarily a direct sum of private color blocks. Exact arbitrary-inventory controls certify that this construction selects primes, composites, squares, and unrelated deterministic inventories equally well.

A technical firewall is essential. Independent word coefficients must be checked before the color variables commute. We exhibit a three-color graded representation for which all tested power traces of the commuting pencil are correct, while the two oppositely oriented words $012$ and $210$ have supertraces $+1$ and $-1$. Abelianization makes their monomials equal and hides the error. This counterexample prevents a correct scalar Euler product from being used as evidence for a correct cyclic branch ledger.

The result is deliberately source scoped. The arithmetic starting point is the full-shift semiring relation, and the analytic return branches retain a self-delimiting logarithmic integer code. Prime labels may be substituted as one inventory, but no theorem derives that inventory from the selector. No target-zero data, continuation through the trace-class boundary, self-adjoint carrier, or Route-B object appears.

The rest of the paper proceeds from algebra to analysis. fixes the classical boundary. construct the selector and compute its minimal memory. proves semisimple and virtual rigidity. derives the determinant and the aggregate counterexample. audits canonical complexes, and performs the holomorphic tensor and countable limit. record the exact evidence and strict route verdict.

# Literature and theorem boundary {#sec:literature}

The individual tools used below are classical. The contribution lies in putting their sharp versions against one frozen cyclic coefficient and then following that coefficient into the holomorphic transfer determinant.

#### Recognizable series and minimal realization.

Finite linear representations of noncommutative series originate in the automata framework of @schutzenberger1961automata. Hankel rank is the minimal linear-state dimension [@carlyle1971realizations], and modern treatments organize the residual, rational, and syntactic-algebra viewpoints together [@berstel2010noncommutative]. The formal-series and syntactic algebra theory of @reutenauer1980syntactiques already relates central rational series, finite-dimensional syntax, and character combinations. We use these results as boundaries, then compute the two exact Hankel ranks and diagonal syntactic algebras for [\[eq:intro-selector\]](#eq:intro-selector){reference-type="eqref" reference="eq:intro-selector"}. We do not present the general equivalence between rationality and recognizability as new.

#### Cyclic languages and virtual characters.

The nonempty pure-power language is regular and cyclic. The theorem of @berstel1990zeta places characteristic series of regular cyclic languages in an integral span of finite trace series and derives rational zeta consequences. @masuda2015characters recover the virtual-character statement through monoid character theory over arbitrary fields. Hence the existence of some signed trace realization is prior art. Our narrower result classifies every finite complex matrix-trace realization of this coefficient, including the dormant empty-word ambiguity and the radical that characters cannot detect.

#### Exterior automata and categorical traces.

Exterior powers of deterministic automata already yield alternating determinant formulas for sofic zeta functions [@beal1995exterior]. Recent work packages recognizable word and circle evaluations in one-dimensional TQFT or decorated-cobordism categories [@gustafson2023automata; @khovanov2024cobordisms]. These results rule out a broad priority claim for exterior cancellation or categorical trace packaging. The support exterior fiber below has a different, elementary role: it computes the exact coefficient from the completed support, after which we ask whether a fixed stationary compilation can avoid color memory.

#### Bar and Hochschild complexes.

The bar construction and Hochschild theory provide canonical cyclic invariants [@hochschild1945cohomology; @loday1998cyclic]. For a separable algebra, positive Hochschild degrees vanish, a fact also organized among additive invariants by @tabuada2016separable. Applied to $\mathbb C^m$, this calculation is exact and decisive: the only homological survivors are the $m$ primitive color idempotents. It gives a canonical selector only after the atom split is supplied.

#### Holomorphic transfer determinants.

The analytic layer inherits periodic-word trace expansions from transfer operator theory [@ruelle1976zeta], the trace-class determinant calculus [@simon1977determinants], and nuclearity estimates for holomorphic composition/transfer operators on Bergman spaces [@bandtlow2008eigenvalue]. The logarithmic history uses Elias's self-delimiting integer code [@elias1975universal]. We do not reopen the local fixed-point calculation. The new question is whether tensoring the already-proved local de Rham cancellation with the color selector creates a shared analytic object or merely reinstates disjoint blocks.

L31mm L48mm Y Mechanism & Classical boundary & SD-C28 specialization\
Recognizable cyclic series & finite traces, Hankel minimization, semisimple syntax & exact ranks $m/m+1$ and algebras $\mathbb C^m/\mathbb C^{m+1}$\
Virtual characters & regular cyclic languages admit signed trace expressions & every finite even realization has one net color simple\
Exterior automata & alternating determinants for supplied finite presentations & reduced-support coefficient is exact but word-indexed\
Brauer--Nesbitt principle & characters determine semisimplification & dormant, matched, and radical freedoms are isolated explicitly\
Separable Hochschild theory & positive homology vanishes & successful stationary algebra has only supplied atom classes\
Holomorphic Fredholm theory & trace-class operators and periodic trace logs & color tensor is an honest but disjoint atom product\

We did not locate a source stating this full selector-rigidity and source-locked Fredholm collapse as one theorem. Terminology varies among cyclic, circular, central, recognizable, and pseudocharacter series, so this negative search result is not a claim of global priority. The algebraic ingredients are short consequences of classical theory; the strongest new content is their exact coupling to the shared-renewal obligation, the wordwise/aggregate firewall, and the countable holomorphic collapse.

# Frozen coefficient and two exact selectors {#sec:selectors}

## Wordwise and empty-word conventions

Let $A_m^+$ denote the positive words in $A_m$. The support of a word is the set of letters that occur in it.

For $w\in A_m^+$, define $$\chi_m(w)=\mathbf 1_{\{|\operatorname{supp}(w)|=1\}}.
 \label{eq:chi-definition}$$ The equality in [\[eq:chi-definition\]](#eq:chi-definition){reference-type="eqref" reference="eq:chi-definition"} is imposed on each individual positive word before any commuting color variables are introduced.

Cyclic rotation does not change support, and $\operatorname{supp}(w^r)=\operatorname{supp}(w)$. Thus $\chi_m$ is an exact cyclic and all-repetition coefficient. The empty word needs a separate convention.

We use two extensions to $A_m^*=A_m^+\cup\{\varepsilon\}$.

1.  The *character convention* sets $\chi_m(\varepsilon)=m$, the identity trace on the canonical color fiber.

2.  The *language convention* sets $\chi_m(\varepsilon)=0$, so the series is the characteristic series of the nonempty pure-power language.

The empty word never occurs in a determinant trace logarithm, but it changes minimal linear realization by one dormant mode.

This distinction also separates two theorem classes. A general recognizable series may have a bilinear readout $f(w)=\alpha\mu(w)\beta$; its minimal dimension is controlled by the Hankel matrix. The character theorem in assumes instead that the coefficient is a matrix trace or supertrace of a stationary multiplicative representation. No character classification is asserted for an arbitrary bilinear readout.

## An orbitwise support-incidence coefficient

For a nonempty finite set $S$, define its reduced permutation space $$Q_S=\ker\!\left(\mathbb C^S\xrightarrow{\sum}\mathbb C\right),
 \qquad \dim Q_S=|S|-1.
 \label{eq:reduced-support}$$ Give $\Lambda^\bullet Q_S$ the parity of exterior degree.

For every positive word $w$, $$\operatorname{Str}\!\left(I\mid\Lambda^\bullet Q_{\operatorname{supp}(w)}\right)
 =(1-1)^{|\operatorname{supp}(w)|-1}=\chi_m(w).
 \label{eq:support-euler}$$ The coefficient is invariant under cyclic rotation, relabeling, and repetition.

The alternating dimension is

$$\sum_{j=0}^{|S|-1}(-1)^j\binom{|S|-1}{j}=(1-1)^{|S|-1}.$$ For a singleton support, $\Lambda^0(0)=\mathbb C$, so the value is one; otherwise it is zero. The asserted invariances follow because only the cardinality of support occurs.

Equation [\[eq:support-euler\]](#eq:support-euler){reference-type="eqref" reference="eq:support-euler"} is a genuine positive answer to the coefficient problem, but it is not yet a stationary transfer representation. The fiber $Q_{\operatorname{supp}(w)}$ is selected after the completed word is known. With zero differential, the even and odd mixed-support classes cancel in Euler characteristic; they are not acyclic. We will not call this virtual cancellation a homological deletion.

## A stationary projector character

Let $V_m=\mathbb C^m$ with basis $e_1,\ldots,e_m$, and let $$P_i=e_ie_i^*,\qquad P_iP_j=\delta_{ij}P_i.
 \label{eq:projectors}$$

For $w=a_{i_1}\cdots a_{i_r}$, $$\operatorname{Tr}(P_{i_1}\cdots P_{i_r})=\chi_m(w).
 \label{eq:projector-selector}$$ The representation is positive, permutation-natural, and exact at every repetition.

If all letters agree, the product is $P_i$ and has trace one. If two colors occur, cyclically rotate the word until an unequal adjacent pair occurs; the corresponding projector product is zero, and cyclicity of trace gives the claim.

The construction is stationary, but its state space already contains one orthogonal recurrent line per supplied color. This observation does not by itself prove minimality: a different nonorthogonal or graded realization might appear smaller. The next two sections close precisely that loophole.

L37mm c c c Y Construction & exact words & repetitions & stationary & retained data\
Reduced-support exterior & yes & yes & no & completed support $S$\
Coordinate projectors & yes & yes & yes & one line per supplied color\

# Hankel memory and syntactic algebra {#sec:hankel}

The support automaton may remember every subset of colors, but the minimal linear memory is much smaller and still grows with $m$. Let

$$H_m(u,v)=\chi_m(uv),\qquad u,v\in A_m^*,$$

be the two-sided Hankel matrix under either empty-word convention.

[\[thm:hankel-rank\]]{#thm:hankel-rank label="thm:hankel-rank"} Over $\mathbb C$, $$\operatorname{rank}H_m=
 \begin{cases}
  m,&\chi_m(\varepsilon)=m,\\
  m+1,&\chi_m(\varepsilon)=0.
 \end{cases}
 \label{eq:hankel-ranks}$$

The submatrix with rows and columns indexed by the single letters satisfies

$$H_m(a_i,a_j)=\chi_m(a_ia_j)=\delta_{ij},$$

so its rank is $m$. Every residual following a nonempty pure prefix is one of the $m$ color residuals; a mixed prefix has the zero residual. Under the character convention, the empty residual is the sum of the color residuals, so the full rank is at most $m$. Under the language convention, the empty residual is independent: at the empty suffix it has value zero, whereas every color residual has value one. It adds one and no more. This proves [\[eq:hankel-ranks\]](#eq:hankel-ranks){reference-type="eqref" reference="eq:hankel-ranks"}.

By the Hankel realization theorem, the ranks in are the minimal dimensions for general bilinear linear representations, not only for trace realizations. In particular, no fixed finite-dimensional linear recognizer works for unbounded color inventories.

The same calculation can be stated intrinsically through the syntactic algebra. Let $R_m=\mathbb C\langle a_1,\ldots,a_m\rangle$.

[\[thm:syntactic-algebra\]]{#thm:syntactic-algebra label="thm:syntactic-algebra"} The syntactic algebra of the selector is $$\mathcal A_{\chi_m}\cong
 \begin{cases}
  \mathbb C^m,&\chi_m(\varepsilon)=m,\\
  \mathbb C^{m+1},&\chi_m(\varepsilon)=0.
 \end{cases}
 \label{eq:syntactic-algebra}$$ In the second line, the extra simple is dormant: every letter acts on it by zero.

For the character convention, let

$$\pi:R_m\longrightarrow\mathbb C^m,
 \qquad \pi(a_i)=e_i,$$

where the $e_i$ are primitive orthogonal idempotents, and put $\tau(v)=\sum_i v_i$. Then $\chi_m(w)=\tau(\pi(w))$. The context pairing on the image is

$$(v,w)\longmapsto\tau(vw)=\sum_i v_iw_i,$$

which is nondegenerate. Therefore the largest two-sided ideal invisible in all contexts is exactly $\ker\pi$, and the observable quotient is $\mathbb C^m$.

For the language convention, add a coordinate $e_0$. Send the algebra unit to $(1,\ldots,1)$, every $a_i$ to $e_i$, and use

$$\tau_0(v)=\sum_{i=1}^m v_i-mv_0.$$

The identity has value zero, every nonempty pure power has value one, and a mixed word maps to zero. The context form is diagonal with weights $(-m,1,\ldots,1)$, hence nondegenerate over $\mathbb C$. The quotient is $\mathbb C^{m+1}$, and all letters have zero $e_0$-coordinate.

Any finite recognizable construction for $\chi_m$ may contain redundant or exponentially large support memory, but its minimal observable quotient has one active coordinate per color. The language empty-word convention adds exactly one determinant-invisible coordinate.

L33mm c c Y Convention & Hankel rank & syntactic algebra & extra determinant content\
$\chi_m(\varepsilon)=m$ & $m$ & $\mathbb C^m$ & none\
$\chi_m(\varepsilon)=0$ & $m+1$ & $\mathbb C^{m+1}$ & dormant simple; letters act by zero\

The syntactic theorem closes the general recognizable-readout loophole. A stronger question remains for trace presentations: does the wordwise cyclic character force each color to survive as an actual simple factor, or could a smaller collection of noncommuting matrices emulate all traces? The next section proves the sharp semisimple answer.

# Ordinary and graded character rigidity {#sec:character}

For $0\le i\le m$, define one-dimensional $R_m$-modules by $$a_j\big|_{L_i}=\delta_{ij}\quad(i\ge1),
 \qquad
 a_j\big|_{L_0}=0.
 \label{eq:color-characters}$$ Put $\Lambda_m=\bigoplus_{i=1}^mL_i$. On every positive word, $$\operatorname{Tr}(w\mid\Lambda_m)=\chi_m(w),
 \label{eq:target-character}$$ while the identity trace is $m$.

[\[thm:ordinary-rigidity\]]{#thm:ordinary-rigidity label="thm:ordinary-rigidity"} Let $\rho:R_m\to\operatorname{End}(V)$ be finite dimensional over $\mathbb C$. If $$\operatorname{Tr}\rho(w)=\chi_m(w)\qquad(w\in A_m^+),
 \label{eq:ordinary-word-hypothesis}$$ then $$V^{\mathrm{ss}}\cong
 \Lambda_m\oplus L_0^{\oplus(\dim V-m)}.
 \label{eq:ordinary-semisimplification}$$ In particular, $\dim V\ge m$, and every active color character occurs once.

Let $d=\dim V-m$. The trace difference between $V$ and $\Lambda_m$ vanishes on the augmentation ideal spanned by positive words. If $d\ge0$, the characters of $V$ and $\Lambda_m\oplus L_0^{\oplus d}$ agree also at the identity. If $d<0$, compare instead $V\oplus L_0^{\oplus(-d)}$ with $\Lambda_m$. In either case the two representations factor through their finite-dimensional combined image algebra.

Quotient that image algebra by its Jacobson radical. The resulting complex semisimple algebra is a finite product of matrix algebras, and its irreducible trace functionals are linearly independent. Equality of characters therefore gives equality of semisimplifications. The case $d<0$ would put a positive $L_0$-multiplicity on the first side and no $L_0$ on the second, impossible because simple-module classes form a free basis of the Grothendieck group. Thus $d\ge0$, and [\[eq:ordinary-semisimplification\]](#eq:ordinary-semisimplification){reference-type="eqref" reference="eq:ordinary-semisimplification"} follows.

The proof is a finite-image form of the Brauer--Nesbitt principle. It uses the trace of every algebra element, obtained by linearity from every word; it does not infer a common eigenbasis for the original generators.

Now let $V=V_+\oplus V_-$ be $\mathbb Z/2$-graded and require each letter to act evenly.

[\[thm:graded-rigidity\]]{#thm:graded-rigidity label="thm:graded-rigidity"} If $$\operatorname{Str}\rho(w)=\chi_m(w)\qquad(w\in A_m^+),
 \label{eq:graded-word-hypothesis}$$ then $$-[V_-^{\mathrm{ss}}]
 =\sum_{i=1}^m[L_i]+d[L_0],
 \qquad d=\dim V_+-\dim V_- -m.
 \label{eq:virtual-class}$$ Equivalently, there are a semisimple module $W$ and integers $a,b\ge0$, $a-b=d$, such that $$V_+^{\mathrm{ss}}\cong W\oplus\Lambda_m\oplus L_0^{\oplus a},
 \qquad
 V_-^{\mathrm{ss}}\cong W\oplus L_0^{\oplus b}.
 \label{eq:virtual-decomposition}$$

Add $|d|$ dormant modules to the side required to match the identity trace. Dormant modules vanish on every positive word, so [\[eq:graded-word-hypothesis\]](#eq:graded-word-hypothesis){reference-type="eqref" reference="eq:graded-word-hypothesis"} and [\[eq:target-character\]](#eq:target-character){reference-type="eqref" reference="eq:target-character"} give equality of the full ordinary characters of the two enlarged sides. Apply the same finite combined-image argument as in , then cancel common simple multiplicities. This yields [\[eq:virtual-class\]](#eq:virtual-class){reference-type="eqref" reference="eq:virtual-class"} and [\[eq:virtual-decomposition\]](#eq:virtual-decomposition){reference-type="eqref" reference="eq:virtual-decomposition"}.

[\[prop:radical-counterexample\]]{#prop:radical-counterexample label="prop:radical-counterexample"} There are noncommuting, nonsplit realizations satisfying every word trace in [\[eq:ordinary-word-hypothesis\]](#eq:ordinary-word-hypothesis){reference-type="eqref" reference="eq:ordinary-word-hypothesis"}. Moreover, arbitrary common representations may be added in even and odd degree without changing a single supertrace.

Choose strictly upper-triangular matrices $N_i$ in a basis compatible with the projector diagonal and set $A_i=P_i+N_i$. Every product $A_w$ is upper triangular with diagonal equal to that of $P_w$. Hence $\operatorname{Tr}A_w=\operatorname{Tr}P_w=\chi_m(w)$, while the $A_i$ need not commute and the module need not split. The second statement follows because identical even and odd traces cancel word by word.

is the operative interpretation of the collapse. An implementation can look connected through its upper-triangular blocks, but no such connection changes the observable color character. Conversely, the theorem does not label radical geometry meaningless for every purpose; it says only that cyclic traces and the determinant considered here cannot use it to select arithmetic atoms.

# Full determinant and the aggregate firewall {#sec:determinant}

Let $$T_\pm(x)=\sum_{i=1}^m x_i\rho_\pm(a_i),
 \label{eq:weighted-color-pencil}$$ where the $x_i$ are independent commuting scalars. Independence is used only after the ordered-word trace identities have been imposed.

[\[thm:determinant-collapse\]]{#thm:determinant-collapse label="thm:determinant-collapse"} Every realization satisfying the wordwise hypothesis of obeys, for $r\ge1$, $$\operatorname{Str}T(x)^r=\sum_{i=1}^m x_i^r,
 \label{eq:pure-power-traces}$$ and $$\frac{\det(I-zT_+(x))}{\det(I-zT_-(x))}
 =\prod_{i=1}^m(1-zx_i).
 \label{eq:finite-color-product}$$

Expanding the $r$th power gives $$\operatorname{Str}T(x)^r
 =\sum_{i_1,\ldots,i_r}x_{i_1}\cdots x_{i_r}
   \operatorname{Str}\rho(a_{i_1}\cdots a_{i_r}).$$ Every mixed word has supertrace zero, and for each $i$ the pure word $a_i^r$ has supertrace one. This proves [\[eq:pure-power-traces\]](#eq:pure-power-traces){reference-type="eqref" reference="eq:pure-power-traces"}. The formal trace logarithm then gives $$\begin{aligned}
 \log\frac{\det(I-zT_+)}{\det(I-zT_-)}
 &=-\sum_{r\ge1}\frac{z^r}{r}\operatorname{Str}T^r\\
 &=-\sum_i\sum_{r\ge1}\frac{(zx_i)^r}{r}
 =\sum_i\log(1-zx_i),
 \end{aligned}$$ which exponentiates to [\[eq:finite-color-product\]](#eq:finite-color-product){reference-type="eqref" reference="eq:finite-color-product"}.

The left side of [\[eq:finite-color-product\]](#eq:finite-color-product){reference-type="eqref" reference="eq:finite-color-product"} is a graded determinant, or finite-dimensional Berezinian: a quotient of two ordinary determinants. It is not the ordinary determinant of the ungraded block sum, which equals

$$\det(I-z(T_+\oplus T_-))=\det(I-zT_+)\det(I-zT_-).$$

Radical extensions and common even/odd modules may remain in the operator presentation, but [\[eq:finite-color-product\]](#eq:finite-color-product){reference-type="eqref" reference="eq:finite-color-product"} shows that the full cyclic determinant has already forgotten them.

## Why a correct scalar product is not enough

The converse direction fails after abelianization. Let

$$R_0=E_{12},\qquad R_1=E_{23},\qquad R_2=E_{31}.$$

Put the atom projectors plus $R_i$ in even degree and $R_i^T$ in odd degree. Transposition makes the non-atom part of every power trace of the commuting pencil cancel. Thus the aggregate identity

$$\operatorname{Str}\left(\sum_{i=0}^2x_iA_i\right)^r=\sum_{i=0}^2x_i^r
 \label{eq:aggregate-passes}$$

holds in the exact fixtures. Yet oriented words retain information erased by commuting variables:

$$\operatorname{Str}(A_0A_1A_2)=1,
 \qquad
 \operatorname{Str}(A_2A_1A_0)=-1.
 \label{eq:oriented-witness}$$

Both words become the monomial $x_0x_1x_2$, so their errors cancel in [\[eq:aggregate-passes\]](#eq:aggregate-passes){reference-type="eqref" reference="eq:aggregate-passes"}.

The implication used in the paper is therefore one way:

$$\text{wordwise selector}
 \Longrightarrow\text{all power traces}
 \Longrightarrow\text{determinant product},$$

where neither reverse arrow is licensed. This is stronger than a numerical warning. It is an exact algebraic counterexample to any protocol that certifies branch purity only from a commutative Euler product.

# Canonical complex audit {#sec:complexes}

The support-Euler formula suggests that a canonical chain complex might kill mixed necklaces without fixed color projectors. Three objects must be kept separate: a shared free bar complex, a word-indexed exterior Euler fiber, and the bar complex of the separable color algebra.

## Shared free and polynomial sources

In a one-object free-renewal algebra, every sequence of return letters is composable. Its cyclic bar construction therefore organizes mixed necklaces rather than deleting them. Passing to a commutative polynomial algebra does not help: the Koszul and Hochschild descriptions retain mixed classes such as $e_i\wedge e_j$ or $dx_i\wedge dx_j$. The algebraic complex remembers exactly the mixed support that the selector was meant to remove.

The reduced-support space $Q_S$ from [\[eq:reduced-support\]](#eq:reduced-support){reference-type="eqref" reference="eq:reduced-support"} has the correct Euler number, but its zero-differential exterior algebra has nonzero classes in both parities for $|S|>1$. Their dimensions cancel in supertrace. Moreover, the support $S$ is supplied only after the completed word has been read. Consequently this construction is an exact orbitwise coefficient, not a stationary bar resolution and not a proof that mixed classes are null-homologous.

## The separable color algebra

There is a canonical stationary success after one changes the algebra. Put $$B_m=\mathbb C^m=\bigoplus_{i=1}^m\mathbb Ce_i,
 \qquad e_ie_j=\delta_{ij}e_i.
 \label{eq:color-algebra}$$ Left multiplication by $e_i$ is the coordinate projector $P_i$.

[\[thm:hochschild-collapse\]]{#thm:hochschild-collapse label="thm:hochschild-collapse"} For $B_m$ over $\mathbb C$, $$\operatorname{HH}_0(B_m)\cong B_m,
 \qquad
 \operatorname{HH}_q(B_m)=0\quad(q>0).
 \label{eq:hochschild-color}$$ The surviving basis consists of the $m$ supplied primitive idempotents.

The element

$$E=\sum_{i=1}^m e_i\otimes e_i$$

is a separability idempotent: multiplication sends it to the unit, and it centralizes the left and right $B_m$-actions. Hence $B_m$ is projective as a $B_m^e$-module, so

$$\operatorname{HH}_q(B_m)=\operatorname{Tor}^{B_m^e}_q(B_m,B_m)=0$$

for $q>0$. Degree zero is $B_m/[B_m,B_m]$, equal to $B_m$ because the algebra is commutative.

The theorem is positive and limiting at once. A one-object category with $m$ freely composable loop letters contains mixed cycles. The successful algebra [\[eq:color-algebra\]](#eq:color-algebra){reference-type="eqref" reference="eq:color-algebra"} has $m$ orthogonal objects/idempotents, one private recurrent sector per color. Its separability contraction already names those colors through $E$. Homology does not reveal a hidden shared selector; it retracts to the supplied atom list.

L40mm c c Y Object & exact selector & stationary & survivor / failure\
Shared free cyclic bar complex & no & yes & mixed necklaces are composable\
Polynomial/Koszul complex & no & yes & mixed exterior classes remain\
Reduced-support exterior fiber & yes & no & Euler cancellation after support is known\
Separable color algebra $\mathbb C^m$ & yes & yes & only $m$ supplied atom classes in $\operatorname{HH}_0$\

The result also explains why adding chain-level decoration cannot by itself escape . Whenever the stationary complex has a finite even trace character, its Euler trace descends to the virtual semisimplification already classified. A future escape must change the finite-recognizable theorem class and justify the resulting infinite or relative trace, not merely lengthen the bar resolution.

# Holomorphic tensor and countable limit {#sec:analytic}

We now attach the selector to the analytic object left by the preceding paper. The construction remains inside Symbolic Dynamics and retains the source code and marker.

## Inherited logarithmic returns

For $n\ge1$, let $c(n)$ be its Elias gamma code and $$\ell(n)=2\lfloor\log_2n\rfloor+1.
 \label{eq:gamma-length}$$ Compose the two affine disk maps

$$\psi_0(z)=\frac z2-\frac14,
 \qquad
 \psi_1(z)=\frac z2+\frac14$$

along $c(n)$, obtaining a branch $\phi_n$ with derivative $q_n=2^{-\ell(n)}$. On the Bergman zero-/one-form pair use

$$U_{n,0}f=f\circ\phi_n,
 \qquad
 U_{n,1}(g\,dz)=q_n(g\circ\phi_n)\,dz.$$

The inherited local theorem says that for every completed branch word $\alpha$, after its scalar weights are removed, $$\operatorname{Str}_{\mathrm{dR}}U_\alpha=1.
 \label{eq:inherited-derham}$$ This is a graded ratio of separately trace-class degreewise operators; the ordinary block determinant remains their product.

## Finite total grading

Give the tensor of a color complex and the de Rham pair total parity. For an ordered branch word, $$\operatorname{Str}_{\mathrm{color}\mathbin{\widehat\otimes}\mathrm{dR}}
 (A_\alpha\otimes U_\alpha)
 =\operatorname{Str}_{\mathrm{color}}(A_\alpha)
  \operatorname{Str}_{\mathrm{dR}}(U_\alpha)
 =\chi_m(\alpha).
 \label{eq:total-supertrace}$$ Thus the local tangent denominator and the mixed label coefficient are both cancelled at every repetition. Before totalization the complex has four bidegrees; its determinant is the quotient of honest total-even and total-odd Fredholm determinants.

## Countable projector fiber

Let $S\subseteq\{2,3,\ldots\}$ be a countable supplied inventory and $\mathcal K_S=\ell^2(S)$. Write $P_n=|e_n\rangle\langle e_n|$ for the coordinate projector. The digit-resolved weight is $$b_n(s,u)=u^{\ell(n)}n^{-s},
 \label{eq:digit-weight}$$ where $u$ counts original binary digit steps. Define degreewise $$\mathcal T^k_{S,s,u}
 =\sum_{n\in S}b_n(s,u)P_n\otimes U_{n,k},
 \qquad k=0,1.
 \label{eq:countable-operator}$$

[\[thm:countable-selector\]]{#thm:countable-selector label="thm:countable-selector"} If $$\sum_{n\in S}|u|^{\ell(n)}n^{-\Re s}<\infty,
 \label{eq:l1-domain}$$ then both operators in [\[eq:countable-operator\]](#eq:countable-operator){reference-type="eqref" reference="eq:countable-operator"} are trace class. For every $r\ge1$, $$\operatorname{Str}(\mathcal T_{S,s,u})^r
 =\sum_{n\in S}u^{r\ell(n)}n^{-rs},
 \label{eq:countable-power-trace}$$ and their graded determinant is $$D_{\mathrm{gr}}(S;s,u,z)=
 \prod_{n\in S}\left(1-zu^{\ell(n)}n^{-s}\right).
 \label{eq:countable-product}$$ For $|u|\le1$, $\Re s>1$ is a uniform domain for every such inventory.

Common compact containment of the affine branches gives a uniform constant $C$ with $\|U_{n,k}\|_1\le C$. Because the coordinate ranges are orthogonal, $$\|\mathcal T^k_{S,s,u}\|_1
 =\sum_{n\in S}|b_n(s,u)|\,\|U_{n,k}\|_1
 \le C\sum_{n\in S}|u|^{\ell(n)}n^{-\Re s}.$$ This proves degreewise trace class. Also $P_nP_j=0$ for $n\ne j$, so every mixed word vanishes before analytic tracing. The surviving pure powers and [\[eq:inherited-derham\]](#eq:inherited-derham){reference-type="eqref" reference="eq:inherited-derham"} give [\[eq:countable-power-trace\]](#eq:countable-power-trace){reference-type="eqref" reference="eq:countable-power-trace"}. The trace-log identity yields [\[eq:countable-product\]](#eq:countable-product){reference-type="eqref" reference="eq:countable-product"}. Finally, $|u|^{\ell(n)}\le1$ and the $p$-series bound give convergence on $\Re s>1$.

The construction is analytically honest and structurally disjoint. The unitary identification $$\ell^2(S)\otimes\mathcal H^k
 \cong\bigoplus_{n\in S}\mathcal H^k
 \label{eq:unitary-disjoint}$$ turns [\[eq:countable-operator\]](#eq:countable-operator){reference-type="eqref" reference="eq:countable-operator"} into one private holomorphic block per supplied label. Its cohomological survivor is the diagonal space $\bigoplus_n\mathbb Ce_n$ with eigenvalues $b_n(s,u)$. The local nonconstant holomorphic modes and the color-complex invisible sectors have both retracted.

## Marker and continuation firewalls

At digit scale, an $r$-fold pure return contributes $u^{r\ell(n)}n^{-rs}$, not $u^rn^{-rs}$. The variable $z$ in [\[eq:countable-product\]](#eq:countable-product){reference-type="eqref" reference="eq:countable-product"} counts completed returns. Setting $u=1$ is legal after first-return induction, or after declaring whole codewords to be the return alphabet; it is not an identity at the original digit scale.

At $u=1$, the constant zero-form mode has absolute eigenvalue $n^{-\Re s}$. For the full integers, and for primes at the corresponding boundary, this prevents continuation of the same trace-class family through the absolute summability line. Meromorphic continuation of a scalar product, if obtained elsewhere, would not by itself continue the operator family in [\[eq:countable-operator\]](#eq:countable-operator){reference-type="eqref" reference="eq:countable-operator"}. SD-C28 claims only the honest A2 domain.

# Exact audit and arbitrary-inventory controls {#sec:audit}

The symbolic computation is a theorem audit rather than a parameter study. All scientific rows use exact integers, rationals, matrices, polynomials, or finite words. No target-zero metric, stochastic fitting, floating threshold, or network input occurs.

L46mm r Y Ledger & rows & theorem role\
Projector words & 34,636 & exact pure/mixed oracle\
Upper-triangular radical words & 15,029 & literal splitting countercontrol\
Graded words & 1,274 & common parity and extension cancellation\
Hankel/syntactic & 8 & ranks $m$ and $m+1$\
Aggregate adversary & 34 & 32 aggregate passes; two oriented witnesses\
Support incidence & 12 & exterior Euler identities\
Bar/Hochschild & 12 & separable atom-homology certificates\
Local de Rham & 72 & chain, power, and quotient checks\
Tensor de Rham words & 120 & individual analytic word supertraces\
Arbitrary inventories & 21 & all marked `PROVES_TOO_MUCH`\
Marker ownership & 511 & digit versus completed-return ledger\
Route gates & 5 & frozen tuple\
Total scientific rows & 51,734 & all exact predicates pass\
Regression suite & 58 & 58/58 pass\

The 34,636 projector rows exhaust the frozen words for color counts through seven and lengths through five. The 15,029 radical rows populate deterministic noncommuting upper-triangular extensions yet retain every word trace. The 1,274 graded rows add nontrivial common modules and a nonsplit even coupling. Together these ledgers corroborate why conclude semisimplification rather than a literal projector normal form.

The aggregate adversary separately verifies 32 scalar-pencil powers over four signed weight fixtures. Every aggregate test passes, while the two necklace-resolved values in [\[eq:oriented-witness\]](#eq:oriented-witness){reference-type="eqref" reference="eq:oriented-witness"} are exactly $+1$ and $-1$. The test is therefore designed to refute an invalid implication, not to approximate a small discrepancy.

Support sizes through twelve satisfy the exterior identity, while mixed supports retain nonzero even and odd dimensions. The separable-algebra rows check the primitive-idempotent multiplication and the degree-zero atom certificate through twelve colors. Seventy-two local polynomial de Rham rows verify chain, power-supertrace, and characteristic-quotient identities. The 120 tensor rows then check individual pure and mixed branch words, keeping the wordwise firewall through the analytic tensor.

The arbitrary-inventory controls include prime, square, Fibonacci, full integer, matched deterministic pseudo-random, matched hash, and modular families. Each uses the same compiler and full-inventory exact sums/products. Every one passes and receives the label `SELECTOR_TAUTOLOGICAL | PROVES_TOO_MUCH`. This is the decisive A1 control: the selector responds to labels supplied at input, not to arithmetic primality derived from the source.

All 511 marker rows retain $u^{\ell(n)}$ and distinguish it from one $z$ per completed return. The compiler can preserve a supplied roof; it does not derive or erase it.

For integrity, the canonical runner generates code/results twice under a fixed hash seed, removes caches, and compares bytes. The two 27-artifact snapshots are identical, with combined SHA-256 `8dba8bd574f02fd364e5e8ea987f19ba200a003e68edb1c02ee2f65ac77375e4`. The 29-entry code/result SHA ledger and the route/scientific integrity audit pass. This double-run certificate covers code and generated results, not the manuscript or documentation. Finite exact rows corroborate the identities; they do not replace the infinite trace-class proof or widen its domain.

# Route evaluation and next obligation {#sec:route}

The selector succeeds as a coefficient and fails as a source selector. The strict evaluation is

L17mm L42mm Y Gate & status & reason\
A0 & `STRUCTURAL``ARITHMETIC``RELATION` & full-shift semiring and logarithmic code are retained without zero data\
A1 & `FAIL` & every stationary exact selector retains one net simple or orthogonal block per supplied label\
A2 & `ANALYTIC_DETERMINANT` & degreewise trace-class operators and their graded ratio exist on $\Re s>1$\
A3 & `FAIL` & no continuation of the same operator/determinant family is constructed\
A4 & `FAIL` & no self-adjoint or unitary spectral mechanism is constructed\

Equivalently,

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_FAIL,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL)

    ROUTE_A_REJECTED
    ROUTE_B_LOCKED

The A2 credit is substantive. The total even and total odd operators are separately trace class on the stated domain, and their graded quotient has the exact all-repetition product. It is not credited as A1 because the color projectors are the inventory. It is not credited as A3 because a scalar continuation is not a continuation of those degreewise trace-class operators. Nothing in the construction supplies the A4 spectral geometry.

## Scope limitations

The collapse theorem is finite dimensional for general trace characters. It does not classify every infinite-dimensional nuclear representation, unbounded complex, odd-letter supercategory, non-type-I trace, or nonlocal completed-orbit weight. The countable result classifies the explicit coordinate-projector family by direct calculation; it is not an infinite Brauer--Nesbitt theorem. Radical extensions remain possible, aggregate commuting products remain weaker than wordwise traces, and the empty-word convention remains a separate recognition issue.

## Paper27 minimum obligation

The next candidate must not install a projector for each desired atom. It must derive a countable factorization or divisibility incidence compiler from the source object and meet all of the following admission gates:

1.  produce individual necklace-resolved coefficients before abelianization, at every repetition;

2.  retain the original digit marker $u^{\ell(n)}$ until explicit first-return induction;

3.  prove an honest trace-class, nuclear, or source-owned relative determinant domain for the whole countable object;

4.  run arbitrary-inventory controls and show why the source distinguishes atoms rather than a supplied list;

5.  either escape finite recognizability with controlled infinite memory, or accept atom collapse and obtain new same-object analytic continuation.

An aggregate Euler product alone cannot pass the first gate, by . A bar complex whose semisimple quotient is $\mathbb C^m$ cannot pass the fourth. These are now theorem-backed admission tests rather than heuristic preferences.

# Conclusion {#sec:conclusion}

The mixed-necklace coefficient problem has an exact answer. Reduced-support exterior parity gives the desired value after a word is complete, while coordinate projectors give it in a stationary finite representation. The same coefficient also exposes their ceiling: its minimal observable algebra is the color algebra, and every finite ordinary or even graded trace realization retains one net semisimple character per supplied label.

This statement survives the two main evasions. Nonsplit radicals may alter the literal matrices but not their word traces. Matched even/odd sectors may alter both degreewise operators but not the virtual character. At full determinant level, only the color factors remain. The separate aggregate counterexample shows why this conclusion must be proved word by word rather than guessed from a correct commutative product.

Tensoring with the holomorphic de Rham sector yields a genuine analytic object: separately trace-class degreewise operators and an exact graded determinant on $\Re s>1$. Yet the countable color fiber is unitarily the direct sum of supplied atom blocks. The construction works unchanged for nonprime inventories, so it cannot receive arithmetic source-selection credit.

The useful outcome is therefore a classified failure rather than a missing calculation. Finite recognizable, virtual-character, and separable bar/Hochschild selectors are now closed as non-atomic repairs of shared renewal. A future route must derive infinite incidence from factorization or divisibility itself, preserve necklace and marker ownership, and justify its operator ideal. SD-C28 supplies no continuation, self-adjoint carrier, RH implication, or Route-B object; its strict verdict is Route-A rejection.

# Proof details and auxiliary ledgers {#app:proofs}

## Residual basis for the two Hankel conventions

For $1\le i\le m$, define the color residual $$r_i(v)=
 \begin{cases}
 1,&v\in\{\varepsilon,a_i,a_i^2,\ldots\},\\
 0,&\text{otherwise}.
 \end{cases}$$ After any nonempty pure prefix of color $i$, the residual is $r_i$; after a mixed prefix it is zero. In the character convention, the empty residual is $\sum_i r_i$. In the language convention, it is the function that is zero at $\varepsilon$ and agrees with $\sum_i r_i$ on nonempty suffixes. Its difference from $\sum_i r_i$ is supported at the empty suffix, giving the one dormant dimension. This explicitly constructs the bases used in .

## Finite-image character argument

Let $U$ and $W$ be finite-dimensional $R_m$-modules whose trace characters agree. Their direct sum defines a homomorphism $$R_m\longrightarrow\operatorname{End}(U\oplus W)$$ with finite-dimensional image $B$. The Jacobson radical $\operatorname{rad}B$ acts by strictly upper-triangular blocks along any composition series and therefore does not affect trace characters. The semisimple quotient has the form $$B/\operatorname{rad}B\cong\prod_{j=1}^tM_{d_j}(\mathbb C).$$ Its simple modules have linearly independent trace characters: evaluating at the central unit of the $j$th block isolates the corresponding multiplicity up to the fixed nonzero dimension $d_j$. Equal characters therefore give equal composition multiplicities. This is the exact step used in .

## A concrete radical family

One may realize the radical qualification without changing dimensions by choosing a total order on the color basis and setting $$A_i=P_i+\sum_{j<k}c_{i,jk}E_{jk}.$$ Every product is upper triangular, and its diagonal is the product of the projector diagonals. Generic coefficients $c_{i,jk}$ make the generators noncommuting. The exact experiment uses deterministic populated instances and checks every frozen word, not merely their characteristic polynomials.

## Transpose reversal adversary

For matrices $R_i$, $$\operatorname{Tr}(R_{i_1}^T\cdots R_{i_r}^T)
 =\operatorname{Tr}(R_{i_r}\cdots R_{i_1}).$$ Thus an even word and its odd transpose sector compare opposite orientations. After summing over all words in a commuting pencil, reversal is a bijection, so the non-atom contributions cancel. At the individual-word level, the cycle $E_{12}E_{23}E_{31}=E_{11}$ has trace one, whereas its reverse product vanishes in the corresponding sector. This yields [\[eq:oriented-witness\]](#eq:oriented-witness){reference-type="eqref" reference="eq:oriented-witness"}.

## Separable contraction ownership

The separability idempotent $E=\sum_ie_i\otimes e_i$ depends explicitly on all primitive color idempotents. Inserting $E$ gives a contracting homotopy of the normalized bar resolution in positive degree. The contraction is canonical relative to $B_m$, but $B_m$ is itself the supplied color split. This ownership fact is why [\[eq:hochschild-color\]](#eq:hochschild-color){reference-type="eqref" reference="eq:hochschild-color"} is a collapse certificate rather than an arithmetic selector.

## Countable determinant convergence

Under [\[eq:l1-domain\]](#eq:l1-domain){reference-type="eqref" reference="eq:l1-domain"}, each degreewise direct sum is trace class and $$\sum_{r\ge1}\frac{|z|^r}{r}
 \left|\operatorname{Str}(\mathcal T_{S,s,u})^r\right|
 \le
 \sum_n\sum_{r\ge1}\frac{|zb_n|^r}{r}$$ converges locally whenever $\sup_n|zb_n|<1$ and $\sum_n|b_n|<\infty$. This justifies rearranging the trace logarithm near $z=0$. Analytic continuation in $z$ then agrees with the canonical Fredholm products on their common domain. No rearrangement in $s$ beyond absolute summability is used.

## Arbitrary-inventory logic

The proofs depend only on distinct labels and the summability of their scalar weights. Replacing primes by composites, squares, or any deterministic inventory leaves every algebraic identity unchanged. The experiment's inventory controls are thus finite certificates of a theorem-level symmetry, not statistical evidence. Prime specialization cannot earn A1 credit unless an additional source-derived mechanism breaks this symmetry.

# Scope, reproducibility, and declarations {#app:scope}

## Claim and ownership ledger

L39mm Y Y Boundary & licensed statement & excluded substitution\
Wordwise / aggregate & every positive word is audited & scalar pencil product as proof of word purity\
Character / language empty word & values $m$ and $0$ are tracked separately & merging ranks $m$ and $m+1$\
Semisimplification / matrices & virtual simple multiplicities are fixed & literal simultaneous diagonalization\
Graded / ordinary determinant & quotient of honest degreewise determinants & ordinary determinant of the ungraded block sum\
Support / stationary fiber & support exterior is orbitwise & word-dependent fiber called a fixed transfer operator\
Digit / return marker & $u^{\ell(n)}$ is retained & one step per codeword without induction\
Finite / countable theorem & finite character rigidity plus explicit countable projectors & universal infinite Brauer--Nesbitt claim\
Scalar continuation / operator continuation & trace class on $\Re s>1$ & continued scalar product as same operator family\

## Data and code availability

All evidence is generated by deterministic exact code stored with the paper project. The canonical runner, source/evaluator separation, exact ledgers, test summary, environment lock, per-file SHA-256 ledger, double-run certificate, and integrity audit are included under the independently owned `code/`, `experiments/`, and `results/` paths. The double-run certificate covers code and generated results only. No external dataset, target-zero file, private service, or stochastic seed is required.

## Limitations

The algebraic collapse theorem assumes finite-dimensional complex representations, stationary multiplication, even letter actions in the graded case, and equality for every positive word. Odd letter maps, supercyclic sign conventions, arbitrary infinite von Neumann traces, non-type-I representations, unbounded derived completions, and nonlocal word-dependent weights lie outside the theorem. The analytic theorem treats the explicit coordinate-projector tensor on its absolute trace-class domain. It neither constructs continuation across $\Re s=1$ nor proves that every infinite selector must be a direct sum.

## Ethics statement

This is a mathematical and exact-computation study. It uses no human participants, animals, personal data, surveillance data, or consequential automated decisions. No ethics-board approval was applicable.

## Author contributions

The anonymous authors jointly contributed conceptualization, formal analysis, methodology, software specification, validation, visualization, writing, and artifact curation. Individual names are withheld in this research draft.

## Funding

No external funding is declared for this research artifact.

## Conflict of interest

The authors declare no competing financial or nonfinancial interests. The standing instruction excluded a manuscript-review loop; source, proof, exact, build, and visual audits were retained.
