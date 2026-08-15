# Independent Manuscript Review — Round 1

**Paper:** *Exact 2-Adic Valuation of Higher-Period Multipliers for a Frozen
PCF Quadratic*  
**Review date:** 2026-08-14  
**Reviewed manuscript SHA-256:**
`5e76f3039d51489d18bb8caf525bc6e0546aa86746d19bfa8202cdf289065812`  
**Reviewed pre-review PDF SHA-256:**
`36cf7d4f50ef712e3208565d081a57dd5602a828c3eedc5ad50e4386603bf8be`  
**Bound source-lock SHA-256:**
`205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1`  
**Bound official-result SHA-256:**
`847564ffb9e69aee2018dfa179490fafa81b733ad58231dab9202b82623f3ce6`  
**Review mode:** fresh independent mathematical, evidentiary, citation, and
presentation review of the frozen pre-review package.

I did not author or revise the manuscript, proof package, source lock, code,
results, citations, figures, or integrity records. I did not execute the
registered candidate, extend its period range, access a prime table or
Riemann-zero dataset, or use the network. The only project artifact created in
this round is this review.

## Verdict

**PASS_WITH_MINORS**

**Overall score:** 8.6/10  
**Confidence:** 0.97  
**Mathematical status of the main theorem:** `PROVABLE_AS_STATED`  
**Critical findings:** 0  
**Major findings:** 0  
**Required minor findings:** 4

The main valuation theorem, rational-integrality corollary,
Frobenius--Hensel model, two-coefficient obstruction, cycle-polynomial
identities, and repeat-return argument survive independent line-by-line
attack. The finite table is an exact transcription of the frozen JSON, and the
manuscript consistently labels it as a development-seen implementation audit
rather than prospective evidence. I found no counterexample, broken
quantifier, false period promotion, rational/modulus/exponent conflation, or
Route claim inflation.

The paper is strongest as the scoped arithmetic-dynamics technical note that
its plan claims it to be. The general local lemma and most Hensel machinery are
standard; the defensible contribution is the exact frozen specialization,
odd-quotient corollary, explicit norm coordinate, concrete residue obstruction,
and unusually disciplined proof/evidence boundary. Four small precision edits
should be made before finalization. None requires a new experiment, a source-
lock change, or a weaker theorem.

## Scores

| Dimension | Score | Assessment |
|---|---:|---|
| Mathematical correctness | 9.4/10 | All stated theorem and proposition conclusions are correct under their displayed hypotheses. |
| Proof completeness | 9.0/10 | The logical chain closes; two standard local-field/Hensel bridges should be written out to remove avoidable referee friction. |
| Significance | 6.8/10 | Useful but deliberately narrow frozen-parameter result; appropriate for a specialized technical note. |
| Standalone novelty | 4.5/10 | Consistent with the package's own search-bounded estimate: low novelty for individual ingredients, moderate novelty for the frozen certificate as a whole. |
| Scope and semantic discipline | 9.8/10 | Rational equality, modulus-only equality, exponent equality, repetition, formal period, finite evidence, and Routes A/B remain separated throughout. |
| Evidence and reproducibility | 9.8/10 | Frozen hashes, one-shot lifecycle, 12 exact target decisions, 38-test JUnit record, strict manifest, and figure/build records cross-close. |
| Writing and visual presentation | 8.8/10 | Clear and compact; Figure 3's internal type is marginally small at compiled-page scale. |

## Mathematical audit

### 1. Local sharp-boundary lemma — PASS

The escape step is correct: if $|z|>1$, then
$|z^2+c|=|z|^2>|z|$. The open unit disk is forward invariant when
$|c|<1$. If an exact cycle of length at least two entered that disk, its
successive adjacent-point distances would satisfy

$$
|f(z_j)-f(z_{j+1})|=|z_j-z_{j+1}|\,|z_j+z_{j+1}|
<|z_j-z_{j+1}|,
$$

and strict decrease around the full cycle would return to the original pair,
a contradiction. Hence every point is a unit, and the chain rule gives the
exact norm $|(f^n)'|=|2|^n$. The exclusion of $n=1$ is necessary: the frozen
map has two different fixed-point residue classes, so the manuscript is right
not to extend this unit-cycle conclusion to fixed points.

### 2. Eisenstein specialization and rational quotient — PASS

