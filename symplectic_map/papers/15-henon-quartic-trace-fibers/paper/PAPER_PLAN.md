# Paper Plan

**Title:** Low-Period Trace Fibers of Quartic Generalized Hénon Maps

**One-sentence contribution:** For single-factor monic-centered quartic generalized Hénon maps, we prove the dependent chain that pure formal fixed traces bound the possible Jacobians, the unique positive-dimensional period-\(\le 2\) trace fiber is \(E=\{a=1,\ p=(x^2-L)^2\}\), and formal period three separates its residual \(L^3\)-coordinate, yielding the sharp global quasi-finite cutoff \(P_{\mathcal H^1}(4)=3\).

**Article type:** Anonymous proof-only research article in complex and algebraic dynamics

**Target venue:** Not selected; the plan assumes no conference template, page limit, or venue-specific claim

**Date:** 2026-08-17

**Main-text budget:** Approximately 25 mathematical-content pages from the abstract through the conclusion, followed by references and approximately 12--15 pages of proof appendices

**Section count:** Eight numbered main sections, plus five proof appendices

**Visual policy:** No figures and no empirical tables. One compact five-stratum mathematical table is optional, non-evidentiary, and may be typeset in the main text only after later publication authorization.

## 1. Public framing and scope

The article tells one proof story rather than presenting three independent contributions:

\[
\operatorname{Trace}_1
\Longrightarrow
\text{finitely many Jacobian candidates}
\Longrightarrow
\text{exact period-}\le 2\text{ exceptional fiber }E
\Longrightarrow
\operatorname{Trace}_3\text{ separates }L^3
\Longrightarrow
\text{sharp quasi-finite cutoff }3.
\]

The title, abstract, introduction, theorem statements, and conclusion must preserve this order. The paper is not to be framed as a short note whose only content is the equation \(P_{\mathcal H^1}(4)=3\).

The public scope is fixed as follows.

- Part A is over an algebraically closed field of characteristic zero.
- Parts B and C are over \(\mathbb C\).
- The source is the single-factor monic-centered normal-form space

  \[
  \mathcal H^1_d
  =
  \{(a,p):a\in k^\ast,\ p\text{ monic centered of degree }d\},
  \qquad
  f_{a,p}(x,y)=(ay+p(x),x).
  \]

- Parts B and C concern only \(\mathcal H^1_4\) and its finite residual quotient \(\mathcal M^1_4=\mathcal H^1_4/\mu_3\).
- Every trace multiset is taken on a formal-period zero-cycle with scheme-theoretic multiplicity.
- The conclusion is quasi-finiteness, not injectivity.
- The period-three second moment is used only on the exceptional curve \(E\).

The article must never silently enlarge any of these statements.

## 2. Headline theorem architecture

The introduction should state one unified theorem, followed later by separately numbered results that prove its three parts.

### Theorem 1.1 (Unified quartic trace-fiber theorem)

Let \(f_{a,p}(x,y)=(ay+p(x),x)\), with \(p\) monic centered.

