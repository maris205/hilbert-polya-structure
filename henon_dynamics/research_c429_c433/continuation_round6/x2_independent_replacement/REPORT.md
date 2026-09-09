# R6 X2 — two bounded replacement tests, no new recommendation

2026-09-10 UTC. Current-team source/proof scout, not admission or peer review.
Only this file is writable by this lane. No manuscript number is proposed.

## Outcome and preserved boundary

**Recommend neither candidate for a new independent contract in this pass.**

| Complete question tested | Decisive result of this scout | Disposition |
| --- | --- | --- |
| M6: ordinary multiplicative periodic data force an original rational transfer, for every unicritical map in every finite characteristic | A uniform elementary counterexample already occurs for the separable map $x^{p+1}$; the obstruction is a $p$-divisible divisor, not a new periodic-data bridge | Retain the explicit falsifier as auxiliary; insufficient independent substance |
| Z6: the ordinary native Artin–Mazur series of $x^2+1$ is transcendental for every odd characteristic | An actual source-owned older question; the new local and carry proofs do not provide its missing all-level integer count/automaticity input | Full question remains unproved; no cheap decisive bridge has been identified |

These are different mathematical questions: rational multiplicative cohomology
versus the analytic/algebraic nature of the unweighted integer counting series.
They share a one-dimensional positive-characteristic setting, not a claimed
new Hénon subtype. No third complete question is opened. The brief algebraic-
group, torus, and affine-map source searches were pre-screening only.

RLG5 is already the fourth admitted contract; PC424-L covers all primes and
unicritical degrees; UL4 and OM4 each remain one contract. CGR5 remains a
GR5 extension. None is relabelled here. The integer tame-spectrum gaps and
the counterexample to a purely dyadic nine-period exclusion are not reopened.
This scout adds **zero** admitted contracts and **zero** completed papers.

## 1. M6 — frozen full question before proof assessment

For every prime $p$, put $k=\overline{\mathbf F}_p$. For every integer
$d\ge2$ and every $c\in k$, let $f(x)=x^d+c$ on $\mathbf A^1(k)$.
For a nonzero rational function $g\in k(x)^\times$, an admissible ordinary
primitive cycle $O$ means a finite native $f$-cycle all of whose points are
neither zeros nor poles of $g$. Its observable is

$$P_g(O)=\prod_{a\in O}g(a)\in k^\times.$$

Every distinct point is used once. One application of $f$, not Frobenius,
a return-map renormalization, or a selected iterate, is one tick.
There is no restriction on the degree of $g$, on primitive periods, or on
their divisibility by $p$. The full proposed implication is

$$
\left[P_g(O)=1\text{ for every admissible primitive cycle }O\right]
\Longrightarrow
\left[\exists h\in k(x)^\times:\ g=h\circ f/h\right]. \tag{M6}
$$

The conclusion requires a transfer in the original rational function field,
not an algebraic extension, its perfection, or an iterate of $f$.
A complete proof would cover every displayed quantifier. One allowed triple
$(p,f,g)$ satisfying all periodic conditions but admitting no rational $h$
is a decisive negative answer to this universal implication. The periodic
product hypothesis is not replaced by products over a finite field alone.

If this is phrased as an equality of a kernel with a coboundary group,
there is an additional domain issue: *all* rational coboundaries need not
satisfy these pointwise periodic conditions. The implication (M6) avoids
assuming that false converse; §1.3 records an explicit diagnostic for it.
A classification of the entire rational kernel, with repaired domain and
saturation conventions, is not claimed to have been completed here.

### 1.1 Source subtraction and genuine remaining difficulty

The already admitted PC424-L result concerns additive polynomial observables
and polynomial transfers. Its proof uses a polynomial normal form, a full
possibly nonreduced cyclic algebra, and adjacent-level carry certificates.
It does not identify $k(x)^\times/(f^*-1)k(x)^\times$ or eliminate divisor
denominators. Taking a formal logarithm is not a valid conversion over $k$.

