---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--41-knauf-rooted-clock-non-descent"
canonical_tex: "symbolic_dynamics/papers/41-knauf-rooted-clock-non-descent/main.tex"
canonical_pdf: "symbolic_dynamics/papers/41-knauf-rooted-clock-non-descent/main.pdf"
source_sha256: "876d2d41c0417ba5c2691a45fb644b9a06ae671c54f0139dea50476130b777e5"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Rooted Knauf Clock Does Not Descend to Cycles

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/41-knauf-rooted-clock-non-descent>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/41-knauf-rooted-clock-non-descent/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/41-knauf-rooted-clock-non-descent/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/41-knauf-rooted-clock-non-descent/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/41-knauf-rooted-clock-non-descent/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The Knauf binary recursion has the source-owned partition limit $\sum_{n\ge1}\varphi(n)n^{-s}=\zeta(s-1)/\zeta(s)$ for $\operatorname{Re}s>2$. We ask the narrower typed question of whether its exact rooted label $h(w)=\mathbf 1^{\mathsf T}M_we_1$ also supplies a cyclic primitive ledger, additive repetition clock, scalar Liouville phase, and a Fredholm determinant whose trace powers enumerate those same primitive returns. It does not. The trailing-zero stable quotient admits no canonical right append-one action; $h(01)\ne h(10)$; and $h(11)\ne h(1)^2$. Moreover, for the Liouville function $\lambda(n)=(-1)^{\Omega(n)}$, where $\Omega(n)$ counts prime factors with multiplicity, $\lambda(h(w))$ fails both cyclic and power descent. A diagonal operator on stable states does realize the partition function as a trace and owns an ordinary marked determinant, but its marker counts inventory powers rather than binary returns. These exact witnesses yield a source-specific Route-A rejection while leaving trace clocks, enlarged states, non-scalar cocycles, and established Farey/Gauss transfer models outside the theorem. The selection and witness package are retrospective and carry no prospective or priority claim.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 17, 2026'
title: The Rooted Knauf Clock Does Not Descend to Cycles
```

## Markdown 正文

# Introduction {#sec:introduction}

An arithmetic partition function can resemble a dynamical zeta expression without carrying the primitive objects that a dynamical determinant counts. The distinction is especially sharp for the rooted Knauf binary recursion: its limiting partition sum is an exact quotient of zeta functions, while its finite source states are rooted words embedded by trailing zeroes. The quotient identity and its phase-transition setting belong to the original number-theoretic spin-chain literature [@knauf1993phases; @knauf1998spin; @knauf1999erratum].

The issue studied here is not whether that arithmetic identity is valid. It is whether the very same finite object and label also determine the data needed for a scalar primitive-orbit determinant: a state on which the binary step acts autonomously, a clock that is independent of the root of a cyclic word and additive under repetition, a scalar phase with the corresponding power law, and an operator whose trace powers count those same returns. A partition trace supplies none of these identifications by notation alone.

We therefore evaluate the smallest object-preserving bridge. We retain the source matrices, the rooted label $h(w)=\mathbf 1^{\mathsf T}M_we_1$, the stable-state quotient under trailing zeroes, ordinary cyclic rotation, ordinary word powers, and the literal Liouville observable $\lambda(h(w))$, where $\lambda(n)=(-1)^{\Omega(n)}$ and $\Omega(n)$ counts prime factors with multiplicity. Exact words of length at most three then settle the necessary descent questions; previews the object-preserving bridge and its first failure. A separate trace-class argument identifies the diagonal determinant that the stable-state inventory actually owns. Neither argument uses target zeros, fitted parameters, or a prime-indexed external component.

Related Farey constructions make the typing issue concrete. A translation-invariant Farey chain can share free energy with a related non-translation-invariant number-theoretic chain, and generalized Farey models connect matrix recursions to intermittent transfer operators [@klebanOzluk1999farey; @fiala2003phase; @fialaKleban2005generalized]. Trace-energy chains exploit cyclic invariance, and prescribed-trace matrix products have their own arithmetic counting theory [@prellbergFialaKleban2006cluster; @technau2023farey]. These are genuine models, but equality of free energy or use of the same generators does not identify their finite objects, clocks, or return operators with the rooted first-column-sum object tested here.

The same firewall applies to determinant language. Orbit zeta and transfer-operator determinants are genuine dynamical constructions when their phase spaces, weights, and operator domains are specified [@ruelle1976zeta; @mayer1990gauss; @mayer1991selberg]; their existence does not identify an operator for the rooted label. Conversely, the diagonal operator constructed below is a valid Fredholm object, but its free marker enumerates powers of inventory eigenvalues rather than binary returns.

The contribution is therefore a closure theorem, not a new zeta mechanism. It has three parts. First, the canonical append-one step does not descend to the trailing-zero colimit. Second, the rooted clock and literal scalar phase fail cyclic and repetition descent by explicit witnesses. Third, the exact state-inventory determinant is derived and assigned to its legal owner. The source recursion and quotient, thermodynamic trace-chain repairs, generalized transfer operators, and the general partition-trace principle remain prior art. The selection that led to this test is retrospective and receives no novelty or priority credit.

records this source ownership and the claim boundary. fixes the types and matrix convention. proves the finite non-descent theorems, and derives the determinant owned by state inventory. maps those results to the strict Route coordinates without adding experiment claims. Complete exact products, domain restrictions, and literature firewalls appear in the appendices.

# Prior ownership, retrospective selection, and scope {#sec:prior-scope}

#### Source arithmetic.

The source literature owns the number-theoretic spin chain, its phase structure, the stable multiplicity $\varphi(n)$, and the quotient $\zeta(s-1)/\zeta(s)$. The partition-function and phase analysis is already present in @knauf1993phases; the binary arithmetic chain and its Riemann-zero program, together with the required correction, are source work of @knauf1998spin [@knauf1999erratum]. We inherit those facts and use the source matrix convention. We do not treat the quotient, the totient ledger, or the phase transition as a Paper-41 result.

#### Thermodynamic equivalence is not object identity.

The Farey fraction chain of @klebanOzluk1999farey is translation invariant and has the same free energy as a related non-translation-invariant number-theoretic chain. Several Farey-fraction models likewise share free energy and connect to transfer-operator thermodynamics [@fiala2003phase]. From these source facts we draw only a typing inference: equality of free energy does not imply equality of finite states, rooting convention, clock, primitive ledger, marker, or operator. This sentence is not attributed to those papers as a quoted theorem; it is the contract discipline used in the present audit.

#### Changed trace and transfer models.

Parameterized generalized chains are connected to an intermittent transfer operator and the Lewis equation [@fialaKleban2005generalized]. A trace-energy Farey chain obtains translation invariance from cyclicity of the matrix trace, while its matrices and energies remain distinguished from generalized Knauf quantities even when thermodynamic limits agree [@prellbergFialaKleban2006cluster]. The adelic Markov operator studied by @knauf2013adelic is a further, separate operator and phase space. None of these changed models acts by declaration on the frozen rooted-state quotient.

#### Recent trace counting.

@technau2023farey counts products of Farey matrices with prescribed trace. That result is relevant positive context for trace-based arithmetic, but trace is conjugacy-compatible whereas $h(w)=\mathbf 1^{\mathsf T}M_we_1$ reads a distinguished column. It therefore does not settle the rooted non-descent theorem below.

\@P.14YYYY@ Source family & Finite object & Clock or energy & Operator owner & Transfer to `SD-C06`\
Exact Knauf rooted chain & Rooted binary word and trailing-zero stable class & $h(w)$ and $\log h(w)$ & Finite inventory; no declared autonomous return operator & Source-owned object; descent must be proved\
Farey trace chain & Cyclic or translation-invariant matrix word & $\operatorname{Tr}(M_w)$-based energy & Trace/Farey model operator & Changed clock and object\
Generalized chain & Parameterized recursive state & Generalized energy/expectation data & Intermittent transfer model & Changed object and operator\
Adelic Markov model & Adelic state space & Markov spectral data & Adelic transition operator & Separate phase space\
Gauss/Selberg family & Continued-fraction or modular returns & Derivative/geodesic weights & Dynamical transfer operator & Comparator only\
Paper-41 diagonal inventory & Stable states indexed with multiplicity $\varphi(n)$ & $n^{-s}$ eigenvalue weight & $Q_s$ on $\ell^2(S_K)$ & Owns only its inventory determinant\

The historical candidate was selected by a Boolean rule applied after all six Session-4 cards, their outcomes, and the present witnesses were known. The unique rule result is `SD-C06`. The rule required the exact card statuses `A0_ANALYTIC_ARITHMETIC_ORIGIN`, `A1_FAIL`, `A2_FAIL`, and `A3_PARTIAL_ANALYTIC_STRUCTURE`, together with the card's request for a primitive-ledger no-go and an endogenous-sign test. Paper 39 supplies existence provenance but performs no ranking or successor authorization; Paper 40 supplies neither selection nor novelty. Uniqueness of this retrospective rule is not prospective evidence and does not establish discovery priority.

Our quantifiers stop at declared source-preserving attempts. Enlarging the state to the full matrix, replacing $h$ by trace or an eigenvalue, adding a history-dependent cocycle, or importing a Farey/Gauss transfer operator is a legitimate new model but not an in-place repair. The bounded literature audit did not locate the exact four-witness conjunction in a primary source; that is a search result rather than a universal novelty theorem. All source modules in retain their own credit.

# Frozen rooted object and typed quotients {#sec:source-types}

We fix the source convention of the Knauf chain [@knauf1998spin; @knauf1999erratum]. Let $W=\{0,1\}^{*}$, with empty word $\varepsilon$, and set $$L=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
 R=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad
 M_w=M_{w_1}\cdots M_{w_k},$$ where $M_0=L$ and $M_1=R$. The rooted label is $$h(w)=\mathbf 1^{\mathsf T}M_we_1,
 \qquad \mathbf 1=(1,1)^{\mathsf T},\quad e_1=(1,0)^{\mathsf T}.$$ The citation fixes source ownership and convention; the calculation below is an explicit derivation rather than an appeal to authority.

For a binary word $u$, let $\bar u$ denote its bitwise complement. Then $$h(u0)=h(u),\qquad h(u1)=h(u)+h(\bar u).$$

Write $M_u=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$. Then $h(u)=a+c$. Right multiplication gives $$M_uL=\begin{pmatrix}a&a+b\\c&c+d\end{pmatrix},\qquad
 M_uR=\begin{pmatrix}a+b&b\\c+d&d\end{pmatrix}.$$ Thus $h(u0)=a+c$ and $h(u1)=a+b+c+d$. With $J=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$ one has $JLJ=R$, $JRJ=L$, and hence $M_{\bar u}=JM_uJ$. It follows that $h(\bar u)=b+d$, proving the recurrence.

This identity matters because $h$ is rooted. It reads the first column of $M_w$, whereas $\operatorname{Tr}(M_w)$ is invariant under cyclic permutation of factors. The latter property underlies trace-energy Farey models [@prellbergFialaKleban2006cluster]; it is a positive control, not an identity for the rooted label.

The relevant mathematical types are listed in . The table prevents three common category errors: equating the trailing-zero colimit with a shift space, treating a necklace as a rooted word with forgotten notation, and interpreting a free Fredholm marker as physical return time.

\@P.18YYYY@ Object & Equivalence or indexing & Marker & Legal data/operator & Prohibited identification\
`KnaufRootedWord` & Equality of rooted words & Depth $k$ & $M_w$, first column, $h(w)$ & Cyclic primitive class\
`KnaufStableState` & Colimit relation generated by $w\sim w0$ & Dirichlet variable $s$ & Stable $h$ and full multiplicity ledger & Autonomous right append action\
`BinaryNecklace` & Cyclic rotation of a nonempty word & Repetition $r$ & Period and powers after a clock descends & Rooted $h$ value\
`FareyTraceWord` & Matrix/cyclic word & Trace or eigenvalue clock & Cyclic trace and matrix-power data & Frozen rooted partition trace\
`LiouvilleState``Observable` & Arithmetic value after evaluating $h$ & Scalar sign & $\lambda(h(w))$ & Endogenous symbolic cocycle\
`StateInventory``Diagonal` & Stable-state basis with multiplicity & Free marker $u$ & $Q_s$ and its marked determinant & Binary return operator\
`DynamicalTransfer``Operator` & Separately declared phase space & Return/iterate marker & Trace powers only when constructed & Source ownership by notation\

In particular, depth $k$, Dirichlet variable $s$, determinant marker $u$, and temporal repetition $r$ have different owners. No result below identifies them.

# Exact non-descent theorem {#sec:non-descent}

All witnesses in this section use the source-owned matrix convention [@knauf1998spin; @knauf1999erratum]. The products are reproduced in ; no literature citation substitutes for their exact evaluation.

The frozen label satisfies $$h(\varepsilon)=1,\quad h(0)=1,\quad h(1)=2,\quad
 h(01)=3,\quad h(10)=2,\quad h(11)=3,$$ and $$h(001)=4,\qquad h(010)=3.$$

These values follow by direct multiplication of $L$ and $R$. For example, $LR=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)$ and $RL=\left(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\right)$, so their first-column sums are $3$ and $2$. The remaining products are displayed in .

[\[thm:rooted-clock\]]{#thm:rooted-clock label="thm:rooted-clock"} There is no map on the trailing-zero quotient satisfying $A_1([w])=[w1]$ for every rooted word. There is no function on binary necklaces whose value on $[w]_{\mathrm{cyc}}$ is $h(w)$ for every nonempty word. Independently, the identity $h(w^r)=h(w)^r$ does not hold for every word and repetition.

Let $\sim_0$ be the equivalence relation generated by $w\sim_0w0$. The recurrence gives $h(w0)=h(w)$, so $h$ is constant on every stable class. Yet $[\varepsilon]=[0]$ while their proposed append-one images would be $[1]$ and $[01]$. Because $h(1)=2\ne3=h(01)$, these images lie in distinct stable classes. Thus the proposed $A_1$ is not well defined.

For cyclic descent, $01$ and $10$ are rotations, but $h(01)=3\ne2=h(10)$. A representative-independent necklace function cannot take both values. For temporal powers, the single-letter word gives $h(11)=3\ne4=h(1)^2$. These failures are logically independent of the first quotient failure. Since all values are positive, the last two equalities are also necessary for $T=\log h$ to be a cyclic and temporally additive orbit clock.

The first assertion excludes the canonical right append-one rule on the source colimit, not every self-map of the underlying set. The second and third concern the exact $h$ clock, cyclic rotation, and ordinary word powers. They do not exclude a chosen-root convention, a full-matrix state, a trace clock, or an eigenvalue clock; each changes at least one frozen coordinate.

[\[thm:phase\]]{#thm:phase label="thm:phase"} The observable $\ell(w)=\lambda(h(w))$ neither descends to binary necklaces nor satisfies $\ell(w^r)=\ell(w)^r$ for all words and repetitions. No one-letter multiplicative character equals $\ell$ on every rooted word.

The cyclic rotations $001$ and $010$ have labels $4$ and $3$. Hence $\ell(001)=\lambda(4)=+1$ whereas $\ell(010)=\lambda(3)=-1$. For repetition, $\ell(1)=\lambda(2)=-1$ while $\ell(11)=\lambda(3)=-1\ne(+1)=\ell(1)^2$.

A one-letter multiplicative character has the form $\chi(w)=\alpha^{\#0(w)}\beta^{\#1(w)}$. Agreement with $\ell$ on $0$ and $1$ forces $\alpha=1$ and $\beta=-1$. Agreement on $11$ would then require $-1=\ell(11)=\beta^2=+1$, a contradiction.

The theorem is about the literal scalar observable evaluated after $h$. It does not quantify over arbitrary history-dependent or matrix-valued cocycles on enlarged states. That distinction is essential: calling $\lambda(h(w))$ endogenous does not make it a symbolic orbit character.

The positive controls show that the argument is projection-specific rather than a blanket no-go. Cyclic trace models are established in the Farey literature, and prescribed-trace products form a valid arithmetic family [@prellbergFialaKleban2006cluster; @technau2023farey]. Algebraically, $\operatorname{Tr}(M_uM_v)=\operatorname{Tr}(M_vM_u)$, and the Perron eigenvalue of a fixed matrix obeys the matrix-power law. Those controls change the rooted clock and therefore do not repair in place.

# The determinant owned by state inventory {#sec:inventory}

Let $S_K$ be the trailing-zero colimit. We inherit the source multiplicity theorem $$\#\{x\in S_K:h(x)=n\}=\varphi(n)$$ and the associated partition identity from the number-theoretic spin-chain literature [@knauf1993phases; @knauf1998spin; @knauf1999erratum]. The following theorem does not create primitive dynamics; it identifies the operator and determinant already forced by that inventory.

[\[thm:inventory-determinant\]]{#thm:inventory-determinant label="thm:inventory-determinant"} For $\operatorname{Re}s>2$, define the diagonal operator on $\ell^2(S_K)$ by $$Q_se_x=h(x)^{-s}e_x.$$ Then $Q_s$ is trace class and $$\operatorname{Tr}Q_s=\sum_{n\ge1}\varphi(n)n^{-s}
 =\frac{\zeta(s-1)}{\zeta(s)}.$$ Its Fredholm determinant is entire in the free variable $u$ and equals $$\Delta_K(s,u)=\det(I-uQ_s)
 =\prod_{n\ge1}(1-un^{-s})^{\varphi(n)}.$$ For $|u|<1$ its local trace-log is $$-\log\Delta_K(s,u)
 =\sum_{r\ge1}\frac{u^r}{r}
   \frac{\zeta(rs-1)}{\zeta(rs)}.$$ Finally, $\Delta_K(s,1)=0$.

Put $\sigma=\operatorname{Re}s>2$. Because $Q_s$ is diagonal, its trace norm is $$\lVert Q_s\rVert_1
 =\sum_{x\in S_K}|h(x)^{-s}|
 =\sum_{n\ge1}\varphi(n)n^{-\sigma}<\infty.$$ Thus $Q_s$ is trace class. Absolute convergence permits regrouping by the exact multiplicity of each label, yielding the displayed zeta quotient.

Trace-class Fredholm theory gives an entire function of $u$ and the product over eigenvalues. Regrouping those eigenvalues by $n$ gives the second product. Moreover $\lVert Q_s\rVert=1$, since the $n=1$ eigenvalue is one and every other eigenvalue has modulus below one. Hence, for $|u|<1$, the operator series for $-\log(I-uQ_s)$ converges in the domain needed to take traces. Therefore $$-\log\det(I-uQ_s)
 =\sum_{r\ge1}\frac{u^r}{r}\operatorname{Tr}(Q_s^r).$$ The same multiplicity ledger gives $$\operatorname{Tr}(Q_s^r)=\sum_{n\ge1}\varphi(n)n^{-rs}
 =\frac{\zeta(rs-1)}{\zeta(rs)},$$ because $\operatorname{Re}(rs)>2$ for every positive integer $r$. Finally, $\varphi(1)=1$, so the determinant product contains the factor $1-u$ and vanishes at $u=1$.

The theorem separates three statements that can otherwise be conflated. The coefficient of $u$ in the trace-log is the source partition function. The higher coefficients count powers of fixed diagonal eigenvalues. The free marker $u$ is neither binary depth nor temporal return time, and $Q_s$ depends on the Dirichlet parameter rather than defining a fixed self-adjoint Hilbert--Polya operator.

This diagonal inventory determinant is not the orbit determinant appearing in expanding-map or Gauss/modular transfer-operator formalisms [@ruelle1976zeta; @mayer1990gauss; @mayer1991selberg]. Its marker enumerates powers of fixed inventory eigenvalues, not returns of binary primitive classes. Those references provide changed-model context; they do not prove the formula for $Q_s$, which was derived above.

Thus is an ownership control. It proves that the obstruction is not an absence of all Fredholm determinants. It also proves why this particular determinant cannot earn A2 primitive-orbit credit: the source binary refinement has no declared return operator on $S_K$, and the rooted clock already fails the cyclic and power laws required for such a ledger.

# Strict Route audit and reproducibility boundary {#sec:route}

The strict Route tuple is a typed summary of the preceding proofs, not a numerical score. Each coordinate has an independent owner and failure mode, as shown in .

\@P.06P.29YP.20@ Rung & Retained evidence & Decisive boundary & Status\
A0 & Source multiplicities give the exact arithmetic partition quotient on $\operatorname{Re}s>2$ & The quotient alone supplies neither primitive rational-prime objects nor an endogenous sign cocycle & `A0_ANALYTIC``ARITHMETIC_ORIGIN`\
A1 & Matrix convention and all finite products are exact & Append-one, cyclic clock, temporal power, and scalar-phase descent fail & `A1_FAIL`\
A2 & $Q_s$ owns a valid marked Fredholm determinant & Its states and marker are inventory powers, not primitive binary returns & `A2_FAIL`\
A3 & The source quotient has a displayed meromorphic continuation & No same-object completed divisor, functional equation, or signed critical-half-plane theorem is derived & `A3_PARTIAL``ANALYTIC``STRUCTURE`\
A4 & A parameter-dependent diagonal trace operator exists & No fixed self-adjoint operator, same-clock trace identity, or target multiplicity theorem exists & `A4_FAIL`\

Consequently the strict tuple is $$%
  \begin{gathered}
  (\texttt{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},\
   \texttt{A1\_FAIL},\
   \texttt{A2\_FAIL},\\
   \texttt{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},\
   \texttt{A4\_FAIL})
  \end{gathered}$$ with overall verdict `ROUTE_A_REJECTED` and Route B disallowed. The positive source identity does not override the object failures in A1 and A2, and the parameter-dependent diagonal operator does not upgrade A4.

The independent DA verified the sealed research package, typed source resolver, matrix convention, exact witnesses, theorem quantifiers, operator domains, retrospective selection, literature boundary, and Route coordinates. That review is governance evidence for the frozen research bytes; it is not a numerical experiment and does not enlarge the theorem.

The reproducibility boundary is therefore simple. Theorems [\[thm:rooted-clock\]](#thm:rooted-clock){reference-type="ref" reference="thm:rooted-clock"}--[\[thm:inventory-determinant\]](#thm:inventory-determinant){reference-type="ref" reference="thm:inventory-determinant"} depend only on the frozen source convention, exact integer products, the inherited multiplicity theorem, and trace-class algebra. A later implementation can independently replay those dependencies, but it cannot strengthen the claim, change the Route tuple, or transfer ownership from another model without a new source lock.

# Limitations and conclusion {#sec:conclusion}

The Knauf partition quotient remains a rigorous arithmetic trace. What the frozen source does not supply is a canonical cyclic primitive ledger with the same rooted clock, ordinary repetition, literal Liouville phase, and binary return operator. The exact witnesses establish that bounded statement, while the diagonal construction identifies the determinant that state inventory actually owns.

The conclusion is intentionally local. Matrix traces, Perron eigenvalues, full-matrix states, non-scalar cocycles, and established transfer operators may restore missing structures by changing the model. Trace/Farey repairs and generalized transfer models are legitimate new source locks [@klebanOzluk1999farey; @fialaKleban2005generalized; @prellbergFialaKleban2006cluster]. The adelic Markov operator is a separate alternative [@knauf2013adelic], and Gauss/modular transfer operators have their own phase spaces and determinant ownership [@mayer1990gauss; @mayer1991selberg]. None is an unresolved exception to the theorem proved here.

A reopened candidate must therefore declare, before analytic target comparison, its phase space, equivalence relation, clock, repetition marker, scalar or non-scalar phase, function space, and operator owner. It must then prove the bridge between those coordinates rather than import it from equal free energy or shared matrices. If the rooted $h$ label and its literal types are retained, the present witnesses remain terminal. If a coordinate is changed, the resulting construction should be evaluated as a new model with its own provenance and Route record.

# Exact algebra and complete proof map {#app:proofs}

This appendix makes every finite calculation used above explicit. The matrix convention and multiplicity input are source-owned [@knauf1998spin; @knauf1999erratum; @knauf1993phases]; all deductions from them are reproduced here.

## Recurrence and exact products

For $M_u=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$, right multiplication by $L$ preserves the first column, while right multiplication by $R$ replaces it by the sum of the two columns. The conjugacy $M_{\bar u}=JM_uJ$ identifies the second-column sum with $h(\bar u)$. This proves $h(u0)=h(u)$ and $h(u1)=h(u)+h(\bar u)$ without transposition or reversed word order.

The exact products needed by all witnesses are

\@c c c@ $w$ & $M_w$ & $h(w)$\
$\varepsilon$ & $\left(\begin{smallmatrix}1&0\\0&1\end{smallmatrix}\right)$ & $1$\
$0$ & $\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$ & $1$\
$1$ & $\left(\begin{smallmatrix}1&0\\1&1\end{smallmatrix}\right)$ & $2$\
$01$ & $\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)$ & $3$\
$10$ & $\left(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\right)$ & $2$\
$11$ & $\left(\begin{smallmatrix}1&0\\2&1\end{smallmatrix}\right)$ & $3$\
$001$ & $\left(\begin{smallmatrix}3&2\\1&1\end{smallmatrix}\right)$ & $4$\
$010$ & $\left(\begin{smallmatrix}2&3\\1&2\end{smallmatrix}\right)$ & $3$\

## Stable quotient and rooted action

Let $\sim_0$ be generated by $w\sim_0w0$. Repeated use of the recurrence shows that $h$ is constant on each equivalence class. Since $\varepsilon\sim_00$, a descended right append-one action would imply $[1]=[01]$. The table gives $h(1)=2$ and $h(01)=3$, contradicting class invariance. The contradiction uses the same invariant that certifies the source quotient; it does not assume a topology or an undeclared shift map.

## Clock and phase descent

The words $01$ and $10$ differ by a cyclic rotation, but their rooted labels are $3$ and $2$. Hence no function on necklaces can equal $h$ on every representative. The power witness is independent: $11=1^2$ as a word, yet $h(11)=3\ne4=h(1)^2$. Because $h>0$, these identities are necessary for $\log h$ to be representative-independent and additive under powers.

For the literal phase, $001$ and $010$ are rotations and have labels $4$ and $3$. Their Liouville values are $+1$ and $-1$. Also $\lambda(h(11))=\lambda(3)=-1$, whereas $\lambda(h(1))^2=\lambda(2)^2=+1$. Finally, a one-letter character agreeing on $0$ and $1$ must have generator values $1$ and $-1$, so it takes the value $+1$ on $11$, contradicting the exact value $-1$.

## Inventory determinant and repair trilemma

The source multiplicity theorem gives one eigenvalue $n^{-s}$ for each of the $\varphi(n)$ stable states with label $n$. Absolute summability on $\operatorname{Re}s>2$ proves trace class, justifies grouping the trace, and yields the product in . For $|u|<1$, the norm-convergent logarithm gives the trace powers. This chain uses no cyclic-word identification. In particular, the $n=1$ inventory state forces the factor $1-u$.

The declared source-preserving repair list is now exhausted. Quotienting rooted words by rotation contradicts the clock witness. Keeping the literal scalar phase contradicts the phase witnesses. Keeping the stable quotient with the full right binary action contradicts append-one non-descent. Using $Q_s$ changes the marker to inventory powers. Trace/eigenvalue clocks and enlarged matrix states change the source object or clock. Thus at least one frozen coordinate must be surrendered; the statement does not range over undeclared extensions.

The positive controls confirm that the proof does not prohibit cyclic or temporal matrix data in general. Direct calculation gives $\operatorname{Tr}(LR)=\operatorname{Tr}(RL)=3$, and the spectral radius of a fixed positive matrix obeys $\rho(M^r)=\rho(M)^r$. Both controls pass only after replacing the rooted first-column-sum clock.

# Operator, literature, Route, and lock boundaries {#app:boundaries}

## Analytic and operator domains

The determinant statement has distinct domains that are not interchangeable.

\@P.27P.23Y@ Statement & Domain & What is not implied\
$\sum_n\varphi(n)n^{-s}=\zeta(s-1)/\zeta(s)$ & $\operatorname{Re}s>2$ by absolute convergence & Finite-depth convergence outside the domain\
$Q_s$ trace class and $\det(I-uQ_s)$ entire in $u$ & Fixed $s$ with $\operatorname{Re}s>2$ & A fixed self-adjoint operator independent of $s$\
Local trace-log series & $\operatorname{Re}s>2$ and $|u|<1$ & A global logarithm across determinant zeros\
Meromorphic continuation of the scalar quotient & As a quotient of zeta functions & Continuation of missing primitive dynamics or signed convergence\

At $u=1$ the determinant vanishes because of the $n=1$ state. This is not a singularity to be removed in order to recover the partition quotient; it is part of the determinant owned by the inventory. The source partition trace is its first trace-log coefficient, not the determinant evaluated at a special marker.

## Literature collision matrix

The literature audit was bounded by the frozen search protocol. The phrase "the audit did not locate" records that search; it is not a claim that no prior work exists.

\@P.22YY@ Prior family & Source-owned result & Paper-41 boundary\
Knauf source chain [@knauf1993phases; @knauf1998spin; @knauf1999erratum] & Partition quotient, phase setting, recursion, and arithmetic program & Only the exact rooted non-descent conjunction is tested here\
Farey free-energy equivalence [@klebanOzluk1999farey; @fiala2003phase] & Equal free energies for related but distinct formulations & No transfer of finite object, clock, ledger, or operator\
Generalized transfer model [@fialaKleban2005generalized] & Parameterized chain, intermittent operator, and Lewis-equation connection & Changed state and operator\
Trace-energy chain [@prellbergFialaKleban2006cluster] & Cyclic trace clock and translation invariance & Positive control; no novelty credit and no rooted-$h$ repair\
Adelic operator [@knauf2013adelic] & Distinct Markov transition operator and spectral problem & Separate phase space\
Prescribed-trace counts [@technau2023farey] & Counts of Farey matrix products with fixed trace & No theorem about first-column sums or Liouville phase\
Dynamical determinants [@ruelle1976zeta; @mayer1990gauss; @mayer1991selberg] & Expanding-map, Gauss, and modular transfer-operator formalisms & Comparator only; no proof or owner for $Q_s$ or the rooted return map\

The metadata used here is limited to sealed records. In particular, the ASCII author form "Ozluk" is retained for the two records whose sealed arXiv metadata uses that spelling; no unverified diacritic or issue number is introduced. Ruelle and Mayer are cited solely as changed-model comparators, not as evidence for the present theorem or its novelty.

## Chronology and immutable boundary

The selector was assembled after all six historical cards, their Route outcomes, and the exact witnesses were known. Its unique result is therefore retrospective provenance, not preregistration, outcome-independent evidence, or priority. Paper 39 records candidate existence but does not rank or authorize this successor; Paper 40 neither selects it nor supplies novelty.

The immutable authority release consists of the exact 16-file `preauthority/` package and the two independent-DA files named by the root research pointer. The manuscript, bibliography, figures, writer handoff, diagnostic compilation, and any later canonical integration block remain mutable writer artifacts. No code, result, experiment, evaluation, paper manifest, root README, registry, Git, or mirror artifact is created by this candidate.

Within this boundary the strict conclusion remains `ROUTE_A_REJECTED`, with Route B false. A changed trace clock, enlarged state, non-scalar cocycle, or imported transfer operator requires a new source lock and a fresh Route evaluation; it cannot be used to reinterpret the exact STOP as a positive result for the original object.
