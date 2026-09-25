# Independent mathematical review — ASFS-20260915-PTI01

**Candidate status:** STOP — EXACT FULL FLAT-TRACE SEQUENCES HAVE NO HILBERT TRACE-CLASS POWER REALIZATION.  
**Review date:** 2026-09-15  
**Reviewer:** spectral_integrality_reviewer, separate author/reviewer invocation  
**Review conclusion:** No mathematical blocker found; the sole minor source-locator clarification is ADDRESSED.  
**Calibration:** NOT_CALIBRATED; model review is not human peer review or formal verification.

## Scope and provenance

This review covers the [paper](../paper.md), [frozen card](../candidate-card.md),
[claim ledger](../claim-ledger.md), [summary](../README.md), and
[evidence record](README.md). The reviewer also read the complete
[153 proof](../../153-saturated-sieve-flat-trace/paper.md), the applicable
AGENTS.md and plan, and the current research entry point. The review did
not edit the author's five core files or any other candidate.

The author and reviewer ran in separate invocations within the same model
family. The reviewer declared the criteria below before the 157 manuscript
was available and reached an initial no-blocker mathematical assessment
before receiving the controller's message that its own read-only check
had found no blocker. That later status message was visible; this is not
a claim of fully blinded or statistically independent review. A separate
read-only source checker located the Simon reference without reading the
author's draft; the reviewer then directly verified the relevant source
passages. Neither role separation nor source verification certifies
mathematical correctness.

ARS was used only for bounded claim/evidence/counterargument discipline.
No venue criteria were supplied: criteria_binding_unavailable. No venue
fit, editorial decision, external publication, or formal Route evaluation
is attempted.

## Predeclared criteria and results

| Criterion | Authority / trigger | Result | Evidence anchor and reason |
| --- | --- | --- | --- |
| Exact same-object sequence | Frozen card; changing roof, weights, multiplicity, or all-powers quantifier would block | MEETS | equation: Paper (1)–(2), (11); all integer components, section points and unit roof retained |
| Complete dyadic asymptotic | Missing endpoint exceptions or an unbounded proper-divisor remainder would block | MEETS | equation: Paper (4)–(6); c_1=2, exact endpoints, and an exponentially smaller all-divisors remainder |
| General complex trace-class argument | Assuming positivity/normality, ignoring phases, or omitting the compact spectral gap would block | MEETS | equation: Paper (9)–(10); Lemma 3 and Proposition 4 handle every peripheral phase and arbitrary Jordan structure |
| Citation scope | Exact theorem clauses must have checkable support; imprecise standard-theorem locator is a minor warning | MEETS; W1 ADDRESSED | text: Current Paper Section 4, "absolute eigenvalue summability through (3.4.14)"; the added Kostenko locators explicitly support the spectral clauses |
| Negative-result boundary and controls | Promoting this result to all operator frameworks, or using finite agreement as a proof, would block | MEETS | equation: Paper (13)–(14); finite-cutoff models are explicit controls and broader frameworks remain outside the theorem |

These are proof-validity criteria, not numerical quality scores.

## Mathematical findings

### S1 — The PNT normalization includes the whole return ledger

**Evidence anchor:** equation: Paper (3)–(8).

For k>=2 the integer definition gives exactly 2^k<p<=2^(k+1).
The k=1 exception really contains both 2 and 3. Multiplying the two
separate PNT expansions by m/2^m makes each error o(1); the remaining
coefficient is (2m/(m+1)-1)/log 2. The proper-divisor estimate uses
d<=m/2 and c_d<=2^d, including d=1, so R_m/2^m tends to zero along
every integer m. It therefore justifies the actual full-sequence limit,
not a special-subsequence surrogate.

The scalar denominator is lambda^m(1-lambda^(-m))^2. Consequently the
scalar/two-form exponential scale is 4/3, whereas the one-form scale
is 2. All three have coefficient 1/log 2. The integral bound places
that coefficient strictly between 1 and 2 without any unproved
irrationality assertion or numerical approximation.

### S2 — Peripheral cancellation and nonnormality are addressed

**Evidence anchor:** equation: Paper (9)–(10), with Lemma 3.

The summable nonzero eigenvalue list has an attained largest modulus,
finitely many eigenvalues there, and a strict gap to the remainder.
The remainder bound is valid with algebraic multiplicity. The rho<1
case gives a zero limit. If rho>1, division by rho^m forces the finite
peripheral phase sum to converge to zero. Lemma 3 rules this out by
extracting each phase coefficient using Cesaro averages. At rho=1
the same extraction leaves only the phase 1, with its positive integer
algebraic multiplicity.

The initial review plan allowed a Cesaro square-mean cancellation test.
The author's coefficient-extraction lemma is a valid, stronger direct
replacement: multiplying a convergent sequence by a unit phase keeps
the o(1) error Cesaro-small and identifies every Fourier coefficient.
No assumption of a positive, normal, self-adjoint, or diagonalizable
operator is made. The treatment of Jordan blocks and the separable
reducing subspace for a possibly nonseparable Hilbert space is correct.

### S3 — Determinant and cutoff controls have the correct scope

**Evidence anchor:** equation: Paper (11)–(14).

Equality of ordinary fixed-operator determinant germs near zero forces
the same normalized logarithmic coefficients, hence all the impossible
power traces. The statement does not conflate trace-class determinants
with Fredholmness of I-zU, or with parameter-dependent operator families.

