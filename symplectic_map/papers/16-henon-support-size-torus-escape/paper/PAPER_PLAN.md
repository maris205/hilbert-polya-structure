# Paper Plan

## Article identity

**Title:** *Support Size and Finite-Rank Torus Escape for Generalized Hénon Maps*

**One-sentence contribution:** We prove that, for generalized Hénon maps with a nonzero constant term, increasing the actual nonconstant support from one monomial to at least two lowers the sharp coefficient-uniform finite-rank torus-survival threshold from four transitions to two, with explicit cardinality bounds and matching shorter-window rank-one families.

**Article type:** Pure-mathematics theorem paper.

**Contribution hierarchy:**

1. PC1 is the dominant result: actual support size \(s\ge 2\) gives an explicit uniform bound already for \(T_2\).
2. PC2 is the matching sharpness result: for every prescribed support with \(s\ge 2\), a rational rank-one example has infinite \(T_1\).
3. PC3 is a fully reproduced but subordinate comparison: support one has a uniform \(T_4\) bound and a rank-one example with infinite \(T_3\).

**Evidence type:** Complete symbolic proofs. There are no experiments, computational results, data, or figures.

**Content target:** 25.0 mathematical-content pages excluding references: 22.0 pages from the abstract through Section 8 and 3.0 pages across Appendices A--C. The acceptable range is 24--26 pages excluding references.

## Claims--evidence matrix

| Claim | Exact evidence | External proof dependency | Planned location | Status |
|---|---|---|---|---|
| Sparse-image lemma | Rank-\(2r\) tuple, Amoroso--Viada nondegenerate count, degree-\(d\) power fiber, all \(2^q-q-2\) degenerate proper subsets, and torsion audit | Amoroso--Viada, Theorem 6.2 | Section 4 | Complete proof in main text |
| PC1 | Rank-\(3r\) first-local count; exhaustive GZ/GU/R0/R1 analysis; endpoint, coefficient-coset, vertical-cancellation, and simultaneous-label checks; exact \(\mathcal M(\mathbf e)\) budget | Amoroso--Viada only, through the sparse-image lemma and local nondegenerate count | Section 5 | Dominant theorem; complete proof in main text |
| PC2 | \(a=b_j=1\), \(c=-s\), \(\Gamma=\langle2\rangle\), and \((1,2^n)\mapsto(2^n,1)\) | None | Section 6 | Direct sharpness proof |
| Essential hypotheses | Explicit infinite \(T_2\) families when \(c=0\) or \(a=0\), plus the actual-collected-support convention | None | Section 6 | Direct counterexamples |
| PC3 | Four rank-\(3r\) local counts; complete A/B/C nine-transition table; BA, CB, and CBA closure; \(3^4d^2\) union; rank-one \(T_3\) family | Amoroso--Viada only for the nondegenerate local count | Section 7 | Subordinate comparison; complete proof in main text |
| Exact phase transition | PC1+PC2 give the threshold \(2\) for \(s\ge2\); PC3 gives the threshold \(4\) for \(s=1\) | No new dependency beyond the preceding theorems | Sections 1 and 8 | Main conceptual conclusion |

## Narrative and notation rules

- The paper sells one mathematical fact: actual support size changes the exact finite-window threshold.
- The abstract and first page state the support-size phase transition before introducing the proof machinery.
- PC1 receives the first theorem display, the largest proof allocation, and the first contribution bullet.
- PC2 appears immediately after PC1 as the reason the two-transition result is exact.
- PC3 is framed as the necessary one-support comparison, not as a coequal headline.
- The paper consistently uses \(s\) for actual collected nonconstant support, \(d=e_s\) for degree, \(r\) for group rank, and \(m\) for the number of transitions.
- The constants are always denoted
  \[
  \mathcal A(q,R),\qquad
  \mathcal S_q(d,r),\qquad
  \mathcal S_*,\qquad
  \mathcal M(\mathbf e).
  \]
- Coefficients remain fixed scalars in unit equations. They are never folded into the variable group or tacitly assumed to lie in \(\Gamma\).
- Every theorem carries all nonvanishing, characteristic, support, and finite-rank hypotheses.
- Appendices are audit redundancy only. Deleting Appendices A--C must leave every theorem proof logically complete.

## Detailed page budget