$Q(U)=U^3-2U^2+2U-2$ is 2-Eisenstein. Consequently
$K\otimes_{\mathbb Q}\mathbb Q_2$ is one totally ramified cubic field, the
place above two is unique, $u$ is a uniformizer, and

$$
2=\frac{u^3}{u^2-u+1},\qquad v_u(2)=3.
$$

At every extension place, Theorem 3.1 applies with $c=-u$ and gives
$w(B_C)=0$, hence $w(\Lambda_C)=n w(2)$. For rational $\Lambda_C$, the
periodic coordinates are roots of the monic polynomial $g^n(X)-X$ over
$\mathcal O_K$, so $B_C$ is an algebraic integer. The equality
$B_C=\Lambda_C/2^n\in\mathbb Q$ then gives $B_C\in\mathbb Z$, and the local
unit statement makes it odd. This genuinely strengthens the predecessor's
$2^n\mathbb Z$ divisibility boundary without claiming that oddness excludes
$B_C=\pm1$.

The theorem should merely specify that the chosen cycle field $L/K$ is finite;
see M1 below. This is a domain-of-notation repair, not a change to the proof.

### 3. Frobenius--Hensel model — PASS

Modulo $u$,

$$
g^n(X)-X\equiv X^{2^n}-X,
$$

whose derivative is $-1$. Hensel lifting therefore gives one root in each of
the $2^n$ residue classes of $\mathbb F_{2^n}$, and the count exhausts the
degree-$2^n$ polynomial. If $\alpha$ has exact Frobenius degree $d\mid n$,
the unique lift as a root of $g^d-X$ is also a root of $g^n-X$; uniqueness in
the residue class identifies it with $z_\alpha$. Reduction then excludes any
smaller positive dynamical period. The manuscript uses this bridge correctly,
but should state the middle sentence explicitly (M2).

Both $\sigma(z_\alpha)$ and $g(z_\alpha)$ solve $g^n-X$ and reduce to
$\alpha^2$, so Hensel uniqueness proves
$\sigma(z_\alpha)=g(z_\alpha)$. Iterating and multiplying gives

$$
B_C=\prod_{j=0}^{n-1}g^j(z_\alpha)
=N_{K_{u,n}/K_u}(z_\alpha).
$$

Thus exact dynamical period, exact Frobenius degree, and formal dynatomic
period are not conflated.

### 4. Modulo-two expansion and periods two through four — PASS AFTER MINOR EXPOSITION REPAIR

Because $(2)=(u^3)$ and the degree-$n$ extension is unramified, the implicit
coefficient ring is

$$
\mathcal O_{K_{u,n}}/(2)
\simeq \mathbb F_{2^n}[\bar u]/(\bar u^3).
$$

Writing Teichmuller coefficients and using $v_u(2)=3$ kills the cross terms in
the square modulo $u^3$. The equation
$\sigma(z_\alpha)=z_\alpha^2-u$ therefore gives
$z_\alpha\equiv\alpha+u+u^2\pmod 2$. With
$t=u+u^2$, one has $t^2\equiv u^2\pmod{u^3}$, and expansion of
$\prod_j(\alpha_j+t)$ yields exactly

$$
B_C\equiv
1+e_{n-1}u+(e_{n-1}+e_{n-2})u^2\pmod 2.
$$

The two signs have the same reduction modulo $(2)$, so $B_C=\pm1$ forces
$e_{n-1}=e_{n-2}=0$. The irreducible lists are correct:

- degree two: $T^2+T+1$;
- degree three: $T^3+T+1$ and $T^3+T^2+1$;
- degree four: $T^4+T+1$, $T^4+T^3+1$, and
  $T^4+T^3+T^2+T+1$.

No degree-two or degree-three polynomial passes the two-coefficient gate,
whereas $T^4+T^3+1$ is irreducible and does pass. The paper correctly calls
this a witness to insufficiency, not an equality cycle. The displayed proof is
mathematically right, but the quotient-ring basis and vanishing-cross-term
step should appear in the manuscript rather than remain implicit (M3).

### 5. Cycle polynomial and repetition — PASS

From $u+z_j=z_{j-1}^2$,

$$
P_C(g(X))=\prod_j(X^2-z_j^2)
=(-1)^nP_C(X)P_C(-X).
$$

