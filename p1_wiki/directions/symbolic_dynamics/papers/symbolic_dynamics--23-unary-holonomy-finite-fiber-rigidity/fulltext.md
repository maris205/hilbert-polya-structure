---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--23-unary-holonomy-finite-fiber-rigidity"
canonical_tex: "symbolic_dynamics/papers/23-unary-holonomy-finite-fiber-rigidity/main.tex"
canonical_pdf: "symbolic_dynamics/papers/23-unary-holonomy-finite-fiber-rigidity/main.pdf"
source_sha256: "31ae56e1ca5c43466c5d35c93443ef3fe2a084d50d58cf637d22d833c0c417c2"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite-Fiber Rigidity of the Ordered Cofactor Spine: Unary Periodicity, Recurrence Supports, and Compiler Collapse

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/23-unary-holonomy-finite-fiber-rigidity>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/23-unary-holonomy-finite-fiber-rigidity/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/23-unary-holonomy-finite-fiber-rigidity/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/23-unary-holonomy-finite-fiber-rigidity/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/23-unary-holonomy-finite-fiber-rigidity/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The holonomy-two cycles of the successor--divisor countable Markov shift carry a canonical ordered quotient word $1^{k-1}2$ at every length $k\ge2$. We prove that this order information does not support a fixed finite-memory prime selector. Every fixed finite group, semigroup, DFA, or NFA responds eventually periodically; every fixed characteristic-zero response $u^{\mathsf T}A^{k-1}Bv$ or $\operatorname{tr}(A^{k-1}B)$ is a linear recurrence sequence whose exact nonzero support is ultimately periodic by Skolem--Mahler--Lech. Hence neither response has infinite prime-only support. The obstruction is asymptotic: an $N$-dimensional nilpotent shift memorizes any prescribed $N$-term response, so finite prime fits also fit squares, hashes, and arbitrary bits and therefore prove too much. In the two licensed countable exact wrappers, computation is either placed in a determinant-invisible transient DAG or closed into long cycles whose $\log n$ roof is diluted until the whole vertex adjacency is noncompact. First return then changes the graph marker. Independently, every block trace-log term retains powers of the natural monomial $z^k((2k-1)!/(k-1)!)^{-2s}$; even a separate one-dimensional oracle deletion control does not yield $zk^{-s}$. A 2026 theorem of de Jong already gives the broad Skolem--Mahler--Lech collision for dynamical period sets, although its hypotheses are not asserted for our countable shift; our contribution is the model-specific memory hierarchy and same-object roof closure. The finite-fiber operator remains trace class exactly for $\Re s>1/2$, but Route A is rejected.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  Finite-Fiber Rigidity of the Ordered Cofactor Spine:\
  Unary Periodicity, Recurrence Supports, and Compiler Collapse
