---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--09-holomorphic-reflection-double"
canonical_tex: "symbolic_dynamics/papers/09-holomorphic-reflection-double/main.tex"
canonical_pdf: "symbolic_dynamics/papers/09-holomorphic-reflection-double/main.pdf"
source_sha256: "2980a9d01a93e9d46003d37f3b64b8aca3c817e369f97eaaddfcb1415fb4cf03"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Holomorphic Reflection Doubles of Positive-Cone Symbolic Transfers: Functional Symmetry, Vertical Sterility, and Finite-Channel Rigidity

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/09-holomorphic-reflection-double>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/09-holomorphic-reflection-double/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/09-holomorphic-reflection-double/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/09-holomorphic-reflection-double/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/09-holomorphic-reflection-double/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Paper08 obtained an exact Euler ledger on a recurrent tensor-prime base using a positive-cone cocycle, but its self-adjoint double restored a divergent inverse backtrack. We remove the adjoint and test the holomorphic reflected double $$\mathcal C_s=\begin{pmatrix}0&T_s^+\\T_{1-s}^-&0\end{pmatrix},$$ where the two layers use independent positive alphabets and a canonical identity trace. This defines SD-C11. The two blocks belong simultaneously to $L^q$ on $1/q<\Re s<1-1/q$, so $q=3$ gives a nonempty critical strip. Layer exchange proves exact $s\mapsto1-s$ determinant symmetry. The hoped-for gain does not occur. With independent positive alphabets, every word using a cross edge is trace-invisible. The surviving pure atom word alternates the two layers, and each pair has weight $p^{-s}p^{-(1-s)}=p^{-1}$. Hence every visible even trace and every regularized determinant is independent of $s$; the vertical parameter is sterile. We prove a finite-channel rigidity theorem: for a holomorphic monomial channel system whose identity-visible closed words are invariant under reflection and use only one atom, reflection balance forces total exponent $k/2$ at length $k$, so the critical-axis phase cancels. Breaking balance restores height dependence only by using unequal atoms, which produces mixed masses $p^{-s}q^{-(1-s)}$, or by inverse-identifying the positive alphabets, which exposes precisely such mixed two-step words. Finite channel multiplicity and constant phases cannot evade the dichotomy. Thus holomorphic doubling avoids the $gg^{-1}$ norm-square divergence but replaces it with vertical sterility. SD-C11 is a sharp scoped obstruction, not a completed determinant; Route B remains locked.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 13, 2026'
title: |
  Holomorphic Reflection Doubles of Positive-Cone Symbolic Transfers:\
  Functional Symmetry, Vertical Sterility, and Finite-Channel Rigidity