| Component | Target pages | Hard content requirement |
|---|---:|---|
| Abstract | 0.50 | Main bound, sharp \(T_1\) obstruction, support-one contrast, proof mechanism |
| Section 1: Introduction and main results | 2.00 | What/why/so-what, all three theorem statements, contribution hierarchy |
| Section 2: Arithmetic-dynamical context | 1.50 | Exact literature roles without a priority claim |
| Section 3: Setup and quantitative unit equations | 2.00 | Map, inverse, \(T_m\), scalar recurrence, ranks, AV field bridge |
| Section 4: Sparse polynomial images in finite-rank tori | 2.75 | Entire sparse-image lemma, degenerate subsums, torsion |
| Section 5: Two-transition finiteness for \(s\ge2\) | 5.00 | Entire PC1 proof and exact component budget |
| Section 6: Sharpness and essential hypotheses | 1.50 | PC2, \(c=0\), \(a=0\), collected support |
| Section 7: The complete support-one comparison | 5.25 | Entire PC3 proof, nine table, all free-chain closures, sharpness |
| Section 8: Phase transition, limitations, and conclusion | 1.50 | Exact synthesis, explicit nonclaims, required publication-relation paragraph |
| Appendix A: Rank and power-fiber audit | 1.00 | Redundant expanded checks only |
| Appendix B: PC1 subset and component ledger | 1.00 | Redundant expanded checks only |
| Appendix C: Support-one continuation ledger | 1.00 | Redundant expanded checks only |
| **Total excluding references** | **25.00** | Within the 24--26 page target |

The page budget is feasible because the main text uses four compact proof tables for exact branch ledgers, while all motivation and literature positioning remain prose. No essential argument is shortened to “routine” or deferred to an appendix.

## Front matter

### Abstract — 0.50 page

Use a compact five-part abstract of roughly 180--220 words.

1. **Result first:** state that actual support \(s\ge2\) gives uniform finiteness after two transitions for arbitrary characteristic-zero fields and arbitrary finite-rank subgroups.
2. **Exact quantitative statement:** display or state inline
   \[
   \#T_2(H,\Gamma)
   \le
   d\mathcal A(s+2,3r)+\mathcal M(\mathbf e)\mathcal S_*.
   \]
3. **Why the proof is nontrivial:** the obstacle is the full vanishing-proper-subsum locus, not the nondegenerate unit equation.
4. **Method:** explain that each degeneracy is either a multi-term sparse graph or a finite vertical root fiber closed by the second recurrence.
5. **Sharp conclusion:** state infinite rank-one \(T_1\) examples for every prescribed \(s\ge2\) support and contrast them with the one-support \(T_4/T_3\) threshold.

The abstract must not contain citations, provenance discussion, publication history, a priority claim, or any of the excluded generalizations.

## Eight-section main-text structure

## 1. Introduction and main results — 2.00 pages

### 1.1 Opening problem and finite-window viewpoint

- Open with the precise phenomenon: a multiplicative subgroup is closed under multiplication but not addition, so a generalized Hénon recurrence need not preserve \(\Gamma^2\).
- Introduce the all-initial-state finite-window question rather than a fixed-orbit return-time question.
- Explain immediately that the number of actual nonconstant monomials changes the shortest uniform finite window.
- Avoid a generic arithmetic-dynamics opening and avoid any “first” or priority language.

### 1.2 Formal setup in light notation

State, before the main results,

\[
1\le e_1<\cdots<e_s=d,\qquad
P(X)=c+\sum_{j=1}^s b_jX^{e_j},
\]

\[
H(x,y)=(P(x)+ay,x),
\qquad
a,c,b_1,\ldots,b_s\in K^*,
\]

where \(K\) has characteristic zero and \(\Gamma\le K^*\) has finite rank \(r\), without a finite-generation assumption.

Define

\[
T_m(H,\Gamma)
=
\{Q\in\Gamma^2:H^j(Q)\in\Gamma^2\text{ for }0\le j\le m\}.
\]

Say explicitly that \(T_m\) records \(m\) transitions and \(m+1\) states. In particular, \(T_2\) contains three states, whereas \(T_4\) contains five.

### 1.3 Main theorem PC1

Define only the constants needed to read the theorem:

\[
\mathcal A(q,R)=(8q)^{4q^4(q+R+1)},
\]

\[
\mathcal S_q(d,r)
=d\bigl(\mathcal A(q,2r)+2^q-q-2\bigr),
\qquad
\mathcal S_*=\max_{2\le q\le s+1}\mathcal S_q(d,r),
\]

and

\[
\mathcal M(\mathbf e)
=
2(2^s-1)
+\sum_{\substack{J\subseteq[s]\\|J|\ge2}}
(e_{\max J}-e_{\min J})
+\sum_{\varnothing\ne J\subseteq[s]}e_{\max J}.
\]

State PC1 prominently:

\[
\boxed{
\#T_2(H,\Gamma)
\le
d\mathcal A(s+2,3r)
+\mathcal M(\mathbf e)\mathcal S_*
}
\qquad(s\ge2).
\]

The subset sums define \(\mathcal M(\mathbf e)\); no closed form replaces this definition.

### 1.4 Sharpness PC2 and support-one comparison PC3

State PC2 next: for every prescribed support \(1\le e_1<\cdots<e_s\) with \(s\ge2\), rational nonzero coefficients and a rank-one subgroup give infinite \(T_1\).

Then state the subordinate support-one comparison:

\[
\#T_4(H,\Gamma)
\le
4d\mathcal A(3,3r)+81d^2
\]

for \(P(X)=c+bX^d\), together with a number-field rank-one family having infinite \(T_3\) for every \(d\ge2\).

### 1.5 Contribution bullets and proof idea

Use three falsifiable bullets:

