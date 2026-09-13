---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--86-finite-field-adjacent-product-process"
canonical_tex: "symbolic_dynamics/papers/86-finite-field-adjacent-product-process/main.tex"
canonical_pdf: "symbolic_dynamics/papers/86-finite-field-adjacent-product-process/main.pdf"
source_sha256: "4444b4aafc7fdf128a374e3ab6715266b227e45d39ec6f9d3796f069c0ed7f0a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite-Field Adjacent-Product Processes: One-Dependence, Infinite Markov Memory, and Exact Support Entropy

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/86-finite-field-adjacent-product-process>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/86-finite-field-adjacent-product-process/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/86-finite-field-adjacent-product-process/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/86-finite-field-adjacent-product-process/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/86-finite-field-adjacent-product-process/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $(U_i)_{i\in\mathbb Z}$ be independent and uniform on the finite field $\mathbb F_q$, and observe only the adjacent products $Y_i=U_iU_{i+1}$. This elementary two-block factor exhibits a sharp separation between dependence range and prediction memory. Its law is stationary, reversible, mixing, and one-dependent, but it is not a Markov chain of any finite order. We identify its support as the mixing two-step shift of finite type obtained by forbidding $a0b$ with $a,b\ne0$. If $L_n$ is the number of supported words of length $n$, then, with $m=q-1$, $$L_{n+3}=qL_{n+2}-mL_{n+1}+mL_n,
   \qquad
   (L_0,L_1,L_2)=(1,q,q^2).$$ Consequently the support entropy is $\log\lambda_q$, where $\lambda_q$ is the Perron root of $t^3-qt^2+(q-1)t-(q-1)$. Exact $2\times2$ matrices give every cylinder probability. More sharply, if a nonzero observation is followed by $r$ zeros, then, for $r\geq1$ and every fixed $b\ne0$, the next-symbol probability is $$\mathbb P(Y_0=b\mid a0^r)
   =\frac{(q-1)F_{r-1}}{qF_{r+1}},
   \qquad F_{r+2}=F_{r+1}+(q-1)F_r.$$ These probabilities oscillate forever and prove infinite Markov order. The same renewal contexts yield an explicit exponentially convergent series for the measure entropy. We state the hidden-Markov and variable-memory ownership boundary and make no absolute priority claim.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 28 August 2026'
title: |
  Finite-Field Adjacent-Product Processes:\
  One-Dependence, Infinite Markov Memory, and Exact Support Entropy