The finite-packet model has trace norm
(sum of retained K_p) times sum_{ell>=1} ell lambda^(-ell), which is
finite. Its cyclic permutation traces give exactly (14). Retaining all
packets with K_p<=M indeed reproduces every complete target with m<=M.
Thus arbitrarily long finite-prefix agreement coexists with the proved
all-powers obstruction. This is a valid adverse control, not a substitute
geometric owner.

## Minor clarification

### W1 — Give an explicit locator for the complete spectral input

**Severity:** Minor.  
**Evidence anchor:** text: Initial reviewed Paper Section 4 before the citation clarification, "their nonzero eigenvalues form an absolutely summable list with algebraic multiplicity".  
**Confidence:** 5 — direct comparison of the cited passages and the theorem's actual hypotheses.  
**State at initial review:** Clarification requested; not a mathematical blocker.

Dai's cited Section 3.1, printed pp. 36–37, explicitly supplies the
trace-class ideal property and Lidskii's formula, but that short passage
does not explicitly spell out absolute eigenvalue summability or the
word "algebraic" for multiplicity. The manuscript's theorem input is
correct; the needed improvement is a more precise companion citation,
not a different proof.

The reviewer verified the author-hosted primary paper
[Simon, Notes on Infinite Determinants of Hilbert Space Operators](https://math.caltech.edu/SimonPapers/74.pdf):
Section 1, pp. 246–247, gives the compact-spectrum and algebraic-multiplicity
conventions; Theorem 2.3, p. 251, (2.7), with p=1, gives absolute
eigenvalue summability; Corollary 4.3, p. 258, gives Lidskii's formula.
Theorem 4.2 on the same page supports the ordinary determinant product.
These statements do not require normality or self-adjointness. This was
an available companion reference, not a requirement to cite this specific
paper or expand the author's reference list unnecessarily.

**Adjudication: ADDRESSED, 2026-09-15.** The author instead added precise
[Kostenko, Trace Ideals with Applications](https://users.fmf.uni-lj.si/kostenko/teach/IdealsNotes.pdf)
locators: Theorem 2.3.1, p. 12; the algebraic-counting convention, p. 36;
(3.4.14) at p=1, p. 37; and Theorem 3.4.7, p. 41. The reviewer directly
checked each passage and found the required support. Section 4 also now
spells out polynomial spectral mapping and algebraic multiplicities for
powers. That explanation is correct. No change to the frozen sequence
or the theorem was made, and no additional Simon citation is required
in the author's core files.

## Source checks and limitations

The reviewer directly opened
[De Angelis, The Classical Proof of the Prime Number Theorem](https://vdeangel.xula.edu/Notes/PNT.html).
Its opening theorem section defines pi(x) with p<=x and explicitly
states the equivalent x/log x asymptotic used in (5). No deeper result
from that article is needed here.

The reviewer directly opened
[Dai, Lectures on Dirac Operators and Index Theory](https://web.math.ucsb.edu/~dai/book.pdf),
Section 3.1, printed pp. 36–37, and checked its ideal property and
Theorem 3.1.2. Kostenko now supplies the explicit companion clauses;
Simon was used as an independent source cross-check. No source's
unrelated integral-kernel, Anosov, or
continuation result is transferred to the present noncompact map.
The first source inspections used browser text. The Kostenko browser
open timed out, so the reviewer independently read that exact source
through curl and pdftotext standard output without saving a PDF. The
successful commands were the following, with the final two extracting
the printed p. 36 algebraic-counting passage missed by the broader search:

~~~bash
curl -L --fail --max-time 30 https://users.fmf.uni-lj.si/kostenko/teach/IdealsNotes.pdf | pdftotext -layout - - | rg -n -A 30 -B 15 'Theorem 2.3.1|Theorem 3.4.7|3.4.14|algebraic multiplicities|separable Hilbert'
curl -sSL --fail --max-time 30 https://users.fmf.uni-lj.si/kostenko/teach/IdealsNotes.pdf | pdftotext -layout - - | sed -n '1755,1795p'
curl -sSL --fail --max-time 30 https://users.fmf.uni-lj.si/kostenko/teach/IdealsNotes.pdf | pdftotext -layout - - | sed -n '1795,1825p'
~~~

All three commands exited 0. These are source-text locators, not claims
of a local-PDF structural preflight or a complete reading of the notes.

The small-m identities were checked by direct substitution:
N_1=2, N_2=6, N_3=8 and T_0(1)=12, T_0(2)=216/25,
T_0(3)=1728/361. These finite arithmetic checks do not prove the
asymptotic or spectral statements. No numerical experiment, finite
matrix fitting, or human-peer-review claim was used.

## Review-file verification receipt

A read-only Node check resolved every local Markdown link from this
report's directory, checked its candidate ID and exact candidate status,
and checked trailing whitespace and table continuity. Output:
files=1, local_links=6, failures=[]. The command
git diff --check -- papers/157-power-trace-integrality-audit/evidence/review.md
also exited 0 without output. This validates report metadata and links,
not the mathematical claims.

## Handoff

Stop the exact ordinary Hilbert trace-class all-powers realization
contract ASFS-20260915-PTI01; retain the proved obstruction as a
search control. The same-object ledger remains intact. The negative
result does not undo 153's distributional flat traces or its graded
identity, and does not exclude all regularized, local meromorphic,
Banach, or non-trace-class frameworks. Such alternatives require their
own exact contracts. Formal Route coordinates remain UNASSIGNED and
Route B remains NOT INVOKED.