The closest actually read regularity source is Roques, *On the reduction
modulo p of Mahler equations*, Theorem 2, Proposition 4 and Corollary 5,
printed pp. 57–60 ([published paper](https://www.jstage.jst.go.jp/article/tmj/69/1/69_1493172128/_pdf)).
Its monomial-base result starts with an already algebraic solution in the
ordinary Laurent-series field and assumes the base degree is prime to $p$.
It supplies no ordinary-cycle-to-algebraic-solution implication. Its finite
extension analysis and the rationality conclusion inside the specified
Laurent field must both be subtracted, not advertised as a new M6 bridge.

Even before an existence bridge, rational multiplicative transfers must
solve the integral divisor equation

$$\operatorname{div}(g)=f^*\operatorname{div}(h)-\operatorname{div}(h).$$

Ordinary $k$-valued products can miss its $p$-divisibility obstruction,
because $k^\times$ has no nontrivial $p$-torsion. This supplies the cheapest
decisive check: test the local divisor coefficient at a totally ramified
fixed point of a monomial. No computation or parameter census is needed.

### 1.2 Complete negative proof of (M6)

**Status: the proposed affirmative implication is false.** For every prime
$p$, set

$$d=p+1,\qquad c=0,\qquad f(x)=x^{p+1},\qquad g(x)=x.$$

The map is separable: $f'(x)=x^p$ is not identically zero. Thus the example
does not merely exploit an inseparable base map.

1. Let $a\ne0$ have ordinary least period $n\ge1$. Then
   $a^{d^n-1}=1$. The whole cycle avoids the only finite zero of $g$, and

   $$P_g(O)=a^{1+d+\cdots+d^{n-1}}.$$

   Since $d-1=p$ as an integer, its $p$th power is

   $$P_g(O)^p=a^{d^n-1}=1.$$

   In characteristic $p$, $X^p-1=(X-1)^p$, so $P_g(O)=1$. This covers
   every admissible ordinary cycle, including periods divisible by $p$.
   The fixed point $0$ is excluded exactly by the frozen admissibility
   convention, since $g(0)=0$.

2. Suppose a rational $h$ satisfied $g=h\circ f/h$. Write
   $m=\operatorname{ord}_0(h)\in\mathbf Z$. Since $f$ is totally ramified
   of local degree $d$ at its fixed point $0$,

   $$\operatorname{ord}_0(h\circ f/h)=(d-1)m=pm.$$

   But $\operatorname{ord}_0(g)=1$, so this would require $pm=1$ in
   the group of integers. This is impossible. No degree restriction on
   $h$ was used.

This proves the full negative answer. The obstruction is removed only by
leaving the conclusion's rational field: in $k(x^{1/p})$, the element
$h=x^{1/p}$ has $h\circ f/h=x$. Also $g^p=f(x)/x$ is already a rational
coboundary. Its fractional valuation explains why this example does not
contradict Roques's ordinary-Laurent-field theorem.

### 1.3 Why a bare rational “kernel equality” needs a domain convention

In characteristic $5$, take $f=x^2$, $h=x-1$ and the reduced quotient

$$g=h\circ f/h=x+1.$$

The fixed cycle $O=\{1\}$ is admissible for $g$, but $P_g(O)=2\ne1$.
Thus cancellation of zeros of $h\circ f$ and $h$ does not justify
telescoping their values at the cancelled point. This is separate from
the $p$-divisibility obstruction above, not a second candidate.

A repaired kernel problem could specify transfers regular and nonzero on
the cycles being tested, or allow omission of finitely many cycles and
explicitly formulate a saturation. Those are changed questions; no such
repair is silently adopted or counted as a new result in this scout.

### 1.4 Substantiality decision

The negative proof is useful as an immediate falsifier for a literal
multiplicative reformulation of PC424-L. But its entire new content is the
elementary characteristic-$p$ root fact and one divisor coefficient. It
does not classify the full kernel for nonmonomial $c$, construct an algebraic
transfer, or supply a target-arithmetic bridge. An absence of an exact
matching title in a bounded search cannot turn this into an independently
substantial paper. **Reject as a new contract; retain as auxiliary.**

## 2. Z6 — frozen native ordinary-zeta question

For every odd prime $p$, put $k=\overline{\mathbf F}_p$ and fix precisely

$$f_p(x)=x^2+1:\mathbf A^1(k)\longrightarrow\mathbf A^1(k).$$

For every integer $n\ge1$, let

$$N_{p,n}=\#\{a\in k:f_p^{\circ n}(a)=a\}
=\deg\operatorname{rad}(f_p^{\circ n}(x)-x),$$

where the radical contains each distinct irreducible factor once. Define

$$Z_p(t)=\exp\left(\sum_{n\ge1}N_{p,n}\frac{t^n}{n}\right)
=\prod_{O\text{ ordinary primitive cycle}}(1-t^{|O|})^{-1}.$$

These are integer counts and a characteristic-zero formal series; they
are not traces computed in $k$. The native clock is one application of
$f_p$, and no periods, places, or wild layers are dropped. Infinity is not
counted; the projective version differs by $(1-t)^{-1}$, which does not
change rationality or transcendence.

The complete prospective statement is

$$Z_p(t)\text{ is transcendental over }\mathbf Q(t)
\quad\text{for every odd prime }p. \tag{Z6}$$

A proof must cover all odd primes and all native levels. A single odd
prime with a proved algebraic $Z_p$ refutes (Z6). A finite coefficient fit,
nonrationality without exclusion of algebraicity, or a natural-boundary
claim for a different weighted/tame series does not settle it. The exclusion
of $p=2$ is declared at freezing: that derivative-zero case has
$N_{2,n}=2^n$ and $Z_2=(1-2t)^{-1}$.

### 2.1 Actual closest-source and internal collision

Bridy's 2012 paper explicitly ends with the rationality problem for this
$x^2+1$ family, Question 2. Therefore neither the object nor asking its
rationality is new. The monomial and additive examples there are proved
through exact ordinary counts and automatic-sequence arguments; they are
not a theorem for general quadratic maps ([primary paper, §§1–4](https://arxiv.org/pdf/1202.0362)).

Bridy's dynamically affine classification, Theorems 1.2–1.3, supplies the
power/Chebyshev/Lattès and additive/subadditive cases. Moreover, Conjecture
1.6 in the arXiv v2 explicitly proposes transcendence for every separable
rational map over $\overline{\mathbf F}_p$, followed by the $x^2+1$ example.
Thus even Z6's stronger transcendence formulation is a subfamily of an
explicit source-owned conjecture ([primary paper](https://arxiv.org/pdf/1306.5267)). In particular $p=3$ is
source-covered, since $x^2+1=x^2-2$ there. That known positive control is
subtracted, not presented as progress on the remaining primes.

Byszewski–Cornelissen–Houben's Theorem A improves the dynamically affine
case to a rational/non-holonomic dichotomy and treats a tame series. Their
definition requires an actual finite quotient of an affine isogeny, and
their introduction explicitly excludes $x^2+1$ from that class when
$p\ne2,3$. The kernel-count reduction in Lemma 3.1 does not apply without
this structure ([primary paper, §§1.2–1.4, 3](https://arxiv.org/pdf/1904.04942)).

The older internal [R3 multiplicity-source report](../../continuation_round3/x1_multiplicity_sources/REPORT.md)
already records these source boundaries while investigating an upper
multiplicity estimate for PC424-L. This scout does not claim to discover
them anew. Z6 differs from PC424-L's completed polynomial-kernel question,
but sharing its map or its failed multiplicity approach is not evidence
that the count-series question has now become easy.

### 2.2 Tests against the actual recent proof interfaces

| Proved input inspected | What it genuinely supplies | Why it does not settle Z6 |
| --- | --- | --- |
| [R5 Hasse-carry proof](../../continuation_round5/a2_excluded_congruence/PROOF_PACKAGE.md), claim and §§1–3; [characteristic-two addendum](../../continuation_round5/a2_excluded_congruence/CHARACTERISTIC_TWO.md), claim/dependency table | Ordinary cycle-sum detection and finite polynomial divisibility certificates; a basis for the full cyclic algebra of dimension $d^n$ | The dimension counts nonreduced length, not $N_{p,n}$. The certificates do not compute the dimension of the reduced algebra or an integer recurrence/automaton for it |
| [R5 independent carry review](../../continuation_round5/reviews/e8_excluded_congruence/REVIEW.md), closing source/multiplicity discussion | Confirms that the completed proof does not rely on an all-$c$ root-multiplicity growth bound | The older maximum-multiplicity route has not silently become a proved consequence of the new carry argument |
| [UL4 full-local-inertia proof](../../continuation_round3/a3_interlevel_contacts/FULL_LOCAL_INERTIA.md), exact claim and §§1–3 | One canonical degree-$p^e$ small-cycle factor for $P_s=(1+s)z+z^2$ over $k((s))$, with full local cyclic inertia | This is a local deformation with $s\ne0$, not a formula for all reduced periodic factors of the fixed $x^2+1$ map over $k$ |
| [OM4 optimal-cycle proof](../../continuation_round4/a1_optimal_cycle_measures/PROOF_PACKAGE.md), original question through proof strategy | Coupled small cycles and convergence for every allowed nontrivially valued field and $0<|\lambda-1|<1$ | It gives one selected local cycle at each $p$-power level, not the integer count of all ordinary cycles at every $n$ |

The last domain mismatch is concrete. Every nonzero element of $k$ is a
root of unity and has absolute value $1$ for any nonarchimedean absolute
value. A constant multiplier $\lambda\in k$ therefore has either
$\lambda-1=0$ or $|\lambda-1|=1$. It never satisfies
$0<|\lambda-1|<1$. Passing to a nonconstant deformation changes the
parameter; specializing back does not preserve numbers of distinct roots
without a separate theorem. Setting $s=0$ is outside UL4's stated field
parameter and is not an allowed use of its generic factor count.

No RLG5 or good-model theorem changes this counting obstruction. Their
number-field descent and affine-lattice questions have different objects
and outputs, so they are preserved without being re-proved here.

### 2.3 Cheap discriminant and exact missing bridge

The useful no-program diagnostic is whether an available input gives a
complete arithmetic description of the sequence $N_{p,n}$, rather than
only a polynomial quotient, one local branch, or the set of detectable
observables. The source route would require, for each odd $p$, enough
all-$n$ structure to contradict the necessary automaticity of the integer
logarithmic-derivative coefficients of an algebraic series after reduction
modulo a suitable auxiliary prime. Alternatively an independently justified
analytic singularity mechanism for the *ordinary full* series would suffice.

Neither input is supplied by the recent proofs inspected above. In
particular, $\deg(f_p^{\circ n}-x)=2^n$ yields only the multiplicity-weighted
series $(1-2t)^{-1}$; using it for $Z_p$ would erase exactly the distinction
at issue. Showing that some root is parabolic or that one ramification
tower is infinite does not by itself exclude cancellation or control every
other ordinary periodic component.

**Status: NOT CURRENTLY JUSTIFIED.** This is a potentially substantial old
problem, but not a candidate with a cheap decisive full bridge established
in this bounded pass. It is not refuted, and no worldwide claim that it
remains open is made. Do not allocate a manuscript or count it toward the
fifth slot from this report alone.

## 3. Access, searches, and execution limits

Instructions used: complete current `idea-creator`, `novelty-check`, and
`proof-writer` entries; repository/batch AGENTS, SCOUT_PLAN, and complete
Route-A batch skill/workflow. The batch's §2 substantiality test is what
prevents the elementary M6 falsifier and the unbridged Z6 question from
becoming paper slots. The fixed two-candidate/current-session/no-computation
allocation overrides broad brainstorming, external-model and GPU examples
in the generic skills. No external-model verification is represented as run.

The relevant local library is the Hénon proof/source collection. The other
repository's root paper stream was not searched or edited. The older M6
source exclusions in [the prior PC source audit](../../../research_c424_c428/continuation_round6/positive_characteristic/SOURCE_AUDIT.md)
were actually read, together with the R3 report and the recent proof passages
identified above. This is selective actual-proof reading, not a claim of
re-auditing all 517 carry-proof lines, all 491 reversor-proof lines, or every
earlier review in this pass.

Primary-source body access:

- Roques: published Theorem 2, Proposition 3/4, Corollary 5 and their
  displayed proofs, with the ordinary Laurent-field hypotheses preserved.
- Bridy 2012: the complete 11-page arXiv v2 text, including both theorem
  proofs and Question 2. Its old date is not a 2026 result.
- Bridy 2016: arXiv v2 body for the introductory statements, Conjecture 1.6,
  definitions, and the displayed kernel-count proof in Lemma 2.4;
  the publisher PDF open timed out. No full re-proof of its classification
  is claimed here.
- Byszewski–Cornelissen–Houben: introduction, definition, Theorem A/B,
  future-question paragraph, recurrence discussion, and Lemma 3.1/counting
  reduction. The 31-page paper was not fully audited in this scout.

Core M6 searches included `rational multiplicative Livsic finite fields`,
`polynomial dynamics periodic orbit products rational coboundary positive
characteristic`, and `finite fields coboundary rational functions
multiplicative`, followed by exact rational/algebraic Livšic variants.
Core Z6 searches included `Artin-Mazur unicritical rationality`,
`Artin-Mazur polynomial positive characteristic rational transcendental`,
`zeta function quadratic Bridy finite fields`, and `Bridy Question 2 zeta`.
Follow-up formulations explicitly used 2024/2025/2026, arXiv-filtered
184-day recency, the date window 2026-03-09 through 2026-09-10, and
Google-Scholar/Semantic-Scholar site filters. These were ordinary indexed
web searches, not authenticated database exports or exhaustive citation
tracking. Some broad queries returned irrelevant formal Artin–Mazur groups,
twisted group algebras, or old seminar pages with fresh crawl dates; these
were not mathematical proof sources. No checked exact later solution of
Z6 or full rational M6 kernel classification was located in this bounded
pass. That negative retrieval result is not a novelty certificate.

The scout used read-only searches/source opens, hand reasoning, and edits
to this single lane report. **Mathematical program executions: 0. New/reused agent
tasks: 0. External model/API uploads: 0. GPU jobs: 0. Git/shared-index/
manuscript/evaluator writes: 0. PDF generation or downloaded-file writes: 0.**
Remote PDFs were read through the browser; no mathematical finite probe or
period-parameter expansion ran. The counterexamples were checked directly
against their frozen universal quantifiers in §1, not inferred from a table.

## 4. Handoff

Reusable negative interface: ordinary $k$-valued multiplicative periodic
products need not detect $p$-divisibility in the integral divisor transfer
equation, even for a separable unicritical base. Both the all-cycle
verification and the all-rational-degree exclusion are proved in §1.2.
The cancelled-zero example in §1.3 additionally blocks careless telescoping.

Unclosed interface: an all-level ordinary count/automaticity or analytic
singularity theorem for the fixed $x^2+1$ maps is still needed to use Z6.
Existing carry certificates, local inertia and optimal-cycle convergence
do not have this output. No new computation is requested on the strength
of this report.

The coordinator can preserve this rejection and continue other independently
authorized bridges. This lane supplies no fifth contract and makes no target
Euler-factor, root-number, automorphy, zero-correspondence or Hilbert–Pólya
claim. `NO_BAD_EULER_OR_ROOT_NUMBER` remains unchanged.