```

## Markdown 正文

# Introduction

A finite-range factor of an independent process need not have finite prediction memory. The distinction is easy to miss: one-dependence says that sufficiently separated *sets* of coordinates are independent, whereas a finite-order Markov property asks whether the most recent bounded window screens the future from the entire past. The process studied here separates the two notions within a minimal algebraic model.

Fix a prime power $q\geq2$. From independent uniform vertices $U_i\in\mathbb F_q$, put on every edge of the integer line the product $Y_i=U_iU_{i+1}$. Nonzero products propagate invertibility along a run, while a zero records only that at least one endpoint vanished. The field zero is therefore both a local singularity and an information-losing reset. That single rank drop is responsible for all of the structure below.

Two-block factors of iid sources are elementary examples of one-dependent processes, inside a literature that includes Aaronson, Gilat, Keane, and de Valk's study of the converse block-factor problem [@AaronsonEtAl1989]. We take that general relationship as prior. Functions of finite-state Markov chains and their entropy go back at least to Blackwell [@Blackwell1957]. Context models with variable memory were introduced in information theory by Rissanen [@Rissanen1983] and formalized statistically by Bühlmann and Wyner [@BuhlmannWyner1999]. Our process is a finite-state hidden Markov process, and its prediction law has an almost-surely finite but unbounded context-tree description; we use the variable-memory comparison in this broad sense, not as a claim of membership in a finite-context statistical subclass. The contribution of this note is the exact finite-field specialization: the support, all cylinder fibers, the unbounded context law, and the entropy series are obtained in closed form from the same second-order recurrence.

The main results are as follows.

1.  The topological support is exactly the two-step shift forbidding the words $a0b$ with $a,b\in\mathbb F_q^\times$. A four-state transfer matrix gives the exact word recurrence and its Perron entropy.

2.  The measure is reversible and one-dependent, hence strongly mixing, but has no finite Markov order. Its prediction after a zero run is a generalized-Fibonacci ratio that alternates around a nontrivial limit and never stabilizes.

3.  Two $2\times2$ matrices count every finite fiber. They also give an explicit context expansion for the entropy rate and show that the measure has a strict entropy gap below the support entropy.

All statements hold for every finite field, including nonprime fields. The proofs use only that multiplication by a nonzero field element is a bijection. The accompanying program checks the defining map, the forbidden language, the fiber matrices, the recurrence, the prediction ratios, and the entropy series over $\mathbb F_2$, $\mathbb F_3$, $\mathbb F_4$, and $\mathbb F_5$.

# The process and its finite fibers {#sec:setup}

Let $q$ be a prime power, let $\mathbb F_q$ be the field with $q$ elements, and set $m=q-1$. On the Bernoulli system $(\mathbb F_q^\mathbb Z,\operatorname{Unif}(\mathbb F_q)^\mathbb Z,\sigma)$ define the two-block code $$\label{eq:factor}
 \Phi(u)_i=u_i u_{i+1},\qquad i\in\mathbb Z.$$ Write $Y=\Phi(U)$, let $\mu_q$ be its law, and let $X_q=\operatorname{supp}(\mu_q)\subseteq\mathbb F_q^\mathbb Z$.

We first record a fiber formula that will be used in each later section. A partial hidden word ending at a vertex can end either at zero or at a nonzero field element. In that order define $$\label{eq:fiber-matrices}
 C_0=\begin{pmatrix}1&m\\[2pt]1&0\end{pmatrix},
 \qquad
 C_a=\begin{pmatrix}0&0\\[2pt]0&1\end{pmatrix}
 \quad(a\in\mathbb F_q^\times).$$

[\[prop:fibers\]]{#prop:fibers label="prop:fibers"} For $w=w_0\cdots w_{n-1}\in\mathbb F_q^n$, the number of hidden words $u_0\cdots u_n\in\mathbb F_q^{n+1}$ satisfying $u_i u_{i+1}=w_i$ for $0\leq i<n$ is $$\label{eq:fiber-count}
 N_q(w)=(1,m)C_{w_0}C_{w_1}\cdots C_{w_{n-1}}
 \binom11.$$ Consequently $$\label{eq:cylinder-law}
 \mu_q([w])=q^{-(n+1)}N_q(w).$$

Suppose a collection of partial lifts contains $z$ lifts whose current hidden endpoint is zero and $r$ whose endpoint is nonzero. If the next observed symbol is zero, a zero endpoint has one zero and $m$ nonzero extensions, while a nonzero endpoint has only the zero extension. Thus the new counts are $(z+r,mz)=(z,r)C_0$. If the next observed symbol is a fixed $a\ne0$, no zero endpoint extends. Each nonzero endpoint $u$ has the unique extension $a/u$, so the new counts are $(0,r)=(z,r)C_a$. Before any edge is read there is one zero and $m$ nonzero choices, giving the initial row $(1,m)$. Summing the two terminal classes proves [\[eq:fiber-count\]](#eq:fiber-count){reference-type="eqref" reference="eq:fiber-count"}. Uniformity of $U_0,\ldots,U_n$ gives [\[eq:cylinder-law\]](#eq:cylinder-law){reference-type="eqref" reference="eq:cylinder-law"}.

The formula depends on a nonzero symbol only through its being nonzero. Actual nonzero labels nevertheless remain distinct in the observed language; their multiplicity will enter the topological transfer matrix.

# Exact support and word complexity {#sec:support}

Let $\mathbb F_q^\times=\mathbb F_q\setminus\{0\}$. Denote by $\mathcal X_q$ the two-step shift of finite type over $\mathbb F_q$ whose forbidden list is $$\label{eq:forbidden}
 \mathcal F_q=\{a0b:a,b\in\mathbb F_q^\times\}.$$

[\[thm:support\]]{#thm:support label="thm:support"} For every prime power $q\geq2$, $$X_q=\Phi(\mathbb F_q^\mathbb Z)=\mathcal X_q.$$ Every nonempty cylinder in $X_q$ has positive $\mu_q$-measure. The shift $X_q$ is topologically mixing.

If $y_{i-1}=a\ne0$, then $u_i\ne0$. If also $y_i=0$, the equality $u_i u_{i+1}=0$ forces $u_{i+1}=0$, and hence $y_{i+1}=0$. Thus no image contains a word $a0b$ with both exterior symbols nonzero.

Conversely, take $y\in\mathcal X_q$. On every maximal interval of nonzero edges, choose one endpoint in $\mathbb F_q^\times$ and solve successively by division. Two such intervals are separated by at least two zero edges. The first zero edge after a nonzero interval can therefore be lifted by making its new endpoint zero, and the last zero edge before the next interval is then automatically compatible. Set any remaining unconstrained endpoints in a zero gap equal to zero. The same construction works for one-sided or bi-infinite nonzero intervals; for an all-nonzero configuration choose one hidden value and solve in both directions. This constructs $u\in\mathbb F_q^\mathbb Z$ with $\Phi(u)=y$.

Proposition [\[prop:fibers\]](#prop:fibers){reference-type="ref" reference="prop:fibers"} now shows that every legal finite word has a positive cylinder probability. Finally, two legal words can be joined by two zeros: the only newly created length-three words meeting the bridge have at least two consecutive zeros. Arbitrarily many further zeros may be inserted, so the shift is topologically mixing.

For exact word counts, collapse each symbol to its zero/nonzero type. In the ordered pair states $00,0*,*0,**$, where $*$ means nonzero, appending a nonzero symbol has multiplicity $m$. The resulting weighted transfer matrix is $$\label{eq:transfer}
 A_q=
 \begin{pmatrix}
 1&m&0&0\\
 0&0&1&m\\
 1&0&0&0\\
 0&0&1&m
 \end{pmatrix}.$$ Its directed graph is strongly connected and has a loop, hence $A_q$ is primitive. A direct determinant calculation gives $$\label{eq:charpoly}
 \det(tI-A_q)
 =t\bigl(t^3-qt^2+mt-m\bigr).$$

[\[thm:complexity\]]{#thm:complexity label="thm:complexity"} Let $L_n=|\mathcal L_n(X_q)|$, with $L_0=1$. Then $$\begin{aligned}
 L_1&=q, & L_2&=q^2, & L_3&=q^3-(q-1)^2,
 \label{eq:initial-complexity}\\
 L_{n+3}&=qL_{n+2}-(q-1)L_{n+1}+(q-1)L_n
 \quad(n\geq0).\label{eq:complexity-recurrence}\end{aligned}$$ If $\lambda_q$ is the largest real root of $$\label{eq:pf-cubic}
 p_q(t)=t^3-qt^2+(q-1)t-(q-1),$$ then $$\label{eq:top-entropy}
 h_{\mathrm{top}}(X_q)=\log\lambda_q.$$

Words of length at most two are unrestricted, while the forbidden list contains $m^2$ length-three words. This gives [\[eq:initial-complexity\]](#eq:initial-complexity){reference-type="eqref" reference="eq:initial-complexity"}. For $n\geq2$, all length-$n$ words are counted by starting with their weighted pair state and applying $A_q^{n-2}$. Cayley--Hamilton and [\[eq:charpoly\]](#eq:charpoly){reference-type="eqref" reference="eq:charpoly"} give [\[eq:complexity-recurrence\]](#eq:complexity-recurrence){reference-type="eqref" reference="eq:complexity-recurrence"} for $n\geq3$. The three remaining cases are checked directly. Besides $L_3=q^3-m^2$, inclusion--exclusion over the possible locations of a forbidden word gives $$L_4=q^4-2qm^2,
 \qquad
 L_5=q^5-3q^2m^2+m^3.$$ Indeed, adjacent forbidden occurrences are incompatible, and at length five the first and third locations overlap in exactly $m^3$ words. Substitution of $L_0,\ldots,L_5$ verifies the recurrence for $n=0,1,2$. Primitivity and Perron--Frobenius give $L_n=\exp(n\log\lambda_q+O(1))$, proving [\[eq:top-entropy\]](#eq:top-entropy){reference-type="eqref" reference="eq:top-entropy"}.

For example, $L_n$ for $q=2$ begins $$1,2,4,7,12,21,37,65,114,200,$$ and for $q=3$ it begins $$1,3,9,23,57,143,361.$$ These are definition-level counts, not fitted recurrences.

# Short dependence and unbounded prediction memory {#sec:memory}

[\[prop:mixing\]]{#prop:mixing label="prop:mixing"} The process $Y$ is stationary and time-reversible. Moreover, $$\sigma(Y_i:i\leq0)
 \quad\text{and}\quad
 \sigma(Y_i:i\geq2)$$ are independent. Thus $Y$ is one-dependent, strongly mixing with mixing coefficient zero from lag two onward, and ergodic.

The code [\[eq:factor\]](#eq:factor){reference-type="eqref" reference="eq:factor"} commutes with the shift, so stationarity follows from stationarity of the iid source. Put $V_i=U_{1-i}$. Then $V$ has the same law as $U$, and commutativity of field multiplication gives $V_iV_{i+1}=U_{1-i}U_{-i}=Y_{-i}$. Hence the process is reversible.

The past sigma-field displayed in the statement is contained in $\sigma(U_i:i\leq1)$, while the future sigma-field is contained in $\sigma(U_i:i\geq2)$. These source sigma-fields are independent. The mixing and ergodicity conclusions follow.

Short dependence does not bound the length of a predictive context. Define the generalized Fibonacci sequence $$\label{eq:F-recurrence}
 F_0=0,\qquad F_1=1,\qquad
 F_{r+2}=F_{r+1}+mF_r\quad(r\geq0).$$ For $a\in\mathbb F_q^\times$ and $r\geq1$, let $$\label{eq:context-event}
 E_r(a)=\{Y_{-r-1}=a,\ Y_{-r}=\cdots=Y_{-1}=0\}.$$ Each event has positive probability.

[\[thm:infinite-memory\]]{#thm:infinite-memory label="thm:infinite-memory"} For $a,b\in\mathbb F_q^\times$ and $r\geq1$, $$\label{eq:context-probability}
 \mathbb P(Y_0=b\mid E_r(a))
 =\frac{mF_{r-1}}{qF_{r+1}}.$$ The value is independent of $a$ and $b$. As $r$ increases, the right-hand side never takes the same value at two consecutive indices and alternates around its limit. Consequently $\mu_q$ is not a Markov measure of any finite order.

Conditioning on $Y_{-r-1}=a\ne0$ makes the right hidden endpoint of that edge nonzero. Starting from one nonzero endpoint, the zero-edge transition in [\[eq:fiber-matrices\]](#eq:fiber-matrices){reference-type="eqref" reference="eq:fiber-matrices"} gives $$\label{eq:zero-run-counts}
 (0,1)C_0^r=(F_r,mF_{r-1}).$$ The identity follows by induction from [\[eq:F-recurrence\]](#eq:F-recurrence){reference-type="eqref" reference="eq:F-recurrence"}. There are therefore $F_{r+1}=F_r+mF_{r-1}$ compatible continuations through the zero run, of which $mF_{r-1}$ end at a nonzero value $U_0$. Conditional on such a nonzero $U_0$, exactly one of the $q$ equally likely choices for $U_1$ satisfies $U_0U_1=b$. This proves [\[eq:context-probability\]](#eq:context-probability){reference-type="eqref" reference="eq:context-probability"}.

The same calculation is unchanged by an arbitrary compatible earlier word $v$. Indeed, if $(1,m)C_v=(z,c)$, then reading $a\ne0$ gives $(z,c)C_a=(0,c)$; the scalar $c$ multiplies both the numerator and denominator after the zero run and cancels. Thus [\[eq:context-probability\]](#eq:context-probability){reference-type="eqref" reference="eq:context-probability"} is a genuine context conditional, not merely a calculation under a truncated past.

Set $t_r=mF_{r-1}/F_r$ for $r\geq1$. Then $t_1=0$ and $$\label{eq:mobius}
 t_{r+1}=\frac{m}{1+t_r}.$$ The map on the right is injective and decreasing on $[0,\infty)$. Its unique nonnegative fixed point is $$\label{eq:tstar}
 t_*=\frac{\sqrt{4q-3}-1}{2}.$$ No finite iterate of $t_1=0$ can equal $t_*$: injectivity would otherwise allow repeated backward cancellation and force $0=t_*$. Thus $t_{r+1}\ne t_r$ for every $r$, and the decreasing recurrence alternates strictly around $t_*$. Since the probability in [\[eq:context-probability\]](#eq:context-probability){reference-type="eqref" reference="eq:context-probability"} equals $t_r/[q(1+t_r)]$, the same conclusions hold for the prediction values.

If the process had Markov order $k\geq1$, all earlier histories ending in the same $k$ zeros would give the same next-symbol law. Taking consecutive $r,r+1\geq k$ in [\[eq:context-event\]](#eq:context-event){reference-type="eqref" reference="eq:context-event"} contradicts this. Order zero is also impossible: after the allowed context $a0$ a nonzero next symbol has probability zero, whereas its unconditional probability is positive.

The first few probabilities for a fixed nonzero $b$ are $$0,\quad \frac{q-1}{q^2},\quad
 \frac{q-1}{q(2q-1)},\quad
 \frac{q-1}{q^2+q-1},\quad\ldots,$$ where the unsimplified pattern is governed by [\[eq:context-probability\]](#eq:context-probability){reference-type="eqref" reference="eq:context-probability"}. For $q=2$ the sequence begins $$0,\quad \frac14,\quad \frac16,\quad \frac15,\quad
 \frac3{16},\quad \frac5{26}.$$

# An exact entropy-rate series {#sec:entropy}

The nonzero symbols are regeneration markers for prediction. Let $R$ be the number of consecutive zeros immediately before time zero: $$\label{eq:age}
 R=\min\{r\geq0:Y_{-r-1}\ne0\}.$$ Since $\mathbb P(Y_i\ne0)=m^2/q^2>0$ and the process is ergodic, $R$ is finite almost surely.

Define $$\label{eq:alpha-s}
 \alpha_0=1,
 \qquad
 \alpha_r=\frac{mF_{r-1}}{F_{r+1}}\ (r\geq1),
 \qquad
 s_r=\frac{m}{q}\alpha_r.$$ Here $\alpha_r$ is the posterior probability that $U_0\ne0$ given a past whose last nonzero observation is followed by $r$ zeros, and $s_r$ is the conditional probability that $Y_0\ne0$.

Write $$h_{\mathrm b}(s)=-s\log s-(1-s)\log(1-s),$$ with $0\log0=0$.

[\[thm:entropy\]]{#thm:entropy label="thm:entropy"} The age distribution is $$\label{eq:age-law}
 w_r:=\mathbb P(R=r)=\frac{m^2F_{r+1}}{q^{r+2}},
 \qquad r\geq0.$$ The entropy rate of $\mu_q$, in nats, is the exponentially convergent series $$\label{eq:entropy-series}
 h(\mu_q)
 =\sum_{r=0}^{\infty}w_r
 \bigl(h_{\mathrm b}(s_r)+s_r\log m\bigr).$$ Moreover, $$\label{eq:strict-gap}
 h(\mu_q)<h_{\mathrm{top}}(X_q)=\log\lambda_q.$$

The event $Y_{-r-1}\ne0$ has probability $m^2/q^2$. Given that event, the right endpoint of the observed edge is nonzero. There are $$(0,1)C_0^r\binom11=F_{r+1}$$ hidden continuations through $r$ zero edges, out of $q^r$ total continuations. This proves [\[eq:age-law\]](#eq:age-law){reference-type="eqref" reference="eq:age-law"}. The generating function $$\label{eq:F-generating}
 \sum_{j\geq0}F_jz^j=\frac{z}{1-z-mz^2}$$ shows that $\sum_{r\geq0}w_r=1$ after setting $z=1/q$.

Conditioning further on any compatible observations before the last nonzero edge can bias its hidden endpoint among the nonzero field elements, but it cannot change that endpoint's zero/nonzero type. Every nonzero starting value has the same type-counts through a zero run, so the common scalar cancels from the posterior ratio. Consequently, given the complete observed past with $R=r$, the calculation in [\[eq:zero-run-counts\]](#eq:zero-run-counts){reference-type="eqref" reference="eq:zero-run-counts"} gives $\mathbb P(U_0\ne0\mid Y_{-\infty}^{-1})=\alpha_r$. If $U_0\ne0$, then the independent uniform $U_1$ makes each of the $m$ nonzero values of $Y_0$ have probability $1/q$. Hence, conditional on $R=r$, the symbol zero has probability $1-s_r$ and each nonzero symbol has probability $s_r/m$. Its entropy is $h_{\mathrm b}(s_r)+s_r\log m$. Averaging over $R$ proves [\[eq:entropy-series\]](#eq:entropy-series){reference-type="eqref" reference="eq:entropy-series"} by the standard identity $h(\mu_q)=H(Y_0\mid Y_{-\infty}^{-1})$.

The growth rate of $F_r$ is the positive root of $x^2=x+m$, which is strictly smaller than $q$; indeed $q^2-q-m=m^2>0$. Thus the weights in [\[eq:age-law\]](#eq:age-law){reference-type="eqref" reference="eq:age-law"} decay exponentially.

By [\[thm:support\]](#thm:support){reference-type="ref" reference="thm:support"}, $X_q$ is a mixing shift of finite type. Its unique measure of maximal entropy is the finite-state intrinsic Markov measure constructed by Parry [@Parry1964]. On the ordered-pair presentation its transition law is one-step Markov, so in the original symbol coordinates it has Markov order at most two. Theorem [\[thm:infinite-memory\]](#thm:infinite-memory){reference-type="ref" reference="thm:infinite-memory"} shows that $\mu_q$ is not that measure. Uniqueness of the maximal measure therefore gives the strict inequality in [\[eq:strict-gap\]](#eq:strict-gap){reference-type="eqref" reference="eq:strict-gap"}.

For orientation, the control program evaluates

   $q$   $h(\mu_q)$ (nats)   $\log\lambda_q$ (nats)
  ----- ------------------- ------------------------
    2    0.484678454953871     0.562399148645924
    3    0.853898202937607     0.924806254398638
    4    1.134074691264723     1.216224572920358
    5    1.361005489603169     1.454951935105873

The strict gap is structural; the decimals are not used in its proof.

# Ownership boundary and scope {#sec:ownership}

Aaronson, Gilat, Keane, and de Valk [@AaronsonEtAl1989] belong to the general one-dependent/block-factor ownership line. Blackwell's work [@Blackwell1957] owns the general problem of entropy for functions of finite-state Markov chains. Rissanen [@Rissanen1983] introduced context-based variable-memory models, and Bühlmann and Wyner [@BuhlmannWyner1999] developed variable-length Markov chains as a statistical class. Parry [@Parry1964] owns the intrinsic Markov measure used only to identify the strict entropy gap.

The present note does not claim any of these frameworks. Its theorem package is the calculation for the specific singular edge factor $u_i u_{i+1}$ over $\mathbb F_q$: the forbidden support, exact fiber matrices, complexity cubic, generalized-Fibonacci context probabilities, and entropy series. A bounded search through 28 August 2026 using the exact defining formula and combinations of "adjacent product", "finite field", "one-dependent", and "hidden Markov" found no direct primary source for this combined package. That negative search is a narrow collision firewall, not evidence of absolute priority.

Several extensions are deliberately left open. Replacing the field by a finite ring introduces zero divisors and more than two endpoint types; replacing multiplication by a general binary operation asks which singularities create an unbounded context tree. Both directions require new fiber semigroups and are not consequences of the two matrices above.

# Conclusion

Adjacent products over a finite field give a compact example in which local dependence ends after one site but predictive memory is unbounded. The field zero turns the image into a mixing two-step SFT, while uncertainty inside zero runs produces a generalized-Fibonacci context law. The same two-state fiber calculation controls cylinders, word growth, failure of finite Markov order, and the entropy rate. The example isolates a reusable mechanism: a finite-block factor can be strongly mixing at a fixed finite range and still retain arbitrarily long variable-length memory through a singular observation symbol.