```

## Markdown 正文

# Introduction {#sec:introduction}

The Session-4 symbolic chain now supplies three exact components. Tensor indecomposable full shifts recover rational primes and their entropy clock. An atom-loop transfer gives the Euler product. A positive-cone cocycle over a bidirectional atom grammar retains base recurrence while the canonical trace removes mixed periodic lifts. The obstruction in Paper08 arose only after self-adjointization: the adjoint introduced inverse words, and $gg^{-1}$ created a positive divergent quadratic trace.

The natural next attempt is to keep reflection but discard the adjoint. Use one holomorphic transfer at $s$, another at $1-s$, and alternate them in a two-layer symbolic grammar. Independent positive alphabets prevent an edge in one layer from cancelling an edge in the other. The resulting operator pencil is holomorphic and has a common Schatten strip containing the critical line.

This paper shows that the cure has an exact price. Any identity-visible closed word of the off-diagonal double alternates the two layers equally. For a pure atom $p$, its weight is $$(p^{-s}p^{-(1-s)})^r=p^{-r}.                \tag{1.1}$$ The phase $e^{-it\log p}$ from one layer cancels the phase $e^{it\log p}$ from the reflected layer. The functional symmetry is exact, but it is achieved by making the determinant independent of height.

Could more channels or signed phases help? We prove a finite-channel rigidity statement for monomial symbolic transfers. If identity-visible closed words are pure in the atom label and the channel grammar enforces reflection balance, their total exponent is fixed by word length and their critical phase vanishes. A height-dependent visible word must either use unequal numbers of $s$ and $1-s$ weights or use unequal atom labels. The first breaks the reflected closed-channel balance; the second creates an unwanted mixed arithmetic mass. Finite phases can cancel individual controls but not alter this exponent ledger.

The contributions are:

1.  SD-C11, a frozen holomorphic two-layer positive-cone symbolic transfer;

2.  its exact common $L^q$ strip and reflection symmetry;

3.  an all-order vertical-sterility theorem for independent positive alphabets;

4.  a finite-channel exponent-balance rigidity theorem;

5.  exact controls for shared positive, inverse-identified, and cross-atom reflected labels;

6.  a determinant classification showing that height dependence and the exact pure-prime ledger cannot coexist in this class;

7.  a Route-A scoped stop and a locked Route B.

Only Symbolic Dynamics is developed. The result is intentionally a theorem paper about the boundary of the current route, not a forced positive claim.

# Holomorphic transfer pencils and symmetry {#sec:related}

Symbolic zeta determinants and holomorphic transfer families are classical [@bowenlanford1970; @ruelle1976]. Group twists organize periodic words by their cocycle monodromy [@parrypollicott1990], while identity-word zeta coefficients for matrices over free-group algebras provide the algebraic precedent for the positive-cone trace [@kasselreutenauer2014].

Flip systems and reversal signatures already provide nontrivial symbolic matrix formalisms for time reversal [@kimleepark2003; @ryu2023]. Their reversal-fixed counts are different from the tautological channel exchange used here. Classical regularized determinants supply the $\det_q$ expansion [@simon1977]; they do not turn block exchange into arithmetic content.

The present question is narrower than a general transfer-operator functional equation. We impose $s\leftrightarrow1-s$ directly through a two-layer symbolic grammar and ask whether one holomorphic determinant can both retain the tensor-prime ledger and move vertically. This differs from self-adjointization: no conjugation or adjoint appears in the definition.

Formal-language zeta theory shows that cyclic languages can admit finite-dimensional virtual-character realizations [@berstelreutenauer1990]; exterior automata give alternating determinants for sofic systems [@beal1995]. These results warn that finite channels and signs can change a trace presentation without changing the language's exponent ledger. Our rigidity theorem makes that warning explicit for reflected tensor-prime monomials.

We found no primary source proving the precise balance dichotomy used here: a finite-channel reflected positive-cone double over entropy-derived tensor-prime atoms is either vertically sterile on pure identity-visible words or admits mixed arithmetic masses. We claim this scoped theorem and its source-locked synthesis, not novelty for holomorphic transfer operators, twisted zeta functions, or formal-language determinants.

# SD-C11: the holomorphic reflected double {#sec:source}

Let $\operatorname{At}=\{F_{p_n}\}$ be the entropy-ordered tensor atoms. Retain the recurrent nearest-neighbor base grammar of SD-C10. Let $\mathbb F_+$ and $\mathbb F_-$ be free groups generated by disjoint directed-positive edge alphabets. Their group von Neumann algebras carry canonical traces $\tau_+$ and $\tau_-$. Work in $$\mathcal N=B(\ell^2(\operatorname{At}))\bar\otimes
 L(\mathbb F_+)\bar\otimes L(\mathbb F_-),
 \quad \Phi=\operatorname{Tr}\otimes\tau_+\otimes\tau_-.   \tag{3.1}$$

For $\varepsilon\in\{+,-\}$, let $T_s^\varepsilon$ be the SD-C10 transfer with its own positive alphabet: $$\begin{aligned}
 T_s^\varepsilon={}&\sum_np_n^{-s}E_{nn}\otimes1\notag\\
 &+\sum_n\frac{p_n^{-s}+p_{n+1}^{-s}}2
 \left(E_{n+1,n}\otimes\lambda(g_{n,+}^\varepsilon)
 +E_{n,n+1}\otimes\lambda(g_{n,-}^\varepsilon)\right). \tag{3.2}\end{aligned}$$ The unused group tensor factor acts as the identity. Define $$\boxed{
 \mathcal C_s=\begin{pmatrix}0&T_s^+\\T_{1-s}^-&0\end{pmatrix}}
 \quad\text{on }\mathbb C^2\otimes\ell^2(\operatorname{At})\otimes
 \ell^2(\mathbb F_+\times\mathbb F_-).       \tag{3.3}$$

The lower block is the same positive-monoid representation evaluated at $1-s$. It is not the adjoint, not the group-ring transpose, and does not apply $g\mapsto g^{-1}$. This convention is essential: each of those involutions would restore identity words that the positive cone is meant to filter.

This freezes SD-C11. The two channel states form a period-two symbolic extension; every step switches layers. Atom-loop weights are $p^{-s}$ in the plus layer and $p^{-(1-s)}$ in the minus layer. Cross-edge endpoint roofs and potentials are inherited unchanged. The determinant convention is the noncommutative regularized trace-series determinant $\det_q(I-z\mathcal C_s)$ on a common $L^q$ strip.

No Riemann zeros, target scales, fitted phases, or external system family are allowed. Reflection is the fixed layer swap $$J=\begin{pmatrix}0&I\\I&0\end{pmatrix}.     \tag{3.4}$$

[\[prop:strip\]]{#prop:strip label="prop:strip"} For integer $q\ge1$, $$\mathcal C_s\in L^q\quad\Longleftrightarrow\quad
 \frac1q<\operatorname{Re}s<1-\frac1q.               \tag{3.5}$$ The first nonempty integer strip is $q=3$. Moreover, after exchanging the two independent alphabets by their canonical generator bijection, $$J\mathcal C_sJ=\mathcal C_{1-s}.                          \tag{3.6}$$ Consequently every normalized trace-series $\det_q$ obeys $\Delta_q(s,z)=\Delta_q(1-s,z)$.

The two off-diagonal blocks belong to $L^q$ precisely when $q\Re s>1$ and $q(1-\Re s)>1$, as in the banded ideal theorem for SD-C10. Layer exchange swaps the blocks; the alphabet bijection identifies their otherwise disjoint universal copies. Trace and regularized determinant are invariant under this trace-preserving conjugacy.

The block-exchange identity holds for any family inserted in this two-channel template. It is therefore a proves-too-much control, not by itself a Riemann functional equation. Arithmetic credit depends entirely on the filtered closed-word ledger studied next.

# Pure-word vertical sterility {#sec:rigidity}

Independent positive alphabets ensure that no word containing a cross edge has identity monodromy. Indeed, its projection to at least one free factor is a nonempty positive word. Thus the only $\Phi_2$-visible closed words of $\mathcal C_s$ are alternating pure loops at one atom.

[\[thm:sterility\]]{#thm:sterility label="thm:sterility"} For every $r\ge1$ in the common trace domain, $$\Phi_2(\mathcal C_s^{2r})=2\sum_pp^{-r},
 \qquad
 \Phi_2(\mathcal C_s^{2r+1})=0.                    \tag{4.1}$$ Hence every regularized trace-series determinant of $\mathcal C_s$ is independent of $s$. Formally before regularization, $$\det_\Phi(I-z\mathcal C_s)=\prod_p(1-z^2/p).       \tag{4.2}$$ The product diverges at quadratic order; on the $L^3$ strip, $$\det{}_3(I-z\mathcal C_s)
 =\prod_p(1-z^2/p)e^{z^2/p},                 \tag{4.3}$$ which is convergent, reflection symmetric, and vertically constant.

Odd powers are off-diagonal. In an even closed word the layer grammar alternates exactly $r$ plus and $r$ minus steps. Canonical trace kills every cross-edge word. At a pure loop $p$, the weight is $$(p^{-s}p^{-(1-s)})^r=p^{-r}.$$ There are two starting layers, proving [\[eq:sterile-traces\]](#eq:sterile-traces){reference-type="ref" reference="eq:sterile-traces"}: $$\Phi_2(\mathcal C_s^{2r})=2\sum_pp^{-r}.
 \label{eq:sterile-traces}$$ The logarithmic determinant expansion gives the products. The $r=1$ prime harmonic term diverges and is precisely the quadratic subtraction in $\det_3$; all retained traces begin at $r=2$ and remain independent of $s$.

The construction therefore avoids Paper08's positive $gg^{-1}$ norm square, but reaches the same regularized product through a different obstruction: reflection balance makes every pure two-step mass $p^{-1}$.

## Finite-channel rigidity

We now isolate what two layers are doing. Consider a finite directed channel graph $H$ with an involution $\iota$ implementing reflection. Each edge $e$ carries an atom $p(e)$, a type $\epsilon(e)\in\{0,1\}$, and monomial weight $$w_e(s)=c_e p(e)^{-[(1-\epsilon(e))s+\epsilon(e)(1-s)]}, \tag{4.4}$$ where $c_e$ is independent of $s$. A closed word $W$ has plus count $a_W$, minus count $b_W$, and weight phase on $s=1/2+it$ $$\exp\left[-it\left(\sum_{e:\epsilon=0}\log p(e)
 -\sum_{e:\epsilon=1}\log p(e)\right)\right]. \tag{4.5}$$

[\[thm:finite-channel\]]{#thm:finite-channel label="thm:finite-channel"} Assume:

1.  every identity-visible closed word is pure in its atom label;

2.  the channel grammar is bipartite under reflection, so every closed word has $a_W=b_W$;

3.  coefficients and cocycle labels are independent of $s$.

Then every identity-visible weight is independent of $t$ on the critical line. Finite direct sums, constant signed phases, and virtual channel differences preserve this conclusion. Conversely, a height-dependent identity-visible word must violate purity or reflection balance.

For a pure word at $p$, [\[eq:channel-phase\]](#eq:channel-phase){reference-type="ref" reference="eq:channel-phase"} becomes $$e^{-it(a_W-b_W)\log p}=1.
 \label{eq:channel-phase}$$ The remaining real weight is $p^{-(a_W+b_W)/2}$ times the constant product of $c_e$. Taking finite sums, supertraces, or multiplying constant phases cannot reintroduce $t$. The contrapositive gives the final assertion.

This theorem is scoped to finite-channel monomial transfers with a bipartite reflection grammar. Infinite memory, nonmonomial potentials, or moving channel number are not ruled out.

# Every elementary escape pays one of two prices {#sec:controls}

## Shared positive labels

If the plus and minus layers use the same positive generator rather than independent alphabets, every word containing a cross edge still has positive total degree. The canonical trace kills it. The pure-loop formula [\[thm:sterility\]](#thm:sterility){reference-type="ref" reference="thm:sterility"} is unchanged. Independence is therefore not the source of vertical sterility.

## Inverse identification

Suppose instead that a minus-layer edge is labelled by the inverse of a plus-layer edge. A two-step reflected word can now have identity monodromy. For a plus edge carrying atom endpoint mass $p^{-s}$ and its reflected minus edge carrying $q^{-(1-s)}$, the new term is $$p^{-s}q^{-(1-s)}
 =\frac{1}{\sqrt{pq}}
 e^{-it\log(p/q)}.                           \tag{5.1}$$ It moves with $t$ exactly when $p\ne q$. But then its arithmetic length is the mixed ordered pair $(p,q)$, not a repetition $p^r$ of one primitive atom. If $p=q$, the term is the allowed mass $p^{-1}$ and is vertically constant.

[\[prop:two-step\]]{#prop:two-step label="prop:two-step"} An identity-visible reflected two-step monomial is either:

1.  pure, with weight $p^{-1}$ independent of $s$; or

2.  height-dependent, with weight $p^{-s}q^{-(1-s)}$, $p\ne q$, and hence an unwanted mixed-atom ledger entry.

No constant phase changes this dichotomy.

Equation (5.1) gives both cases. Multiplication by an $s$-independent phase does not change its frequency $\log(p/q)$ or its atom support.

## More channels and signed cancellation

A finite channel grammar can pair several words with the same mixed frequency and choose phases whose coefficients sum to zero. If cancellation is exact, that frequency disappears from every traced determinant coefficient and cannot move its divisor. If any mixed frequency remains, unique factorization identifies its ordered prime exponent vector, so it remains a mixed ledger term. Pure balanced words remain frequency zero by [\[thm:finite-channel\]](#thm:finite-channel){reference-type="ref" reference="thm:finite-channel"}.

Thus finite channels offer no third elementary outcome: $$\boxed{
 \text{pure reflected word}\Rightarrow\text{no motion},
 \qquad
 \text{moving reflected word}\Rightarrow\text{mixed ledger}.}$$ This is stronger than a failed numerical fit: it is an all-order exponent classification for the frozen model class.

## What the theorem does not exclude

The result does not cover infinite-channel cancellations, nonlocal infinite-memory potentials, or a holomorphic roof that is not a finite monomial combination of entropy endpoints. Such extensions would need their own source provenance, nuclear domain, and adversarial controls. They cannot be inferred by taking a formal infinite limit of this theorem.

# Exact finite falsification design {#sec:experiment}

The mathematics is exact enough that computation serves as a bookkeeping audit. The frozen finite experiment should enumerate atom prefixes, channel words, and reduced cocycle labels without loading target zeros.

For atoms $p,q$, the minimal pure block is $$\mathcal C_s^{(p)}=
 \begin{pmatrix}0&p^{-s}\\p^{-(1-s)}&0\end{pmatrix},
 \qquad
 (\mathcal C_s^{(p)})^2=p^{-1}I.                   \tag{6.1}$$ Its eigenvalues are $\pm p^{-1/2}$ for every $s$. The minimal inverse-labelled cross block is $$\mathcal M_s^{(p,q)}=
 \begin{pmatrix}0&p^{-s}\\q^{-(1-s)}&0\end{pmatrix},
 \qquad
 (\mathcal M_s^{(p,q)})^2=p^{-s}q^{-(1-s)}I.       \tag{6.2}$$ It moves for $p\ne q$ and fails the pure ledger immediately.

The preregistered checks are:

1.  symbolic verification of [\[thm:sterility\]](#thm:sterility){reference-type="ref" reference="thm:sterility"} through a frozen word cutoff for independent and shared positive labels;

2.  zero vertical range of all pure-block eigenvalues and retained regularized traces;

3.  exact reflection residual under layer/alphabet exchange;

4.  exact mixed frequency $\log(p/q)$ after inverse identification;

5.  random finite bipartite channel controls satisfying balance;

6.  unbalanced-channel and cross-atom controls showing, respectively, reflection failure and mixed-ledger leakage;

7.  composite, random-integer, and shuffled atom inventories.

The decisive falsification is qualitative. If a balanced pure control shows height motion, the implementation is wrong. If an inverse cross-atom control does not show the frequency $\log(p/q)$, word reduction or endpoint weights are wrong. Root fitting and Riemann-zero comparison are forbidden.

The experiment cannot promote a finite zero census to analytic continuation or a global divisor. Its task is to validate the exponent dichotomy and the common ideal bookkeeping.

# Route-A outcome and Route-B lock {#sec:route}

SD-C11 is source-complete and testable: atom source, channel grammar, endpoint roofs, positive cocycles, von Neumann function space, trace, reflection, and regularized determinant are frozen.

0.99L0.08L0.25X Layer & Verdict & Evidence\
A0 & analytic arithmetic origin & tensor atoms and entropy clock are inherited without target data\
A1 & analytic pass, sterile double & canonical trace retains pure alternating atom loops; reflected repetitions have mass $p^{-r}$\
A2 & analytic regularized determinant & $\det_3$ exists on $1/3<\Re s<2/3$ and has an exact prime product, but it is vertically constant and not the Euler determinant\
A3 & partial obstruction theorem & exact reflection and finite-channel rigidity are proved; no continuation, Gamma completion, counting law, or moving divisor results\
A4 & fail/formal only & the holomorphic double is not self-adjoint and supplies no fixed spectral generator\

The tuple is

  -----------------------------------------------------------
      `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_PASS_ANALYTIC,`
   `A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE,`
                          `A4_FAIL).`
  -----------------------------------------------------------

Because the promoted SD-C11 determinant does not carry the Euler ledger $\sum_pp^{-rs}$ and has no vertical motion, the overall verdict is $$\boxed{\texttt{ROUTE\_A\_EXPLORATORY}.}$$ The stage status is

The proves-too-much controls are explicit. Any positive inventory gives the same reflection-balance sterility. Shared abelian labels pass. Finite balanced channel decorations pass. Inverse cross-atom labels move only by creating mixed masses. Thus the theorem cannot certify an RH-like statement.

Route B is not testable. $\mathcal C_s$ is a holomorphic pencil rather than a fixed self-adjoint operator, its determinant is vertically constant, and no operator domain, compact-resolvent law, von-Mangoldt trace, Weil form, or completed divisor exists. Hence $$\mathtt{route\_b\_invocation\_allowed=false}.$$

The next same-family theorem must leave the finite balanced-channel monomial class while remaining symbolic. The smallest option is an infinite-memory renewal channel with a source-derived nonmonomial potential. It must first prove nuclearity and show an identity-visible pure-prime coefficient with a nonzero critical frequency; otherwise it is rejected before any zero test.

# Conclusion: exact symmetry is not spectral motion {#sec:conclusion}

SD-C11 solves one Paper08 problem and exposes another. By replacing the adjoint with a holomorphic reflected layer, it avoids the automatic positive $gg^{-1}$ norm square. It also obtains a nonempty common Schatten strip and an exact $s\leftrightarrow1-s$ determinant symmetry.

But the same layer alternation that creates reflection forces every visible pure word to use $s$ and $1-s$ equally. Its vertical phases cancel, and the regularized determinant is independent of height. Inverse-identifying the layers restores visible two-step words; those words move only when their two atom labels differ, which is exactly an unwanted mixed arithmetic ledger.

The finite-channel rigidity theorem turns this into a scoped no-go result: constant phases, finite multiplicity, and virtual differences cannot create a moving pure-prime coefficient once reflection balance is imposed. The symbolic frontier is therefore $$\boxed{
 \text{balanced pure reflection}\Rightarrow\text{vertical sterility},
 \qquad
 \text{visible vertical motion}\Rightarrow\text{mixed atoms}.}$$

The next step, if pursued, must justify genuinely infinite memory or a nonmonomial symbolic potential from the tensor source itself. Its first obligation is not a Riemann-zero fit but a theorem: one pure-prime identity-visible trace coefficient must retain nonzero critical frequency in a nuclear common domain.

Route B remains locked. Any idea requiring a separate geometric mechanism to supply reflection phases is recorded only as a round-two clue.

# Proof details and scope firewall {#app:scope}

## Regularization index

At $s=1/2+it$, both reflected blocks have coefficient scale $p^{-1/2}$. Thus they fail $L^2$ because $\sum_p1/p$ diverges, but belong to every $L^q$, $q>2$. The first integer regularization is $q=3$. Odd traces vanish; the quadratic term is the first nonzero term and is exactly the subtraction needed to obtain $$\prod_p(1-z^2/p)e^{z^2/p}.$$ Calling this a continuation of the original Euler determinant is forbidden: its local factors, trace powers, and spectral variable are different.

## Unique-factorization separation

A critical-line monomial word has frequency $$\omega_W=\sum_{e:\epsilon=0}\log p(e)
 -\sum_{e:\epsilon=1}\log p(e).$$ If $\omega_W=0$, unique factorization implies equality of the prime exponent vectors on the two sides. For a pure word this is exactly channel balance. For a moving word, at least one exponent differs; its ledger records more than repetitions of a single atom unless the channel itself is unbalanced. This is the algebraic basis of [\[thm:finite-channel\]](#thm:finite-channel){reference-type="ref" reference="thm:finite-channel"}.

## Evidence labels

The following are `PROVED`: the common ideal strip, reflection symmetry, all-order trace formulas, regularized product, finite-channel rigidity, and two-step motion/ledger dichotomy. The possibility of an infinite-memory or nonmonomial symbolic escape is `OPEN`. Analytic continuation to a completed function, a target divisor, and a Hilbert--Pólya operator are `NOT_ESTABLISHED`.

## Data firewall

The candidate definition uses tensor multiplication, topological entropy, universal positive alphabets, canonical traces, and a fixed two-layer grammar. It uses no Riemann-zero list, fitted phase, fitted scale, or von-Mangoldt input. The implications $$\begin{aligned}
 \Delta_3(s,z)=\Delta_3(1-s,z)&\not\Rightarrow
 \text{Riemann functional equation},\\
 \text{holomorphic reflected pencil}&\not\Rightarrow
 \text{self-adjoint operator},\\
 \text{finite-channel no-go}&\not\Rightarrow
 \text{all symbolic systems fail}\end{aligned}$$ are explicitly forbidden. Any external carrier is outside the primary system family.