Since the fixed point $-a$ cannot belong to an exact cycle of length at least
two, cancellation at $X=-a$ is legitimate. Substitution at $-a$, $0$, and
$u$ gives the stated values at $a$, $-u$, and $u$ with the correct signs. The
warning that a single-cycle polynomial need not lie in $K[X]$ prevents a
Galois overreach.

The root-of-unity argument also closes. Prime-to-two roots of unity inject into
$\mathbb F_2^\times$, and a root of 2-power order at least four generates an
even-degree extension of $\mathbb Q_2$, which cannot be a subfield of the
degree-three field $K_u$. Hence $\mu(K_u)=\{\pm1\}$. If a rational repeated
return has ordinary absolute value $2^{nr}$, then $B_C^r=\pm1$ and therefore
$B_C=\pm1$. The manuscript correctly keeps the point's least period equal to
$n$, not $nr$, and makes no modulus-only inference without rationality.

## Registered-result and provenance audit

The source lock fixes periods $2,\ldots,7$, both signs, exact symbolic
arithmetic, and no post-null extension. Every registered period was disclosed
as development-seen before the lock; `new_blind_periods=[]`. I independently
parsed the current frozen files and obtained:

| $n$ | Run | $\deg\Psi_n^{\rm set}$ | Exact cycles | $\deg\gcd(B_n-1)$ | $\deg\gcd(B_n+1)$ | Time (ns) |
|---:|---|---:|---:|---:|---:|---:|
| 2 | R042 | 2 | 1 | 0 | 0 | 63,931,487 |
| 3 | R043 | 6 | 2 | 0 | 0 | 174,504,404 |
| 4 | R044 | 12 | 3 | 0 | 0 | 411,053,181 |
| 5 | R045 | 30 | 6 | 0 | 0 | 1,637,080,691 |
| 6 | R046 | 54 | 9 | 0 | 0 | 4,033,271,287 |
| 7 | R047 | 126 | 18 | 0 | 0 | 16,919,324,815 |

The times sum to exactly `23,239,165,865 ns`. All twelve exact rational field
norms are nonzero and factor exactly as Table 2 reports; the printed degree-2,
degree-3, and degree-4 exact components agree coefficient-by-coefficient with
the serialized $1,u,u^2$ arrays. The terminal record is the sole
`REGISTERED_RUN_0001` record and says `COMPLETED_NO_HIT`, with one immutable
claim and all six frozen periods started and completed.

The JUnit XML contains 38 distinct test cases, zero failures, zero errors, and
zero skips. The result manifest lists 12 regular files; all 12 SHA-256 values
recompute correctly, and its missing, extra, nested, symlink, unsupported,
unsafe, and semantic-error lists are empty. The independent result-integrity
record is consistent with those observations.

The finite classification is therefore exactly
`BASE2_EQUALITY_ABSENT_N2_TO_N7_DEVELOPMENT_SEEN`. It is not a blind split and
cannot establish an all-period theorem. The proof-backed classification is
separately `EXACT_2ADIC_VALUATION_ALL_PERIODS_CERTIFIED_BY_PROOF`, while the
equality question remains `OPEN_FOR_N_GE_4`. The manuscript gets all three
levels right.

One phrase should be calibrated: gcd and resultant are mathematically
equivalent nonintersection certificates, even though they are implemented by
separate exact code paths. Calling them simply "independent target tests" can
suggest stronger epistemic independence than the package establishes (M4).

## Citation, originality, and genealogy audit

The manuscript uses all 12 bibliography keys, the compiled bibliography
contains all 12 entries, and no key is missing or unused. The local citation
verification ledger records primary publisher, DOI, or official arXiv checks
for each entry. Within the no-network boundary of this review, every manuscript
use stays within that verified claim envelope:

- Silverman and Morton--Silverman supply standard arithmetic-dynamics and
  formal-versus-least-period context;
- Benedetto--Ingram--Jones--Levy and Rivera--Letelier supply neighboring
  non-Archimedean attracting-cycle/strict-threshold context, not the present
  equality proof;
- Hutz and Rajagopal--Zhang supply good-reduction period context, not the
  specialized Hensel norm identity;
- Buff--Gauthier and Murakami--Sano--Takehira supply multiplier-locus and
  multiplier-polynomial context, not a value-specific frozen conclusion;
