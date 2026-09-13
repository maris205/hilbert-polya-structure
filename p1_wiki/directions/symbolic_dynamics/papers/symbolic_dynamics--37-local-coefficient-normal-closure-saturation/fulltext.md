---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--37-local-coefficient-normal-closure-saturation"
canonical_tex: "symbolic_dynamics/papers/37-local-coefficient-normal-closure-saturation/main.tex"
canonical_pdf: "symbolic_dynamics/papers/37-local-coefficient-normal-closure-saturation/main.pdf"
source_sha256: "a37bf4fce1ce7cdbc61d0b520d935c57809e02404f24313d739be4f05567725e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Cancel the Relator, Lose the Ledger: Local-Coefficient Saturation on an Affine Hashimoto Shift

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/37-local-coefficient-normal-closure-saturation>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/37-local-coefficient-normal-closure-saturation/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/37-local-coefficient-normal-closure-saturation/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/37-local-coefficient-normal-closure-saturation/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/37-local-coefficient-normal-closure-saturation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We prove a finite-coefficient saturation trilemma for the unquotiented affine Hashimoto shifts associated with $M_r=\langle u,v\mid vu=u^rv\rangle^+$, $r\ge2$. Source-coordinate damping makes every uniformly bounded finite-rank matrix-weighted shift trace class while preserving one free variable per original transition. Complete ordinary deletion of a primitive matrix Euler factor is nevertheless impossible for invertible local transport: the factor is trivial exactly when its holonomy is nilpotent. An explicit graded rank-two shear pair gives a sharper near miss. It cancels the defining relator, every conjugate, and every repetition because the two holonomies have the same characteristic polynomial, but the primitive mixed word $\bar u^r v\bar u^{r-1}vu\bar v^2$ has supertrace $-4r^4(r-1)\ne0$. Strengthening cancellation to every mixed product of conjugated relators removes this leakage only by covering the full normal closure: every closed Cayley factor then cancels and the graded determinant is identically one. A source/evaluator-separated exact audit passes 131/131 checks; all eight affine direct factors cancel, all eight rows leak, and every accidental direct match in 48 random one-relator and 24 paired two-relator controls also leaks. Thus the frozen finite-rank mechanism has no selective point between relation leakage and total closed-ledger erasure. The conclusion does not extend to arbitrary groupoids, cocycles, or infinite-dimensional coefficient algebras.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 15, 2026'
title: |
  Cancel the Relator, Lose the Ledger:\
  Local-Coefficient Saturation on an Affine Hashimoto Shift
