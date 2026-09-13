---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--151-unequal-spider-first-passage"
canonical_tex: "symbolic_dynamics/papers/151-unequal-spider-first-passage/main.tex"
canonical_pdf: "symbolic_dynamics/papers/151-unequal-spider-first-passage/main.pdf"
source_sha256: "86bac9c061a2af00505438c8e9910a097c1f033fcba9bba323dfa264eb385268"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Leaf-Marked First Passage on Unequal Finite Spiders: A Rational Transform, Sharp Extremizers, and a Coarse-Data Inverse

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/151-unequal-spider-first-passage>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/151-unequal-spider-first-passage/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/151-unequal-spider-first-passage/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/151-unequal-spider-first-passage/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/151-unequal-spider-first-passage/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Join $r\ge2$ finite paths of positive integer lengths at one centre, start simple random walk at the centre, and absorb it at the first leaf. We derive an explicit continuant factorization of the probability generating functions jointly marked by the absorbing leaf for arbitrary unequal arms. A centre-excursion renewal specializes the generic time/place law to a common rational denominator for all leaf marks. Besides parity and the first possible atom, the specialization yields the compact formula $$\operatorname{Var}(T)=\frac{C-2L}{3H}+\frac{L^2}{3H^2},
   \qquad
   H=\sum_i\ell_i^{-1},\quad L=\sum_i\ell_i,\quad C=\sum_i\ell_i^3.$$ For fixed arm count and total length, strict integer transfers identify the exact mean-minimizing profile---one long arm and all other arms of length one---and the exact mean-maximizing balanced profiles. The labelled endpoint law determines precisely the primitive arm-length ratios and is blind to a common dilation; adding the mean recovers that scale uniquely. General-tree endpoint and mean formulas, an unequal-arm endpoint exercise, equal-arm star laws, spider spectral methods, generic finite-chain time/place laws, general tree hitting-time generating functions, and inverse first-passage frameworks are treated as prior background. An exact-arithmetic audit performs $1{,}446{,}432$ exact recurrence, coefficient, moment, extremal, and inverse checks.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Leaf-Marked First Passage on Unequal Finite Spiders:\
  A Rational Transform, Sharp Extremizers, and a Coarse-Data Inverse