- Benedetto--Goksel is correctly limited to neighboring Misiurewicz/unit
  arithmetic;
- Ji--Xie--Zhang is used only for global exponent-spectrum context;
- Wang is used only to document the frozen parameter's genealogy. No result,
  empirical table, prime data, or zero data from that article enters the proof.

The immediate project predecessor proves only the global
$\Lambda_C\in2^n\mathbb Z$ boundary and explicitly leaves
$|\Lambda_C|=2^n$ open for higher periods. This manuscript advances that
genealogy by proving exact local valuation, oddness of the rational quotient,
and equality exclusion at periods two and three. It re-proves the short
integrality step instead of making an unpublished local artifact the sole
support of a theorem.

The novelty posture is honest. The package's search-bounded estimate of 3/10
for the general local lemma and 4.5/10 for the frozen certificate is credible;
no historical-first claim is made. This modest depth would be a venue-fit risk
for a broad journal, but it is not a correctness defect and does not block the
declared specialized technical-note form.

## Devil's Advocate stress test and adjudication

### Strongest counter-argument

A skeptical referee can argue that the headline theorem is mostly an immediate
application of a standard non-Archimedean observation: once every nontrivial
cycle is forced onto the unit circle, the multiplier formula already gives
$|\Lambda|_2=|2|_2^n$, and the 2-Eisenstein cubic only supplies the convenient
uniformizer. The Frobenius--Hensel correspondence is likewise a familiar
good-reduction mechanism. The development-seen computation contributes no
prospective confirmation and stops at seven despite a pre-lock observation at
eight. On that reading, the paper does not solve its most interesting residual
question, $B_C=\pm1$ for all $n\ge4$, and its protocol machinery may look
larger than its mathematical advance.

### Adjudication

This objection is **validated as a significance and venue-fit limitation**, not
as a mathematical defect. The manuscript explicitly calls the local lemma
standard, makes no priority claim, labels every finite period as development-
seen, and boxes the all-period equality question as open. The new frozen
content is narrower but real: exact valuation at every extension place, the
odd rational quotient, the local norm coordinate, the two-coefficient
obstruction, and the degree-four insufficiency witness. For the declared
technical-note scope, that supports `PASS_WITH_MINORS`; it would not support a
claim of a broad rigidity theorem or a breakthrough equality exclusion.

**DA-CRITICAL adjudication:** no DA-style Critical issue was found. There is no
validated or unresolved Critical item to block acceptance.  
**DA-MAJOR adjudication:** no Major issue was found. The depth objection is
fully disclosed and cannot be repaired by overstating novelty.

## PDF, figures, build, and release audit

I inspected all 11 pages of `paper_pre_review.pdf` at rendered page resolution.
There is no clipping, overlap, corrupt glyph, missing figure, missing reference,
or illegible raw-table entry. The PDF is letter size, unencrypted, contains no
JavaScript, and has embedded/subset fonts. `manuscript.pdf` and
`paper_pre_review.pdf` are byte-identical at the reviewed SHA-256.

The current LaTeX log contains no error, citation/reference warning, overfull
box, or underfull box. The build script has valid shell syntax, fixes
`SOURCE_DATE_EPOCH`, `FORCE_SOURCE_DATE`, and `TZ`, and contains no candidate
execution. I did not rebuild the bound snapshot because this review was
strictly read-only; instead I checked the current build inputs, the identical
bound PDFs, the final log, and the existing two-build byte-identity record.

All 32 figure-manifest input/artifact paths currently hash to their recorded
values. The determinism record reports two byte-identical generations of all
nine PDF/SVG/PNG outputs. Figures 1 and 2 clearly carry the theorem/open and
development-seen boundaries. Figure 3 correctly labels the quartic witness
"necessary only." Its box and cell type is nevertheless marginal at 100%
compiled-page scale; the optional presentation fix below would improve print
readability.

## Required minor revisions

### M1. Specify the cycle field in Theorem 4.1

**Severity:** Minor  
**Evidence Anchor:** text: Theorem 4.1, p. 5, "let $L$ contain its coordinates"  
**Confidence:** 5/5 — core expertise: local and algebraic number fields