1. the explicit \(T_2\) theorem and its complete four-case degeneracy proof;
2. the prescribed-support rank-one \(T_1\) family proving exactness;
3. the fully proved support-one comparison yielding the support-size phase transition.

End with the proof insight: an extra nonconstant monomial forces every apparently free first-step degeneracy to expose a genuinely multi-term sparse polynomial, immediately or at the next recurrence.

## 2. Arithmetic-dynamical context — 1.50 pages

Organize this section by mathematical question, not paper by paper.

### 2.1 Quantitative unit equations

- Amoroso--Viada, Theorem 6.2, is the sole external theorem used in any proof.
- Record its algebraically closed characteristic-zero scope and exact bound.
- Present Evertse--Schlickewei--Schmidt, Theorem 1.1, only as the historical quantitative predecessor.
- Do not imply that either source analyzes Hénon degeneracies or finite windows.

### 2.2 One-variable \(S\)-unit images and orbits

- Krieger--Levin--Scherr--Tucker--Yasufuku--Zieve, Theorem 1.7: monic \(S\)-integral one-variable image bound.
- Their Theorem 1.8: local non-Archimedean valuation statement under one exceptional-coefficient condition.
- Their Corollary 1.9: the associated number-field \(S\)-unit orbit consequence.
- Explain that none is a two-dimensional, all-initial-state, arbitrary-field finite-rank window theorem.

### 2.3 Fixed-orbit subgroup intersections

- Bell--Ghioca, Theorem 1.1, fixes one orbit and a finitely generated subgroup.
- Part (i) gives arithmetic progressions plus a Banach-density-zero residual.
- Under regularity, part (ii) makes only the residual finite, not the entire hitting-time set.
- Note that the Hénon restriction to \(\mathbb G_m^2\) is generally rational because its first coordinate can vanish.

### 2.4 Current Hénon and higher-dimensional boundaries

- Ji--Xie--Zhang, arXiv v2 dated 2026-01-20: Theorem 1.8 and Corollary 1.9 are cyclotomic periodic-point non-density results, not finite-rank cardinality bounds.
- Mello--Yasufuku, arXiv v1 dated 2026-04-04: Theorems 1.1--1.2 and Corollary 1.3 use \(\mathrm{Hyp}_\epsilon\) for \(\epsilon\ge(1+c)/2\); Theorem 4.2 plus Vojta applies only for sufficiently small \(\epsilon\) with additional divisor assumptions. State the mismatch without resolving or using it.
- Kim--Krieger--Postolache--Szeto, arXiv v2 dated 2025-07-08: Theorem A treats odd \(d>2\), degree at most \(d\), and at least \((d-4)^2\) rational periodic points; Theorem B treats \(d\equiv1\pmod6\) and an integer cycle of length \((8d+10)/3\).
- Position these as neighboring regimes, never as proof inputs or classifications of all rational or integral periodic points.

The section ends by separating three quantifiers: one orbit over many times, selected maps with periodic points, and all starting points over a fixed short window.

## 3. Setup and quantitative unit equations — 2.00 pages

### 3.1 Map, inverse, and scalar recurrence

Give the inverse

\[
H^{-1}(X,Y)=\left(Y,\frac{X-P(Y)}a\right)
\]

and state why \(a\ne0\) is structural.

For an orbit write

\[
H^i(x_0,x_{-1})=(x_i,x_{i-1}),
\qquad
x_{i+1}=P(x_i)+ax_{i-1}.
\]

Explain how local states pull back injectively to initial states.

### 3.2 Finite rank and product ranks

- Define \(r=\dim_{\mathbb Q}(\Gamma\otimes_{\mathbb Z}\mathbb Q)\).
- Prove or record directly that \(\operatorname{rank}(\Gamma^q)=qr\).
- Stress that arbitrary torsion and lack of finite generation are allowed.
- Distinguish fixed coefficients from variable-group coordinates.

### 3.3 Amoroso--Viada with the mandatory field bridge

State Theorem 6.2 in the exact form needed:

\[
\alpha_1X_1+\cdots+\alpha_qX_q=1
\]

has at most \(\mathcal A(q,R)\) nondegenerate solutions in a rank-\(R\) subgroup of an algebraic torus over an algebraically closed characteristic-zero field.

Then give the entire bridge in the main text:

1. choose an algebraic closure \(\overline K\);
2. include \(K^*\) and \(\Gamma\) into \(\overline K^*\);
3. preserve the abstract rank of \(\Gamma\), while homomorphic tuple images have rank at most the stated \(2r\) or \(3r\);
4. inject every \(K\)-solution into the \(\overline K\)-solution set;
5. apply the theorem upstairs to bound the original set;
6. make no descent claim and no equality claim for the two solution sets.

Conclude with a boxed convention: \(a,c,b_j\) remain fixed nonzero coefficients and need not lie in \(\Gamma\).

## 4. Sparse polynomial images in finite-rank tori — 2.75 pages

This section contains the complete sparse-image lemma and proof. Nothing essential moves to an appendix.

### 4.1 Statement and constants

Let