```

## Markdown 正文

# Introduction

Paper 36 leaves a precise coefficient question. Filling every affine Cayley relation cell cancels too much: the resulting complex is contractible, and its inhomogeneous cell does not preserve the original unit edge clock. Can one instead keep every path and the same clock, then use finite-dimensional parallel transport to make relation factors invisible inside an honestly owned matrix Fredholm determinant?

We answer this question on the frozen source itself. For $$M_r=\langle u,v\mid vu=u^rv\rangle^+,
  \qquad r\ge2,$$ retain the formal-reverse oriented-edge graph, its cyclically nonbacktracking Hashimoto shift, one factor of $z$ per transition, and the source-coordinate damping inherited from Paper 36. Every edge transport is invertible and the reverse edge receives the inverse matrix. The accepted unit is the complete primitive matrix Euler factor, including all repetitions; a vanishing first trace is not enough.

The resulting obstruction is a fork, not a failure to define an operator. Source damping gives a trace-class matrix Hashimoto operator on the full uninduced state space for the frozen generator-role connection (and, more generally, for uniformly bounded finite-rank transports). In an ordinary determinant, however, a primitive factor is one exactly when its holonomy is nilpotent. Invertible transport cannot satisfy that condition. A graded ratio can cancel nontrivial holonomy, but matching the defining cell does not propagate through mixed products. If that propagation is imposed as an additional obligation, it reaches the whole normal closure and erases every closed orbit.

#### Analytic ownership.

For each fixed uniformly bounded finite-rank edge connection, the weighted Hashimoto operator is trace class. Its connected Fredholm logarithm groups into complete matrix factors on the same path space and the same free $z$. The graded object is stated separately as a ratio of two ordinary determinants; it is never rebranded as a positive determinant.

#### Explicit leakage.

The source-derived shear fixture sends $u$ to $A=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$ and sends $v$ to $B_{\pm r}=\left(\begin{smallmatrix}1&0\\ \pm r&1\end{smallmatrix}\right)$ in the two parities. The direct relator holonomies have equal characteristic polynomials, so all their powers cancel. Yet the primitive mixed word $$\bar u^r v\bar u^{r-1}vu\bar v^2$$ has graded trace $-4r^4(r-1)$. This formula is nonzero for every exponent in the theorem range and is visible before any finite audit.

#### Contributions.

The paper establishes four source-locked claims.

-   A source-coordinate-damped, uniformly bounded matrix Hashimoto operator owns one trace-class Fredholm determinant and the unchanged transition marker.

-   An ordinary finite-dimensional primitive factor disappears exactly for nilpotent holonomy; invertible local transport therefore deletes none.

-   A frozen graded connection cancels the direct affine cell at all powers but leaks on an explicit primitive mixed relation word for all $r\ge2$.

-   Cancellation on every mixed normal-closure product makes every closed Cayley factor invisible, so exact completion proves too much.

The composite exponent $r=4$ is the baseline. Balanced $r=1$, exponent mutations $2,3,5,6,7,8$, six fixed one-relator mutations, 48 random one-relator controls, and 24 paired two-relator controls test genericity. They show that direct factor matching is neither unique to the affine family nor an arithmetic recognition rule.

#### Scope.

The theorem is finite-rank and factorwise. It does not claim a new twisted Ihara theory, a no-go for every groupoid or infinite-dimensional coefficient algebra, or an arithmetic Euler product. No prime basis, support projector, finite quotient, first return, KMS/GNS boundary slice, target coefficient, or target zero enters the source. Route B remains locked.

The remainder separates established matrix-zeta theory from the narrow claim, freezes the coefficient object, proves the trilemma, audits the exact controls, and closes the branch with the only eligible successor object.

# Primary literature and claim boundary {#sec:literature}

Matrix holonomy in dynamical factors is established. The twisted Perron--Frobenius framework attaches finite-dimensional twists to periodic orbits and dynamical $L$-functions [@AdachiSunada1987]. Matrix-weighted graph zeta has also been related to group presentations and twisted Alexander polynomials [@Goda2020]. These sources own the principle that a closed orbit carries a complete matrix factor. They do not ask a coefficient rule to erase the normal closure of one affine presentation while retaining a proper primitive subledger.

The analytic determinant is likewise not new. Infinite weighted graphs with finite total weight admit Ihara products and Fredholm determinant formulas [@Deitmar2015]. Unitary matrix-weighted Ihara factors package Wilson-loop power traces, making repetition ownership explicit [@MatsuuraOhta2024]. Paper 37 specializes these established mechanisms to a source-coordinate-damped affine edge shift; novelty is not claimed for trace ideals, determinant logarithms, or matrix holonomy products.

Recent work makes the presentation collision closer. Holonomy-preserving transformations of matrix- and group-weighted graphs connect graph zeta data with transformations of group presentations [@Nagasaka2025]. Current matrix-weighted digraph formulas retain edge/vertex determinants and complete trace expansions [@GodaMorifuji2026]. Their aim is preservation and identification of zeta data. The present question is the opposite: how much of the orbit ledger remains after factorwise relation cancellation?

Two other boundaries prevent attribution drift. Gray and Steinberg provide the contractible one-relator monoid complex used only in the flat branch [@GraySteinberg2022]; this paper does not claim that topology as new. Simple-cycle and trace-monoid determinant formulas retain a graph's cycle ledger [@Watanabe2026]; they do not supply a coefficient system that deletes presentation consequences.

The source-locked claim is therefore narrow. For the frozen affine shift, a finite-rank graded edge connection can cancel all repetitions of the defining relator while leaking on an explicit primitive mixed consequence; requiring cancellation on the full normal closure instead makes every closed factor invisible. Newton identities, Cayley--Hamilton, twisted zeta theory, and contractibility remain attributed background. No priority claim is made for matrix-weighted determinants, local systems, or Ihara products.

# Frozen same-object coefficient model {#sec:source}

## Paths, marker, and edge transport

Let $G_r=\mathbb Z[1/r]\rtimes_r\mathbb Z$ be the enveloping group, with $vuv^{-1}=u^r$. We retain the formal-reverse enlargement of the positive right Cayley graph of $M_r$. A Hashimoto state is an oriented edge, and $$e\longrightarrow f
  \quad\Longleftrightarrow\quad
  t(e)=o(f),\qquad f\ne\bar e,
  \label{eq:hashimoto-rule}$$ with the same exclusion at the cyclic join. Paths are not quotiented, induced, or accelerated. Every application of [\[eq:hashimoto-rule\]](#eq:hashimoto-rule){reference-type="ref" reference="eq:hashimoto-rule"} contributes one free factor of $z$.

Let $E$ be a finite-dimensional complex fiber. Assign invertible transports $$P_e:E_{o(e)}\longrightarrow E_{t(e)},
  \qquad P_{\bar e}=P_e^{-1}.
  \label{eq:inverse-transport}$$ A transport family enters the analytic Fredholm statement only when it is uniformly bounded: $$M_P:=\sup_{e\in E_r^{\mathrm{or}}}\lVert P_e\rVert<\infty.
  \label{eq:uniform-transport}$$ The frozen shear fixture is generator-role constant, so this condition is automatic. The factorwise finite-matrix statements below do not otherwise depend on uniform boundedness. With row fibers, a closed word $\gamma=e_0\cdots e_{\ell-1}$ has holonomy $$W_\gamma=P_{e_0}\cdots P_{e_{\ell-1}}.
  \label{eq:holonomy}$$ A cyclic base change conjugates this matrix and preserves its complete determinant factor.

## Damping and matrix Fredholm object

If $o(e)=(b(e),k(e))$, freeze $$d_\theta(e)=\theta^{1+b(e)+k(e)},\qquad
  T_{P,\theta}=(D_{\theta}\otimes I_E)H_P(D_{\theta}\otimes I_E),
  \qquad 0<\theta<1.
  \label{eq:matrix-operator}$$ The damping depends only on affine source coordinates and is applied unchanged to every control. For a primitive orbit set $$q_\theta(\gamma)=\prod_{e\in\gamma}d_\theta(e)^2>0.
  \label{eq:orbit-weight}$$ The accepted ordinary unit is $$\det\!\left(I-q_\theta(\gamma)z^{|\gamma|}W_\gamma\right)^{-1}.
  \label{eq:ordinary-factor}$$ Neither one trace nor a scalar obtained by merging distinct orbit monomials is an accepted replacement.

## Graded ownership and terminology

For $E_+\oplus E_-$, with each parity family satisfying [\[eq:uniform-transport\]](#eq:uniform-transport){reference-type="ref" reference="eq:uniform-transport"}, keep the two ordinary trace-class operators distinct and define $$Z_{\mathrm{gr}}(z)=\frac{\det(I-zT_-)}{\det(I-zT_+)}.
  \label{eq:graded-ratio}$$ This virtual ratio is not called an ordinary positive determinant. Its factor at $\gamma$ is the quotient of the odd and even determinant polynomials from [\[eq:ordinary-factor\]](#eq:ordinary-factor){reference-type="ref" reference="eq:ordinary-factor"}.

A genuine local coefficient system on the filled Cayley $2$-complex is flat: each relation-cell holonomy is identity. A rule with nontrivial cell holonomy is instead an edge connection on the unfilled $1$-skeleton. The distinction is essential because the filled complex is contractible.

An orbit is cancelled only when its complete determinant polynomials agree in the two parities, equivalently when every super-power-trace vanishes. Equality at the first trace, after $z=1$, or after aggregation across primitive orbits earns no credit.

The source process may construct presentations, words, bounded mixed products, and the frozen matrices. The evaluator independently performs free/cyclic reduction, affine evaluation, exact matrix multiplication, factor comparison, and decisions. Prime or factor tables, accepted support, target zeros, coefficient fitting, and network data are forbidden from both processes.

# Finite-coefficient relation-saturation trilemma {#sec:theorem}

[\[thm:saturation\]]{#thm:saturation label="thm:saturation"} Fix $r\ge2$, the unquotiented affine Hashimoto shift, the unit transition marker $z$, the damping in [\[eq:matrix-operator\]](#eq:matrix-operator){reference-type="ref" reference="eq:matrix-operator"}, and finite-rank transports satisfying [\[eq:inverse-transport,eq:uniform-transport\]](#eq:inverse-transport,eq:uniform-transport){reference-type="ref" reference="eq:inverse-transport,eq:uniform-transport"}.

1.  *Ordinary branch.* No primitive orbit with invertible holonomy has a trivial complete Euler factor.

2.  *Flat graded branch.* If the coefficients descend to the filled Cayley $2$-complex, relation-factor cancellation occurs only at balanced parity; balanced parity cancels every closed orbit.

3.  *Non-flat graded branch.* Cancelling each translated defining cell, its free-group conjugates, and every repetition does not imply cancellation of mixed cell products. The frozen shear pair cancels the direct affine relator but has a primitive mixed word with supertrace $-4r^4(r-1)$. If cancellation is strengthened to every finite mixed product of conjugated cells and inverses, it applies to every closed Cayley word, and $Z_{\mathrm{gr}}(z)=1$.

Consequently this coefficient class cannot erase the complete affine relation ledger while retaining a nonzero primitive arithmetic sector on the same object.

The clauses have separate dependencies. The ordinary branch uses only finite-dimensional determinant algebra. The flat branch uses the inherited contractibility theorem. The direct-pass/mixed-fail statement uses exact $2\times2$ multiplication. Complete saturation uses only the presentation kernel as a normal closure. The finite audit proves none of these infinite-scope statements.

[\[cor:first-trace\]]{#cor:first-trace label="cor:first-trace"} The condition $\mathop{\mathrm{Tr}}W=0$ does not delete a primitive factor. For $$J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
  \qquad \mathop{\mathrm{Tr}}J=0,$$ one has $\mathop{\mathrm{Tr}}(J^2)=-2$ and $\det(I-tJ)=1+t^2$. A factor decision must include every repetition.

[\[cor:nilpotent\]]{#cor:nilpotent label="cor:nilpotent"} The matrix $N=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)$ satisfies $\mathop{\mathrm{Tr}}(N^m)=0$ for all $m\ge1$ and $\det(I-tN)=1$, but $N$ is not invertible. It is an endomorphism weight or automaton transition, not local parallel transport.

[\[cor:flat\]]{#cor:flat label="cor:flat"} Let the parity ranks be $d_+$ and $d_-$. On the filled contractible Cayley complex, every closed holonomy is identity up to gauge, so a graded primitive factor is $(1-t)^{d_--d_+}$. Unequal ranks retain every factor; equal ranks cancel every factor.

The theorem does not infer mixed-product cancellation from individual-cell cancellation. That implication is false, and the explicit shear family below is its counterexample. The terminal conclusion instead says that if mixed cancellation is imposed for the entire normal closure, then the target class is already the whole closed ledger.

# Ordinary factors and determinant ownership {#sec:factor}

## Trace class on the full edge space

At most four oriented edges originate at any affine vertex. Therefore $$\mathop{\mathrm{Tr}}(D_{\theta})
  \le 4\sum_{b,k\ge0}\theta^{1+b+k}
  =\frac{4\theta}{(1-\theta)^2}<\infty.
  \label{eq:damping-trace}$$ Tensoring with a finite-dimensional identity preserves trace class. With $M_P$ from [\[eq:uniform-transport\]](#eq:uniform-transport){reference-type="ref" reference="eq:uniform-transport"}, every row and column of $H_P$ contains at most three nonzero blocks. The block Schur test gives $$\lVert H_P\rVert\le3M_P.
  \label{eq:block-schur}$$ The two-sided trace-ideal property now makes $T_{P,\theta}$ trace class. This is the weighted infinite-graph Fredholm setting, not a determinant assigned to a finite quotient [@Deitmar2015].

For $|z|<\lVert T_{P,\theta}\rVert^{-1}$, $$-\log\det(I-zT_{P,\theta})
  =\sum_{n\ge1}\frac{z^n}{n}\mathop{\mathrm{Tr}}(T_{P,\theta}^n).
  \label{eq:fredholm-log}$$ No quotient, support projection, or boundary representation appears in this ownership statement.

## Primitive grouping

Expanding a diagonal block in [\[eq:fredholm-log\]](#eq:fredholm-log){reference-type="ref" reference="eq:fredholm-log"} gives one based cyclically nonbacktracking path. A primitive orbit $\gamma$ repeated $m$ times contributes $|\gamma|$ cyclic base states; this cancels the factor $m|\gamma|$ coming from the logarithm at length $m|\gamma|$. Absolute convergence near zero permits grouping into $$-\log\det(I-zT_{P,\theta})
  =\sum_{[\gamma]\ \mathrm{primitive}}\sum_{m\ge1}
  \frac{q_\theta(\gamma)^m z^{m|\gamma|}}{m}
  \mathop{\mathrm{Tr}}(W_\gamma^m).
  \label{eq:primitive-expansion}$$ Equation [\[eq:ordinary-factor\]](#eq:ordinary-factor){reference-type="eqref" reference="eq:ordinary-factor"} follows by the finite-dimensional determinant logarithm. This matrix-holonomy organization is established in twisted and matrix-weighted graph zeta theory [@AdachiSunada1987; @Goda2020; @MatsuuraOhta2024]; the source-locked question is what factorwise cancellation can leave.

For two parities, subtraction is allowed only after each determinant has been owned: $$\log Z_{\mathrm{gr}}(z)
  =\sum_{[\gamma]}\sum_{m\ge1}
  \frac{q_\theta(\gamma)^m z^{m|\gamma|}}{m}
  \left[\mathop{\mathrm{Tr}}((W_\gamma^+)^m)-\mathop{\mathrm{Tr}}((W_\gamma^-)^m)\right].
  \label{eq:graded-expansion}$$

## Why ordinary deletion is impossible

Let $W$ be $d\times d$. Its primitive factor is trivial precisely when $$\det(I-tW)=1.
  \label{eq:factor-one}$$ If [\[eq:factor-one\]](#eq:factor-one){reference-type="ref" reference="eq:factor-one"} holds, every nonconstant characteristic coefficient vanishes. Equivalently, Newton identities make every power trace vanish and the characteristic polynomial is $x^d$. Cayley--Hamilton gives $W^d=0$. The converse is immediate for nilpotent $W$. Thus $$\det(I-tW)=1
  \quad\Longleftrightarrow\quad
  \mathop{\mathrm{Tr}}(W^m)=0\ (m\ge1)
  \quad\Longleftrightarrow\quad
  W\ \text{nilpotent}.
  \label{eq:nilpotence}$$

Every holonomy formed from [\[eq:inverse-transport\]](#eq:inverse-transport){reference-type="ref" reference="eq:inverse-transport"} is invertible. The ordinary branch therefore cannot delete one affine relation factor, much less the complete relation ledger. Allowing the nilpotent control from [\[cor:nilpotent\]](#cor:nilpotent){reference-type="ref" reference="cor:nilpotent"} changes the coefficient category rather than repairing local transport.

The free marker survives this negative result. Each term of [\[eq:primitive-expansion\]](#eq:primitive-expansion){reference-type="ref" reference="eq:primitive-expansion"} carries the actual edge length $z^{m|\gamma|}$, and no cell comparison changes it. The Route-A analytic gate therefore passes even though the recurrence-selection gates fail.

# Direct cancellation and mixed leakage {#sec:shear}

The graded branch can delete a nontrivial factor by spectral matching. Freeze $$A=\begin{pmatrix}1&1\\0&1\end{pmatrix},
  \qquad
  B_c=\begin{pmatrix}1&0\\c&1\end{pmatrix}.
  \label{eq:shear-matrices}$$ Both parities send $u$ to $A$. The even parity sends $v$ to $B_r$, the odd parity sends $v$ to $B_{-r}$, and formal reverse letters receive exact inverses. The rule reads only generator roles and the source exponent.

For the defining cyclic word $R_r=vu\bar v\bar u^r$, $$W_c(R_r)=B_cAB_c^{-1}A^{-r},
  \qquad
  \mathop{\mathrm{Tr}}W_c(R_r)=2+c^2r,
  \qquad
  \det W_c(R_r)=1.
  \label{eq:direct-characteristic}$$ The choices $c=r$ and $c=-r$ have identical characteristic polynomials. Hence their power traces agree for every $m\ge1$. Free-group conjugation conjugates the matrices, so every conjugate and every repetition of the direct relator cancels exactly in [\[eq:graded-expansion\]](#eq:graded-expansion){reference-type="ref" reference="eq:graded-expansion"}.

This all-orders success does not pass through multiplication. Consider $$M_r=\bar u^r v\bar u^{r-1}vu\bar v^2.
  \label{eq:mixed-word}$$ It is an actual closed path based at $(r^2,0)$: $$\begin{aligned}
  (r^2,0)&\xrightarrow{\bar u^r}(r^2-r,0)
  \xrightarrow{v}(r^2-r,1)
  \xrightarrow{\bar u^{r-1}}(0,1)\\
  &\xrightarrow{v}(0,2)
  \xrightarrow{u}(r^2,2)
  \xrightarrow{\bar v^2}(r^2,0).
\end{aligned}
\label{eq:mixed-path}$$ No adjacent pair is an inverse, including the cyclic join. The word is primitive because it has exactly one lowercase $u$, impossible for a proper word power. Its length is $2r+4$, so it is neither the direct relator nor a repetition of its length $r+3$.

Exact multiplication gives $$\begin{aligned}
  \mathop{\mathrm{Tr}}W_c(M_r)
  ={}&-2c^3r^2+2c^3r-c^2r^2\\
     &+6c^2r-c^2+2.
\end{aligned}
\label{eq:mixed-trace-polynomial}$$ Subtracting the odd value from the even value yields $$\mathop{\mathrm{Tr}}W_r(M_r)-\mathop{\mathrm{Tr}}W_{-r}(M_r)
  =-4r^4(r-1)\ne0,
  \qquad r\ge2.
  \label{eq:mixed-leak}$$ The source damping multiplies this coefficient by $q_\theta(M_r)>0$ and cannot cancel it.

At the balanced control $r=1$, the displayed polynomial difference vanishes; the preregistered bounded census instead finds a different primitive mixed leak. Each exponent mutation $r=2,\ldots,8$ follows [\[eq:mixed-leak\]](#eq:mixed-leak){reference-type="ref" reference="eq:mixed-leak"}. Direct matching is thus a presentation-syntax rule. The surviving mixed word receives no arithmetic credit merely because it belongs to the affine presentation.

# Normal-closure saturation erases the ledger {#sec:normal-closure}

Let $F=F(u,v)$ and let $$N_r=\langle\!\langle R_r\rangle\!\rangle_F,
  \qquad G_r=F/N_r.
  \label{eq:normal-closure}$$ Every closed path label maps to the identity in $G_r$. Its freely reduced word therefore lies in $N_r$ and has a finite expression $$w=\prod_{j=1}^{m}a_jR_r^{\varepsilon_j}a_j^{-1},
  \qquad \varepsilon_j\in\{+1,-1\}.
  \label{eq:normal-form-product}$$ Hashimoto reduction only removes adjacent inverse letters and does not move a word outside the normal closure. By [\[eq:inverse-transport\]](#eq:inverse-transport){reference-type="ref" reference="eq:inverse-transport"}, each such removal also leaves both parity holonomies unchanged.

Equation [\[eq:direct-characteristic\]](#eq:direct-characteristic){reference-type="eqref" reference="eq:direct-characteristic"} cancels each individual conjugate and repetition, but matrix multiplication does not preserve spectral matching factor by factor. The nonzero value in [\[eq:mixed-leak\]](#eq:mixed-leak){reference-type="ref" reference="eq:mixed-leak"} is an explicit counterexample to such an inference.

Now impose the complete inherited obligation: every finite mixed product in [\[eq:normal-form-product\]](#eq:normal-form-product){reference-type="ref" reference="eq:normal-form-product"}, including inverses and repetitions, must have a trivial graded primitive factor. This obligation applies to every cyclically reduced closed path and hence to every primitive root in [\[eq:graded-expansion\]](#eq:graded-expansion){reference-type="ref" reference="eq:graded-expansion"}. All connected coefficients vanish, so $$\log Z_{\mathrm{gr}}(z)=0,
  \qquad
  Z_{\mathrm{gr}}(z)=1.
  \label{eq:empty-graded-ledger}$$

The flat branch reaches the same terminal state by a different route. The filled Cayley $2$-complex is contractible under the verified one-relator monoid hypotheses [@GraySteinberg2022]. A flat connection has identity holonomy on each closed loop. In ordinary rank $d$, the factor $(1-t)^{-d}$ survives. For graded ranks $d_+,d_-$, the ratio is $(1-t)^{d_--d_+}$. Only balanced parity cancels the relation, and then it cancels every closed path.

Four ledgers must not be conflated:

1.  the ordinary positive matrix factors of $T_+$ or $T_-$;

2.  the virtual graded ratio $Z_{\mathrm{gr}}$;

3.  flat holonomy on the filled contractible complex;

4.  the non-flat shear connection on the unfilled graph.

They share a presentation and marker notation but not positivity, flatness, or cancellation semantics.

The theorem therefore proves an exact dichotomy. Omitting mixed products leaves relation leakage; including the complete normal closure erases the whole closed ledger. A proper intermediate class would need an independent, source-canonical definition before coefficients are chosen. The failed shear representation cannot define that class after observing its residue.

# Exact source/evaluator-separated audit {#sec:audit}

The frozen prototype tests finite witnesses and implementation identities; it does not numerically approximate the infinite Fredholm determinant. The source process constructs presentations, relator products, and the frozen matrices. A separate evaluator imports no source module and independently performs free and cyclic reduction, affine evaluation, exact integer matrix arithmetic, characteristic-polynomial comparison, and decisions.

All 131 preregistered assertions pass. For $r=1,\ldots,8$, every direct factor cancels. Every row also has a primitive mixed leak in the bounded two-cell census.

::: {#tab:affine-audit}
    $r$ role                 shortest leak in frozen census     length   first supertrace
  ----- -------------------- -------------------------------- -------- ------------------
      1 balanced control     `UUVuvvuV`                              8               $-8$
      2 mutation             `UUvUvuVV`                              8              $-64$
      3 mutation             `UUUvUUvuVV`                           10             $-648$
      4 composite baseline   `UUUUvUUUvuVV`                         12            $-3072$
      5 mutation             `UUUUUvUUUUvuVV`                       14           $-10000$
      6 mutation             `UUUUUUvUUUUUvuVV`                     16           $-25920$
      7 mutation             `UUUUUUUvUUUUUUvuVV`                   18           $-57624$
      8 mutation             `UUUUUUUUvUUUUUUUvuVV`                 20          $-114688$

  : Affine controls. Uppercase letters denote formal inverses. For $r\ge2$, the row is [\[eq:mixed-word\]](#eq:mixed-word){reference-type="ref" reference="eq:mixed-word"} and its value is exactly $-4r^4(r-1)$. "Shortest" is relative only to the preregistered bounded census.
:::

The generic controls distinguish direct-factor matching from arithmetic selection.

\@L0.38rrL0.25@ control family & total & direct matches & mixed result after match\
affine $r=1,\ldots,8$ & 8 & 8 & leaks $8/8$\
random cyclic one-relator & 48 & 9 & leaks $9/9$\
paired random two-relator & 24 & 2 both-match & both leak\

The evaluator checks power supertraces through order twelve, the traceless invertible and nilpotent boundaries, exact inverse-edge matrices, all affine closed paths, six fixed mutations, and the random controls generated with seed $370037$. The independent authority layer reproduces all 131 assertions and passes 32/32 integration tests. Fresh A/B and isolated cold C reproduce the scientific, source-packet, and Route bytes exactly; four metadata states, two manifest states, and a second materialization leave the scientific bytes unchanged. The closed result set has 26 files, all 82 integrity checks pass, and all 39 immutable-ledger entries verify. The scientific payload SHA-256 is `b17967f294da018e2e045ae70ac7731f5612f4bd4693115ea33dbaebb7fc0d6e`. The pre-seal Route card is schema-audited separately from that immutable ledger so its paired provenance can be bound metadata-only.

The finite data corroborate the direct-match formula, mixed leakage, generic firewall, and source/evaluator split. Trace-class ownership, arbitrary-rank nilpotence, flat triviality, the all-$r$ formula, and normal-closure saturation are proved independently in [\[sec:factor,sec:shear,sec:normal-closure\]](#sec:factor,sec:shear,sec:normal-closure){reference-type="ref" reference="sec:factor,sec:shear,sec:normal-closure"}.

# Route decision and conclusion {#sec:conclusion}

The coefficient mechanism owns an analytic determinant but fails every selection obligation downstream of that ownership.

\@lL0.20Y@ gate & status & source-locked reason\
A0 & structural origin & $r$ occurs in the affine relation and semidirect multiplication; no external arithmetic oracle defines it\
A1 & fail & partial cancellation leaves mixed relation recurrence, while complete saturation leaves no recurrence\
A2 & analytic determinant & $T_+$ and $T_-$ are trace class on the same full edge shift and retain the unit $z$ marker\
A3 & fail & the graded determinant is either relation-contaminated or identically one and supplies no target analytic structure\
A4 & fail & no fixed self-adjoint carrier, target divisor, or critical-line mechanism is constructed\

The exact repository tuple is $$\begin{gathered}
(\texttt{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},\quad
 \texttt{A1\_FAIL},\quad
 \texttt{A2\_ANALYTIC\_DETERMINANT},\\
 \texttt{A3\_FAIL},\quad
 \texttt{A4\_FAIL}).
\end{gathered}$$ The overall decision is `ROUTE_A_REJECTED`; Route B is not invoked. The branch conclusion is $$\boxed{\texttt{CLOSE\_LOCAL\_COEFFICIENT\_SATURATION\_BRANCH}.}$$

The result is not that every matrix-weighted graph determinant is trivial. It is that the frozen complete relation obligation has no selective finite-rank solution on this Cayley ledger. Ordinary invertible transport cannot start deletion. The explicit graded mechanism deletes direct cells but not their mixed consequences. Completing that mechanism makes the target class equal to every closed path and forces $Z_{\mathrm{gr}}=1$.

The only eligible successor changes the symbolic object rather than another matrix. Paper 38 may test the presentation-canonical Bass--Serre tree of the original ascending HNN splitting, its full nonbacktracking geodesic shift, and the canonical modular cocycle. It must quantify the new tree-edge clock and receives no same-object credit for the Cayley shift studied here. Another representation, character, fiber rank, nilpotent automaton, boundary support, or arbitrary completion on the current ledger is ineligible.

No completion, functional equation, explicit formula, target-zero calculation, critical-line form, or RH implication appears in the argument.

# Proof details and exact calculations

## Primitive factor grouping

In a diagonal block of $T_{P,\theta}^n$, each admissible cyclic edge word contributes the product of its $n$ transport blocks and two copies of every diagonal damping weight. For $\gamma^m$, cyclic re-basing gives $|\gamma|$ diagonal terms, while the trace-log divisor at length $m|\gamma|$ is $m|\gamma|$. Their quotient is $1/m$. This proves [\[eq:primitive-expansion\]](#eq:primitive-expansion){reference-type="ref" reference="eq:primitive-expansion"}; applying the finite identity $$-\log\det(I-tW)=\sum_{m\ge1}\frac{t^m}{m}\mathop{\mathrm{Tr}}(W^m)$$ gives the complete primitive factor. All regrouping occurs inside the absolute-convergence disk of the trace-class Fredholm series.

## Graded factor criterion

If every super-power-trace of $W_+,W_-$ vanishes, subtracting the two formal determinant logarithms gives zero. Their determinant polynomials have constant term one, so the quotient is exactly one. Conversely, equality of the determinant polynomials gives equality of every logarithmic coefficient. Newton identities recover each polynomial from finitely many power traces; no diagonalizability assumption is needed.

For invertible matrices, equality of determinant polynomials is equality of the full eigenvalue multisets with algebraic multiplicity. Zero eigenvalues cannot be inserted to hide a rank mismatch.

## Direct shear multiplication

The inverse matrices in [\[eq:shear-matrices\]](#eq:shear-matrices){reference-type="ref" reference="eq:shear-matrices"} are $$A^{-1}=\begin{pmatrix}1&-1\\0&1\end{pmatrix},
  \qquad
  B_c^{-1}=\begin{pmatrix}1&0\\-c&1\end{pmatrix}.$$ Since $A^{-r}=\left(\begin{smallmatrix}1&-r\\0&1\end{smallmatrix}\right)$, direct multiplication of $B_cAB_c^{-1}A^{-r}$ gives determinant one and trace $2+c^2r$. A $2\times2$ characteristic polynomial is fixed by trace and determinant, proving equality for $c=\pm r$.

## Mixed path and primitivity

Using $(b,k)(d,\ell)=(b+r^kd,k+\ell)$, the vertices in [\[eq:mixed-path\]](#eq:mixed-path){reference-type="ref" reference="eq:mixed-path"} remain in $\mathbb N_0\rtimes_r\mathbb N_0$ whenever a positive edge is traversed; every reverse segment is the formal reverse of an existing positive segment. Hence the displayed word is a path in the frozen graph, not merely an identity in the group completion.

Its cyclic adjacent pairs have generator types $$\bar u\bar u,\ \bar u v,\ v\bar u,\ \bar u v,\ vu,\ u\bar v,
  \ \bar v\bar v,\ \bar v\bar u,$$ none of which is an inverse pair. A proper $d$-fold temporal power would repeat the number of lowercase $u$ letters by $d$; the word contains exactly one. Thus it is primitive.

Multiplying $A^{-r}B_cA^{-(r-1)}B_cAB_c^{-2}$ gives $$\mathop{\mathrm{Tr}}W_c(M_r)
=-2c^3r^2+2c^3r-c^2r^2+6c^2r-c^2+2.$$ Its odd part in $c$ is $-2c^3r(r-1)$. Evaluating at $c=r$ and $c=-r$ therefore yields $-4r^4(r-1)$.

## Normal-closure coverage

A closed path label is an identity in $G_r=F/N_r$, so it lies in $N_r$ by definition. Every element of the normal closure is a finite product of conjugates of $R_r$ and $R_r^{-1}$. Free reduction may shorten such a product but cannot change its image in $F/N_r$; the inverse-edge rule also makes each removed transport pair equal to the identity. Consequently, an obligation imposed on every mixed product applies to each primitive closed-path root. Substitution in [\[eq:graded-expansion\]](#eq:graded-expansion){reference-type="ref" reference="eq:graded-expansion"} proves [\[eq:empty-graded-ledger\]](#eq:empty-graded-ledger){reference-type="ref" reference="eq:empty-graded-ledger"}.

# Scope declarations and ownership ledger

\@L0.22L0.19L0.22Y@ object & coefficient/marker & trace framework & frozen conclusion\
positive affine graph & none / unit edge & none needed & acyclic before formal reverses\
formal-reverse Hashimoto shift & scalar / unit $z$ & path ledger & relation and mixed closed paths present\
$T_{P,\theta}$ & invertible matrices / unit $z$ & Hilbert trace; trace class & ordinary primitive factors cannot be deleted\
$T_+,T_-$ & graded matrices / unit $z$ & two ordinary Fredholm traces & direct match leaks on mixed products\
$Z_{\mathrm{gr}}$ & virtual ratio / unit $z$ & difference after ownership & saturation gives determinant one\
filled Cayley complex & flat local system & homotopy/cellular & contractible; balanced grading cancels all\
nilpotent control & noninvertible endomorphism & finite matrices & factor one, but not parallel transport\

The no-go applies only to finite-rank inverse-edge mechanisms under the complete mixed-relation obligation on this affine Cayley shift. It does not rule out matrix-weighted graph zeta in general, an infinite-dimensional trace, a groupoid cocycle, or an independently defined loop class on another object.

Six substitutions receive no credit: a first trace for a complete factor; a nilpotent endomorphism for invertible transport; a graded ratio for a positive determinant; $z=1$ for equality of free germs; a quotient, first return, or boundary support for the full source; or a representation-discovered residue for a source-canonical arithmetic class.

No peer-review or LLM review loop was run, following the project instruction. The mathematical proof, primary-source audit, exact source/evaluator audit, compilation, typography, and provenance checks remain separate deterministic evidence layers.