**Problem:** A place and completion are invoked for $L$, but the statement only
says that $L$ contains the coordinates. Since the coordinates are algebraic,
the intended finite extension is available; it should be stated.

**Exact fix:** Replace the opening by, for example:

> Let $L/K$ be a finite extension containing the coordinates of the exact
> period-$n$ cycle $C$, and let $w$ be an additive non-Archimedean valuation of
> $L$ above the unique valuation of $K$ over two.

No theorem or proof conclusion changes.

### M2. Write the $d\mid n$ Hensel-uniqueness bridge explicitly

**Severity:** Minor  
**Evidence Anchor:** text: Proposition 5.1 proof, p. 6, "the same uniqueness applied to $g^d(X)-X$"  
**Confidence:** 5/5 — core expertise: Hensel lifting and finite fields

**Problem:** The conclusion is correct, but the current sentence suppresses the
reason the two Hensel lifts are the same element.

**Exact fix:** Add the following bridge before the exactness-by-reduction
sentence:

> Let $y$ be the unique lift of $\alpha$ solving $g^d(y)=y$ in
> $K_{u,d}\subset K_{u,n}$. Since $d\mid n$, $y$ also solves $g^n(y)=y$;
> uniqueness among roots of $g^n-X$ reducing to $\alpha$ gives
> $y=z_\alpha$.

### M3. Make coefficient comparison modulo two self-contained

**Severity:** Minor  
**Evidence Anchor:** equation: Section 6, equations (14)--(16), especially the coefficient comparison after equation (15)  
**Confidence:** 5/5 — core expertise: ramified local rings and norm expansions

**Problem:** The calculation is right, but the manuscript does not explicitly
identify the quotient ring in which $1,u,u^2$ are compared or explain why the
cross terms vanish. This is the only compressed step in the proof of the
period-two/three exclusion.

**Exact fix:** Add three short facts:

1. $(2)=(u^3)$ and
   $\mathcal O_{K_{u,n}}/(2)\simeq
   \mathbb F_{2^n}[\bar u]/(\bar u^3)$;
2. cross terms in $(\alpha+b_1u+b_2u^2)^2$ contain a factor $2$ and vanish
   modulo $u^3$;
3. for $t=u+u^2$, $t^2\equiv u^2\pmod{u^3}$, so
   $\prod_j(\alpha_j+t)=e_n+e_{n-1}t+e_{n-2}t^2+\cdots$ gives (15), with
   $e_n=1$ and $e_k\in\mathbb F_2$.

This closes the exposition without changing Proposition 6.1.

### M4. Calibrate the two-certificate independence wording

**Severity:** Minor  
**Evidence Anchor:** text: Introduction, contribution 4, p. 2, "two independent target tests"  
**Confidence:** 5/5 — direct comparison of manuscript and frozen implementation contract

**Problem:** Gcd nonintersection and nonzero resultant are algebraically
equivalent. The package establishes separately implemented exact code paths,
not statistically or logically independent evidence. Appendix B already says
they are equivalent decisions obtained by independent code paths.

**Exact fix:** Replace "two independent target tests" and similar unqualified
phrasing by:

> two separately implemented but algebraically equivalent exact target
> certificates (gcd and resultant/field norm)

The evidence remains strong; the edit only states its independence class
precisely.

## Optional presentation polish

**Figure 3, p. 6:** enlarge the internal flow-box/table/control text or split
the figure into two panels/figures. The vector original is sharp and readable
under zoom, but several labels are marginal at normal print scale. This does
not affect the scientific verdict.

## Round-2 acceptance gate

Round 2 may return `PASS` if and only if:

1. Theorem 4.1 states a finite cycle-field extension and a place/valuation on
   it;
2. Proposition 5.1 explicitly links the $g^d-X$ Hensel lift to the $g^n-X$
   lift when $d\mid n$;
3. Section 6 states the quotient-ring basis and the vanishing-cross-term/norm-
   expansion steps;
4. the gcd/resultant paths are described as separately implemented but
   algebraically equivalent certificates;
5. the manuscript, retrospective claim/integrity indexes, and PDF hashes are
   refreshed consistently, the paper builds cleanly, and the existing safe
   test suite remains green.

No new candidate execution, higher-period cutoff, prime/zero data access,
numerical match, theorem weakening, bibliography expansion, or source-lock
revision is required.