\[
F(X)=\sum_{\ell=1}^q f_\ell X^{m_\ell},
\qquad
0\le m_1<\cdots<m_q\le d,
\qquad q\ge2,
\]

with every \(f_\ell\ne0\), and let \(\lambda\in K^*\). State

\[
\#\{(t,u)\in\Gamma^2:\lambda u=F(t)\}
\le
\mathcal S_q(d,r).
\]

### 4.2 Nondegenerate solutions

Normalize to

\[
\sum_{\ell=1}^q
\frac{f_\ell}{\lambda}t^{m_\ell}u^{-1}=1.
\]

Show that

\[
(t,u)\longmapsto
\bigl(t^{m_1}u^{-1},\ldots,t^{m_q}u^{-1}\bigr)
\]

has image of rank at most \(2r\). Amoroso--Viada gives at most \(\mathcal A(q,2r)\) nondegenerate image tuples.

For any two coordinates,

\[
t^{m_j-m_i}=X_j/X_i,
\]

where \(1\le m_j-m_i\le d\). This has at most \(d\) roots \(t\); the original equation then fixes \(u\). The nondegenerate contribution is at most \(d\mathcal A(q,2r)\).

### 4.3 Degenerate proper subsums

- A singleton cannot vanish because \(f_\ell,t,u\ne0\).
- The possible subsets have \(2\le |I|\le q-1\), hence number \(2^q-q-2\).
- Each produces the nonzero polynomial
  \[
  F_I(X)=\sum_{\ell\in I}f_\ell X^{m_\ell}
  \]
  of degree at most \(d\).
- It has at most \(d\) roots; for each root the original equation fixes \(u\).
- A union bound gives \(d(2^q-q-2)\).

Add the two contributions to prove the lemma.

### 4.4 Torsion and coefficient audit

Explain explicitly why arbitrary, even infinite, torsion creates no additional fiber: Amoroso--Viada is rank-based and every remaining fiber is bounded by a nonzero polynomial degree. Reiterate that \(\lambda\) is a fixed coefficient; \(\lambda u\) may lie in a coefficient coset of \(\Gamma\), but the variables remain \((t,u)\in\Gamma^2\).

Finish by defining \(\mathcal S_*\) and stating that Sections 5 and 7 will apply the lemma only with term counts between \(2\) and \(s+1\).

## 5. Two-transition finiteness for support \(s\ge2\) — 5.00 pages

This is the center of the paper and contains the entire proof of PC1.

### 5.1 Two recurrences and the normalized first equation

Write

\[
Q=(v,u),\qquad
H(Q)=(z,v),\qquad
H^2(Q)=(w,z),
\]

so \(u,v,z,w\in\Gamma\) and

\[
z=c+\sum_{j=1}^s b_jv^{e_j}+au,
\qquad
w=c+\sum_{j=1}^s b_jz^{e_j}+av.
\]

Fix the notation

\[
Z=\frac zc,\qquad
U=-\frac{au}{c},\qquad
M_j=-\frac{b_jv^{e_j}}c,
\]

so

\[
Z+U+\sum_{j=1}^sM_j=1.
\]

For nonempty \(J\subseteq[s]\), define

\[
B_J(X)=\sum_{j\in J}b_jX^{e_j}.
\]

### 5.2 Nondegenerate contribution and rank \(3r\)

The tuple

\[
(z,u,v^{e_1},\ldots,v^{e_s})
\]

is a homomorphic image of \(\Gamma^3\), hence has rank at most \(3r\). Fixed coefficients \(1/c,-a/c,-b_j/c\) do not enlarge this rank.

Amoroso--Viada gives at most \(\mathcal A(s+2,3r)\) nondegenerate tuples. Recovering \(v\) from its powers costs at most \(d\), after which \(u\) and the initial state are fixed. Therefore this class contributes at most

\[
d\mathcal A(s+2,3r).
\]

### 5.3 Exact four-case degeneracy ledger

Choose any nonempty proper vanishing subsum. Classify it by membership of \(Z\) and \(U\). Table 1 must appear in the main text with all of the following information.

| Type | Membership | Convention for \(J\) | Equations | Immediate budget |
|---|---|---|---|---:|
| GZ | \(Z\) in, \(U\) out | Nonempty monomial set in the vanished subsum | \(z=B_J(v)\), \(-au=c+B_{J^c}(v)\) | \(\mathcal S_*\) per \(J\) |
| GU | \(Z\) out, \(U\) in | Nonempty monomial set in the vanished subsum | \(au=-B_J(v)\), \(z=c+B_{J^c}(v)\) | \(\mathcal S_*\) per \(J\) |
| R0 | Neither \(Z\) nor \(U\) in | Monomial set in the vanished subsum, \(|J|\ge2\) | \(B_J(v)=0\) | \(e_{\max J}-e_{\min J}\) roots |
| R1 | Both \(Z\) and \(U\) in | Nonempty complementary monomial set | \(c+B_J(v)=0\) | \(e_{\max J}\) roots |

The text around Table 1 must derive each line, not merely cite the table.

