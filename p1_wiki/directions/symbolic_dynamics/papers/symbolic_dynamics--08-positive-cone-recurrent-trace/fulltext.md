---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--08-positive-cone-recurrent-trace"
canonical_tex: "symbolic_dynamics/papers/08-positive-cone-recurrent-trace/main.tex"
canonical_pdf: "symbolic_dynamics/papers/08-positive-cone-recurrent-trace/main.pdf"
source_sha256: "6050e658e4b15cc99ef0447398bb9d23c00a1bf40f556f1e39d6de72be19f216"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Positive-Cone Cocycles on a Recurrent Tensor-Prime Shift: Exact $\tau$-Euler Ledger and the Chiral Backtracking Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/08-positive-cone-recurrent-trace>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/08-positive-cone-recurrent-trace/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/08-positive-cone-recurrent-trace/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/08-positive-cone-recurrent-trace/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/08-positive-cone-recurrent-trace/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  An exact tensor-prime Euler transfer can avoid mixed primitive cycles by making its atom graph acyclic. We ask whether recurrence can instead be retained in the base symbolic grammar while mixed lifts are removed by an intrinsic trace. Order the tensor atoms by entropy, put loops and both nearest-neighbor arrows on the atom graph, label every directed cross edge by a distinct positive generator of a free group, and assign the symmetric endpoint weight $a_n(s)=(p_n^{-s}+p_{n+1}^{-s})/2$. The base graph is strongly connected and aperiodic, but every mixed closed base word has a nonempty positive cocycle word. The canonical trace $\tau$ therefore kills it. On the semifinite algebra $B(\ell^2(\operatorname{At}))\bar\otimes L(\mathbb F_\infty)$ we prove $$(\operatorname{Tr}\otimes\tau)(T_s^r)=\sum_pp^{-rs},\qquad
   \det_\tau(I-zT_s)=\prod_p(1-zp^{-s})$$ in the honest trace-class half-plane. This defines SD-C10 and upgrades the Euler ledger from an acyclic base to a recurrent one. The mechanism is positive-cone rather than specifically free: an abelian positive control also works. Its limitation is sharp. The self-adjoint chiral double uses $T_t^*$ and hence introduces inverse words. Immediate backtracks $gg^{-1}$ contribute the strictly positive mixed term $4\sum_n|a_n(1/2+it)|^2$ to the quadratic trace. This diverges, so neither $\det_1$ nor $\det_2$ exists; $\det_3$ exists but subtracts precisely that first recurrent term. A two-atom formula proves that the fourth trace and $\det_3$ still move with height. Thus the analytic $\tau$-determinant sees the Euler ledger but not the nonnormal geometry, while Fuglede--Kadison and Brown data see magnitude geometry but do not supply a holomorphic Euler divisor. The stage reaches a recurrent noncommutative A2/A3 mechanism and stops at a unified divisor.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 13, 2026'
title: |
  Positive-Cone Cocycles on a Recurrent Tensor-Prime Shift:\
  Exact $\tau$-Euler Ledger and the Chiral Backtracking Obstruction
