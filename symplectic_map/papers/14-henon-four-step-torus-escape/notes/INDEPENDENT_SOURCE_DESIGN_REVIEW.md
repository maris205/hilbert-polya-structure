# SOURCE_DESIGN_PASS

## Review identity, scope, and freeze

This is a fresh, independent source-design review dated 2026-08-16.  The
authoring stage was treated as stopped.  I read all ten pre-review files in
full, independently replayed the mathematical proof, checked the primary
literature roles against the cited sources, and performed targeted
primary-source collision searches through the freeze date.  I did not use a
parameter, prime, or modulus scan.

The review verdict is:

> **SOURCE_DESIGN_PASS.**  No mathematical, quantifier, scope, citation-role,
> or source-state repair is required before the next authorized stage.

This verdict concerns the frozen source design.  It is not manuscript
acceptance, an absolute-priority claim, or a substitute for later line-level
refereeing.

## Frozen source-state audit

Before this authorized review file was added, the project contained exactly
the following ten regular files and no symbolic links:

| Frozen file | Pre-review SHA-256 |
|---|---|
| `experiments/EXPERIMENT_PLAN.md` | `709b32fa83e7cf1502e57393e4b46daf33c83ccb88832a498e223d084eabbd95` |
| `experiments/EXPERIMENT_TRACKER.md` | `da117759e1e6a95579fcae16f27c3c868bd67b6d0b8b5d98e936b456a9354a97` |
| `notes/CITATION_VERIFICATION.md` | `ccd48de4e4c96a2b207cf9da911fda427fe8e79c35320779dc02dc2ab694b87c` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `d1887968e8626c1a8e30c9cb1675a13277c76662ca0fee8834ea024123650f6e` |
| `notes/NOVELTY_ASSESSMENT.md` | `eed574ca465683985dfb329f7a494b6f7862ff6cc60ef07550796be8046c845f` |
| `notes/PROOF_PACKAGE.md` | `c43d8377707e0ee69aa6447984b77c2b5ef6d1d79bc1d56c6b5ab72ea4c8f5aa` |
| `notes/RESEARCH_QUESTION.md` | `782b48dfec973d877bf87c964a3bdd7227b52a21101b68a9a576929441bedb9c` |
| `refine-logs/FINAL_PROPOSAL.md` | `af46eae7ef8cc4e8872bcc2ce33ee80c82ff354c7e52346aa575c8018b14db33` |
| `refine-logs/INITIAL_PROPOSAL.md` | `ecb3a5151c75dba6ac4b8415d000f9a9a3c36ff80af5b651b9de7ecbad7a6e22` |
| `refine-logs/REVIEW_SUMMARY.md` | `ac2a75bb0f393de1255958705bbcd2e75fa1e0800805d420f048cb0f72c5d54f` |

The only pre-review subdirectories were `experiments`, `notes`, and
`refine-logs`.  There was no code tree, results tree, paper/manuscript tree,
or `source_lock`.  The experiment files record a proof-only design and no
computational result.  This review is the authorized eleventh file; it does
not change the status of any of the ten frozen files.

The workspace root is not a Git worktree, so source integrity is certified
by the complete filesystem manifest and SHA-256 comparison rather than by a
Git status.  The post-write self-hash of this review is necessarily reported
outside the file, together with the final rehash of all eleven files.

## Exact theorem audited

Let \(K\) be a field of characteristic zero, let \(d\ge 2\) be an integer,
let \(a,b,c\in K^\ast\), and let \(\Gamma\le K^\ast\) have finite rank
\(r\).  Put

\[
H(x,y)=(b x^d+a y+c,x)
\]

and, for \(m\ge0\),

\[
T_m(H,\Gamma)=
\{P\in\Gamma^2:H^j(P)\in\Gamma^2\text{ for }0\le j\le m\}.
\]

The source package claims

\[
\#T_4(H,\Gamma)
\le
4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2. \tag{1}
\]