### 5.4 GZ and GU: endpoints and coefficient cosets

For GZ:

- if \(J=[s]\), use \(z=B_J(v)\), which has \(s\ge2\) terms;
- if \(|J|=1\), use \(-au=c+B_{J^c}(v)\), which has \(s\ge2\) terms;
- in intermediate cases, either multi-term side works.

For GU:

- if \(J=[s]\), use \(au=-B_J(v)\), which has \(s\ge2\) terms;
- if \(|J|=1\), use \(z=c+B_{J^c}(v)\), which has \(s\ge2\) terms;
- in intermediate cases, use a side with at least two terms.

Apply the sparse-image lemma with fixed \(\lambda=-a\), \(a\), or \(1\), as appropriate. This is the place to explain the coefficient-coset issue: \(a\) need not lie in \(\Gamma\), because the lemma accepts any fixed \(\lambda\in K^*\) while keeping \(u,v,z\) as group variables. There are \(2^s-1\) labels in each graph family.

### 5.5 R0 and R1: root budgets

For R0, factor

\[
B_J(X)=X^{e_{\min J}}
\sum_{j\in J}b_jX^{e_j-e_{\min J}}.
\]

Since \(v\ne0\), the remaining polynomial has nonzero constant term and degree \(e_{\max J}-e_{\min J}\), giving that many possible \(v=\rho\).

For R1, explain why the complementary \(J\) is nonempty. The polynomial \(c+B_J(X)\) is nonzero of degree \(e_{\max J}\), giving at most \(e_{\max J}\) possible roots.

### 5.6 Closing every vertical root fiber

For either root type, fix \(v=\rho\). The second recurrence becomes

\[
w=(c+a\rho)+\sum_{j=1}^s b_jz^{e_j}.
\]

- If \(c+a\rho\ne0\), this polynomial has \(s+1\) distinct nonzero terms.
- If \(c+a\rho=0\), the constant cancels but exactly \(s\ge2\) nonconstant terms remain.

Apply the sparse-image lemma to \((z,w)\), obtaining at most \(\mathcal S_*\) pairs. Then recover

\[
u=\frac{z-P(\rho)}a.
\]

This subsection must explicitly rule out a free vertical chain.

### 5.7 Simultaneous zero subsums and exact component count

State that a point can realize several vanishing proper subsums. Choose any valid label and union over all labels; this deliberately overcounts and never requires disjointness.

Define the component budget in its primary form:

\[
\boxed{
\mathcal M(\mathbf e)
=
2(2^s-1)
+\sum_{\substack{J\subseteq[s]\\|J|\ge2}}
(e_{\max J}-e_{\min J})
+\sum_{\varnothing\ne J\subseteq[s]}e_{\max J}.
}
\]

Then prove the checks

\[
\sum_{\varnothing\ne J\subseteq[s]}e_{\max J}
=\sum_{k=1}^s2^{k-1}e_k,
\]

\[
\sum_{\substack{J\subseteq[s]\\|J|\ge2}}
(e_{\max J}-e_{\min J})
=
\sum_{k=1}^s(2^{k-1}-2^{s-k})e_k,
\]

and hence

\[
\mathcal M(\mathbf e)
=
2^{s+1}-2
+\sum_{k=1}^s(2^k-2^{s-k})e_k.
\]

Also record the crude bound

\[
\mathcal M(\mathbf e)
\le
2(2^s-1)+d(2^{s+1}-s-2).
\]

Label both later expressions as checksums, not definitions. Sum the nondegenerate and degenerate contributions and close PC1 in the main text.

## 6. Sharpness and essential hypotheses — 1.50 pages

### 6.1 PC2: one transition does not suffice

For every prescribed support with \(s\ge2\), take

\[
K=\mathbb Q,\qquad
a=1,\qquad
b_1=\cdots=b_s=1,\qquad
c=-s,\qquad
\Gamma=\langle2\rangle.
\]

Then \(P(1)=0\), and for every \(n\ge0\),

\[
Q_n=(1,2^n),
\qquad
H(Q_n)=(2^n,1).
\]

The \(Q_n\) are distinct, so \(T_1\) is infinite. State that PC1 and PC2 together make two transitions exact for \(s\ge2\). A short remark may note the rank-zero roots-of-unity variant, while keeping the rational rank-one example as the theorem.

### 6.2 The constant term is essential

If \(c=0\), take

\[
P(X)=X^d+X,\qquad a=-1.
\]

For every \(t\) in an infinite subgroup,

\[
(t,t^d)\longmapsto(t,t)\longmapsto(t^d,t),
\]

so \(T_2\) is infinite. This is a counterexample, not an extension.

### 6.3 The Hénon coefficient is essential

If \(a=0\), take

\[
P(X)=-1+X+X^2.
\]

Then

\[
(1,t)\longmapsto(1,1)\longmapsto(1,1),
\]

so the initial second coordinate remains free. Explain that the inverse and local pullback arguments also fail in this triangular degeneration.

### 6.4 Actual support convention