```

## Markdown 正文

# Introduction {#sec:introduction}

A source-derived orbit label can be exact and still be arithmetically too weak. The successor--divisor countable Markov shift provides a sharp example. Its first nontrivial cofactor class consists of the primitive cycles $$C_k=(k,k+1,\ldots,2k-1),\qquad k\ge2.$$ Product holonomy treats every $C_k$ alike, but the ordered labels retain the length: $$\mathsf W(C_k)=1^{k-1}2.$$ The smallest unresolved question is therefore whether a fixed finite noncommutative or weighted fiber can read this word and retain precisely the prime values of $k$.

The question sits at the intersection of three established boundaries. Unary finite automata have arithmetic-progression structure [@Chrobak1986; @Chrobak2003Erratum; @To2009]; prime recognition by finite automata is classically obstructed [@HartmanisShank1968]; and fixed linear representations generate recurrence sequences [@Schutzenberger1961]. In Symbolic Dynamics, @deJong2026 already applies Skolem--Mahler--Lech to classify period sets when the logarithmic derivative of the Artin--Mazur zeta function is rational and classifies least-period sets for finitely presented systems. Thus a broad claim that SML excludes prime periods would not be new. What remains unresolved is the exact same-object chain forced by this cofactor word, its finite block determinant, and its inherited endpoint roof. Our countable shift is not asserted to be compact or finitely presented, and its trace logarithmic derivative is not asserted rational; de Jong's theorem bounds the novelty language rather than being applied to SD-C25.

We close that chain. A finite semigroup sees $1^{k-1}2$ as $a^{k-1}b$, which is eventually periodic. A fixed linear fiber sees it as $$u^{\mathsf T}A^{k-1}Bv
        \quad\hbox{or}\quad
        \operatorname{tr}(A^{k-1}B),$$ which satisfies the characteristic recurrence of $A$. The Skolem--Mahler--Lech theorem turns the exact nonzero support into an ultimately periodic set, and an infinite ultimately periodic subset of the rational primes is impossible. These two reductions establish the infinite no-go without using prime density, a prime table in the source, or any target-zero data.

The finite-cutoff converse is equally important. A nilpotent shift of dimension $N$ realizes every prescribed response through $N$, in both bilinear and trace form. Prime indicators are no more distinguished than square indicators, powers of two, or a seeded bit string. A growing finite-dimensional success therefore records its target rather than discovering an invariant.

Countable memory can decide primality, but the two determinant wrappers licensed from Papers19--20 lose the desired explanation. Transient computation lies on no closed walk, so pruning leaves only accepted diagonal loops. Recurrent closure keeps the computation in the orbit ledger, but distributing total roof $\log n$ over a cycle of length $\ell(n)\gg\log n$ forces edge weights toward one and destroys compactness. Inducing on one marked state restores a diagonal weight only by changing $z^{\ell(n)}$ to $z$.

These memory obstructions do not exhaust the failure. The original canonical orbit has graph length $k$ and endpoint roof $$R(C_k)=2\log M_k,\qquad
 M_k=\frac{(2k-1)!}{(k-1)!}.$$ Even a separately assumed one-dimensional oracle prime-deletion control therefore produces $$z^pM_p^{-2s},$$ not the one-step prime monomial $zp^{-s}$. The same complex block adjacency has an honest trace-class Fredholm determinant in the sharp half-plane $\Re s>1/2$, in the sense of the classical trace-ideal framework [@Simon1977]; analytic legitimacy and arithmetic completion are separate claims.

Our contributions are:

1.  We derive the canonical ordered word $1^{k-1}2$ from the frozen successor--tensor source and prove a fixed finite-semigroup/DFA/NFA eventual-periodicity theorem, including an explicit composite witness in every accepted tail class.

2.  We prove that every fixed characteristic-zero bilinear or trace response is an LRS and use Skolem--Mahler--Lech to exclude infinite prime-only exact support, while explicitly excluding sign and cutpoint overclaims.

3.  We construct exact nilpotent realizations for arbitrary finite prefixes and use matched target families to classify every growing finite-fit result as [Proves Too Much]{.smallcaps}.

4.  We integrate the finite-memory no-go with the same complex trace-class adjacency, the transient/recurrent countable-wrapper alternatives licensed from Papers19--20, and the immutable factorial roof, obtaining a strict Route-A rejection.

displays the argument before any implementation details. sets the literature boundary; freezes the symbolic object; prove the fixed-memory theorems; supplies the finite-fit control; connect the result to the whole operator and countable wrappers; and records the route decision.

# Prior boundary and model-specific novelty {#sec:prior}

#### Unary automata and prime recognition.

Unary regular languages are controlled by the eventual behavior of a single transition map. Chrobak's quantitative analysis of unary automata is a standard reference, but its correction history matters: @Chrobak2003Erratum records an erratum to @Chrobak1986, and @To2009 repairs a subtle point in the arithmetic-progression normal-form proof. Our finite-DFA argument uses only the elementary eventual periodicity of powers and does not inherit the quantitative normal-form issue. More directly, @HartmanisShank1968 prove a classical prime-recognition obstruction for finite and pushdown automata. We do not relabel that theorem as our contribution: our narrower claim begins only after the quotient word is derived from a particular countable Markov shift and then follows the same object through its weighted determinant and roof.

#### Multiplicity and weighted automata.

Schützenberger's multiplicity-automata framework links finite linear representations and rational formal series [@Schutzenberger1961]. Contemporary work continues to relate unary or restricted weighted automata to linear recurrence sequences and pumping phenomena [@BarloyEtAl2020; @MazowieckiPuchSmertnig2026]. The response $A^{k-1}B$ is therefore classical linear-representation behavior. Our candidate-specific step is the exact derivation of the two letters from $C_k$, followed by the comparison with the unchanged graph marker and endpoint roof.

#### Skolem--Mahler--Lech.

The classical characteristic-zero zero-set theorem goes back to @Lech1953. We cite @Bell2006 for a modern statement and record @Bell2008Corrigendum, which corrects the generalized $p$-adic analytic-arc argument. We use only the classical conclusion: the zero set of an LRS is a finite union of arithmetic progressions plus a finite set. It controls exact zero/nonzero and, after subtracting a constant, fixed-level support. It does not imply that arbitrary signs, thresholds, phases, or cutpoints are ultimately periodic.

#### Direct collision in Symbolic Dynamics.

The closest collision is @deJong2026. For systems whose logarithmic derivative of the Artin--Mazur zeta function is rational, that work applies Skolem--Mahler--Lech to classify period sets; it also classifies least-period sets for finitely presented systems. Consequently, we make no claim to the first SML obstruction for dynamical period support. De Jong does not treat the successor--divisor cofactor family, the word $1^{k-1}2$, the finite/growing/countable memory hierarchy, or the factorial endpoint roof. Those model-specific links define the scope of this paper.

We do not assert that the present countable Markov shift is compact or finitely presented, nor that its trace logarithmic derivative is rational. Accordingly, de Jong's theorem is a direct collision for broad novelty wording, not an applicability theorem for our operator.

#### Fredholm layer.

Trace-class determinants of Hilbert-space operators are classical [@Simon1977]. Our analytic theorem is not a new determinant theory: it identifies the exact nuclear half-plane of one frozen complex block adjacency. The role of the Fredholm layer is diagnostic. It prevents an arithmetic no-go from being dismissed as a consequence of an ill-defined operator, while also preventing Fredholm analyticity from being mistaken for a prime Euler identity.

L2.8cmYY Line of work & Existing result used & SD-C25-specific remainder\
Unary automata & eventual arithmetic-progression behavior; correction chain & quotient word derived from $C_k$ and connected to its roof\
Prime automata & finite/pushdown prime-recognition obstruction & canonical marked-cycle formulation and determinant consequences\
Weighted automata & finite linear representations yield rational/LRS behavior & exact $A^{k-1}B$ fiber on the cofactor spine\
SML & exact zero sets are semilinear in one dimension & prime-only support corollary inside the same graph ledger\
Symbolic periods & de Jong's SML period classification and FP least-period classification & finite/growing/countable memory and factorial-roof closure\

Our literature conclusion is deliberately search-bounded. We found no primary source containing the complete closure chain, but we do not claim global priority. The valid novelty sentence is: *for this exact successor--divisor family, ordered cofactor memory is either finite-periodic, finitely memorized, or countably compiled, while the source roof remains factorial*.

# Frozen symbolic source and operator {#sec:source}

## Full shifts and the successor--divisor graph

Let $F_n$ denote the full shift on an $n$-letter alphabet, up to topological conjugacy. We freeze $$F_m\mathbin{\boxtimes}F_n\cong F_{mn},\qquad
 F_m\mathbin{\boxplus}F_n\cong F_{m+n},\qquad
 S(F_n)=F_n\mathbin{\boxplus}F_1\cong F_{n+1}.$$ Here $\mathbin{\boxplus}$ means alphabet disjoint union followed by the full-shift functor; it is not asserted to be the categorical coproduct of subshifts. The intrinsic entropy is $h(F_n)=\log n$.

The vertex set and edges are $$V=\{2,3,\ldots\},\qquad
 n\longrightarrow d
 \iff d\ge2,\ d\mid n+1.$$ An edge is equivalently the factor witness $$S(F_n)\cong F_d\mathbin{\boxtimes}F_q,
\qquad
        q=q(n,d)=\frac{n+1}{d}.$$ The resulting one-sided countable Markov shift is $$X_G^+
 =\{(n_0,n_1,\ldots)\in V^\mathbb N:n_j\to n_{j+1}\}.$$ No prime predicate enters this definition.

## Canonical holonomy-two cycles

We import the exact classification that the cofactor product $Q=2$ occurs precisely on $$C_k=(k,k+1,\ldots,2k-1),\qquad k\ge2,$$ up to cyclic rotation. Each orbit is primitive and has a unique least vertex.

[\[thm:word\]]{#thm:word label="thm:word"} Mark $C_k$ at its unique least vertex. Then $$\mathsf W(C_k)=1^{k-1}2.$$

The first $k-1$ edges are $n\to n+1$, and $$q(n,n+1)=1.$$ The closing edge is $2k-1\to k$, with $$q(2k-1,k)=2.$$ The unique least vertex fixes the displayed ordering.

The trace of a matrix product is invariant under cyclic rotation. A bilinear matrix coefficient is not. We use the unique-minimum mark for bilinear responses and never treat a marked coefficient as an unmarked orbit invariant.

## Roof and graph marker

The graph-step marker is $z$ per edge, and the frozen endpoint roof is $$\tau(n,d)=\log(nd).$$ Put $$M_k=\prod_{n=k}^{2k-1}n
            =\frac{(2k-1)!}{(k-1)!}.$$

[\[prop:monomial\]]{#prop:monomial label="prop:monomial"} The length, total roof, and scalar monomial of $C_k$ are $$|C_k|=k,\qquad
 R(C_k)=2\log M_k,\qquad
 z^{|C_k|}\mathrm e^{-sR(C_k)}=z^kM_k^{-2s}.$$

Every cycle vertex occurs once as a source and once as a target. Therefore $$R(C_k)
 =\sum_{(n,d)\in C_k}(\log n+\log d)
 =2\sum_{n=k}^{2k-1}\log n.$$ The word in [\[thm:word\]](#thm:word){reference-type="ref" reference="thm:word"} has $k$ letters.

## Algebraic and analytic fibers

For the algebraic recurrence theorem, $\mathbb F$ may be any characteristic-zero field, with fixed $$A,B\in M_d(\mathbb F),\qquad u,v\in\mathbb F^d.$$ We study $$x_k=u^{\mathsf T}A^{k-1}Bv,\qquad
 y_k=\operatorname{tr}(A^{k-1}B).$$

The analytic layer is more restrictive. It uses $$A,B\in M_d(\mathbb C),\qquad
        \mathcal H=\ell^2(V)\otimes\mathbb C^d.$$ On the quotient-$\{1,2\}$ spine, define the column-source weighted vertex adjacency $$\begin{aligned}
 L_{s,A,B}(e_n\otimes\xi)
 &=[n(n+1)]^{-s}e_{n+1}\otimes A\xi\\
 &\quad+\mathbf 1_{\{n\ {\rm odd}\}}
 [n(n+1)/2]^{-s}e_{(n+1)/2}\otimes B\xi.
\end{aligned}$$ This is not called a Ruelle operator. On $\Re s>1/2$, where [\[thm:traceclass\]](#thm:traceclass){reference-type="ref" reference="thm:traceclass"} proves $L_{s,A,B}\in\mathcal S_1$, we set $$D_{A,B}(s,z)=\det_{\mathcal H}(I-zL_{s,A,B}).$$ The determinant is entire in $z$. Its trace logarithm is used only as the normalized germ at $z=0$; no global logarithm through determinant zeros is assumed.

Starting at the least vertex, column composition around $C_k$ is $BA^{k-1}$. Cyclicity gives $$\operatorname{tr}(BA^{k-1})
        =\operatorname{tr}(A^{k-1}B).$$ This convention will be essential when the analytic and recurrence layers meet in [7](#sec:fredholm){reference-type="ref" reference="sec:fredholm"}.

# Finite-fiber periodicity {#sec:finite}

A set $E\subseteq\mathbb N$ is *ultimately periodic* if there are $N,m\ge1$ such that $$n\ge N
        \quad\Longrightarrow\quad
        [n\in E\Longleftrightarrow n+m\in E].$$

[\[lem:primeperiod\]]{#lem:primeperiod label="lem:primeperiod"} An ultimately periodic subset of the rational primes is finite.

Suppose that $E\subseteq\mathbb P$ is infinite, with tail threshold $N$ and period $m$. Choose $p\in E$, $p\ge N$. Repeated periodicity places $p+tm$ in $E$ for every $t\ge0$. Taking $t=p$ gives $$p+pm=p(1+m),$$ which is composite. This contradicts $E\subseteq\mathbb P$.

The witness in [\[lem:primeperiod\]](#lem:primeperiod){reference-type="ref" reference="lem:primeperiod"} is elementary. It needs no prime number theorem and proves the stronger statement that *every* infinite prime-only ultimately periodic support is impossible.

[\[lem:semigrouppower\]]{#lem:semigrouppower label="lem:semigrouppower"} Let $S$ be a finite semigroup and $a\in S$. There are $\mu,\lambda\ge1$ such that $$a^{n+\lambda}=a^n\qquad(n\ge\mu).$$

Two terms among $$a,a^2,\ldots,a^{|S|+1}$$ agree, say $a^i=a^j$ with $i<j$. Right multiplication by $a^r$ gives $a^{i+r}=a^{j+r}$ for every $r\ge0$. Set $\mu=i$ and $\lambda=j-i$.

[\[thm:finite-semigroup\]]{#thm:finite-semigroup label="thm:finite-semigroup"} Let $\phi:\{1,2\}^{+}\to S$ be a morphism into a fixed finite semigroup, and let $H\subseteq S$. Then $$E_{\phi,H}
 =\{k\ge2:\phi(1^{k-1}2)\in H\}$$ is ultimately periodic. If $E_{\phi,H}\subseteq\mathbb P$, it is finite. Moreover, every scalar response $$f\bigl(\phi(1^{k-1}2)\bigr)$$ is eventually periodic.

Put $a=\phi(1)$ and $b=\phi(2)$, with $\phi(xy)=\phi(x)\phi(y)$, so multiplication follows reading order. The canonical word evaluates to $$\phi(1^{k-1}2)=a^{k-1}b.$$ By [\[lem:semigrouppower\]](#lem:semigrouppower){reference-type="ref" reference="lem:semigrouppower"}, the power is eventually periodic; right multiplication by $b$, membership in $H$, and evaluation by $f$ preserve equality. Apply [\[lem:primeperiod\]](#lem:primeperiod){reference-type="ref" reference="lem:primeperiod"}.

[\[cor:finitegroup\]]{#cor:finitegroup label="cor:finitegroup"} For a fixed finite group, $a^{k-1}b$ is periodic from the start with period dividing $\operatorname{ord}(a)$. Membership, class functions, characters, and matrix coefficients of fixed representations cannot have infinite prime-only support.

[\[thm:automata\]]{#thm:automata label="thm:automata"} A fixed DFA or NFA cannot accept exactly $$\{1^{p-1}2:p\in\mathbb P\},$$ or any infinite prime-only sublanguage of the form $\{1^{k-1}2:k\in E\}$.

For a DFA, let $T_1,T_2$ be the two transition maps acting on column states. Function composition is right-to-left, so the final state is $$(T_2\circ T_1^{k-1})(q_0).$$ The transformations of a finite state set form a finite semigroup, so [\[thm:finite-semigroup\]](#thm:finite-semigroup){reference-type="ref" reference="thm:finite-semigroup"} applies. For an NFA, either use the subset construction or view the letter transitions as elements of the finite Boolean-relation semigroup.

is consistent with the stronger classical prime-recognition boundary of @HartmanisShank1968, but its proof is tied directly to the word derived in [\[thm:word\]](#thm:word){reference-type="ref" reference="thm:word"}.

[\[rem:quantifiers\]]{#rem:quantifiers label="rem:quantifiers"} The theorem says $$\forall\text{ fixed finite fiber}\quad
 \exists(\mu,\lambda)\quad
 \text{eventual periodicity}.$$ The tail and period may depend sharply on the fiber. The theorem does not provide one universal period and does not forbid a sequence of fibers whose size grows with the cutoff. That change of quantifiers is analyzed in [6](#sec:growing){reference-type="ref" reference="sec:growing"}.

L3.0cmYY Fiber & Response on $1^{k-1}2$ & Consequence\
finite semigroup & $f(a^{k-1}b)$ & eventually periodic\
finite group & character or matrix coefficient of $a^{k-1}b$ & periodic with period dividing $\operatorname{ord}(a)$\
DFA & membership of $(T_2\circ T_1^{k-1})(q_0)$ & ultimately periodic language\
NFA & Boolean relation power or determinized state & ultimately periodic language\

The no-go concerns exact acceptance. A finite fiber may correlate with prime indicators on a short prefix or accept both primes and composites. Neither observation contradicts [\[thm:finite-semigroup\]](#thm:finite-semigroup){reference-type="ref" reference="thm:finite-semigroup"}.

# Linear-recurrence support rigidity {#sec:lrs}

Finite weights replace Boolean acceptance by a scalar sequence. That enlargement removes literal eventual periodicity of the values, but not the rigidity of their exact zero sets.

## Cayley--Hamilton reduction

Let $\mathbb F$ be a characteristic-zero field and fix $$A,B\in M_d(\mathbb F),\qquad u,v\in\mathbb F^d.$$ Define $$x_k=u^{\mathsf T}A^{k-1}Bv,\qquad
 y_k=\operatorname{tr}(A^{k-1}B).$$

[\[thm:recurrence\]]{#thm:recurrence label="thm:recurrence"} If $$\chi_A(t)=t^d+c_{d-1}t^{d-1}+\cdots+c_0,$$ then $x_k$ and $y_k$ satisfy $$r_{k+d}+c_{d-1}r_{k+d-1}
 +\cdots+c_1r_{k+1}+c_0r_k=0$$ for every $k\ge1$. Their generating functions are rational: $$\sum_{k\ge1}x_kz^{k-1}
 =u^{\mathsf T}(I-zA)^{-1}Bv,$$ $$\sum_{k\ge1}y_kz^{k-1}
 =\operatorname{tr}\bigl((I-zA)^{-1}B\bigr).$$

Cayley--Hamilton gives $$A^d+c_{d-1}A^{d-1}+\cdots+c_0I=0.$$ Multiply by $A^{k-1}$ and apply either linear functional $$X\mapsto u^{\mathsf T}XBv
\quad\hbox{or}\quad
        X\mapsto\operatorname{tr}(XB).$$ The resolvent formulas follow from $$(I-zA)^{-1}=\sum_{n\ge0}z^nA^n$$ as formal series. The adjugate formula makes both functions rational.

This derivation is the concrete one-letter instance of the classical finite linear-representation framework [@Schutzenberger1961].

## Exact support

[\[thm:smlsupport\]]{#thm:smlsupport label="thm:smlsupport"} For $r_k=x_k$ or $r_k=y_k$, the zero set $$Z(r)=\{k\ge1:r_k=0\}$$ is a finite union of arithmetic progressions and a finite set. Consequently $$\operatorname{supp}(r)=\{k\ge1:r_k\ne0\}$$ is ultimately periodic. If $\operatorname{supp}(r)\subseteq\mathbb P$, then $\operatorname{supp}(r)$ is finite.

makes $r$ an LRS over a characteristic-zero field. The Skolem--Mahler--Lech theorem [@Lech1953; @Bell2006; @Bell2008Corrigendum] gives the zero-set classification. Beyond the finite exceptional set, membership is periodic modulo the least common multiple of the finitely many progression moduli. The complement is therefore ultimately periodic. Apply [\[lem:primeperiod\]](#lem:primeperiod){reference-type="ref" reference="lem:primeperiod"}.

[\[cor:fixedlevel\]]{#cor:fixedlevel label="cor:fixedlevel"} For fixed $c\in\mathbb F$, the level set $$\{k:r_k=c\}$$ is ultimately periodic. The same holds for every finite Boolean combination of zero tests or fixed-level tests on finitely many fixed linear responses.

The constant sequence is an LRS, so $r_k-c$ is an LRS. Apply [\[thm:smlsupport\]](#thm:smlsupport){reference-type="ref" reference="thm:smlsupport"}. Finite Boolean combinations of ultimately periodic sets remain ultimately periodic.

[\[cor:noprimecoefficient\]]{#cor:noprimecoefficient label="cor:noprimecoefficient"} There are no fixed $d,A,B,u,v$ over a characteristic-zero field such that $$u^{\mathsf T}A^{k-1}Bv\ne0
 \Longleftrightarrow k\in\mathbb P,$$ or $$\operatorname{tr}(A^{k-1}B)\ne0
 \Longleftrightarrow k\in\mathbb P.$$

[\[rem:smlfirewall\]]{#rem:smlfirewall label="rem:smlfirewall"} The proof controls exact zero/nonzero support and, through [\[cor:fixedlevel\]](#cor:fixedlevel){reference-type="ref" reference="cor:fixedlevel"}, exact equality to a fixed scalar. It does not show that sign, positivity, order, phase sector, threshold, or cutpoint recognition is ultimately periodic. It also does not cover nonlinear updates, positive characteristic, growing dimension, or infinite-dimensional representations. None of those stronger statements receives credit in this paper.

L3.4cmL3.0cmY Predicate on $r_k$ & Status & Reason\
$r_k=0$ or $r_k\ne0$ & proved & direct SML zero-set theorem\
$r_k=c$, fixed $c$ & proved & apply SML to $r_k-c$\
finite Boolean combinations & proved & closure of ultimately periodic sets\
sign, positivity, cutpoint & not claimed & not a zero-set consequence of SML\
variable dimension or nonlinear state & not claimed & outside fixed LRS model\

The exact-support formulation is sufficient for the intended Euler coefficient: composites must contribute zero if only prime-indexed primitive factors are to remain.

# Growing finite memory and finite-fit non-evidence {#sec:growing}

freezes the dimension before $k$ tends to infinity. Finite experiments reverse those quantifiers unless the model is held fixed. The reversal admits an exact universal construction.

[\[thm:bilmemorizer\]]{#thm:bilmemorizer label="thm:bilmemorizer"} Fix $N\ge1$ and arbitrary $\eta_1,\ldots,\eta_N\in\mathbb F$. Let $J_N\in M_N(\mathbb F)$ satisfy $$J_Ne_j=e_{j+1}\quad(j<N),\qquad J_Ne_N=0.$$ With $$v=e_1,\qquad B=I,\qquad
        u=\sum_{j=1}^N\eta_je_j,$$ one has $$u^{\mathsf T}J_N^{k-1}Bv
 =
 \begin{cases}
 \eta_k,&1\le k\le N,\\
 0,&k>N.
 \end{cases}$$

For $k\le N$, $J_N^{k-1}e_1=e_k$, so the contraction reads the $k$-th coordinate of $u$. For $k>N$, $J_N^{k-1}=0$.

[\[thm:trmemorizer\]]{#thm:trmemorizer label="thm:trmemorizer"} With the same $J_N$, let $B_\eta$ have entries $$(B_\eta)_{1k}=\eta_k,\qquad 1\le k\le N,$$ and all other entries zero. Then $$\operatorname{tr}(J_N^{k-1}B_\eta)
 =
 \begin{cases}
 \eta_k,&1\le k\le N,\\
 0,&k>N.
 \end{cases}$$

The only nonzero contribution to the trace is $$(J_N^{k-1})_{k1}(B_\eta)_{1k}=\eta_k.$$ Nilpotence gives zero after $N$.

The two constructions expose where the apparent information resides: $\eta$ is stored directly in the endpoint covector $u$ or the first row of $B_\eta$. Nothing in the successor--divisor source selects those entries.

[\[cor:provestoomuch\]]{#cor:provestoomuch label="cor:provestoomuch"} For every cutoff $N$, the same nilpotent architecture realizes each of: $$\begin{array}{c}
\text{prime indicator},\quad
\text{square indicator},\quad
\text{powers of two},\quad
\text{Fibonacci membership},\\
\text{a seeded bit string},\quad
\text{a hash-derived string},\quad
\text{arbitrary signed rational values}.
\end{array}$$ Therefore finite-prefix success is $$\text{\normalfont\scshape Control}
        \mid
        \text{\normalfont\scshape Proves Too Much}.$$

L3.1cmYY Regime & Quantifiers & Interpretation\
fixed finite dimension & $\forall d,A,B,u,v$, no infinite prime-only exact support & asymptotic no-go from SML\
growing cutoff model & $\forall N,\eta_{1:N}$, an $N$-dimensional realization exists & target vector is memorized\
valid finite audit & freeze $d,A,B,u,v$, then enlarge evaluation cutoff & tests the fixed theorem without changing the model\

The memorizer fits every bit pattern with zero residual. Increasing $N$ and rebuilding $J_N,u,B_\eta$ merely enlarges the stored table. A finite prime experiment becomes informative only if the dimension and all parameters are frozen first and evaluated beyond their construction range. Matched arbitrary-target controls are mandatory even then.

This control also guards the later countable construction. Infinite memory can encode a total decider; the question is not whether primality is computable, but whether the computation is source-derived and visible to the same recurrent determinant.

# Same-object Fredholm and factorial-roof ledger {#sec:fredholm}

The algebraic response theorem does not by itself guarantee that the lifted graph operator is analytically legitimate. We now specialize to complex fibers and prove the sharp nuclear domain before comparing determinant coefficients.

## Sharp trace-class half-plane

[\[thm:traceclass\]]{#thm:traceclass label="thm:traceclass"} Let $A,B\in M_d(\mathbb C)$ be fixed and not both zero. On $\mathcal H=\ell^2(V)\otimes\mathbb C^d$, $$L_{s,A,B}\in\mathcal S_1(\mathcal H)
        \Longleftrightarrow
        \Re s>\frac12.$$ On this half-plane, $s\mapsto L_{s,A,B}$ is $\mathcal S_1$-valued holomorphic.

Write $\sigma=\Re s$ and split the operator into successor and return parts. Their edge rank-one expansions give $$\|S_{s,A}\|_1
 \le \|A\|_1\sum_{n\ge2}[n(n+1)]^{-\sigma},$$ $$\|R_{s,B}\|_1
 \le \|B\|_1\sum_{d\ge2}[(2d-1)d]^{-\sigma}.$$ Both scalar series are comparable to $\sum n^{-2\sigma}$, so $\sigma>1/2$ is sufficient.

If $A\ne0$, compress the domain to even sources and the range to odd targets. Even sources have no quotient-two return edge, and the compression is an injective block weighted shift with trace norm $$\|A\|_1
 \sum_{m\ge1}[(2m)(2m+1)]^{-\sigma}.$$ It is not nuclear at $\sigma\le1/2$. If $A=0$ and $B\ne0$, the return map $2d-1\mapsto d$ is injective and has trace norm $$\|B\|_1
 \sum_{d\ge2}[(2d-1)d]^{-\sigma},$$ with the same boundary. Local uniform convergence of the edge expansions on compact sub-half-planes proves holomorphy.

[\[cor:fredholm\]]{#cor:fredholm label="cor:fredholm"} For $\Re s>1/2$, $$D_{A,B}(s,z)=\det_{\mathcal H}(I-zL_{s,A,B})$$ is an honest Fredholm determinant, entire in $z$.

## Four ledgers that must not be conflated

Put $$w_k=z^kM_k^{-2s},
\qquad
        P_k=BA^{k-1}.$$ Column-source traversal gives $P_k$, while trace cyclicity gives $\operatorname{tr}(P_k)=\operatorname{tr}(A^{k-1}B)$.

[\[prop:blockfactor\]]{#prop:blockfactor label="prop:blockfactor"} The complete local $d$-dimensional block factor associated with $C_k$ is $$\Delta_k(s,z)
        =\det_{\mathbb C^d}(I-w_kP_k).$$ As a normalized germ at $w_k=0$, $$-\log\Delta_k(s,z)
 =\sum_{r\ge1}\frac{w_k^r}{r}\operatorname{Tr}(P_k^r).$$ The expression $w_k\operatorname{Tr}(P_k)$ is only its first trace-log term.

The local return matrix is the scalar orbit weight $w_k$ times its fiber monodromy $P_k$. The finite-dimensional determinant identity $$-\log\det(I-X)
        =\sum_{r\ge1}\frac1r\operatorname{Tr}(X^r)$$ holds near $X=0$. Substitute $X=w_kP_k$.

[\[rem:tracenotfactor\]]{#rem:tracenotfactor label="rem:tracenotfactor"} If $P_k=\operatorname{diag}(1,-1)$, then $$\operatorname{Tr}(P_k)=0
\quad\hbox{but}\quad
        \det(I-w_kP_k)=1-w_k^2.$$ Thus $\operatorname{Tr}(P_k)=0$ does not mean that $C_k$ disappears from the block determinant. A marked bilinear observable $$u^{\mathsf T}A^{k-1}Bv$$ is separate again: it is neither the full block factor nor an unmarked trace coefficient.

[\[thm:exteriorlrs\]]{#thm:exteriorlrs label="thm:exteriorlrs"} Expand $$\Delta_k(s,z)
 =\sum_{j=0}^d(-w_k)^j\alpha_{j,k},
\qquad
 \alpha_{0,k}=1.$$ For each fixed $j\ge1$, $$\alpha_{j,k}
 =\operatorname{Tr}\!\left((\wedge^jB)(\wedge^jA)^{k-1}\right)$$ is a fixed finite-dimensional LRS. Consequently, $$E_{\rm block}
 =\{k:\Delta_k(s,z)\not\equiv1
      \text{ as a polynomial in }w_k\}$$ is ultimately periodic. If $E_{\rm block}\subseteq\mathbb P$, it is finite.

The coefficient of $(-w_k)^j$ in $\det(I-w_kP_k)$ is $\operatorname{Tr}(\wedge^jP_k)$. Exterior powers preserve multiplication: $$\wedge^jP_k
 =(\wedge^jB)(\wedge^jA)^{k-1}.$$ therefore applies to each $\alpha_{j,k}$. The factor is nontrivial exactly when at least one of the finitely many $\alpha_{j,k}$, $j\ge1$, is nonzero. A finite union of ultimately periodic supports is ultimately periodic; use [\[lem:primeperiod\]](#lem:primeperiod){reference-type="ref" reference="lem:primeperiod"}.

repairs a tempting but false shortcut: the first trace cannot stand for the whole determinant. The correct full-block statement is nevertheless finite-dimensional and remains within the same recurrence obstruction.

## Scalar oracle control and immutable roof

A different object is useful only as a hostile control. After the source is frozen, suppose a one-dimensional oracle attaches $$c_k=\mathbf 1_{\mathbb P}(k)$$ and defines $$\Delta_k^{\rm oracle}=1-w_kc_k.$$ This deletion rule is not inferred from $\operatorname{Tr}(P_k)$, $\Delta_k$, or the marked bilinear response.

[\[thm:factorial\]]{#thm:factorial label="thm:factorial"} Every $r$-th block trace-log term has base monomial $$w_k^r=z^{kr}M_k^{-2sr}.$$ The separate one-dimensional oracle control yields $$\prod_{p\in\mathbb P}(1-z^pM_p^{-2s}),$$ not $$\prod_{p\in\mathbb P}(1-zp^{-s}).$$

gives the block powers. The oracle formula follows by substituting $c_k=\mathbf 1_{\mathbb P}(k)$. Neither operation changes [\[prop:monomial\]](#prop:monomial){reference-type="ref" reference="prop:monomial"}.

[\[prop:stirling\]]{#prop:stirling label="prop:stirling"} $$\log M_k
        =k\log k+(2\log2-1)k+O(\log k).$$

Stirling's formula in $\log(2k-1)!-\log(k-1)!$ gives $$\begin{aligned}
\log M_k
 &=2k\log(2k)-2k-k\log k+k+O(\log k)\\
 &=k\log k+(2\log2-1)k+O(\log k).
\end{aligned}$$

The natural roof is therefore of order $2k\log k$, not $\log k$. The fixed block operator earns analytic-determinant credit, but neither its complete factor nor the oracle deletion control has the prime Euler monomial.

# Licensed countable wrappers {#sec:countable}

Fixed finite memory cannot isolate prime-only support, while growing finite memory can store any cutoff. Countable memory can run a total primality algorithm. We do not claim that all countable symbolic extensions fail. We analyze only the two licensed architectures inherited from Papers19--20: transient computation and recurrent closure.

## Transient computation is trace-invisible

[\[thm:transient\]]{#thm:transient label="thm:transient"} Let $S\subseteq\{2,3,\ldots\}$ be decided by a total deterministic machine with finite runtime $T(n)$. Put the computation for input $n$ on a one-way finite chain. Send acceptance to a self-loop of weight $n^{-s}$ and rejection to a one-way acyclic cemetery ray. Give computation edge $t$ weight $[n(t+2)]^{-s}$ and cemetery edge $j$ weight $[n(j+1)]^{-s}$.

For $\Re s>1$, the whole weighted vertex adjacency is trace class and $$\operatorname{Tr}L_{S,s}^r=\sum_{n\in S}n^{-rs},$$ $$\det(I-zL_{S,s})
        =\prod_{n\in S}(1-zn^{-s}).$$

Writing $\sigma=\Re s$, the edge-rank-one majorant is $$\begin{aligned}
\|L_{S,s}\|_1
&\le
\sum_{n\ge2}\sum_{t=0}^{T(n)}[n(t+2)]^{-\sigma}\\
&\quad+
\sum_{n\notin S}\sum_{j\ge1}[n(j+1)]^{-\sigma}
+\sum_{n\in S}n^{-\sigma}\\
&\le
2\left(\sum_{n\ge2}n^{-\sigma}\right)
 \left(\sum_{j\ge2}j^{-\sigma}\right)
+\sum_{n\ge2}n^{-\sigma}<\infty.
\end{aligned}$$ All computation and cemetery edges are acyclic. Closed walks occur only on accepted loops, which gives the trace and determinant formulas.

[\[cor:selector\]]{#cor:selector label="cor:selector"} compiles every total decidable support, including primes, squares, powers of two, and seeded total predicates. Pruning the transient states leaves exactly the accepted diagonal loops. The determinant cannot distinguish how the support was computed and is [[Proves Too Much]{.smallcaps}]{.upright}.

## Recurrent computation clock-dilutes

[\[thm:clock\]]{#thm:clock label="thm:clock"} Close accepted computations into pairwise disjoint deterministic cycles of lengths $\ell(n)$. Assign nonnegative roofs $\tau_{n,1},\ldots,\tau_{n,\ell(n)}$ with $$\sum_{j=1}^{\ell(n)}\tau_{n,j}=\log n.$$ If, along an infinite accepted subsequence, $$\frac{\ell(n)}{\log n}\longrightarrow\infty,$$ then for every fixed $\sigma>0$ the whole weighted vertex adjacency is noncompact.

Some edge satisfies $$\tau_{n,j}\le\frac{\log n}{\ell(n)},$$ and therefore has weight $$\mathrm e^{-\sigma\tau_{n,j}}
 \ge n^{-\sigma/\ell(n)}
 \longrightarrow1.$$ Choose one such edge on each disjoint cycle. Its source vectors are orthonormal, and their images have mutually orthogonal components with norms bounded away from zero. The images have no convergent subsequence, so the operator is not compact.

[\[cor:spinedilution\]]{#cor:spinedilution label="cor:spinedilution"} If the natural endpoint roof on $C_k$ is replaced by total roof $\log k$, every nonnegative allocation over its $k$ edges produces a noncompact whole adjacency, because $$\frac{k}{\log k}\longrightarrow\infty.$$

Acceptance-independent padding is a matched control. Adding $n$ dummy steps to every input, regardless of acceptance, makes $\ell(n)/\log n$ diverge for any decidable support. The obstruction is therefore not prime-specific.

## First return changes the object

[\[prop:inducing\]]{#prop:inducing label="prop:inducing"} First return to one marked state per accepted cycle multiplies its edge weights into $n^{-s}$, but changes $$z^{\ell(n)}\longmapsto z.$$ For $C_k$, it erases $1^{k-1}2$ and maps $z^k$ to $z$.

A return step represents one full original circuit. The product of the edge weights becomes one return weight, while the induced graph assigns one new edge to that circuit. The old edge count is therefore not preserved.

separates four statements that are often merged: computability, recurrence visibility, whole-operator compactness, and marker preservation. The scoped conclusion is:

> Within the Paper19 transient and Paper20 recurrent total-decider wrappers, exact selection either becomes determinant-invisible computation, loses compactness under a short recurrent roof, or changes the orbit ledger under induction.

No universal countable-state impossibility theorem is asserted.

# Exact audit protocol {#sec:audit}

The computational layer is a certificate audit of identities already stated in the theorem package; it is not statistical evidence for prime selectivity. The candidate generator is frozen before any predicate-aware evaluator runs. In particular, the source layer contains no primality, factorization, prime-table, or Riemann-zero call.

L1.0cmL3.6cmY ID & Frozen range & Exact obligation\
E1 & $2\le k\le4096$ & certify $C_k$, $\mathsf W(C_k)=1^{k-1}2$, $|C_k|=k$, $Q(C_k)=2$, and a clean source-oracle scan\
E2 & unary state sets $|Q|\le4$ & enumerate finite transformations/relations and verify tail--period certificates\
E3 & post-freeze evaluator & construct the same-residue composite $p(1+\lambda)$ from an accepted tail prime $p$\
E4 & rational matrices $1\le d\le8$ & verify Cayley--Hamilton residuals and rational generating functions through at least $4d+16$\
E5 & $N\in\{32,64,128,256\}$ & fit prime and six matched arbitrary target families with both nilpotent memorizers\
E6 & periods $r\le32$ & compare sparse graph traces, $\operatorname{Tr}(P_k^r)$, exterior-power coefficients, and full block determinants\
E7 & $\sigma\in\{.45,.49,.50,.51,.60,1\}$ & separate successor/return nuclear partial sums, including $A=0$ and $B=0$ controls\
E8 & five decidable supports & compare full/pruned transient traces, padded recurrent clocks, and pre/post-inducing markers\
E9 & $2\le k\le4096$ & verify $\prod_{(n,d)\in C_k}nd=M_k^2$ and preserve the distinct monomials $z^kM_k^{-2s}$ and $zk^{-s}$\
E10 & two clean runs & require byte identity, environment lock, SHA-256 inventory, and candidate/evaluator provenance\

The determinant audit uses the complete hierarchy from [\[prop:blockfactor,thm:exteriorlrs\]](#prop:blockfactor,thm:exteriorlrs){reference-type="ref" reference="prop:blockfactor,thm:exteriorlrs"}: a first trace-log coefficient is never substituted for the full local factor. Likewise, a marked bilinear coefficient and the separate one-dimensional oracle deletion control are recorded in distinct fields. The trace-zero example of [\[rem:tracenotfactor\]](#rem:tracenotfactor){reference-type="ref" reference="rem:tracenotfactor"} is a mandatory regression case.

[\[prop:auditsoundness\]]{#prop:auditsoundness label="prop:auditsoundness"} Passing E1--E10 can falsify an implementation that disagrees with a proved identity, detect oracle leakage, and certify deterministic provenance. It cannot prove the SML theorem, establish the sharp infinite-volume nuclear threshold from finite partial sums, or convert a finite prime fit into asymptotic evidence.

Each positive statement in the first sentence is a finite equality or a finite source/integrity check. The excluded statements contain an infinite quantifier or invoke an external theorem. In particular, [\[thm:bilmemorizer,thm:trmemorizer\]](#thm:bilmemorizer,thm:trmemorizer){reference-type="ref" reference="thm:bilmemorizer,thm:trmemorizer"} give an exact fit for every finite target vector, so a finite residual cannot distinguish primes from the matched controls.

No target-zero data enter this protocol. Route evaluation is written in a separate artifact with two-stage provenance: the candidate records its frozen claims, while an external evaluator may later record an independent score without altering the candidate source.

## Integrated exact outcome

The frozen implementation passed all $32$ collected tests. E1 checked $4{,}095$ cycles and $8{,}390{,}655$ edges with no source-policy failure. E2 exhausted $288$ unary transformation maps, $1{,}054{,}474$ terminal/acceptance configurations, $1{,}024$ Boolean relation configurations, and $8{,}067{,}400$ period comparisons, with no failure. E4 checked $2{,}832$ Cayley--Hamilton residuals in $48$ rational matrix cases; E5 checked $56$ matched memorizers; E6 checked $128$ power traces through period $32$ and $12$ direct-versus-Newton determinant rows.

The frozen $2\times2$ regression used $A=I$ and $B=\operatorname{diag}(1,-1)$. It returned $$\operatorname{Tr}(BA^{k-1})=0,
 \qquad
 \operatorname{Tr}((BA^{k-1})^2)=2,
 \qquad
 \det(I-wBA^{k-1})=1-w^2,$$ exactly, so the audit directly detects the forbidden first-trace shortcut. E7 produced $144$ diagnostic rows, E8 imported two licensed certificates and checked five transient supports plus $40$ recurrent rows, and E9 verified all $4{,}095$ roof identities, with the first desired-monomial mismatch already at $k=2$.

Two complete runs produced $31$ byte-identical artifacts with combined SHA-256

`25d1dc42431693a0b380741531238b5b52bbbb62f5c9602afe13845a67ebd336`.

The integrity audit passed, and every entry in its sealed SHA ledger verified. The machine-readable ledger is authoritative because provenance sealing necessarily changes its own digest. These finite results corroborate the implementation consequences listed in [\[tab:audits\]](#tab:audits){reference-type="ref" reference="tab:audits"}; they do not replace the infinite proofs.

# Route-A evaluation and next admission test {#sec:route}

The route score follows the same-object ledger, not the ease with which a predicate can be compiled into an auxiliary machine.

L1.0cmL3.4cmY Gate & Verdict & Certificate\
A0 & `STRUCTURAL` `ARITHMETIC` `RELATION` & the quotient labels and $1^{k-1}2$ are source-derived\
A1 & `WEAK` & the canonical family is exact but indexed by every $k\ge2$, not primes\
A2 & `ANALYTIC` `DETERMINANT` & $L_{s,A,B}\in\mathcal S_1$ exactly for $\Re s>1/2$ when the fixed complex fiber is nonzero\
A3 & `FAIL` & fixed fibers cannot give infinite prime-only exact support; full block factors remain LRS-rigid, while licensed exact wrappers prune, clock-dilute, or change the marker\
A4 & `FAIL` & no critical-line or Hilbert--Pólya mechanism is constructed\

[\[thm:routeclosure\]]{#thm:routeclosure label="thm:routeclosure"} For the frozen canonical family and its fixed finite-dimensional fibers, H1--H9 imply that A3 fails. The full local determinant is $\det_{\mathbb C^d}(I-w_kBA^{k-1})$, its coefficient supports are finite unions of ultimately periodic sets, and its natural monomial remains $z^kM_k^{-2s}$. The separate one-dimensional oracle deletion control can keep prime indices but still retains that marker and roof. Within the licensed Paper19 transient and Paper20 recurrent wrappers, exact countable selection has the failures proved in [8](#sec:countable){reference-type="ref" reference="sec:countable"}.

Finite-semigroup and automaton responses are covered by [\[thm:finite-semigroup,thm:automata\]](#thm:finite-semigroup,thm:automata){reference-type="ref" reference="thm:finite-semigroup,thm:automata"}. Fixed characteristic-zero linear responses are covered by [\[thm:smlsupport\]](#thm:smlsupport){reference-type="ref" reference="thm:smlsupport"}; the complete block factor, rather than merely its first trace-log term, is covered by [\[thm:exteriorlrs\]](#thm:exteriorlrs){reference-type="ref" reference="thm:exteriorlrs"}. Growing finite responses satisfy [\[cor:provestoomuch\]](#cor:provestoomuch){reference-type="ref" reference="cor:provestoomuch"}. The two licensed infinite-memory alternatives are [\[thm:transient,thm:clock,prop:inducing\]](#thm:transient,thm:clock,prop:inducing){reference-type="ref" reference="thm:transient,thm:clock,prop:inducing"}. Finally, [\[prop:monomial,thm:factorial,prop:stirling\]](#prop:monomial,thm:factorial,prop:stirling){reference-type="ref" reference="prop:monomial,thm:factorial,prop:stirling"} fix the marker and roof.

Thus the frozen tuple is $$\boxed{\begin{gathered}
(\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},\\
 \mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},\\
 \mathrm{A3\_FAIL},
 \mathrm{A4\_FAIL})
\end{gathered}}$$ and the overall decision is $$\boxed{\mathrm{ROUTE\_A\_REJECTED}}.$$ Route B remains locked. H1--H9 mathematically certify the A3 failure; `A4_FAIL` records only that this candidate constructs no qualifying spectral mechanism. It does not assert that such a mechanism cannot exist.

## Paper24 admission test

A successor is worth opening only after it presents, before any prime-prefix experiment, a source-derived recurrent grammar satisfying all of the following:

1.  prime selection is intrinsic rather than an attached scalar oracle;

2.  accepted symbolic length and intrinsic roof are both $O(\log n)$;

3.  the whole, uninduced vertex operator is compact or trace class on an explicit half-plane;

4.  the same object preserves the intended orbit marker and produces $n^{-s}$ rather than the factorial monomial;

5.  matched nonprime decidable controls do not pass for the same reason.

These conditions are an admission test, not a claim that no grammar can meet them.

# Conclusion {#sec:conclusion}

The ordered quotient labels do recover information lost by abelian holonomy: the canonical orbit has the exact word $1^{k-1}2$. That positive fact makes the obstruction sharper. A fixed finite reader sees an eventually periodic power; a fixed characteristic-zero linear reader sees an LRS; the complete finite block determinant remains controlled by exterior-power LRS coefficients; and a growing finite reader stores any chosen prefix. None of these operations alters the source marker $z^k$ or the factorial roof $2\log M_k$.

Countable computation is possible, but only the two inherited wrapper architectures were analyzed here. In them, computation is either trace-invisible, recurrently noncompact under a short total roof, or erased from the symbolic marker by inducing. This scoped hierarchy is enough to reject SD-C25 on Route A while leaving the broader search open.

The next constructive obligation is therefore precise: exhibit an intrinsic recurrent grammar of logarithmic symbolic length and logarithmic roof whose whole operator retains the computation and its marker. Until that object exists, further finite prime-prefix fitting would repeat the nilpotent memorizer control rather than advance the arithmetic mechanism.

# Supplementary proof details {#app:proofs}

This appendix records the algebraic and operator facts used in the main argument without enlarging their scope.

## From finite powers to accepted residue classes

If $a^i=a^j$ with $i<j$, then $a^{i+r}=a^{j+r}$ for every $r\ge0$. Hence a membership response to $a^{k-1}b$ is constant on sufficiently large residue classes modulo $\lambda=j-i$. If such a class contains a prime $p$ in the tail, it also contains $p(1+\lambda)$, because $$p(1+\lambda)\equiv p\pmod\lambda.$$ This is the explicit composite witness behind [\[lem:primeperiod,thm:finite-semigroup\]](#lem:primeperiod,thm:finite-semigroup){reference-type="ref" reference="lem:primeperiod,thm:finite-semigroup"}.

## Exterior powers and the complete block factor

For $X\in M_d(\mathbb C)$, the elementary symmetric coefficients of its eigenvalues satisfy $$\det(I-tX)=\sum_{j=0}^d(-t)^j\operatorname{Tr}(\wedge^jX).$$ This is a polynomial identity, so it remains valid without diagonalizability. With $X=BA^{k-1}$, functoriality gives $$\wedge^j(BA^{k-1})
 = (\wedge^jB)(\wedge^jA)^{k-1}.$$ Each coefficient therefore satisfies a Cayley--Hamilton recurrence of dimension at most $\binom dj$. The set where the block factor differs identically from $1$ is the union of the nonzero supports of these finitely many sequences. SML makes that union ultimately periodic. This argument does not replace the full factor by $1-w_k\operatorname{Tr}(BA^{k-1})$.

## Trace-class lower bounds

Let $P_{\mathrm{even}}$ project onto even source vertices and let $Q_{\mathrm{odd}}$ project onto their odd successors. When $A\ne0$, $$Q_{\mathrm{odd}}L_{s,A,B}P_{\mathrm{even}}
 =\bigoplus_{m\ge1}[(2m)(2m+1)]^{-s}A$$ after identifying the orthogonal source and target blocks. Its singular values are the singular values of $A$ multiplied by the scalar edge weights. Thus its trace norm is $$\|A\|_1\sum_{m\ge1}[(2m)(2m+1)]^{-\Re s}.$$ Trace-class ideals are stable under compression, giving necessity of $\Re s>1/2$. If $A=0$ and $B\ne0$, the injective return edges $2d-1\to d$ give the analogous direct sum with weights $[(2d-1)d]^{-s}$. The upper edge expansion in [\[thm:traceclass\]](#thm:traceclass){reference-type="ref" reference="thm:traceclass"} gives sufficiency.

## Why the transient determinant forgets the machine

In [\[thm:transient\]](#thm:transient){reference-type="ref" reference="thm:transient"}, every computation or cemetery vertex lies in a directed acyclic component before the accepted self-loop. No positive power of the adjacency has a diagonal entry supported on such an edge. Consequently the trace logarithm sees only accepted terminal loops. The double zeta majorant proves trace class independently of the runtime $T(n)$, because every finite runtime sum is bounded by the full convergent $j$-series. This proves selector universality and simultaneously explains why the determinant does not certify the computation.

## Clock dilution and inducing

For a cycle of length $\ell$ with nonnegative roofs totaling $\log n$, the smallest roof is at most $\log n/\ell$. Choosing the corresponding edge on each of infinitely many disjoint cycles produces orthonormal source vectors whose images have orthogonal components bounded away from zero when $\ell/\log n\to\infty$. This proves noncompactness, not merely failure of a particular trace-norm bound.

First return is algebraically exact but object-changing. Multiplication of the original edge weights preserves the total roof, while one return edge replaces $\ell$ original graph steps. Hence $z^\ell\mapsto z$ even though the scalar roof product is preserved.

## Factorial asymptotics

Uniform Stirling expansion gives $$\begin{aligned}
\log M_k
 &=\log(2k-1)!-\log(k-1)!\\
 &=k\log k+(2\log2-1)k+O(\log k).
\end{aligned}$$ Thus the canonical total roof is $2k\log k+O(k)$, and no coefficient filter on the frozen cycle can turn it into $\log k$.

# Scope, provenance, and claim ledger {#app:scope}

L3.2cmY Y Ledger & Frozen object & Authorized conclusion\
full block determinant & $\det_{\mathbb C^d}(I-w_kBA^{k-1})$ & all exterior-power coefficients are LRS; a zero first trace does not delete the factor\
first trace-log term & $w_k\operatorname{Tr}(BA^{k-1})$ & one coefficient of the normalized local logarithm only\
marked bilinear observable & $u^{\mathsf T}A^{k-1}Bv$ & mark-dependent LRS response, not an unmarked determinant coefficient\
one-dimensional oracle control & $1-w_k\mathbf 1_{\mathbb P}(k)$ & deletes composite-indexed factors by assumption and therefore [Proves Too Much]{.smallcaps}\

The recurrence layer uses matrices over an arbitrary characteristic-zero field $\mathbb F$. Schatten ideals and Fredholm determinants are asserted only for $A,B\in M_d(\mathbb C)$ on $\ell^2(V)\otimes\mathbb C^d$. For word morphisms we use $\phi(xy)=\phi(x)\phi(y)$; DFA transitions act on column states, so the final state after $1^{k-1}2$ is $(T_2\circ T_1^{k-1})(q_0)$.

L3.7cmL2.6cmY Statement & Status & Boundary\
$Q=2$ cycle classification & imported & predecessor result; ordered word proved here\
finite-fiber periodicity & proved here & fixed semigroup/DFA/NFA only\
LRS support rigidity & external theorem applied here & exact zero/nonzero and fixed levels only\
full block-factor rigidity & proved here & finite complex block, via exterior powers\
trace-class threshold & proved here & fixed nonzero complex fiber\
transient/recurrent wrapper results & licensed imports restated & Paper19/Paper20 architectures only\
A3 failure & theorem consequence & frozen SD-C25 model class\
A4 failure & evaluation & no mechanism constructed; no nonexistence theorem\

The direct 2026 collision of @deJong2026 narrows novelty language, but its theorem is not applied to SD-C25: this countable Markov source is not asserted to be compact or finitely presented, and its trace-log derivative is not asserted to be rational. The candidate-specific claims are the exact cofactor word, the full memory hierarchy, the same-object block/roof audit, and the scoped route closure.

Experiment provenance has two stages. The candidate generator is predicate-blind and frozen; a post-freeze evaluator may compute target labels and scores. Exact arithmetic, matched arbitrary-target controls, two clean byte-identical runs, and a SHA-256 inventory are mandatory. No Riemann-zero data, external review loop, Route-B construction, or silent parameter change is licensed.

The Paper24 admission test is constructive: intrinsic prime selection, logarithmic symbolic length, logarithmic roof, a compact or trace-class whole vertex operator, and preservation of the same orbit marker. Failure to present that package blocks a new finite-fit experiment; it does not prove that no such grammar exists.