1. **Pure fixed-trace Jacobian bound.** Over an algebraically closed field \(k\) of characteristic zero, set

   \[
   s=1-a,\qquad q=p-sx,\qquad
   C_f(T)=\det\!\left(T-M_{p'}\mid k[x]/(q)\right).
   \]

   The formal fixed trace multiset determines \(C_f\), and

   \[
   C_f'(s)=0.
   \]

   Thus a prescribed fixed trace multiset leaves at most \(d-1\) possible Jacobians; in degree four it leaves at most three.

2. **Exact period-\(\le 2\) failure locus.** Over \(\mathbb C\), the exact non-quasi-finite locus of

   \[
   \mathfrak T_{\le 2}:\mathcal H^1_4
   \longrightarrow
   \operatorname{Sym}^4(\mathbb C)\times
   \operatorname{Sym}^{12}(\mathbb C)
   \]

   is

   \[
   E=\{(a,p):a=1,\ p(x)=(x^2-L)^2,\ L\in\mathbb C\}.
   \]

   Its common lower trace data is

   \[
   \operatorname{Trace}_1=0^{\times 4},
   \qquad
   \operatorname{Trace}_2=2^{\times 12},
   \]

   and \(E/\mu_3\simeq\mathbb A^1_{L^3}\).

3. **Sharp period-three cutoff.** Over \(\mathbb C\), the map

   \[
   \mathfrak T_{\le 3}:\mathcal H^1_4
   \longrightarrow
   \prod_{n=1}^3\operatorname{Sym}^{p_n}(\mathbb C)
   \]

   is quasi-finite and descends to a quasi-finite map on \(\mathcal M^1_4\), whereas \(\mathfrak T_{\le 2}\) is not quasi-finite on either space. On \(E\),

   \[
   S_2^{(3)}(L)=-1296000-1572864L^3.
   \]

   Consequently \(P_{\mathcal H^1}(4)=3\) for formal pure trace data on this normalized single-factor space.

The introduction must say immediately that Cantat--Dujardin already exhibit \(E\) and its period-one/two blindness. The article's contribution is the full dependent chain: deriving the Jacobian candidates from pure traces, proving \(E\) is the exact lower failure locus, and closing the global cutoff with formal period three.

## 3. Claims--evidence matrix

Only direct proofs in the article and the verified primary sources listed below may support public claims.

| ID | Public claim | Evidence and proof vehicle | Planned location | Status in article |
|---|---|---|---|---|
| M1 | Formal trace data defines regular symmetric-product morphisms with multiplicities | Cantat--Dujardin's formal-period convention, followed by an explicit elementary-symmetric-coordinate construction | Definition 2.2 and Proposition 2.3 | Full convention and construction in main text |
| M2 | Pure fixed traces determine \(C_f\) and satisfy \(C_f'(1-a)=0\) | Direct fixed-algebra proof, including squarefree and nonreduced cases | Lemmas 3.1--3.3 and Theorem 3.4 | Complete proof in main text |
| M3 | Fixed traces leave at most \(d-1\) Jacobians, hence at most three for quartics | Degree of \(C_f'\) in characteristic zero and \(J=s-1\) | Corollary 3.5 | Complete proof in main text |
| M4 | Every period-\(\le 2\) fiber with \(a\ne 1\) is finite | M3 first; only then Cantat--Dujardin Theorem 4.2 at fixed Jacobian | Proposition 4.1 | Complete reduction in main text |
| M5 | On \(a=1\), formal period two is determined by formal period one | Direct length-\(16\) tensor-algebra computation and subtraction of the length-\(4\) formal fixed cycle | Proposition 4.2 | Complete proof in main text |
| M6 | The \([1111]\), \([31]\), and \([211]\) strata have finite fixed-trace fibers | Sugiyama only on \([1111]\); direct root-coordinate algebra on \([31]\) and \([211]\) | Propositions 5.1--5.3 | Complete proofs in main text |
| M7 | \([22]\cup[4]\) is exactly \(E\), with lower fiber \((0^4,2^{12})\), and no other lower positive-dimensional fiber exists | Direct partition and boundary analysis; Cantat--Dujardin Example 4.3 credited as direct precedent for \(E\) | Lemma 5.4, Proposition 5.5, Theorem 5.7 | Complete proof in main text |
| M8 | The raw period-three second moment on \(E\) is \(-1296000-1572864L^3\) | Complete-intersection trace--residue identity, two-term support proof, two slope certificates, and constant recurrence ledger | Propositions 6.1--6.4; Appendices A--C | Logical proof and certificate summaries in main text; full finite ledgers in appendices |
| M9 | Formal subtraction leaves pointwise length \(60\), and the cyclewise moment is \(-432000-524288L^3\) | Nilpotence on the fixed algebra and formal local elimination at multiplicities \(2\) and \(4\) | Proposition 6.5, Corollary 6.7; Appendix D | Transparent proof in main text; expanded elimination in appendix |
| M10 | \(\mathfrak T_{\le 3}\) has finite geometric fibers and is quasi-finite | M4--M9, followed by the finite-type finite-fiber criterion in Stacks Tag 02NH | Theorem 7.1 and Corollary 7.2 | Complete proof in main text |
| M11 | The quotient map is quasi-finite and the cutoff is sharply three | Direct residual action \(L\mapsto\zeta L\), finite quotient, lower curve \(E/\mu_3\), and M10 | Corollaries 7.3--7.4 | Complete proof in main text |

No claim may be supported by a computation, experiment, scan, or unverified citation. The exact coefficient tables are parts of a symbolic proof, not experimental evidence.

## 4. Page budget and section-by-section plan

The target is approximately 25 pages of mathematical content, including a half-page abstract but excluding references and appendices.

| Part | Target length | Cumulative target |
|---|---:|---:|
| Abstract | 0.5 page | 0.5 |
| §1 Introduction and unified theorem | 2.25 pages | 2.75 |
| §2 Normalized spaces, formal traces, and prior framework | 2.75 pages | 5.5 |
| §3 Pure fixed traces and the Jacobian | 3 pages | 8.5 |
| §4 Reduction to the conservative slice | 2.5 pages | 11 |
| §5 The five quartic strata and the exact exceptional fiber | 4.5 pages | 15.5 |
| §6 Formal period three on the exceptional curve | 6.5 pages | 22 |
| §7 Global quasi-finiteness, quotient, and sharpness | 2 pages | 24 |
| §8 Limitations, publication disclosure, and conclusion | 1 page | 25 |

References are expected to occupy approximately 2--3 pages. Appendices A--E are expected to occupy approximately 12--15 pages. If the main proof exceeds 25 pages, only line-by-line coefficient reductions and expanded local calculations may move to the appendices; theorem logic, hypotheses, formal multiplicities, and the input/output of every certificate must remain in the main text.

### Abstract (approximately 0.5 page; 180--230 words)

Use a compact five-part structure.

1. State the exact achievement in the first sentence: the sharp quasi-finite pure-trace cutoff is three on the single-factor normalized quartic space.
2. State the obstruction: low-period trace rigidity theorems require a fixed Jacobian, while the Jacobian-\(-1\) quartic curve has constant period-one/two traces.
3. State the bridge: the fixed-algebra identity \(C_f'(1-a)=0\) bounds the Jacobian candidates, and five root partitions identify the exact lower bad locus.
4. State the formal-period-three mechanism: a complete-intersection residue calculation gives the affine \(L^3\)-moment.
5. State the memorable guarantees, with scope: at most three quartic Jacobians, unique lower curve \(E\), and global quasi-finiteness through period three over \(\mathbb C\).

The abstract must use “quasi-finite,” not “identifies uniquely.” It should contain no citation and no absolute priority wording.

### §1. Introduction and unified theorem (approximately 2.25 pages)

**Goal.** Make the What, Why, and So What explicit before any technical preliminaries.

**Opening.** Begin with the concrete identifiability question for formal multiplier traces of a single generalized Hénon map. Avoid a generic history of polynomial dynamics.

**Prior boundary.** In one compact paragraph, explain that Cantat--Dujardin prove full trace rigidity and existence of some finite cutoff, prove fixed-Jacobian period-one/two finiteness away from Jacobian \(-1\), and exhibit the exceptional quartic family. This paragraph must distinguish the May 10, 2026 author version from arXiv v1 without suggesting a publication status that does not exist.

**Gap.** State the two missing links:

- a pure trace theorem cannot feed an unknown Jacobian into a fixed-Jacobian theorem;
- exhibiting \(E\) does not prove it is the exact lower failure locus or that period three closes every global fiber.

**Main theorem.** State Theorem 1.1 with Parts A--C exactly as above. The theorem statement itself must carry the field split, the single-factor restriction, the formal-cycle convention, and quasi-finite wording.

**Contribution bullets.** Use exactly three dependent bullets:

1. fixed-algebra Jacobian enumeration from pure fixed traces;
2. exact five-stratum classification of the period-\(\le 2\) failure locus;
3. formal period-three removal of the residual \(L^3\)-fiber and the sharp cutoff.

**Results preview.** Display

\[
C_f'(1-a)=0,\qquad
E=\{a=1,\ p=(x^2-L)^2\},\qquad
S_2^{(3)}(L)=-1296000-1572864L^3.
\]

Explain in one sentence why each formula supplies the next arrow in the proof chain.

**No hero figure.** The three displayed formulas and a short dependency paragraph are clearer than a diagram. A decorative theorem-flow figure is prohibited.

**Key citations.** Cantat--Dujardin and Friedland--Milnor.

### §2. Normalized spaces, formal traces, and prior framework (approximately 2.75 pages)

**Goal.** Fix all objects and imported theorem scopes before the new proofs begin.

**Definition 2.1 (normalized spaces).** Define \(\mathcal H^1_d\), the Jacobian \(J(f_{a,p})=-a\), the residual diagonal action

\[
(a,p(x))
\longmapsto
\left(a,\zeta^{-1}p(\zeta x)\right),
\qquad
\zeta^{d-1}=1,
\]

and \(\mathcal M^1_d=\mathcal H^1_d/\mu_{d-1}\). State explicitly that “centered” means vanishing \(x^{d-1}\)-coefficient.

**Definition 2.2 (formal trace cycles).** Reproduce the Cantat--Dujardin formal-period convention accurately. Distinguish the \(f^n\)-fixed cycle from the formal-period-\(n\) cycle, retain intersection multiplicities, and define the trace multiset as the formal eigenvalue multiset of the trace function on the finite cycle. In quartic degree, record the formal lengths

\[
p_1=4,\qquad p_2=12,\qquad p_3=60.
\]

**Proposition 2.3 (regular trace morphisms).** Explain that elementary symmetric functions of the regular trace function define

\[
\operatorname{Trace}_n:\mathcal H^1_d
\longrightarrow\operatorname{Sym}^{p_n}(\mathbb C),
\]

and hence \(\mathfrak T_{\le P}\). Give the finite-type target in elementary-symmetric coordinates; do not rely on an informal “unordered list” model.

**Definition 2.4 (cutoff).** Define \(P_{\mathcal H^1}(4)\) as the least \(P\) for which the formal pure trace map is quasi-finite on \(\mathcal H^1_4\). State that this is not an injectivity threshold.

**Lemma 2.5 (residual invariance).** Compute the diagonal conjugacy directly and prove trace invariance and descent through the finite quotient.

**Prior-work synthesis.** Organize the discussion by role, not paper by paper:

- generalized Hénon normal forms and finite normalization ambiguity;
- formal-period trace rigidity and low-period fixed-Jacobian results;
- one-variable fixed-multiplier fibers on the no-multiple-fixed-point locus;
- complete-intersection residue and formal-period methods.

State as quoted inputs, with exact hypotheses, Cantat--Dujardin Theorems 3.7 and 4.2 and Example 4.3. State Sugiyama's \(V_4\) domain. Huguin and Hutz remain contextual, not proof engines. The Stacks criterion is reserved for §7.

**Key citations.** Friedland--Milnor; Cantat--Dujardin; Sugiyama I and II; Hutz; Huguin; Cattani--Dickenstein--Sturmfels.

### §3. Pure fixed traces and the Jacobian (approximately 3 pages)

**Goal.** Prove Part A completely and eliminate the hidden-Jacobian problem before invoking any fixed-Jacobian theorem.

**Lemma 3.1 (fixed algebra and trace polynomial).** From the fixed equations derive

\[
s=1-a,\qquad q=p-sx,\qquad A_q=k[x]/(q).
\]

Compute

\[
Df=
\begin{pmatrix}
p'(x)&a\\
1&0
\end{pmatrix},
\]

so the formal fixed traces are the formal eigenvalues of multiplication by \(p'\) on \(A_q\). Conclude that pure \(\operatorname{Trace}_1\) determines the monic degree-\(d\) polynomial \(C_f(T)\).

**Lemma 3.2 (squarefree residue identity).** For monic squarefree \(q\) of degree \(d\ge 2\), prove

\[
\sum_{q(\alpha)=0}\frac1{q'(\alpha)}=0
\]

by taking the \(x^{d-1}\)-coefficient in the Lagrange interpolation identity for \(1\). Apply \(p'=q'+s\) to obtain \(C_f'(s)=0\). The proof may display the logarithmic derivative only because \(C_f(s)\ne 0\) in this squarefree case.

**Lemma 3.3 (nonreduced local factor).** If \(q\) has a root of local length \(m\ge 2\), show that \(q'\) is nilpotent in that local Artin factor. Thus multiplication by \(p'=s+q'\) has characteristic factor \((T-s)^m\), so \(C_f'(s)=0\). Do not divide by \(C_f(s)\) here.

**Theorem 3.4 (pure fixed-trace derivative identity).** Combine Lemmas 3.1--3.3 to prove \(C_f'(s)=0\) for every parameter in Part A's scope.

**Corollary 3.5 (Jacobian candidate bound).** Since \(C_f'\) is nonzero of degree \(d-1\) in characteristic zero and \(J=s-1\), a fixed trace multiset gives at most \(d-1\) Jacobian candidates. State the quartic bound as three. Never introduce the discarded count seven.

**Proof-placement rule.** Every line of this proof remains in the main text. Nothing in Part A is deferred to an appendix.

### §4. Reduction to the conservative slice (approximately 2.5 pages)

**Goal.** Use Part A to close every \(a\ne 1\) candidate and prove that, on \(a=1\), period two adds no fiber information beyond period one.

**Proposition 4.1 (finite fibers for \(a\ne 1\)).** Fix a value of \(\mathfrak T_{\le 2}\). First use Corollary 3.5 to enumerate at most three quartic values of \(a\), discarding \(a=0\) because it is outside the Hénon parameter space. For each remaining \(a\ne 1\), and only after this enumeration, apply Cantat--Dujardin Theorem 4.2 with its fixed-Jacobian input. A finite union of finite fibers is finite.

The prose must make the logical order impossible to miss:

\[
\operatorname{Trace}_1
\longrightarrow
\{a_1,a_2,a_3\}
\longrightarrow
\text{Theorem 4.2 on each candidate with }a_i\ne 1.
\]

**Proposition 4.2 (formal period two on \(a=1\)).** Set \(A_1=\mathbb C[x]/(p)\). Prove that the full \(f^2\)-fixed algebra is

\[
A_2=\mathbb C[x,y]/(p(x),p(y))\simeq A_1\otimes A_1
\]

of length \(16\), and compute

\[
\operatorname{tr}(Df^2)=2+p'(x)p'(y).
\]

If the formal eigenvalues of \(M_{p'}\) are \(r_1,\ldots,r_4\), the full \(f^2\)-fixed multiset is \(\{2+r_ir_j\}_{i,j}\). Identify the embedded length-\(4\) formal fixed cycle, with values \(2+r_i^2\), and subtract it scheme-theoretically. The resulting length-\(12\) formal period-two multiset is determined by \(\operatorname{Trace}_1\), including at nonreduced roots.

**Corollary 4.3 (remaining problem).** The period-\(\le 2\) fiber problem on \(a=1\) is exactly the fixed-trace fiber problem for monic centered quartics. This corollary sets up the five-stratum proof.

### §5. The five quartic strata and the exact exceptional fiber (approximately 4.5 pages)

**Goal.** Exhaust the entire \(a=1\) slice and prove that \(E\) is the exact, not merely an exhibited, positive-dimensional lower fiber.

**Proposition 5.1 (the \([1111]\) stratum).** Put \(h=x+p\). At each simple root \(\alpha\) of \(p\), verify

\[
h'(\alpha)=1+p'(\alpha)\ne 1.
\]

Invoke Sugiyama only here, on \(V_4\), to get finite fibers in polynomial moduli. Explain why the residual monic-centered normalization contributes only finitely many representatives.

**Proposition 5.2 (the \([31]\) stratum).** Write

\[
p=(x-r)^3(x+3r),\qquad
\operatorname{Trace}_1=\{0,0,0,-64r^3\}.
\]

Show directly that prescribed trace data leaves finitely many \(r\), including the \(r=0\) boundary.

**Proposition 5.3 (the \([211]\) stratum).** With roots \(r,r,r+u,r+v\) and \(4r+u+v=0\), compute

\[
A=u^2(u-v),\qquad
B=-v^2(u-v),\qquad
\frac BA=-\left(\frac vu\right)^2.
\]

After choosing one of the two orderings of \(A,B\), recover finitely many values of \(v/u\), then \(u^3\), then \(u,v,r\). State every nonvanishing condition and keep the finite ordering ambiguity explicit.

**Lemma 5.4 (closure relations).** Verify separately that \(u=0\) or \(v=0\) lands in \([31]\), \(u=v\ne 0\) lands in \([22]\), and \(u=v=0\) lands in \([4]\). This lemma prevents a boundary component from escaping the classification.

**Proposition 5.5 (the \([22]\) and \([4]\) strata).** Prove

\[
[22]\cup[4]
=
\{p=(x^2-L)^2:L\in\mathbb C\}.
\]

Show both directions: centering makes two double roots opposite, and fixed trace \(0^{\times 4}\) forces every root to be multiple, leaving only these two partitions. Use Proposition 4.2 to obtain the exact common lower fiber \((0^{\times 4},2^{\times 12})\).

**Lemma 5.6 (residual quotient on \(E\)).** Compute

\[
\zeta^{-1}(\zeta^2x^2-L)^2=(x^2-\zeta L)^2,
\qquad
\zeta^3=1,
\]

so \(L\mapsto\zeta L\) and \(E/\mu_3\simeq\mathbb A^1_{L^3}\).

**Theorem 5.7 (exact lower non-quasi-finite locus).** Combine Proposition 4.1 and Propositions 5.1--5.5. For the displayed lower trace value, also use \(C_f(T)=T^4\) and \(C_f'(s)=4s^3\) to force \(s=0\), hence \(a=1\); this rules out an unseen \(a\ne 1\) component. Apply the pointwise finite-type criterion to conclude that every point outside \(E\) is a quasi-finite point and every point of \(E\) is not.

**Optional Table 1 (non-evidentiary).** If a later publication stage authorizes it, include one compact mathematical table with columns: root partition, centered parameterization, nonzero fixed traces, finiteness argument, and boundary. It summarizes Propositions 5.1--5.5 but proves nothing. It must not replace any formula or proof paragraph.

### §6. Formal period three on the exceptional curve (approximately 6.5 pages)

**Goal.** Give enough proof in the main article to establish the exact affine \(L^3\)-moment with formal multiplicities. Appendices expand finite ledgers but do not hide a logical step.

Put

\[
p_L(x)=(x^2-L)^2,\qquad q_L(x)=4x(x^2-L),
\]

and introduce cyclic variables and a bookkeeping parameter:

\[
F_i=(x_i^2-L)^2+\varepsilon(x_{i-1}-x_{i+1}),
\]

\[
t_\varepsilon
=
q_0q_1q_2+\varepsilon^2(q_0+q_1+q_2),
\qquad
q_i=4x_i(x_i^2-L).
\]

**Proposition 6.1 (rank, Jacobian, and trace--residue bridge).** Prove that the leading monomials \(x_0^4,x_1^4,x_2^4\) give a monic free quotient of rank \(64\), with standard monomials \(0\le e_i<4\). Check the cyclic signs directly and show that \(t_\varepsilon\) is the complete-intersection Jacobian. At \(\varepsilon=1\), multiply the three derivative matrices and show that the same element is \(\operatorname{tr}(Df_L^3)\). Invoke the classical quotient trace--residue identity in the exact form

\[
\operatorname{Tr}(M_h)=\operatorname{Res}(h\,t_\varepsilon).
\]

For \(h=t_\varepsilon^2\), emphasize the exponent:

\[
\operatorname{Tr}(M_{t_\varepsilon^2})
=
\operatorname{Res}(t_\varepsilon^3).
\]

This proposition is the transparent bridge from the formal nonreduced \(f^3\)-fixed algebra to a coefficient calculation; it must not be replaced by a reduced-point sum.

**Lemma 6.2 (two-term support).** Assign weights

\[
\operatorname{wt}(x_i)=1,\qquad
\operatorname{wt}(L)=2,\qquad
\operatorname{wt}(\varepsilon)=3.
\]

First derive the four candidates

\[
\varepsilon^6,\qquad
L^3\varepsilon^4,\qquad
L^6\varepsilon^2,\qquad
L^9.
\]

Remove \(L^9\) at \(\varepsilon=0\) using the separated double-root algebra and \(q_i^2=0\). Remove \(L^6\varepsilon^2\) over \(L\ne 0\) by writing \(x_i=\alpha_i+\delta_i\), \(\alpha_i^2=L\), and treating the only two root-cluster types:

- exactly two \(\alpha_i\) agree, giving two \(q_i\)-valuations \(1/2\), the third at least \(3/4\), and \(v(t_\varepsilon)\ge 7/4\);
- all three agree, giving \(v(t_\varepsilon)\ge 3\) on every nontrivial branch.

Then isolate the diagonal fixed branch and use the nilpotence argument in Proposition 6.5 to show its second-moment contribution is zero. Explain why the finite-algebra trace sums support values with local lengths and kills nilpotent parts, so no \(\varepsilon^2\) coefficient survives. Extend from \(L\ne 0\) to all \(L\) polynomially. Conclude

\[
S_2(L,\varepsilon)
=
C_2\varepsilon^6+D_2L^3\varepsilon^4.
\]

**Proposition 6.3 (slope coefficient).** Present two independently replayable certificates.

1. Define the finite \(H/A\) sums used at \(m=2\), calculate

   \[
   H(2,1)=2,\qquad A_{2,2}=-2,\qquad A_{2,1}=0,
   \]

   and conclude \(D_2=3\cdot4^9(-2)=-1572864\).

2. Starting from the quartic residue itself, state the Laurent functionals \(\rho_{n,h}(e)\), display every nonzero \(\rho_{3,h}(e)\) needed, and show that the only denominator-increment pattern is the three cyclic placements of \((2,1,1)\), each contributing \(-2\). Record the vanishing of the \(j=1,2,3\) alternatives and conclude independently that

   \[
   D_2=4^9(-6)=-1572864.
   \]

The main text must include the definitions, nonzero-value table, and final arithmetic. Appendix A gives the first certificate line by line; Appendix B gives every Laurent expansion and sign.

**Proposition 6.4 (constant coefficient).** At \(L=0,\varepsilon=1\), define \(R(e_0,e_1,e_2)\) as the top-standard-monomial coefficient. Display the three exact reduction recurrences and the seven exponent-pattern values, including

\[
R(9,9,9)=-6,\qquad
R(9,6,6)=2,\qquad
R(6,6,3)=-1.
\]

Group the six contribution types to \(t^3\) and show in the main text

\[
-1572864+294912-18432+384=-1296000.
\]

Appendix C contains every terminating reduction path. The main text must explain why the recurrences reduce total exponent and therefore certify, rather than merely sample, the coefficient.

**Proposition 6.5 (formal fixed subtraction and local length).** On the fixed algebra \(\mathbb C[x]/((x^2-L)^2)\), prove \(q^2=0\) and hence

\[
t_\varepsilon=q^3+3\varepsilon^2q,\qquad
t_\varepsilon^2=0.
\]

Thus the formal fixed contribution to the second moment vanishes. For a root \(\alpha\) of multiplicity \(r=2\) or \(4\), introduce

\[
\delta=x_0-\alpha,\qquad
u=x_1-x_0,\qquad
v=x_2-x_0.
\]

Show that the transverse \((u,v)\)-Jacobian is invertible and formally eliminate \(u,v\), leaving

\[
3p_L(\alpha+\delta)+O(\delta^{2r-1}),
\]

of exact order \(r\). This proves that the \(f^3\)-fixed local length equals the fixed-scheme length and that no fixed support remains after formal subtraction. Keep this argument in the main text; Appendix D expands the formal substitutions.

**Theorem 6.6 (pointwise formal period-three moment).** Combine Propositions 6.1--6.5 to obtain

\[
S_2^{(3)}(L)=-1296000-1572864L^3.
\]

State explicitly that this is the second power sum on the pointwise formal period-three zero-cycle, after fixed-cycle subtraction.

**Corollary 6.7 (length and cyclewise normalization).** The full \(f^3\)-fixed scheme has length \(64\), the fixed scheme has length \(4\), and the formal period-three scheme has pointwise length \(60\). Only after this subtraction, use three points per orbit to divide the moment by three:

\[
-432000-524288L^3.
\]

Do not mix pointwise and cyclewise normalization anywhere earlier.

### §7. Global quasi-finiteness, quotient, and sharpness (approximately 2 pages)

**Goal.** Convert the local exceptional-curve separator into the global theorem without adding an injectivity claim.

**Theorem 7.1 (finite geometric fibers through period three).** Fix a full value of \(\mathfrak T_{\le 3}\) and forget period three.

- If the lower fiber is outside \(E\), Theorem 5.7 already makes it finite.
- If the lower value is \((0^{\times 4},2^{\times 12})\), use \(C_f(T)=T^4\) and \(C_f'(s)=4s^3\) to force \(a=1\), then Proposition 5.5 to identify the entire lower fiber as \(E\).
- On \(E\), equality of full formal period-three multisets implies equality of second power sums, hence

  \[
  L^3=M^3.
  \]

  This leaves finitely many normalized representatives and one quotient coordinate.

Conclude that every geometric fiber is finite.

**Corollary 7.2 (quasi-finiteness).** Model the trace target as a finite product of affine symmetric products. Since source, target, and morphism are of finite type and the geometric fibers are finite, apply Stacks Project Tag 02NH to prove that \(\mathfrak T_{\le 3}\) is quasi-finite.

**Corollary 7.3 (finite quotient).** Use the explicit \(\mu_3\)-invariance and finite quotient to prove the descended map on \(\mathcal M^1_4\) has finite geometric fibers and is quasi-finite. Give the quotient-fiber argument directly; do not cite fpqc descent to widen the field.

**Corollary 7.4 (sharpness).** Period two is not quasi-finite because it contracts \(E\), and the quotient period-two map contracts \(E/\mu_3\simeq\mathbb A^1_{L^3}\). Period three is sufficient by Corollaries 7.2--7.3. Therefore the quasi-finite cutoff is sharply three.

### §8. Limitations, publication disclosure, and conclusion (approximately 1 page)

**Limitations paragraph.** State the scope boundaries plainly:

- the global theorem is complex and quartic;
- it treats one normalized Hénon factor;
- it establishes quasi-finiteness but not injectivity, degree, or a branch locus;
- it does not give a positive-characteristic or all-degree cutoff;
- its one explicit period-three moment separates only \(E\).

**Mandatory publication-overlap disclosure.** Include an explicit paragraph with the following substance:

> Paper15 fully absorbs Paper12's overlapping theorem and proof. They cannot be submitted as parallel papers. Any publication path must use the unified Paper15 treatment or withdraw the overlapping Paper12 claim.

This disclosure is mandatory even though the article assigns no novelty credit to the absorbed exceptional-curve classification or coefficient ledger.

**Conclusion.** Restate the proof chain in new words: formal fixed traces first turn an unknown Jacobian into a finite list, the quartic boundary analysis isolates one lower-period curve, and a formal period-three residue moment makes that last coordinate finite. End with the exact scoped conclusion \(P_{\mathcal H^1}(4)=3\), not a claim about all degrees or all Hénon automorphisms.

## 5. Main-text versus appendix proof placement

No theorem may have only a proof sketch in the main text. The appendices expand finite arithmetic and formal substitutions; they do not supply a missing logical implication.

| Result | Mandatory main-text content | Appendix expansion |
|---|---|---|
| Formal trace morphisms | Formal-cycle convention, multiplicities, symmetric-product coordinates, regularity | Appendix E may record auxiliary coordinate details only |
| \(C_f'(s)=0\) | Entire squarefree and nonreduced proof | None |
| Cantat--Dujardin reduction | Jacobian enumeration before theorem invocation and finite-union argument | None |
| Period two on \(a=1\) | Length \(16\), trace element, length-\(4\) subtraction, length \(12\) conclusion | Appendix E may spell out the embedded-cycle map |
| Five quartic strata | All parameterizations, formulas, finite recovery, and boundary cases | None |
| Complete-intersection bridge | Rank \(64\), cyclic signs, equality of Jacobian and derivative trace, and \(\operatorname{Tr}(M_{t^2})=\operatorname{Res}(t^3)\) | Appendix E may give matrix multiplication details |
| Two-term support | Weight equation, \(L^9\) removal, both Puiseux cluster cases, diagonal zero, continuation to \(L=0\) | Appendix E gives expanded valuation bookkeeping |
| Slope \(D_2\) | Definitions and decisive values for both certificates; exact agreement | Appendix A: full \(H/A\) certificate; Appendix B: full tensor--Laurent ledger |
| Constant \(C_2\) | Recurrences, exponent-pattern table, grouped contributions, exact sum | Appendix C: every terminating recurrence path |
| Formal subtraction and length | \(q^2=0\), \(t^2=0\), transverse Jacobian, exact order \(r\), length \(60\), delayed division by three | Appendix D: full local expansions for \(r=2,4\) |
| Global quasi-finiteness | Exact two-case fiber proof, finite-type criterion, quotient, and sharpness | None |

### Appendix A. First finite slope certificate (approximately 2 pages)

Reproduce the finite definitions of \(H(r,k)\), \(A_{m,r}\), and the specialized coefficient expression. List all admissible pairs for \(H(2,1)\), prove \(A_{2,2}=-2\) and \(A_{2,1}=0\), and show every power of four and combinatorial factor leading to \(D_2=-1572864\). Do not state or suggest an all-\(m\) theorem beyond what is needed for the quartic certificate.

### Appendix B. Tensor--Laurent slope ledger (approximately 3 pages)

Expand \(1/(P_i+\varepsilon\Lambda_i)\), define every \(\rho_{n,h}(e)\) and \(\mu_n\), list all values used, and give all cyclic signs and multiplicities. Prove \(\mathcal C_{2,0}=-6\), prove the \(j=1\) and \(j=2\) terms vanish for the stated negative-power reasons, and exclude \(j=3\) by \(\varepsilon\)-degree. End by comparing this route with Appendix A.

### Appendix C. Normal-form constant ledger (approximately 3--4 pages)

State the three reduction recurrences, prove termination by total exponent, and show every path producing the seven exponent-pattern values. Expand the six groups in \(t^3\), including cyclic and permutation multiplicities, and verify \(C_2=-1296000\) line by line.

### Appendix D. Formal period-three subtraction and local lengths (approximately 2--3 pages)

Give the fixed-algebra nilpotence calculation and the complete formal elimination in \((\delta,u,v)\) at root multiplicities \(2\) and \(4\). Verify the transverse Jacobian, error order \(2r-1\), exact remaining order \(r\), and the pointwise-to-cyclewise normalization. This appendix corresponds to the absorbed local formal-period proof and must not rely on reduced support.

### Appendix E. Auxiliary convention and valuation details (approximately 2--3 pages)

Collect only supporting expansions: elementary-symmetric target coordinates, the embedded formal fixed-cycle map in period two, the three-matrix trace multiplication, and the complete Puiseux valuation branches used in Lemma 6.2. This appendix may shorten exposition but cannot introduce a new assumption or theorem.

## 6. Notation plan

Use one symbol for each object throughout.

| Symbol | Meaning | Restriction |
|---|---|---|
| \(f_{a,p}\) | \((x,y)\mapsto(ay+p(x),x)\) | Single factor only |
| \(J(f)\) | \(-a\) | Never treated as supplied trace data |
| \(s\) | \(1-a=1+J(f)\) | Used in Part A |
| \(q\) | \(p-sx\) in Part A | Use \(q_L=p_L'\) only with the subscript to avoid collision |
| \(C_f(T)\) | Characteristic polynomial of multiplication by \(p'\) on \(k[x]/(q)\) | Determined by formal fixed traces |
| \(\operatorname{Trace}_n\) | Formal-period-\(n\) trace multiset | Always includes scheme multiplicity |
| \(\mathfrak T_{\le P}\) | Tuple of trace multisets through period \(P\) | Pure trace map |
| \(\mathcal H^1_d\) | Monic-centered single-factor parameter space | Not a composition space |
| \(\mathcal M^1_d\) | Finite quotient \(\mathcal H^1_d/\mu_{d-1}\) | Do not call it a fine moduli space without proof |
| \(E\) | \(a=1,\ p=(x^2-L)^2\) | Known exceptional curve |
| \(S_2^{(3)}\) | Pointwise formal period-three second power sum | Distinguish from cyclewise moment |
| \(F_i,t_\varepsilon\) | Period-three complete-intersection equations and Jacobian/trace element | Cyclic indices modulo \(3\) |

Terminology must remain stable: “formal period,” “trace multiset,” “geometric fiber,” “quasi-finite,” “normalized representative,” and “residual quotient.” Do not alternate these with “exact period,” “multiplier list,” “unique reconstruction,” or “moduli identification” unless the distinction is explicitly proved.

## 7. Citation plan and version controls

Bibliographic data must be transcribed from the verified primary records at the manuscript stage; no citation is to be generated from memory. The following records and roles are fixed, with no temporary citation markers.

1. **Serge Cantat and Romain Dujardin, “Multiplier rigidity for complex Hénon maps.”** Use the 51-page author PDF dated May 10, 2026 as the controlling text; identify arXiv:2603.09445 v1 as an earlier, byte-distinct version. Cite §§3.1--3.2 for formal trace conventions, Theorem 3.7 only for existence of an unspecified finite cutoff, Theorem 4.2 only over \(\mathbb C\) with fixed Jacobian and \(a\ne 1\), and Example 4.3 for the known exceptional quartic family and period-one/two blindness. Do not imply a journal publication.
2. **Toshi Sugiyama, “The Moduli Space of Polynomial Maps and Their Fixed-Point Multipliers,” Advances in Mathematics 322 (2017), 132--185, DOI 10.1016/j.aim.2017.10.013.** Cite only for finite fixed-multiplier fibers on \(V_4\), the simple-root \([1111]\) stratum.
3. **Toshi Sugiyama, “The Moduli Space of Polynomial Maps and Their Fixed-Point Multipliers: II. Improvement to the Algorithm and Monic Centered Polynomials,” Ergodic Theory and Dynamical Systems, online February 3, 2023, DOI 10.1017/etds.2022.120.** Use only to clarify monic-centered normalization on the same no-multiple-fixed-point domain.
4. **Shmuel Friedland and John Milnor, “Dynamical properties of plane polynomial automorphisms,” Ergodic Theory and Dynamical Systems 9(1) (1989), 67--99, DOI 10.1017/S014338570000482X.** Cite for generalized Hénon normal-form background and finite residual ambiguity, not for any new lemma.
5. **Eduardo Cattani, Alicia Dickenstein, and Bernd Sturmfels, “Computing Multidimensional Residues,” Progress in Mathematics 143 (1996), 135--164, DOI 10.1007/978-3-0348-9104-2_8.** Cite for the classical complete-intersection residue and quotient-trace method.
6. **Benjamin Hutz, “Dynatomic cycles for morphisms of projective varieties,” New York Journal of Mathematics 16 (2010), 125--159.** Cite as formal-period background only; the operative convention remains Cantat--Dujardin's.
7. **Valentin Huguin, “Moduli spaces of polynomial maps and multipliers at small cycles,” arXiv:2412.19335.** Cite as adjacent one-variable small-cycle work, not as a theorem about the Jacobian-\(-1\) Hénon slice.
8. **The Stacks Project, Tag 02NH.** Cite for the finite-type finite-fiber criterion for quasi-finiteness. Do not use Tag 02VI to claim descent of Parts B--C beyond \(\mathbb C\).

Section allocation:

- §1: Cantat--Dujardin; Friedland--Milnor.
- §2: all background records, organized by theorem role.
- §3: no external theorem beyond the elementary algebra proved in place.
- §4: Cantat--Dujardin Theorem 4.2, after Corollary 3.5.
- §5: Sugiyama I and II only in Proposition 5.1; Cantat--Dujardin Example 4.3 when crediting \(E\).
- §6: Cattani--Dickenstein--Sturmfels for the residue identity; no citation substitutes for the coefficient proof.
- §7: Stacks Tag 02NH.
- §8: no priority language; citations only when restating the known boundary.

The literature statement must be conservative: a bounded primary-source search through 2026-08-17 found no indexed statement of the unified three-part result. The article must not turn this into “first,” “newly discovered exceptional family,” or an assertion about unpublished work.

## 8. Figure and table plan

**Figures:** none. The proof dependency is short enough to state as one displayed implication chain, and the paper has no empirical or geometric visualization that would justify a hero figure.

**Empirical tables:** none. There are no experiments, datasets, baselines, metrics, or numerical results.

**Conditional mathematical table:** at most one in-text table summarizing the five quartic root partitions. It is non-evidentiary and conditional on later publication authorization. Its caption should say that the table is a roadmap to the complete proofs in §5. It must use no color, external asset, or generated data.

The coefficient ledgers in §6 and Appendices A--C are proof tables, not empirical result tables. They should be typeset directly from the exact symbolic derivation if manuscript writing is later authorized.

## 9. Risks and mandatory controls

| Risk | Consequence | Required control in the article |
|---|---|---|
| Treating the Jacobian as known | Destroys the pure-trace theorem | Put Theorem 3.4 and Corollary 3.5 before every use of Cantat--Dujardin Theorem 4.2 |
| Dividing by \(C_f(s)\) in the nonreduced case | Invalid proof at multiple fixed points | Use the local factor \((T-s)^m\), \(m\ge 2\) |
| Applying Sugiyama to a singular stratum | Exceeds \(V_4\) | Confine it to Proposition 5.1 and prove \([31]\), \([211]\), \([22]\), and \([4]\) directly |
| Omitting a root-partition boundary | Could leave an unclassified lower fiber | State Lemma 5.4 and check all four boundary patterns |
| Replacing formal cycles by reduced points | Invalidates multiplicities and lengths | Work with finite algebras, characteristic polynomials, and scheme-theoretic subtraction throughout |
| Using the wrong residue exponent | Changes the period-three moment | Derive \(\operatorname{Tr}(M_{t^2})=\operatorname{Res}(t^3)\) explicitly |
| Sign or multiplicity error in \(D_2\) | Breaks the nonzero slope | Retain two independent exact certificates and require exact agreement |
| Arithmetic error in \(C_2\) | Corrupts the displayed moment | State recurrences, termination, pattern table, and six grouped contributions |
| Dividing by three before formal subtraction | Confuses pointwise and cyclewise moments | Prove length \(64-4=60\) first; divide only in Corollary 6.7 |
| Calling a finite-fiber statement injective | Overclaims the theorem | Use “quasi-finite” consistently and state non-injectivity as an open possibility |
| Treating one moment as a global classifier | Overstates the calculation | Use it only after the lower fiber has been proved to be exactly \(E\) |
| Widening Parts B--C beyond \(\mathbb C\) | Exceeds verified source scope | Keep the field split in Theorem 1.1 and every corollary |
| Parallel publication of overlapping versions | Creates publication overlap | Include the mandatory Paper12/Paper15 disclosure in §8 |

## 10. Scope exclusions and nonclaims

The manuscript must not claim any of the following.

1. The Jacobian is supplied to the pure trace map.
2. The trace map is injective, globally unique, or generically degree one.
3. An exact fiber cardinality, map degree, generic degree, or branch divisor is known.
4. The theorem covers degree-four compositions, arbitrary loxodromic polynomial automorphisms, an unnormalized space, or a multifactored moduli problem.
5. Parts B--C hold over every algebraically closed characteristic-zero field.
6. A positive-characteristic analogue holds.
7. Reduced periodic points may replace formal-period zero-cycles.
8. Cantat--Dujardin's general rigidity, unspecified cutoff, exceptional family, or lower-period blindness is new here.
9. Residue identities, Friedland--Milnor normal forms, Sugiyama, Huguin, fixed-point identities, or formal dynatomic methods are new here.
10. The absorbed exceptional-curve classification, formal subtraction, coefficient ledgers, or period-three moment receives new novelty credit merely by appearing in this unified article.
11. \(P(d)=3\) for all degrees, an effective all-degree cutoff, or universal nonvanishing of a coefficient family has been proved.
12. The period-three second power sum classifies all of \(\mathcal H^1_4\).
13. A computation, CAS run, parameter scan, experiment, or numerical check is theorem evidence.
14. The article has absolute priority or rules out unpublished work.

## 11. Anonymity and publication-overlap rules

- Use an anonymous author block until a later publication decision explicitly changes it.
- Include no author names, affiliations, acknowledgments, grants, self-identifying links, or self-identifying prose.
- Keep the public article free of internal process metadata and unpublished operational details.
- Cite public prior work neutrally. Do not fabricate a public citation for a non-public development artifact.
- Preserve the mandatory Paper12/Paper15 overlap disclosure in §8 and in any editor-facing cover material. The unified article is the only admissible external vehicle for the overlapping central theorem and proof.
- A venue has not been selected. Do not add a venue name, page-limit claim, checklist, broader-impact section, or template-specific boilerplate.

## 12. Fresh plan-review checklist

Before any manuscript authorization, a fresh independent reviewer should check all of the following against this plan.

1. The title is exactly **Low-Period Trace Fibers of Quartic Generalized Hénon Maps**.
2. The one-sentence contribution contains the full dependent chain and does not reduce the story to the naked cutoff.
3. Part A is characteristic-zero algebraic, while Parts B--C remain over \(\mathbb C\).
4. The article covers only \(\mathcal H^1_4\) and its finite residual quotient in the global theorem.
5. Formal trace targets, degrees \(4,12,60\), and nonreduced multiplicities are explicit.
6. The fixed-algebra proof appears completely in the main text.
7. Cantat--Dujardin Theorem 4.2 appears only after Jacobian enumeration and only for \(a\ne 1\).
8. Sugiyama is used only on \([1111]\), and the remaining four partitions are direct proofs.
9. Every \([211]\) ordering and boundary is represented.
10. The exact period-two fiber and exact non-quasi-finite locus are proved, not inferred from the known example.
11. The main text explains rank \(64\), cyclic signs, the trace--residue exponent, two-term support, and formal subtraction.
12. Both slope routes and the constant ledger have clear main-text inputs and outputs, with complete Appendices A--C.
13. The local-length proof handles multiplicities \(2\) and \(4\), yields length \(60\), and delays division by three.
14. Finite geometric fibers, finite type, the \(\mu_3\) quotient, and sharpness are separate logical steps.
15. The citation version distinctions and theorem scopes match the primary records, with no unresolved citation marker.
16. The limitations and fourteen anti-claims are respected.
17. The Paper12/Paper15 overlap paragraph is mandatory and unambiguous.
18. No figure, empirical table, experiment, computation, or unsupported priority language has entered the plan.

## 13. Later-stage permission fence

This plan authorizes no manuscript text, LaTeX source, bibliography file, figure, table asset, code, scientific execution, result, compilation, submission, upload, or external release. The optional five-stratum table remains conceptual and must not be created at this stage.

If the fresh plan review finds a proof-placement, citation-scope, page-budget, anonymity, or overlap problem, the plan must be revised before any later stage. A coefficient or formal-multiplicity conflict is a mathematical blocker; it may not be hidden in an appendix or repaired by a computational check.

Only after a fresh independent paper-plan review passes, and only under a separate authorization, may manuscript drafting be considered.

**Next required action: obtain a fresh independent review of this paper plan before authorizing any manuscript artifact.**