State that equal exponents are collected and zero coefficients deleted before \(s\) is counted. The theorem is not about a syntactic presentation. A zero displayed \(b_j\) is outside the stated hypotheses.

## 7. The complete support-one comparison — 5.25 pages

This section contains the complete PC3 proof. No transition or free-chain argument is deferred.

### 7.1 Statement and scalar recurrence

Set

\[
P(X)=c+bX^d,\qquad
H(x,y)=(bx^d+ay+c,x),\qquad d\ge2.
\]

State

\[
\boxed{
\#T_4(H,\Gamma)
\le
4d\mathcal A(3,3r)+81d^2
}
\]

and the existence, for every \(d\ge2\), of a number-field rank-one example with infinite \(T_3\).

Use

\[
x_{i+1}=bx_i^d+ax_{i-1}+c,
\qquad
H^i(x_0,x_{-1})=(x_i,x_{i-1}).
\]

### 7.2 Nondegenerate local equations

There are four local indices \(i=0,1,2,3\) for \(T_4\). Normalize

\[
\frac{x_{i+1}}c-\frac bcx_i^d-\frac acx_{i-1}=1.
\]

The tuple

\[
(x_{i+1},x_i^d,x_{i-1})
\]

has rank at most \(3r\). Amoroso--Viada and the degree-\(d\) power fiber give at most \(d\mathcal A(3,3r)\) initial states per index. The four-index union gives \(4d\mathcal A(3,3r)\).

### 7.3 Derivation of the A/B/C labels

Put \(\alpha=-c/a\). Derive, from the three possible vanishing pair subsums,

\[
\begin{array}{lll}
A_i:&x_{i-1}=\alpha,&x_{i+1}=bx_i^d,\\
B_i:&bx_i^d=-c,&x_{i+1}=ax_{i-1},\\
C_i:&bx_i^d=-ax_{i-1},&x_{i+1}=c.
\end{array}
\]

Explain why singletons cannot vanish and why simultaneous labels will be covered by the word union.

### 7.4 Entire nine-transition table

Table 2 must appear in the main text exactly as the complete adjacent-word ledger.

| Word | Necessary conditions on \(u=x_{i-1}\), \(v=x_i\) | Bound or status |
|---|---|---:|
| \(AA\) | \(u=\alpha,\ v=\alpha\) | \(1\) |
| \(AB\) | \(u=\alpha,\ b^{d+1}v^{d^2}=-c\) | \(d^2\) |
| \(AC\) | \(u=\alpha,\ b^{d+1}v^{d^2}=-av\) | \(d^2-1\) |
| \(BA\) | \(v=\alpha,\ b\alpha^d=-c\) | \(u\) free |
| \(BB\) | \(v^d=-c/b,\ u^d=-c/(ba^d)\) | \(d^2\) |
| \(BC\) | \(v^d=-c/b,\ u^d=-v/(ba^{d-1})\) | \(d^2\) |
| \(CA\) | \(v=\alpha,\ u=-b\alpha^d/a\) | \(1\) |
| \(CB\) | \(bc^d=-c,\ u=-bv^d/a\) | \(v\) free |
| \(CC\) | \(v=-bc^d/a,\ u=-bv^d/a\) | \(1\) |

Derive all nine rows by substitution. Conclude that only \(BA\) and \(CB\) can remain free after two labels.

### 7.5 Closure of every BA branch

Under \(b\alpha^d=-c\), write the coordinate chain

\[
t,\ \alpha,\ at,\ ba^dt^d.
\]

Table 3 must show the third-label constraints.

| Word | Equation | Bound |
|---|---|---:|
| \(BAA\) | \(at=\alpha\) | \(1\) |
| \(BAB\) | \(b^{d+1}a^{d^2}t^{d^2}=-c\) | \(d^2\) |
| \(BAC\) | \(b^{d+1}a^{d^2}t^{d^2}=-a^2t\) | \(d^2-1\) |

For \(BAC\), divide by \(t\ne0\) to justify the \(d^2-1\) degree. Conclude that every BA branch closes at the third label.

### 7.6 Closure of CB and the exceptional CBA branch

For \(CB\), require

\[
bc^d=-c,
\qquad\text{equivalently}\qquad
bc^{d-1}=-1,
\]

and use the chain

\[
-bt^d/a,\ t,\ c,\ at.
\]

Table 4 must carry both levels of continuation.

| Word | Equation or compatibility | Bound or status |
|---|---|---:|
| \(CBB\) | \(ba^dt^d=-c\) | \(d\) |
| \(CBC\) | \(ba^dt^d=-ac\) | \(d\) |
| \(CBA\) | \(c=-c/a\), hence \(a=-1\) | free only under compatibility |
| \(CBAA\) | \(-t=c\) | \(1\) |
| \(CBAB\) | \(b^{d+1}(-t)^{d^2}=-c\) | \(d^2\) |
| \(CBAC\) | \(b^{d+1}(-t)^{d^2}=-t\) | \(d^2-1\) |

Under \(a=-1\) and \(bc^{d-1}=-1\), display the exceptional chain