It also claims that for every \(d\ge2\) there is an example with
\(\operatorname{rank}\Gamma=1\) and \(\#T_3(H,\Gamma)=\infty\), and the
weighted whole-orbit periodic corollary recorded below.  Every quantifier and
hypothesis in this formulation is necessary for the proof as written and is
present consistently in the current theorem-bearing files:

- \(K\) is arbitrary of characteristic zero; it is not silently assumed to
  be a number field, algebraically closed, or global.
- \(d\) is an integer at least two.
- \(abc\ne0\).  In particular, \(a\ne0\) makes \(H\) invertible, while
  \(b,c\ne0\) are used in the normalized unit equation and degeneracy
  analysis.
- \(\Gamma\) need only have finite rank.  It is not required to be finitely
  generated, and no coefficient is required to belong to \(\Gamma\).
- Membership at time zero is included explicitly in \(T_m\).

## Independent proof replay

### 1. Fixed-coefficient ESS input and the \(4dE\) term

Write \(P=(x_0,x_{-1})\) and

\[
x_{i+1}=b x_i^d+a x_{i-1}+c.
\]

For every relevant index \(i\in\{0,1,2,3\}\), division by \(c\) gives

\[
\frac1c x_{i+1}-\frac bc x_i^d-\frac ac x_{i-1}=1. \tag{2}
\]

The variables \((x_{i+1},x_i^d,x_{i-1})\) lie in \(\Gamma^3\), a subgroup
of \((K^\ast)^3\) of rank \(3r\).  The three displayed ratios involving
\(a,b,c\) are fixed coefficients, not variables.  Published Theorem 1.1 of
[Evertse--Schlickewei--Schmidt](https://annals.math.princeton.edu/2002/155-3/p04)
(displayed as Theorem 0.1 in the
[arXiv conversion](https://arxiv.org/abs/math/0409604)) therefore bounds the
nondegenerate solutions of (2) by

\[
E(3,3r)=\exp\!\bigl((6\cdot3)^9(3r+1)\bigr)
=\exp\!\bigl(18^9(3r+1)\bigr). \tag{3}
\]

This is exactly the fixed-coefficient use of ESS.  Neither coefficient
membership nor a rank expansion to \(\langle\Gamma,a,b,c\rangle\) occurs.

For a fixed ESS triple, \(x_i^d\) has at most \(d\) possible \(x_i\)'s in
characteristic zero.  Once \(x_{i-1},x_i\) are fixed, the recurrence is
unique in both directions because

\[
H^{-1}(X,Y)=\left(Y,\frac{X-bY^d-c}{a}\right).
\]

Thus the subset on which index \(i\) is nondegenerate has size at most
\(dE(3,3r)\).  Taking the union over the four indices gives the first term
\(4dE(3,3r)\).  This is a union bound; it needs no independence between
indices.

### 2. Exhaustive degeneracy labels

All coordinates and coefficients in (2) are nonzero.  Hence a degenerate
three-variable ESS solution is exactly one for which one of the three pair
subsums vanishes.  With \(\alpha=-c/a\), the locked labels are

\[
\begin{array}{lll}
A_i:&x_{i-1}=\alpha,&x_{i+1}=b x_i^d,\\
B_i:&b x_i^d=-c,&x_{i+1}=a x_{i-1},\\
C_i:&b x_i^d=-a x_{i-1},&x_{i+1}=c.
\end{array} \tag{4}
\]

These are exhaustive, and their indexing is consistent in every current
theorem/proof file.

### 3. Full \(b\)-version nine-transition audit

Set \(u=x_{i-1}\) and \(v=x_i\).  Direct substitution into two consecutive
labels gives the following complete table.

| Word | Forced conditions on \((u,v)\) | Number unless marked free |
|---|---|---:|
| \(AA\) | \(u=\alpha,\ v=\alpha\) | \(1\) |
| \(AB\) | \(u=\alpha,\ b^{d+1}v^{d^2}=-c\) | \(\le d^2\) |
| \(AC\) | \(u=\alpha,\ b^{d+1}v^{d^2}=-av\) | \(\le d^2-1\) |
| \(BA\) | \(v=\alpha,\ b\alpha^d=-c\) | \(u\) free |
| \(BB\) | \(v^d=-c/b,\ u^d=-c/(ba^d)\) | \(\le d^2\) |
| \(BC\) | \(v^d=-c/b,\ u^d=-v/(ba^{d-1})\) | \(\le d^2\) |
| \(CA\) | \(v=\alpha,\ u=-b\alpha^d/a\) | \(1\) |
| \(CB\) | \(bc^d=-c,\ u=-bv^d/a\) | \(v\) free |
| \(CC\) | \(v=-bc^d/a,\ u=-bv^d/a\) | \(1\) |

The root counts are valid over any characteristic-zero field and count only
more generously than the solutions lying in \(\Gamma\).  The table shows that
the only free adjacent words are \(BA\) and \(CB\).

### 4. Closure of the \(BA\) and \(CB\) chains

For \(BA\), let \(t=x_{i-1}\).  Subject to the compatibility
\(b\alpha^d=-c\), the four consecutive coordinates are

\[
t,\quad \alpha,\quad at,\quad ba^d t^d.
\]

The third symbol \(A,B,C\), respectively, imposes

\[
at=\alpha,qquad
b^{d+1}a^{d^2}t^{d^2}=-c,qquad
b^{d+1}a^{d^2}t^{d^2}=-a^2t.
\]

These give at most \(1,d^2,d^2-1\) values of \(t\).  Thus every \(BA\ast\)
chain is closed by its third symbol.

For \(CB\), the compatibility is \(bc^{d-1}=-1\).  With \(t=x_i\), the
coordinates are

\[
-\frac{bt^d}{a},\quad t,\quad c,\quad at.
\]

A third \(B\) or \(C\) imposes, respectively,

\[
ba^d t^d=-c,qquad ba^d t^d=-ac,
\]

and hence gives at most \(d\) values.  A third \(A\) is possible without
restricting \(t\) exactly when \(a=-1\).  Together with the preceding
compatibility, the sole free length-three chain is therefore

\[
CBA,qquad a=-1,qquad bc^{d-1}=-1. \tag{5}
\]

In (5), the coordinates extend as

\[
bt^d,\quad t,\quad c,\quad -t,\quad b(-t)^d.
\]

The fourth symbol \(A,B,C\), respectively, imposes

\[
-t=c,qquad
b^{d+1}(-t)^{d^2}=-c,qquad
b^{d+1}(-t)^{d^2}=-t.
\]

The corresponding counts are at most \(1,d^2,d^2-1\).  Thus the unique free
length-three chain closes at length four.

### 5. The \(81d^2\) term and simultaneous degeneracy

There are \(3^4=81\) four-letter words.  If the first adjacent pair is not
\(BA\) or \(CB\), the table already gives at most \(d^2\) initial states.  If
it is \(BA\), the third letter gives that bound.  If it is \(CB\), either the
third letter gives that bound or the exceptional \(CBA\) chain is closed by
the fourth letter.  The recurrence then determines the whole window.
Consequently every word contributes at most \(d^2\), and all-four-indices
degenerate states contribute at most \(81d^2\).

There is no hidden disjointness assumption.  In normalized coordinates
\((X,Y,Z)\) for \(X+Y+Z=1\), the pairwise simultaneous degeneracies are

\[
A\cap B=(-1,1,1),\qquad
A\cap C=(1,-1,1),\qquad
B\cap C=(1,1,-1).
\]

A triple intersection would force a nonzero normalized variable to vanish
because \(2\ne0\), so it is impossible in characteristic zero.  A state in a
pairwise intersection is simply represented by more than one word.  The
union bound deliberately overcounts it, so simultaneous degeneracy cannot
invalidate (1).

### 6. Short periods

The proof never assumes that the states \(H^j(P)\), or any of the coordinates
\(x_i\), are distinct.  Periods \(1,2,3,4\), coordinate repetitions, and
words with simultaneous labels therefore remain inside the same union
argument.  No subtraction or special correction for short periods is
needed.

### 7. Rank-one sharpness at three steps

For each \(d\ge2\), choose \(c\) with \(c^{d-1}=-1\), put

\[
K=\mathbb Q(c),\qquad b=1,\qquad a=-1,
\qquad \Gamma=\langle2,c,-1\rangle.
\]

Both \(c\) and \(-1\) are torsion, while \(2\) is not, so
\(\operatorname{rank}\Gamma=1\).  For \(t=2^n\), set
\(P_t=(t,t^d)\).  Direct calculation gives

\[
H(P_t)=(c,t),\qquad
H^2(P_t)=(-t,c),\qquad
H^3(P_t)=((-t)^d,-t).
\]

Every displayed coordinate lies in \(\Gamma\), and the \(P_t\)'s are
distinct for infinitely many integers \(n\ge0\).  Thus \(T_3\) is infinite.
The labels are exactly \(CBA\).  The package correctly uses this example
only to prove sharpness of the universal window length; it does not call the
family periodic and does not promote it to a classification of all infinite
\(T_3\) strata.

### 8. Weighted whole-orbit periodic corollary

Let \(C_n^\Gamma(H)\) be the number of exact-period-\(n\) orbits
\(\mathcal O\) satisfying the essential condition
\(\mathcal O\subseteq\Gamma^2\).  Every point of every such orbit belongs to
\(T_4(H,\Gamma)\); distinct exact-period orbits are disjoint; and an
exact-period-\(n\) orbit contains \(n\) points.  Therefore

\[
\sum_{n\ge1} n C_n^\Gamma(H)
\le \#T_4(H,\Gamma)
\le 4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2. \tag{6}
\]

The argument also shows that only finitely many summands in (6) can be
nonzero.  It does **not** bound all points of
\(\operatorname{Per}(H)\cap\Gamma^2\) when only one point, rather than the
whole orbit, lies in \(\Gamma^2\).  The source package states this distinction
correctly everywhere.

## Claim, nonclaim, and wording audit

The theorem, proof package, research question, final proposal, review
summary, claims/evidence matrix, novelty assessment, and proof-only planning
files agree on the mathematical center: (1), rank-one \(T_3\) sharpness, the
full \(b\)-coefficient transition analysis, and (6).

The following regression checks pass:

- **No coefficient-membership regression.**  The current theorem says
  \(a,b,c\in K^\ast\), not \(a,b,c\in\Gamma\), and uses rank \(3r\).  The
  `INITIAL_PROPOSAL.md` records the earlier \(b=1\),
  \(-1,a,c\in\Gamma\) formulation only under the explicit heading
  “Historical starting point,” identifies it as defective, and derives the
  corrected fixed-coefficient formulation.  It is not a live claim.
- **No rank-expansion regression.**  No live proof places coefficient-scaled
  variables in \(\Gamma^3\), and no live theorem replaces \(r\) by
  \(\operatorname{rank}\langle\Gamma,a,b,c\rangle\).
- **No unproved stratification promotion.**  A complete classification of
  infinite \(T_3\) sets and any full \(T_2/T_3\) coefficient stratification
  are explicitly held back as secondary questions or nonclaims.  The only
  asserted \(T_3\) result is the concrete rank-one infinite family above.
- **No title overreach.**  The safe and final title is “Four-Step Escape from
  Finite-Rank Tori for Monomial Hénon Maps.”  The word “monomial” prevents an
  implication that arbitrary polynomial/general Hénon maps are covered.
- **No arithmetic overreach.**  The package does not claim a bound for all
  rational or integral periodic points, arbitrary \(p(x)\), characteristic
  \(p\), \(d=1\), zero coefficients, heights, effectivity, optimal constants,
  realizability of all words, or absolute literature priority.
- **No imported unrelated project claim.**  The package expressly excludes
  Paper 15/quartic material and imports no theorem, score, or evidence from
  it.

The claims/evidence matrix correctly marks the exact four-step theorem,
sharpness example, and whole-orbit corollary as supported; the collision
conclusion and scores as bounded/advisory; and the full stratification and
broader Hénon statements as pending or forbidden.  The planning files do not
upgrade proposed proof checks into computational evidence.

## Primary-literature and theorem-role audit

The citation architecture is sound.  Exactly one external theorem is used
in the proof:

- [Evertse--Schlickewei--Schmidt, Annals of Mathematics 155 (2002),
  Theorem 1.1](https://annals.math.princeton.edu/2002/155-3/p04) supplies
  (3) for arbitrary fixed nonzero coefficients over a characteristic-zero
  field and a multiplicative subgroup of finite rank.  It supplies none of
  the dynamical pullback factor \(d\), four-index factor \(4\), transition
  table, \(81d^2\), sharpness family, or periodic corollary.

All other citations are used only to delimit prior-art scope, and those roles
match their primary sources:

- [Krieger--Levin--Scherr--Tucker--Yasufuku--Zieve](https://arxiv.org/abs/1406.1990),
  [Canci--Paladino](https://arxiv.org/abs/1403.2293),
  [Canci--Vishkautsan](https://arxiv.org/abs/1604.03965), and
  [Canci--Troncoso--Vishkautsan](https://arxiv.org/abs/1711.04649) concern
  one-dimensional rational dynamics, \(S\)-units, or good reduction, not the
  present two-dimensional finite-window initial-state count.
- [Ostafe--Sha--Shparlinski--Zannier](https://arxiv.org/abs/1706.05874) and
  [Bérczes--Ostafe--Shparlinski--Silverman](https://arxiv.org/abs/1811.04971)
  concern multiplicative dependence of univariate values/iterates.
- [Bell--Chen--Hossain](https://arxiv.org/abs/2005.04281) and
  [Grieve--Noytaptim](https://arxiv.org/abs/2407.08614) concern hitting-time
  or non-density structure for a fixed orbit, not a count of all initial
  states.
- [Noytaptim--Zhong](https://arxiv.org/abs/2412.15141) includes Hénon-type
  common-zero questions but no four-step finite-rank torus theorem.
- [Kim--Krieger--Postolache--Szeto, v2 (2025-07-08)](https://arxiv.org/abs/2412.01668)
  constructs, for odd \(d\), Hénon maps with at least \((d-4)^2\) integral
  periodic points; this correctly motivates the nonclaim that arbitrary
  integral points are bounded here.
- [Ji--Xie--Zhang, v2 (2026-01-20), Theorem 1.8 and Corollary
  1.9](https://arxiv.org/abs/2511.13443) gives cyclotomic periodic-point
  non-density for Hénon-type maps and then plane positive-entropy maps.  The
  package correctly does not turn non-density into finiteness.
- [Mello--Yasufuku, v1 (2026-04-04)](https://arxiv.org/abs/2604.03745)
  studies higher-dimensional integrality and multiplicative dependence via
  non-density hypotheses, not the unconditional explicit bound (1).
- [Ingram](https://arxiv.org/abs/1111.3609) and
  [Hsia--Kawaguchi](https://arxiv.org/abs/1810.03841) provide Hénon height and
  parameter context only.

A fresh targeted search of primary literature through 2026-08-16 found no
direct theorem combining arbitrary characteristic-zero fields, arbitrary
finite-rank \(\Gamma\), a coefficient-uniform four-step monomial-Hénon
survivor count, the explicit \(d,r\) bound, and rank-one three-step
sharpness.  This supports only the package's carefully worded bounded-search
statement; it does not prove absolute priority or rule out unpublished or
unindexed work.

## Two-audit score audit

The two source-stage assessment records are transcribed consistently in
`NOVELTY_ASSESSMENT.md`, `FINAL_PROPOSAL.md`, and `REVIEW_SUMMARY.md`:

| Record | Novelty | Standalone size | Proof confidence | Recorded disposition |
|---|---:|---:|---:|---|
| A | \(7.0/10\) | \(6.0\)--\(6.5/10\) | \(9.5/10\) | GO after minor formal repair |
| B | \(7.0/10\) | \(6.0\)--\(6.3/10\) | \(9.7/10\) | GO with source-package corrections |

The repairs named by A and B are present: \(T_4/T_3\) is the headline,
whole-orbit containment is explicit, the full \(b x^d\) family is used, and
fixed ESS coefficients eliminate coefficient-membership assumptions without
changing rank \(3r\).  The package correctly labels the scores as advisory,
keeps them separate, and disclaims cross-model certification.  This review
certifies their exact transcription and the completion of their stated
repairs; the ten-file package does not contain raw process logs from which an
outside reader could independently reconstruct auditor identity or process
independence, and it does not rely on that metadata as theorem evidence.

## Final source-design disposition

All requested checks pass:

1. fixed-coefficient ESS applies at rank \(3r\);
2. the nondegenerate contribution is at most \(4dE(3,3r)\);
3. the full \(b\)-version nine-transition table is correct;
4. \(BA\) closes at the third letter and \(CB\) has only the exceptional
   free continuation \(CBA\), which closes at the fourth;
5. the degenerate contribution is at most \(81d^2\);
6. simultaneous degeneracy is safely covered by overcounting;
7. periods \(1\)--\(4\) require no separate correction;
8. the \(T_3\) example has rank exactly one and proves window sharpness;
9. the periodic corollary has the necessary whole-orbit condition and the
   correct weight \(n\);
10. quantifiers, coefficient hypotheses, claims, nonclaims, citation roles,
    scores, title, and lifecycle state are aligned across all ten files.

Accordingly the canonical disposition is **SOURCE_DESIGN_PASS**, with no
repair list and no authorization here to create a manuscript, code, results,
or a `source_lock`.