```

## Markdown 正文

# Introduction {#sec:introduction}

The tensor monoid of finite full shifts satisfies $$F_m\boxtimes F_n\cong F_{mn},\qquad h_{\rm top}(F_n)=\log n.$$ Its nonunit atoms are therefore $F_p$, and their entropy supplies the logarithmic arithmetic clock. The diagonal atom-loop transfer gives the Euler product exactly. Paper07 then coupled adjacent masses along increasing entropy. Its chiral spectrum moved, but its base grammar was directed acyclic; the added edges could never enter a periodic word.

This paper takes the opposite step. We restore both orientations between adjacent atoms, so the base is strongly connected and has mixed periodic words at every scale. Rather than cancel their scalar weights, we lift the grammar by a cocycle. Each directed cross edge receives a distinct positive free-group generator, while loops receive the identity. The canonical trace of the group von Neumann algebra extracts the identity coefficient. A nonempty positive word cannot reduce to the identity, so every mixed base cycle disappears from the traced periodic ledger.

This construction, SD-C10, is a genuine change of object rather than another coordinate added to SD-C09. Its transfer acts in the semifinite von Neumann algebra $$\mathcal N=B(\ell^2(\operatorname{At}))\bar\otimes L(\mathbb F_\infty),
 \qquad \Phi=\operatorname{Tr}\otimes\tau.                 \tag{1.1}$$ In $\Re s>1$ it is $\Phi$-trace class and its analytic traced determinant is exactly $1/\zeta(s)$. Thus recurrence has been retained in the base grammar without contaminating the Euler ledger.

The success is not free-group magic. Labelling both orientations by a shared positive generator of $\mathbb Z$ gives the same identity-extraction rule. The universal directed labels are preferred because they are functorial in the directed edge set and expose which word was traversed, but positivity of the label monoid is the operative property.

The obstruction arrives at self-adjointization. On $s=1/2+it$, the natural chiral block contains $T_t$ and $T_t^*$. The adjoint reverses the group letters. Every cross edge can now be followed by its adjoint, producing $gg^{-1}=e$. This is a positive norm-square contribution, not a phase that can cancel. It occurs in the quadratic trace, diverges over the tensor atoms, and is precisely the term removed by the first available determinant $\det_3$.

The contributions are:

1.  a recurrent, aperiodic tensor-prime base grammar with a universal directed-positive free cocycle;

2.  an exact primitive/repetition $\Phi$-trace ledger and analytic $\tau$-Euler determinant;

3.  sharp boundedness, compactness-in-$\mathcal N$, and noncommutative Schatten domains;

4.  free, shared-positive, abelian-positive, and inverse-label controls;

5.  an exact chiral $gg^{-1}$ backtracking formula and divergence theorem;

6.  a two-atom fourth-trace theorem proving surviving $\det_3$ motion;

7.  a separation of analytic $\tau$, Fuglede--Kadison, and Brown determinant data;

8.  a Route-A advance with a sharp unified-divisor stop and Route-B lock.

Only Symbolic Dynamics and its cocycle transfer are primary. Any proposed external carrier is recorded solely as a future clue.

# Symbolic cocycles and traced zeta functions {#sec:related}

Determinant formulas for finite symbolic shifts begin with the classical Bowen--Lanford construction [@bowenlanford1970]; transfer operators and twisted symbolic dynamical $L$-functions place group representations into a much wider periodic-orbit framework [@ruelle1976; @parrypollicott1990]. Those theories make a cocycle determinant natural, but do not select the tensor-prime atom source or the positive-cone trace used here.

The closest algebraic precedent is the zeta function of a matrix over a free group algebra, whose coefficients are extracted using the identity word [@kasselreutenauer2014]. Analytic graph determinants in finite von Neumann algebras and convergence of $L^2$ graph zeta functions provide operator-algebraic precedents for traced determinant constructions [@clairmokhtari2002; @guidoisolalapidus2009]. Our result uses the same canonical identity-coefficient principle but on a countable tensor-prime symbolic grammar with an entropy-derived roof.

The relevant determinant notions must be separated. Fuglede and Kadison introduced the positive determinant $\exp\tau(\log|A|)$ for finite factors [@fugledekadison1952]; a complex trace determinant requires a chosen path or logarithm branch [@delaharpeskandalis1984]. Brown measure is controlled by the logarithmic Fuglede--Kadison potential [@haagerupschultz2007]. These objects see magnitude and nonnormal geometry, but they are not the same as the locally holomorphic traced determinant obtained from cyclic power traces. The distinction becomes decisive for SD-C10.

Our use of a free group should not be overinterpreted. The proof needs a positive monoid embedded in a group, together with a trace that returns one at the identity and zero elsewhere. A shared positive generator in $\mathbb Z$ already kills every nonempty positive mixed word. Free directed generators form the universal implementation because distinct directed edge words remain distinguishable before the trace is taken.

We found no primary source combining this positive-cone trace mechanism with the tensor-prime full-shift monoid, a recurrent nearest-neighbor atom grammar, and the exact chiral backtracking obstruction. This is a bounded synthesis claim, not a first-ever claim about group-cocycle zeta functions, von Neumann determinants, or free-group traces.

# The recurrent tensor-prime cocycle {#sec:source}

Let $\operatorname{At}=\{F_{p_n}:n\ge1\}$ be the tensor atoms, ordered by increasing topological entropy. The base directed graph $\mathcal G$ has a loop at every $n$ and both arrows between $n$ and $n+1$. It is strongly connected and aperiodic: every vertex reaches every other, and each loop has length one. Every cross edge belongs to a mixed base two-cycle. We use "recurrent" in this graph-theoretic sense. The unweighted countable half-line shift is not claimed to be positive recurrent in the Vere--Jones sense.

Let $\mathbb F_\infty$ be freely generated by $$\{g_{n,+},g_{n,-}:n\ge1\}.$$ The arrow $n\to n+1$ is labelled $g_{n,+}$ and the arrow $n+1\to n$ is labelled the independent positive generator $g_{n,-}$. The reverse label is deliberately not $g_{n,+}^{-1}$. Every loop is labelled by the identity $e$. This is the universal directed-positive cocycle.

Let $\lambda$ be the left regular representation, let $\mathcal M=L(\mathbb F_\infty)$, and let $$\tau(\lambda(g))=\begin{cases}1,&g=e,\\0,&g\ne e.\end{cases}$$ On $$\mathcal N=B(\ell^2(\operatorname{At}))\bar\otimes\mathcal M,
 \qquad \Phi=\operatorname{Tr}\otimes\tau,                 \tag{3.1}$$ define $$d_n(s)=p_n^{-s},\qquad
 a_n(s)=\frac{p_n^{-s}+p_{n+1}^{-s}}2,        \tag{3.2}$$ and $$\begin{aligned}
 T_s={}&\sum_nd_n(s)E_{nn}\otimes1 \notag\\
 &+\sum_na_n(s)\bigl(
 E_{n+1,n}\otimes\lambda(g_{n,+})
 +E_{n,n+1}\otimes\lambda(g_{n,-})\bigr).   \tag{3.3}\end{aligned}$$

Equation (3.3) is the transfer of one symbolic system. The loop roof is $\log p_n$. Each cross direction has two parallel endpoint-roof edges with potential $-\log2$, compressed into $a_n(s)$. The phase space, grammar, roof, potential, cocycle, function space, trace, and determinant convention are fixed before any zero comparison. No Riemann-zero list is allowed.

## Controls fixed with the candidate

Three label choices distinguish the mechanism:

1.  *directed free positive*: the SD-C10 implementation above;

2.  *shared abelian positive*: label every cross edge by the same generator $u\in\mathbb Z$; a mixed word is $u^k$, $k>0$, and the canonical trace still kills it;

3.  *inverse/time reversal*: label $n+1\to n$ by $g_{n,+}^{-1}$; the base two-cycle now has identity monodromy and must leak into the quadratic trace.

Trivial labels, randomized positive directed labels, shuffled masses, composites, and matched random masses are further adversarial controls.

# Exact traced periodic ledger and analytic determinant {#sec:tau-euler}

[\[thm:ledger\]]{#thm:ledger label="thm:ledger"} For every integer $r\ge1$ and every $s$ in a noncommutative $L^r$ domain, $$\Phi(T_s^r)=\sum_pp^{-rs}.                  \tag{4.1}$$ The $\Phi$-visible primitive objects are exactly the atom loops $\gamma_p$, and their repetitions are $\gamma_p^r$ with length $r\log p$.

Expanding $T_s^r$, the matrix trace keeps precisely closed base words. A word using only the loop at $p$ contributes $p^{-rs}\lambda(e)$. Every mixed closed base word contains at least one cross edge. Its cocycle product is a nonempty word in positive free generators. There are no inverse letters, so free reduction cannot make it the identity. The canonical trace $\tau$ kills it. Summation over loop vertices proves the identity and the primitive/repetition statement.

The same proof works for the shared abelian-positive control: its mixed word has strictly positive exponent. Thus exact deletion comes from the positive cone, not from noncommutativity alone.

[\[prop:ideals\]]{#prop:ideals label="prop:ideals"} Put $\sigma=\operatorname{Re}s$. For $\sigma>0$, $T_s$ is bounded and belongs to the $\Phi$-compact ideal. For $q\ge1$, $$T_s\in L^q(\mathcal N,\Phi)\quad\Longleftrightarrow\quad q\sigma>1. \tag{4.2}$$ In particular, $T_s$ is $\Phi$-trace class for $\sigma>1$, while on the critical line it belongs to every $L^q$, $q>2$, but not to $L^2$.

The matrix has bandwidth one and coefficient bound $$\|T_s\|\le\sup_n
 \bigl(|d_n(s)|+|a_{n-1}(s)|+|a_n(s)|\bigr)<\infty.$$ All coefficients tend to zero, giving $\Phi$-compactness by finite atom cutoffs. Decompose $T_s$ into its diagonal and two weighted shifts. Their $L^q$ norms are equivalent, up to fixed finite-band constants, to $\sum_np_n^{-q\sigma}$. This converges exactly when $q\sigma>1$. Conversely, the trace-preserving diagonal conditional expectation sends $T_s$ to $D_s$, so $L^q$ membership forces the same prime sum to converge.

[\[thm:det\]]{#thm:det label="thm:det"} For $\operatorname{Re}s>1$, define the normalized trace-series dynamical determinant by $$\det_\Phi(I-zT_s)
 :=\exp\left(-\sum_{r\ge1}\frac{z^r}{r}\Phi(T_s^r)\right). \tag{4.3}$$ The series converges for $|z|<2^{\operatorname{Re}s}$, and $$\det_\Phi(I-zT_s)=\prod_p(1-zp^{-s})        \tag{4.4}$$ there. Its canonical entire continuation in $z$ is the convergent product on the right. In particular the $z=1$ specialization is $\zeta(s)^{-1}$ in its honest Euler half-plane.

Insert [\[thm:ledger\]](#thm:ledger){reference-type="ref" reference="thm:ledger"} into [\[eq:analytic-det\]](#eq:analytic-det){reference-type="ref" reference="eq:analytic-det"}: $$\log\det_\Phi(I-zT_s)
 =-\sum_{r\ge1}\frac{z^r}{r}\sum_pp^{-rs}
 =\sum_p\log(1-zp^{-s}).
 \label{eq:analytic-det}$$ Absolute convergence holds for $|z|<2^{\operatorname{Re}s}$, since the closest local factor is $p=2$. The product converges locally uniformly for every finite $z$, giving its entire continuation. Since $1<2^{\operatorname{Re}s}$, no continuation is needed at $z=1$ when $\operatorname{Re}s>1$.

This trace-series object agrees with the local path-integral analytic $\Phi$-determinant wherever $I-zT_s$ stays in the small-norm invertible component. Beyond that component we claim the dynamical trace-series continuation, not operator invertibility. It is not an ordinary Fredholm determinant on $\ell^2(\operatorname{At})\otimes\ell^2(\mathbb F_\infty)$. Each group unitary has infinite ordinary multiplicity, so ordinary compactness and trace class fail. The trace $\Phi$ is part of the frozen dynamical data.

# Chiral self-adjointization and positive backtracking {#sec:chiral}

On the critical line write $T_t=T_{1/2+it}$ and form the natural self-adjoint chiral operator $$B_t=\begin{pmatrix}0&T_t\\T_t^*&0\end{pmatrix}                \tag{5.1}$$ in $M_2(\mathcal N)$, with trace $\Phi_2=\operatorname{tr}_2\otimes\Phi$. The adjoint reverses each free word. Even though the original base reverse edge was independently positive, the analytic adjoint of every individual edge supplies its inverse.

Put $$m_n=p_n^{-1},
 \qquad
 y_n(t)=|a_n(1/2+it)|^2
 =\frac{m_n+m_{n+1}+2\sqrt{m_nm_{n+1}}
 \cos(t\log(p_{n+1}/p_n))}{4}.               \tag{5.2}\label{eq:y-n}$$

[\[thm:backtrack\]]{#thm:backtrack label="thm:backtrack"} The quadratic chiral trace is $$\Phi_2(B_t^2)
 =2\Phi(T_t^*T_t)
 =2\left(\sum_nm_n+2\sum_ny_n(t)\right).    \tag{5.3}$$ Relative to the pure-loop sector, the mixed immediate-backtracking term is $$4\sum_ny_n(t)>0.                            \tag{5.4}$$ It diverges for every real $t$. Consequently $B_t\notin L^2$; neither an unregularized determinant nor $\det_2$ is available. One has $B_t\in L^q$ for every $q>2$, so $\det_3$ exists but subtracts powers one and two, precisely deleting [\[eq:mixed-backtrack\]](#eq:mixed-backtrack){reference-type="ref" reference="eq:mixed-backtrack"}: $$\text{the first positive recurrent mixed trace.}
 \label{eq:mixed-backtrack}$$ Every $\det_q$ with $q\ge3$ has the same loss.

The identity $B_t^2=\operatorname{diag}(T_tT_t^*,T_t^*T_t)$ gives the first equality. The canonical trace of $T_t^*T_t$ is the sum of squared $L^2(\mathcal M,\tau)$ coefficients in each matrix column. Loops give $\sum_nm_n$. The two directed cross coefficients at each adjacent pair give $2\sum_ny_n(t)$. Each is the word product $g^{-1}g=e$ arising from an edge and its adjoint, hence is nonnegative.

For fixed $t$, the prime number theorem gives $p_{n+1}/p_n\to1$, so $t\log(p_{n+1}/p_n)\to0$. For all sufficiently large $n$ the cosine in [\[eq:y-n\]](#eq:y-n){reference-type="ref" reference="eq:y-n"} is nonnegative, and hence $$y_n(t)\ge\frac{m_n+m_{n+1}}4.
 \label{eq:yn}$$ The harmonic prime sum diverges, and hence so does the mixed term. Thus the $L^2$ norm diverges. supplies $L^q$ membership for $q>2$. The logarithm of $\det_q$ begins at power $q$, proving the stated regularization loss.

## Inverse-label control before chiralization

If the original reverse base edge is labelled $g_{n,+}^{-1}$ rather than an independent positive generator, then the base two-cycle already has identity monodromy. In the holomorphic power trace, $$\Phi(T_s^2)-\sum_pp^{-2s}=2\sum_na_n(s)^2.  \tag{5.5}$$ Thus exact $\tau$ cancellation, recurrent periodic lifts, and local inverse time-reversal labels cannot coexist. The positive-cone choice preserves the first two only by breaking inverse closure before self-adjointization.

## The fourth trace still moves

Odd chiral traces vanish. Although $\det_3$ deletes the quadratic term, its first retained coefficient is the fourth trace and is nonconstant.

[\[prop:two-atom\]]{#prop:two-atom label="prop:two-atom"} For atoms $p<q$, put $x=p^{-1/2}$, $y=q^{-1/2}$ and $$u(t)=\frac{x^2+y^2+2xy\cos(t\log(q/p))}{4}.$$ For the directed-independent positive free labels, $$\begin{aligned}
 \Phi(T_t^*T_t)&=x^2+y^2+2u(t),\tag{5.6}\\
 \Phi((T_t^*T_t)^2)
 &=x^4+y^4+4u(t)(x^2+y^2)+2u(t)^2,\tag{5.7}\\
 \Phi_2(B_t^4)&=2\Phi((T_t^*T_t)^2).\tag{5.8}\end{aligned}$$ For $p=2,q=3$, with $c=\cos(t\log(3/2))$, $$\Phi_2(B_t^4)
 =\frac{c^2}{6}+\frac{25\sqrt6}{36}c+\frac{329}{144}. \tag{5.9}$$ This is strictly increasing in $c\in[-1,1]$ and hence gives genuine height-dependent $\det_3$ motion.

Expand the two matrix columns in the orthonormal group basis. Distinct positive labels are orthogonal under $\tau$; multiplication by the adjoint produces only the stated norm-square contractions. Substitution of $x^2=1/2$, $y^2=1/3$ gives [\[prop:two-atom\]](#prop:two-atom){reference-type="ref" reference="prop:two-atom"}. Its derivative in $c$ is $c/3+25\sqrt6/36>0$ on $[-1,1]$.

Thus self-adjointization does create determinant-visible motion at order four. It does so only after the first recurrent mixed trace at order two has been amputated by regularization.

# Three determinant data types {#sec:det-boundary}

SD-C10 naturally produces three determinant-like objects, but they answer different questions.

1.  The *analytic trace-series dynamical determinant* $\det_\Phi(I-zT_s)$ is reconstructed from cyclic $\Phi$-power traces. It equals the Euler product on $\Re s>1$. Near the identity it agrees with the path-integral analytic operator determinant; its scalar trace-series continuation does not assert that $I-zT_s$ remains operator-invertible. Precisely because $\tau$ deletes every nonidentity positive word, it does not see the recurrent cocycle geometry.

2.  The *Fuglede--Kadison determinant* $$\Delta_\Phi(X)=\exp\Phi(\log|X|)$$ is positive real, when defined. It sees singular-value geometry and hence the backtracking sector, but is not a holomorphic complex function carrying phase or an oriented zero divisor.

3.  Brown measure is encoded distributionally by the logarithmic Fuglede--Kadison potential $\lambda\mapsto\log\Delta_\Phi(T-\lambda)$. It may change when a nonnormal cocycle radical changes, even if every positive analytic moment agrees with a diagonal transfer. It is not thereby identified with the zeros of the Euler determinant.

[\[thm:trilemma\]]{#thm:trilemma label="thm:trilemma"} Within the frozen construction:

1.  the analytic $\Phi$-determinant has the exact Euler ledger but no proved continuation or chiral magnitude motion;

2.  Fuglede--Kadison and Brown data can see nonnormal or self-adjoint magnitude geometry but do not furnish a holomorphic Euler divisor;

3.  the holomorphic regularized chiral determinant $\det_3$ moves, but deletes the divergent first positive mixed trace.

Therefore no determinant presently belonging to SD-C10 simultaneously owns the exact Euler ledger, recurrent chiral trace, and a holomorphic critical divisor.

The first assertion is [\[thm:det\]](#thm:det){reference-type="ref" reference="thm:det"}; the second follows from the definitions and nonnormal dependence of $|T-\lambda|$; the third is [\[thm:backtrack,prop:two-atom\]](#thm:backtrack,prop:two-atom){reference-type="ref" reference="thm:backtrack,prop:two-atom"}. Combining different coordinates would violate the one-object rule rather than prove a unified determinant.

This is a structural stop, not a statement that no noncommutative symbolic determinant can work. It isolates the missing theorem: a single holomorphic relative determinant must retain a mixed coefficient in a nonempty analytic domain without requiring the divergent inverse-backtracking trace.

# Route-A decision and Route-B lock {#sec:route}

SD-C10 freezes one compatible symbolic object through its base graph, entropy roof, endpoint potential, positive cocycle, von Neumann function space, canonical trace, and analytic determinant. The self-adjoint chiral double is derived from that transfer rather than imported from another family.

0.99L0.08L0.25X Layer & Verdict & Evidence\
A0 & analytic arithmetic origin & tensor indecomposables give primes; entropy gives $\log p$ and their order, without prime or zero tables\
A1 & analytic pass & recurrent base cycles are exact; canonical trace retains precisely atom loops and their repetitions in the lifted identity sector\
A2 & analytic determinant & $\det_\Phi(I-zT_s)=\prod_p(1-zp^{-s})$ on the honest trace-class half-plane\
A3 & partial analytic structure & noncommutative Schatten strip, self-adjoint critical pencil, and moving $\det_3$ exist; the divergent quadratic backtrack prevents a unified determinant\
A4 & formal hint & canonical Hilbert module and chiralization exist, but no fixed generator, domain/counting theorem, or target divisor is produced\

The tuple is

  -----------------------------------------------------------
      `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_PASS_ANALYTIC,`
   `A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE,`
                      `A4_FORMAL_HINT).`
  -----------------------------------------------------------

The overall verdict is $$\boxed{\texttt{ROUTE\_A\_ANALYTIC\_CANDIDATE}.}$$ The stage status is

## Adversarial controls

The shared abelian-positive label proves that identity extraction is not free-specific. Random directed-positive labels also pass, so the mechanism does not distinguish one free presentation. Composite and random mass inventories pass the formal trace theorem but fail the tensor-atom A0 source. Trivial or inverse reverse labels leak mixed two-cycles. These controls prevent the exact Euler determinant from being promoted into a critical-line claim.

## Why Route B remains locked

$B_t$ is a self-adjoint compact-in-$\mathcal N$ pencil for each $t$, not a fixed self-adjoint operator whose eigenvalues are the height parameter. The ordinary Hilbert-space operator has infinite group multiplicity. There is no compact-resolvent counting theorem, exact von-Mangoldt trace for one fixed generator, Weil compression, or completed-$\xi$ determinant. The analytic $\Phi$, Fuglede--Kadison, Brown, and regularized chiral determinants cannot be combined coordinatewise. Therefore $$\mathtt{route\_b\_invocation\_allowed=false}.$$

The next smallest theorem stays inside Symbolic Dynamics: construct a holomorphic doubled positive-semigroup transfer, without an adjoint, whose relative analytic $\Phi$-determinant has a nonempty common ideal domain and a first retained mixed coefficient; or prove that every inverse-closed self-adjoint symbolic double necessarily has the divergent quadratic backtracking found here.

# Conclusion: recurrence moves into the trace fiber {#sec:conclusion}

SD-C10 restores recurrence to the tensor-prime base grammar. Every adjacent pair supports a mixed two-cycle, yet the universal positive cocycle prevents that cycle from closing in the identity fiber. The canonical trace then recovers exactly the old atom-loop ledger and its Euler determinant. In this precise sense, Paper07's acyclicity has moved from the base graph into the cocycle's positive cone.

The gain is real but bounded. The base periodic structure is richer, the transfer is noncommutative, and its chiral fourth trace moves with height. Nevertheless self-adjointness forces inverse closure. Every edge then meets its adjoint, $gg^{-1}$ becomes visible, and the resulting positive quadratic trace diverges. The first determinant that exists is $\det_3$, which has already subtracted the very recurrent term one hoped to retain.

The stage therefore gives a sharp trilemma: $$\boxed{
 \begin{gathered}
 \text{positive-cone analytic trace: exact Euler ledger},\\
 \text{inverse-closed chiral trace: positive recurrent backtracking},\\
 \text{available regularization: deletes the first backtracking term}.
 \end{gathered}}$$ Fuglede--Kadison and Brown data do not close the triangle because they trade holomorphic divisor information for magnitude geometry.

Paper09 should not search for another fitted phase. It should test a holomorphic doubled free-semigroup transfer using separate positive alphabets for $s$ and $1-s$. The target is one relative analytic determinant whose first mixed coefficient survives in a common Schatten domain. Failure should be upgraded to an inverse-closure/ideal obstruction theorem.

No external geometric system is developed. If local inverse phases need a geometric origin and an additional sign-reversing law, that possibility is a `ROUND2_CLUE`, not part of SD-C10.

# Technical details and scope firewall {#app:proofs}

## Conditional expectation and ideal necessity

The diagonal conditional expectation $$\mathbb E_{\rm diag}:\mathcal N\to
 \ell^\infty(\operatorname{At})\bar\otimes\mathcal M$$ is trace preserving and contractive on noncommutative $L^q$. Since $\mathbb E_{\rm diag}(T_s)=D_s\otimes1$, membership of $T_s$ in $L^q$ forces $$\Phi(|D_s|^q)=\sum_pp^{-q\operatorname{Re}s}<\infty.$$ This proves the necessary half of [\[prop:ideals\]](#prop:ideals){reference-type="ref" reference="prop:ideals"} without relying on a matrix norm comparison.

## The analytic determinant is normalized data

In a finite or semifinite traced algebra, a locally holomorphic determinant can be defined along an invertible path from the identity by integrating $\Phi(A'(z)A(z)^{-1})$. Its logarithm agrees with the power series in [\[thm:det\]](#thm:det){reference-type="ref" reference="thm:det"} near the identity. Different connected components or winding choices require explicit normalization. We claim the operator determinant only on the normalized component reached from the germ. The globally continued scalar Euler product is instead the trace-series dynamical determinant; it is not evidence that $I-zT_s$ is invertible in the whole operator algebra.

## Why the abelian control is legitimate

Let $u$ generate $\mathbb Z$, represented on $\ell^2(\mathbb Z)$, and let $\tau_{\mathbb Z}(u^k)=\delta_{k0}$. If every directed cross edge is labelled $u$, a mixed closed base path containing $k>0$ cross edges has monodromy $u^k$, hence zero canonical trace. The Euler ledger follows exactly. This control proves that the essential structure is a positive grading detected by the trace. The free cocycle remains preferable because it remembers the directed word before extraction.

## Data and interpretation firewall

The candidate uses no Riemann-zero data, fitted critical scale, or target-root objective. Tensor atoms are generated as full-shift indecomposables and ordered by their entropy. The following implications are forbidden: $$\begin{aligned}
 \det_\Phi(I-T_s)=\zeta(s)^{-1}\ (\operatorname{Re}s>1)
 &\not\Rightarrow\text{analytic continuation},\\
 B_t=B_t^*&\not\Rightarrow\text{Hilbert--P\'olya operator},\\
 \det{}_3(I-zB_t)\text{ moves}
 &\not\Rightarrow\text{Riemann divisor},\\
 \Delta_\Phi\text{ or Brown measure exists}
 &\not\Rightarrow\text{holomorphic determinant identity}.\end{aligned}$$

The free-group regular representation and its canonical trace are cocycle data over one symbolic grammar, not a separate operator-algebra research program. Any independent geometric or Hamiltonian realization lies outside the primary system family and may appear only as a round-two clue.