\[
bt^d,\ t,\ c,\ -t,\ b(-t)^d.
\]

For \(CBAC\), divide by \(t\ne0\). Conclude that every fourth label closes the only free three-label chain.

### 7.7 Word cover and simultaneous labels

- Every four-letter word has at most \(d^2\) initial states.
- There are \(3^4=81\) words.
- If a local equation has multiple labels, choose any valid label at each index.
- The word union overcounts overlaps but omits no point.
- The all-degenerate class therefore contributes at most \(81d^2\).

Combine this with the nondegenerate contribution to finish the upper bound.

### 7.8 Rank-one sharpness through three transitions

Choose

\[
c^{d-1}=-1,\qquad
K=\mathbb Q(c),\qquad
b=1,\qquad
a=-1,\qquad
\Gamma=\langle2,c,-1\rangle.
\]

The elements \(c\) and \(-1\) are torsion, while \(2\) has infinite order, so \(\Gamma\) has rank one.

For \(t=2^n\), set \(Q_t=(t,t^d)\). Verify the exact scalar chain

\[
x_{-1},x_0,x_1,x_2,x_3
=
t^d,\ t,\ c,\ -t,\ (-t)^d.
\]

All four states through \(H^3(Q_t)\) lie in \(\Gamma^2\), and distinct \(t\) give distinct initial states. Hence \(T_3\) is infinite.

## 8. Phase transition, limitations, and conclusion — 1.50 pages

### 8.1 Exact support-size transition

Synthesize the theorems in one display rather than a promotional comparison table:

\[
\begin{array}{c|c|c}
\text{actual nonconstant support}
&\text{uniformly finite window}
&\text{sharp shorter failure}\\ \hline
s=1&T_4&T_3\text{ can be infinite},\\
s\ge2&T_2&T_1\text{ can be infinite}.
\end{array}
\]

Explain the mechanism: one extra nonconstant monomial eliminates the long free degeneracy chain because a multi-term sparse image appears no later than the second recurrence.

### 8.2 Limitations and nonclaims

State explicitly that the paper proves none of the following:

- a positive-characteristic analogue;
- a theorem with \(c=0\), \(a=0\), or a zero displayed \(b_j\);
- affine-conjugacy invariance of support size or of the theorem;
- optimality of \(\mathcal A\), \(\mathcal S_q\), \(\mathcal S_*\), \(\mathcal M\), or either cardinality bound;
- effective enumeration of surviving points;
- height estimates;
- classification of periodic points, rational periodic points, or integral cycles;
- classification of every coefficient stratum with an infinite shorter window;
- a theorem for arbitrary rational maps, arbitrary polynomial automorphisms, or arbitrary compositions of Hénon maps;
- a global priority statement.

### 8.3 Publication relation

An earlier manuscript by the same authors treated only the one-monomial case. The present paper reproduces that theorem and proof in full as part of the support-size phase transition, thereby absorbing the earlier manuscript; the two manuscripts will not be submitted in parallel, and the present paper is the sole intended external version of the overlapping material.

This paragraph appears once here and nowhere in the abstract, theorem statements, proofs, literature positioning, novelty discussion, or tables.

### 8.4 Conclusion

Restate the contribution without copying the introduction: the decisive invariant inside the fixed normal form is actual nonconstant support, and the proof identifies exactly how sparse-image finiteness closes every degeneracy. End with two clearly labeled directions rather than claims: improving coarse constants and understanding whether comparable support-sensitive windows exist in broader normal forms.

## Appendices A--C

Each appendix is capped at one page and is dispensable for logical completeness.

## Appendix A. Rank and power-fiber audit — 1.00 page

- Expand the tensor-product proof that \(\operatorname{rank}(\Gamma^q)=qr\).
- List the homomorphisms from \(\Gamma^2\) and \(\Gamma^3\) used in Sections 4, 5, and 7.
- Recheck every degree-\(d\) power fiber and local-state pullback.
- Repeat the arbitrary-torsion check in a compact ledger.
- Do not introduce a stronger lemma or a new hypothesis.

## Appendix B. PC1 subset and component ledger — 1.00 page

- List the allowed \(J\)-ranges for GZ, GU, R0, and R1.
- Recheck \(J=[s]\), \(|J|=1\), and the R1 complementary-index convention.
- Count subsets by maximum and minimum to reproduce the two checksum identities for \(\mathcal M(\mathbf e)\).
- Record the constant-cancellation branch of the second recurrence.
- Treat this as an audit duplicate of Section 5, not the location of any missing proof.

## Appendix C. Support-one continuation ledger — 1.00 page

- Give the coordinate substitutions behind every row of the nine-transition table.
- Expand the BA and CB/CBA coordinate ledgers.
- Record the simultaneous-label overlap calculation and why the word cover remains valid.
- Note that repeated coordinates from a short periodic orbit add constraints and do not create a new branch.
- Treat this as an audit duplicate of Section 7.

## Figure and proof-table plan

### Figures