```

## Markdown 正文

# Process, ownership boundary, and theorem {#sec:setup}

For positive integers $\ell_1,\ldots,\ell_r$, let $\mathcal S(\ell_1,\ldots,\ell_r)$ be the tree formed by identifying one endpoint of $r$ paths of edge lengths $\ell_i$. Call the identified vertex the *centre*, label the other endpoints $1,\ldots,r$, and make those leaves absorbing. Simple random walk starts at the centre. Write $T$ for its first leaf-hitting time and $I$ for the label of the leaf it hits.

Unequal arms obstruct the radial lumping available when all lengths agree: the time and the absorbing label remain coupled. The paper resolves that coupling through a leaf-marked excursion transform. The contribution is a four-part conjunction: the explicit unequal-spider continuant factorization, its compact scalar variance specialization, sharp fixed-total extremizers, and a geometry inverse from deliberately coarse data. Generic existence, rationality, resolvent, time/place, and second-moment formulas receive zero credit. Table [1](#tab:subtraction){reference-type="ref" reference="tab:subtraction"} states the corresponding subtraction.

::: {#tab:subtraction}
  Source                                                   Owned input                                                                                  Boundary retained here
  -------------------------------------------------------- -------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------
  Pearce [@Pearce1980]                                     finite trees with absorbing leaves; endpoint probabilities and expected walk length          neither endpoint mass nor mean is claimed
  Pal--Mesikepp, Problem 2.4 [@PalMesikepp2025]            designated-leaf probability for a star with unequal integer arms                             endpoint law is used only for extrema and inversion
  Castella--Sericola [@CastellaSericola2026]               hitting distributions and moments for equal-length finite stars                              the transform axis requires arbitrary unequal arms and an explicit continuant factorization
  Sericola [@Sericola2024]                                 generic finite-chain joint hitting-time/place law and first/second moment matrices           only the closed unequal-spider continuant product and compact scalar specialization
  Chen [@Chen2007]                                         algorithms for hitting-time generating functions on general trees                            a leaf-marked, unequal-spider closed factorization rather than generic existence or an algorithm
  de la Iglesia--Juarez [@DelaIglesiaJuarez2023]           spectral and stochastic factorization methods for half-line spider chains                    no spectral-framework or generic-resolvent claim
  de la Peña--Gzyl--McDonald [@DelaPenaGzylMcDonald2008]   unknown transitions on a known augmented tree recovered from rich boundary time/place data   fixed simple-walk kernel and unknown integer arms, using only endpoint probabilities plus one mean

  : Primary-source subtraction. The middle column receives zero contribution credit; the right column is the narrower residual studied here.
:::

Sericola's generic identity $\mathbb P_i(T_A=n,X_{T_A}=j)=(P_{A^c}^{n-1}P_{A^c,A})_{ij}$ already owns the joint time/place law and its matrix moments [@Sericola2024]. Chen's general-tree work already owns algorithmic hitting-time generating functions [@Chen2007]. Neither inspected source states the product formula [\[eq:marked\]](#eq:marked){reference-type="eqref" reference="eq:marked"} for unequal finite spiders or its continuant denominator; that explicit specialization is the only residual transform claim.

The term "reflecting--absorbing factorization" in [@DelaIglesiaJuarez2023] denotes a stochastic block factorization and a Darboux transformation, not absorption at finite leaves. Conversely, the inverse theorem in [@DelaPenaGzylMcDonald2008] observes complete joint time/place laws on two boundary layers and recovers transition probabilities; our topology class and transition rule are fixed, while the integer arm lengths are unknown. These distinctions prevent generic spider, resolvent, and tomography language from carrying contribution credit.

Define continuant polynomials by $$\label{eq:P-rec}
 P_0(z)=0,\qquad P_1(z)=1,\qquad P_2(z)=2,
 \qquad P_m(z)=2P_{m-1}(z)-z^2P_{m-2}(z).$$ Put $$\label{eq:D-def}
 P(z)=\prod_{j=1}^rP_{\ell_j}(z),\qquad
 D(z)=rP(z)-z^2\sum_{i=1}^rP_{\ell_i-1}(z)
                 \prod_{j\ne i}P_{\ell_j}(z).$$ Also write $$\label{eq:HLC}
 H=\sum_{i=1}^r\frac1{\ell_i},\qquad
 L=\sum_{i=1}^r\ell_i,\qquad C=\sum_{i=1}^r\ell_i^3.$$

[\[thm:main\]]{#thm:main label="thm:main"} For the walk on $\mathcal S(\ell_1,\ldots,\ell_r)$, the following statements hold.

1.  For every labelled leaf $i$, $$\label{eq:marked}
     F_i(z):=\mathbb E\!\left[z^T\mathbf 1_{\{I=i\}}\right]
     =\frac{z^{\ell_i}\prod_{j\ne i}P_{\ell_j}(z)}{D(z)}.$$ Its support lies in $\ell_i+2\mathbb Z_{\ge0}$, and $$\label{eq:first-atom}
     \mathbb P(T=\ell_i,I=i)=\frac1{r2^{\ell_i-1}}.$$

2.  The endpoint and mean identities $$\label{eq:background-moments}
     \mathbb P(I=i)=\frac{\ell_i^{-1}}H,\qquad \mathbb ET=\frac LH$$ are background inputs from the general-tree and unequal-arm literature in Table [1](#tab:subtraction){reference-type="ref" reference="tab:subtraction"}. The residual second-moment conclusion is $$\label{eq:variance}
     \operatorname{Var}(T)=\frac{C-2L}{3H}+\frac{L^2}{3H^2}.$$

3.  Fix $r$ and $L\ge r$, and write $L=qr+s$ with $0\le s<r$. Then $$\label{eq:extremal}
     \frac{L}{r-1+1/(L-r+1)}\le \mathbb ET
     \le \frac{L}{(r-s)/q+s/(q+1)}.$$ Equality on the left holds exactly for permutations of $(L-r+1,1,\ldots,1)$; equality on the right holds exactly when the arms are balanced, with $r-s$ lengths $q$ and $s$ lengths $q+1$.

4.  The labelled endpoint vector determines the primitive positive integer arm vector $d=(d_i)$, while $\ell=cd$ is invisible for every common positive integer dilation $c$. Adding $\mathbb ET$ determines the unique scale by $$\label{eq:scale}
     c^2=\mathbb ET\,\frac{\sum_i d_i^{-1}}{\sum_i d_i}.$$

The theorem assumes from the outset that the unknown object is a labelled finite spider and that its transition kernel is simple random walk. Part (4) does not recover an arbitrary tree or unknown transition probabilities.

# Killed paths and centre renewal {#sec:transform}

Let $U_m$ denote the Chebyshev polynomial of the second kind, with $U_{-1}=0$. For $m\ge1$, recurrence [\[eq:P-rec\]](#eq:P-rec){reference-type="eqref" reference="eq:P-rec"} is equivalently the polynomial identity $$\label{eq:Cheb}
 P_m(z)=z^{m-1}U_{m-1}(1/z).$$ The Chebyshev notation is a convenient solution of a second-order recurrence; neither generic continuants nor gambler's ruin are contribution claims.

[\[lem:arm\]]{#lem:arm label="lem:arm"} On $\{0,1,\ldots,m\}$, start fair nearest-neighbour walk at $1$ and stop on first hitting $\{0,m\}$. If $\tau$ is this path time, then $$\begin{aligned}
 \mathbb E_1[z^\tau\mathbf 1_{\{X_\tau=m\}}]
   &=\frac1{U_{m-1}(1/z)}=\frac{z^{m-1}}{P_m(z)},\label{eq:success-arm}\\
 \mathbb E_1[z^\tau\mathbf 1_{\{X_\tau=0\}}]
   &=\frac{U_{m-2}(1/z)}{U_{m-1}(1/z)}
     =\frac{zP_{m-1}(z)}{P_m(z)}.\label{eq:return-arm}\end{aligned}$$

For $1\le k\le m-1$, either boundary-marked transform $u_k$ satisfies $$u_k=\frac z2(u_{k-1}+u_{k+1}).$$ For absorption at $m$, the boundary values are $(u_0,u_m)=(0,1)$, and the solution is $$u_k=\frac{U_{k-1}(1/z)}{U_{m-1}(1/z)}.$$ For absorption at zero, the boundary values are $(1,0)$, and the solution is $$u_k=\frac{U_{m-k-1}(1/z)}{U_{m-1}(1/z)}.$$ Evaluating at $k=1$ and applying [\[eq:Cheb\]](#eq:Cheb){reference-type="eqref" reference="eq:Cheb"} proves both identities. For $m=1$, the formulas use $P_0=0$ and express immediate success after the later-added centre step.

An attempt from the centre chooses arm $j$, makes one step to its first vertex, and then either reaches leaf $j$ or returns to the centre. By Lemma [\[lem:arm\]](#lem:arm){reference-type="ref" reference="lem:arm"}, the transform of a successful attempt at leaf $i$ is $$S_i(z)=\frac1r\frac{z^{\ell_i}}{P_{\ell_i}(z)},$$ and the transform of an unsuccessful attempt, with the arm unmarked, is $$Q(z)=\frac{z^2}{r}\sum_{j=1}^r
            \frac{P_{\ell_j-1}(z)}{P_{\ell_j}(z)}.$$ After every failure the walk is again at the centre, so the strong Markov property gives the formal renewal series $$F_i(z)=S_i(z)\sum_{k\ge0}Q(z)^k=\frac{S_i(z)}{1-Q(z)}.$$ Here $Q(0)=0$, so the inverse is valid as a formal series. Also $P_m(1)=m$, whence $$Q(1)=1-\frac Hr<1,
 \qquad D(1)=H\prod_{j=1}^r\ell_j>0.$$ Thus the rational identity is regular at $z=1$ and its endpoint and moment evaluations below are justified analytically as well as probabilistically. Multiplying numerator and denominator by $r\prod_jP_{\ell_j}(z)$ gives [\[eq:marked\]](#eq:marked){reference-type="eqref" reference="eq:marked"}.

Each $P_m$ is a polynomial in $z^2$. Equation [\[eq:marked\]](#eq:marked){reference-type="eqref" reference="eq:marked"} therefore has only powers congruent to $\ell_i$ modulo two, in agreement with bipartiteness. At the first possible time $\ell_i$, the walk must choose arm $i$ and then follow its unique shortest path without backtracking. The probability is $(1/r)(1/2)^{\ell_i-1}$, proving [\[eq:first-atom\]](#eq:first-atom){reference-type="eqref" reference="eq:first-atom"}.

# Excursion moments and the variance {#sec:moments}

The renewal proof also separates the second moment into one-arm quantities. This route avoids treating differentiation of the common denominator as a black box.

[\[lem:attempt\]]{#lem:attempt label="lem:attempt"} Condition on choosing an arm of length $m$. Let $A_m$ be the duration from departure at the centre until the attempt next reaches either the centre or the leaf, including the departure step, and let $R_m$ be the event of return to the centre. Then $$\begin{aligned}
 \mathbb P(R_m^c)&=\frac1m,&
 \mathbb EA_m&=m,\label{eq:attempt-first}\\
 \mathbb EA_m^2&=\frac{m(m^2+2)}3,&
 \mathbb E[A_m\mathbf 1_{R_m}]&=\frac{2(m^2-1)}{3m}.
 \label{eq:attempt-second}\end{aligned}$$

Including the centre step, the success and return transforms from Lemma [\[lem:arm\]](#lem:arm){reference-type="ref" reference="lem:arm"} are $$A_m^{\rm suc}(z)=\frac{z^m}{P_m(z)},\qquad
 A_m^{\rm ret}(z)=\frac{z^2P_{m-1}(z)}{P_m(z)}.$$ Differentiating [\[eq:P-rec\]](#eq:P-rec){reference-type="eqref" reference="eq:P-rec"} and inducting gives $$\begin{aligned}
 P_m(1)&=m,\\
 P_m'(1)&=-\frac{m(m-1)(m-2)}3,\\
 P_m''(1)&=\frac{m(m-1)(m-2)(m^2-7m+7)}{15}.\end{aligned}$$ Substitution into the two quotient derivatives gives $A_m^{\rm suc}(1)=1/m$, $(A_m^{\rm ret})(1)=1-1/m$, $$(A_m^{\rm suc}+A_m^{\rm ret})'(1)=m,$$ $$(A_m^{\rm suc}+A_m^{\rm ret})''(1)
 +(A_m^{\rm suc}+A_m^{\rm ret})'(1)=\frac{m(m^2+2)}3,$$ and $(A_m^{\rm ret})'(1)=2(m^2-1)/(3m)$. These are precisely [\[eq:attempt-first\]](#eq:attempt-first){reference-type="eqref" reference="eq:attempt-first"}--[\[eq:attempt-second\]](#eq:attempt-second){reference-type="eqref" reference="eq:attempt-second"}. The identities remain valid at $m=1$.

Average one attempt over the uniform choice of arm. Let $B$ indicate a successful attempt and $A$ its duration. Lemma [\[lem:attempt\]](#lem:attempt){reference-type="ref" reference="lem:attempt"} gives $$\label{eq:renewal-data}
 p:=\mathbb EB=\frac Hr,\quad
 \mu:=\mathbb EA=\frac Lr,\quad
 \nu:=\mathbb EA^2=\frac{C+2L}{3r},\quad
 \rho:=\mathbb E[A(1-B)]=\frac{2(L-H)}{3r}.$$ Let $T'$ be an independent copy of $T$, used after a failed attempt. Then $T=A+(1-B)T'$. First moments give $p\mathbb ET=\mu$, which recovers the prior mean in [\[eq:background-moments\]](#eq:background-moments){reference-type="eqref" reference="eq:background-moments"}. Squaring before taking expectations gives $$p\mathbb ET^2=\nu+2\rho\mathbb ET.$$ Using [\[eq:renewal-data\]](#eq:renewal-data){reference-type="eqref" reference="eq:renewal-data"} and subtracting $(L/H)^2$ yields [\[eq:variance\]](#eq:variance){reference-type="eqref" reference="eq:variance"}. Finally, evaluating [\[eq:marked\]](#eq:marked){reference-type="eqref" reference="eq:marked"} at $z=1$ gives the prior endpoint identity in [\[eq:background-moments\]](#eq:background-moments){reference-type="eqref" reference="eq:background-moments"}.

# Sharp fixed-mass extrema {#sec:extrema}

The prior mean identity becomes a residual result when optimized with exact integer equality classes.

Because $L$ is fixed, minimizing $\mathbb ET=L/H$ is equivalent to maximizing $H=\sum_i1/\ell_i$. If $2\le a\le b$, the outward unit transfer $(a,b)\mapsto(a-1,b+1)$ changes the reciprocal sum by $$\frac1{a(a-1)}-\frac1{b(b+1)}>0.$$ Repeated outward transfers end only when all but one arm have length one. Strictness proves that the maximizers of $H$ are exactly the permutations of $(L-r+1,1,\ldots,1)$. Substitution gives the left side of [\[eq:extremal\]](#eq:extremal){reference-type="eqref" reference="eq:extremal"}.

For the other direction, if $b\ge a+2$, the inward transfer $(a,b)\mapsto(a+1,b-1)$ changes the old reciprocal sum minus the new one by $$\frac1{a(a+1)}-\frac1{b(b-1)}>0.$$ Thus $H$ decreases strictly until all arm lengths differ by at most one. Writing $L=qr+s$ forces $r-s$ lengths $q$ and $s$ lengths $q+1$; substituting their reciprocal sum gives the right side of [\[eq:extremal\]](#eq:extremal){reference-type="eqref" reference="eq:extremal"}. These strict transfers also prove both equality classifications. If $L=r$, both classes reduce to the all-one profile, so the boundary case is included.

# What the coarse data identify {#sec:inverse}

Let $\pi_i=\mathbb P(I=i)$. The background endpoint identity gives $$\label{eq:ratio}
 \frac{\pi_i}{\pi_j}=\frac{\ell_j}{\ell_i}.$$ Hence the labelled vector $\pi$ determines the rational ray containing $(\ell_i)$ and therefore its unique primitive positive integer representative $d=(d_i)$. It cannot determine scale: every $cd$, $c\in\mathbb Z_{>0}$, has the same endpoint vector. Conversely, if two labelled spiders have the same endpoint vector, [\[eq:ratio\]](#eq:ratio){reference-type="eqref" reference="eq:ratio"} makes their arm vectors proportional; primitive integer normalization shows that common dilation is the entire ambiguity.

For $\ell=cd$, the prior mean formula becomes $$\mathbb ET=c^2\frac{\sum_i d_i}{\sum_i d_i^{-1}}.$$ Solving gives [\[eq:scale\]](#eq:scale){reference-type="eqref" reference="eq:scale"}. For data generated by an integer spider, the right-hand side is the square of its unique positive integer scale. No claim is made for arbitrary noisy vectors, unknown topology, or unknown transition kernels.

# Exact audit, limitations, and conclusion {#sec:audit}

A standalone standard-library verifier checks the formulas in exact integer and rational arithmetic. For every ordered profile with $2\le r\le5$ and $1\le\ell_i\le4$, it compares a literal vertex-state Markov recursion with the rational series [\[eq:marked\]](#eq:marked){reference-type="eqref" reference="eq:marked"} coefficient by coefficient through time $2L+12$. Additional exact routes check quotient derivatives, the excursion moments, every positive composition with $2\le r\le6$ and $L\le24$ for the sharp bounds, primitive-ray recovery through arm length eight, and the equal-arm radial collapse as an owned control. Table [2](#tab:audit){reference-type="ref" reference="tab:audit"} records the frozen run.

::: {#tab:audit}
  Control                                           Assertions
  ----------------------------------------------- ------------
  Continuant recurrence and closed coefficients            400
  Literal marked coefficients and mass                 524,816
  Endpoint/mean/variance derivatives                    10,448
  Additional one-attempt moments                           400
  Fixed-mass inequalities and equality classes         760,104
  Primitive ray, dilation, and scale recovery          149,760
  Equal-arm owned-background collapse                      504
  Total                                              1,446,432

  : Exact-arithmetic falsification audit. Counts are assertions, not proof steps or evidence of novelty.
:::

The results have four deliberate limitations. First, the topology class is known and consists only of labelled spiders with positive integer arm lengths. Second, transitions are the unweighted simple-walk transitions; weighted or biased arms are outside the theorem. Third, the inverse uses exact population quantities and gives no estimator, stability bound, or noisy-data guarantee. Fourth, the paper does not address cover times, general trees, generic time/place laws, or equal-arm distribution theory. Sericola's generic joint law and moment matrices and Chen's general-tree PGF algorithm are zero-credit inputs. A bounded primary-source search did not locate the specific continuant-factorization/variance/extremal/inverse conjunction, but a search non-hit is not a novelty, priority, or freedom-to-operate certificate.

Within those boundaries, centre renewal gives an explicit unequal-spider continuant factorization of the generic marked law, while the prior endpoint and mean identities support two additional exact questions: which integer geometries extremize the clock, and which geometry information survives coarse observation. The answers are respectively the strict unbalanced/balanced equality classes and the exact common-dilation boundary.

# Declarations {#declarations .unnumbered}

#### Data availability.

No external dataset is used. The paper-local exact verifier and its frozen text output accompany this anonymous internal manuscript.

#### Ethics statement.

The work is mathematical and uses no human participants, personal data, animals, or interventions.

#### Author contributions.

The anonymous author or authors performed the conceptualization, derivations, exact verification, source audit, and manuscript preparation. Identity and individual role allocation remain suppressed for anonymous review.

#### Conflict of interest.

No conflict of interest is declared.

#### Funding.

No external funding is declared for this manuscript.

#### External status.

The manuscript remains under `HOLD_EXTERNAL`; compilation does not authorize posting, submission, circulation, or author contact.