No figures are required or permitted by this plan. The paper has no empirical evidence, architecture, data, or visual comparison. The title, abstract, first theorem display, and phase-transition statement provide the front-loaded summary.

### Main-text proof tables

| ID | Location | Content | Purpose |
|---|---|---|---|
| Table 1 | Section 5.3 | GZ/GU/R0/R1 membership, equations, \(J\)-convention, and budget | Exhaustiveness and coefficient-coset audit |
| Table 2 | Section 7.4 | All nine adjacent A/B/C words | Exact support-one transition ledger |
| Table 3 | Section 7.5 | BAA/BAB/BAC equations and bounds | Closure of BA |
| Table 4 | Section 7.6 | CBB/CBC/CBA and CBAA/CBAB/CBAC | Closure of CB and exceptional CBA |

These tables carry proof algebra. There are no experimental result tables, literature scorecards, decorative diagrams, or evidentiary visuals.

## Citation plan

- **Section 1:** Cite only enough context to distinguish finite-window survival from fixed-orbit and one-variable questions; do not make a priority claim.
- **Section 2.1:** Amoroso--Viada Theorem 6.2 with exact field scope and bound; ESS Theorem 1.1 as historical predecessor only.
- **Section 2.2:** Krieger et al. Theorem 1.7, Theorem 1.8, and Corollary 1.9 with their distinct roles.
- **Section 2.3:** Bell--Ghioca Theorem 1.1, including the arithmetic-progression residual distinction and regularity caution.
- **Section 2.4:** Ji--Xie--Zhang v2 Theorem 1.8 and Corollary 1.9; Mello--Yasufuku Theorems 1.1--1.2, Corollary 1.3, and Theorem 4.2 with the unresolved range mismatch; Kim et al. v2 Theorems A and B with exact degree and congruence ranges.
- **Sections 3--5 and 7:** Amoroso--Viada is the sole external proof citation. Later uses cross-reference the exact statement and field bridge in Section 3.
- **Sections 6 and 8:** The sharpness families, counterexamples, phase transition, and limitations are proved internally and need no external theorem citation.

No bibliography entry is to be generated from memory. Publication metadata and preprint version dates must be reverified before any later bibliography-authoring stage.

## Main-text completeness checklist

- [ ] The actual collected-support convention and every nonzero coefficient appear before PC1.
- [ ] \(T_m\) is explicitly \(m\) transitions and \(m+1\) states.
- [ ] The arbitrary-field algebraic-closure bridge is complete and makes no descent claim.
- [ ] The sparse-image lemma contains both nondegenerate and degenerate proofs and the torsion audit.
- [ ] The PC1 nondegenerate tuple has rank at most \(3r\) with coefficients kept fixed.
- [ ] GZ, GU, R0, and R1 are derived and Table 1 is complete.
- [ ] Both graph endpoints and every fixed coefficient \(\lambda\) are explicit.
- [ ] The second recurrence handles \(c+a\rho=0\) without losing the \(s\ge2\) term count.
- [ ] Simultaneous zero subsums are unioned without a disjointness claim.
- [ ] \(\mathcal M(\mathbf e)\) is defined by the two subset sums; both checksums are proved.
- [ ] PC2 and the \(c=0\), \(a=0\) counterexamples are directly verified.
- [ ] The support-one A/B/C labels and all nine adjacent transitions appear in the main text.
- [ ] BA, CB, and CBA closures appear in the main text with exact equations and degrees.
- [ ] The \(81d^2\) word cover includes simultaneous labels.
- [ ] Both rank-one sharpness constructions include their rank audits.
- [ ] The exact \(s=1\) versus \(s\ge2\) transition appears in Sections 1 and 8.
- [ ] All explicit nonclaims appear in Section 8.
- [ ] The publication-relation paragraph occurs exactly once, in Section 8.3 only.
- [ ] No appendix carries a logically necessary step.
- [ ] There are zero figures and only the four exact proof tables.

## Independent plan-review questions

1. Does the introduction make the What, Why, and So What legible before the technical setup?
2. Is PC1 visibly dominant, with PC2 as its sharpness theorem and PC3 as the subordinate comparison?
3. Does every claim in the claims--evidence matrix map to a complete main-text proof?
4. Are the Amoroso--Viada theorem, algebraic-closure bridge, and all local rank calculations exact?
5. Does Section 5 close every GZ/GU/R0/R1 branch, including endpoints, coefficient cosets, vertical cancellation, and simultaneous labels?
6. Does Section 7 contain the entire nine-transition table and every BA/CB/CBA continuation?
7. Is the 25-page allocation feasible without moving essential proof into an appendix?
8. Are all literature results confined to their exact theorem-number roles?
9. Are the nonclaims explicit and the publication-relation paragraph present exactly once in its required location?
10. Does the outline remain free of empirical or computational evidence claims?

## Downstream boundary

This document is an outline only. Even a favorable independent review of the outline authorizes no TeX or BibTeX source, bibliography file, manuscript draft, figure, compilation, PDF build, release, submission, upload, or external distribution. Each later action requires a separately invoked and independently reviewed stage.
