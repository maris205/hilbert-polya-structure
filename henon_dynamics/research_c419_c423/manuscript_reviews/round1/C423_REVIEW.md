# C423 — first independent full-manuscript review

2026-09-08 UTC. Reviewer: current-team spectral-lane agent, not the
author of the C423 manuscript or CP9's proof draft. I previously
reviewed CP9's mathematical proof; that prior involvement is disclosed
and is not being relabeled as a fresh or externally independent
review. The present report follows an actual new, complete reading of
the production manuscript and its PDF text.

This is internal AI-assisted nonauthor review, not human peer review,
blind review, an external GPT-5.4 invocation, a calibrated acceptance
score or a Route A evaluation.

## Verdict

**PASS for round-one full-manuscript mathematical and transcription
review, with zero mandatory corrections.**

The manuscript states the admitted classification with the correct
arbitrary-field and geometric-parameter quantifiers. Its two external
inputs are separated from its own arguments. The two-cycle witness,
the exact height coefficient, the reduction to the function-field
setting, both nonzero-difference cases, and the elementary sufficiency
argument survive transcription into the article without a mathematical
gap found in this review.

The two optional suggestions below concern local wording and exposition,
not missing hypotheses in the theorem or invalid proof steps. No new
mathematical execution is requested.

The next appropriate state is the separately required second full-text
review after the author/coordinator has disposed of the optional edits.
This report does not certify final release, final two-directory build
reproducibility, all-final-page visual inspection, global novelty or
submission readiness. No numerical score is assigned: the batch has no
selected journal or ML venue, and manuscript review is separate from
formal evaluation.

## Actual input identity and access

Unless otherwise indicated, manuscript paths below are relative to
papers/C423_two_cycle_preperiodicity/ within research_c419_c423/.

The actual reviewed PDF is builds/author_polished/main.pdf, not the
earlier baseline:

- Title: A two-cycle test for simultaneous preperiodicity in characteristic three.
- Six pages, 317245 bytes, anonymous 11-point article.
- SHA-256: b0aa1ace124faa50d14ff50873a5acaa70c5691c01772cd96cd74bd03626f408.

Every production TeX/Bib input was read completely, including the scope
table. All ten input hashes were checked again before writing this
report and still identify the same files:

| Input | SHA-256 |
| --- | --- |
| main.tex | dc722535544c9cd6def684c3808e5e281f53033b642bbc0b19f66f8d71d5c31c |
| math_commands.tex | 5f1b7b35077808bd827b7d7ddf2b01310b52c33b148e28da411fc4c8f3fcb006 |
| references.bib | 4437129d8e6274755fc6a57ffd2c371d5aa678027ce689026ab82215b88bf3e5 |
| sections/0_abstract.tex | cacc5f0ee72e79bf35e75a887b328b601360abda2e24e5fb8c49918b945abee6 |
| sections/1_result.tex | 1c7d7a71f75bb6e44b7545d4238f25aec0dbd27391491121f0689600bc237d07 |
| sections/2_inputs.tex | 6a5b0a6d52e636e0f061efb95b0b8e6c11d559c067981e862df6081a9fb8818e |
| sections/3_witness.tex | 7dd6ee8d2fee48b4e9a1dc2c4fcc17409bbf193924179de1035ed71b11b6d3c9 |
| sections/4_classification.tex | 9215ececa351d9886720c137dcc7c307dfaaba39f20be4f46517dc550f1ba1c1 |
| sections/5_scope.tex | d5b86ea9e52594b30213189a7dc194306405de7ecebc116597ad61bfc000837c |
| tables/source_scope.tex | 79ba16c90c7569ad4d620b0d55d3eec9adc295a16a49abf5c2574f9a62397788 |

The complete six-page PDF text was extracted directly from that actual
PDF to standard output and read through the bibliography. This is a
fresh manuscript read, not a read of only a proof summary or a prior
PASS. The current final TeX log was searched for
Warning/Overfull/Underfull/undefined/Error; there were no matches.
The search's exit status 1 means no matching text, not a failed build.
PDF metadata were inspected separately.

I did not visually inspect rasterized pages of the author_polished PDF
in this review. The coordinator's earlier visual reading of baseline
pages is not claimed as my own or as a current-PDF visual gate. No
compiler, mathematical checker, experiment, Git mutation or author-file
edit was run here.

## Accepted proof and previous review comparison

The following were actually read completely, not accepted merely from
their verdict labels. These paths are relative to research_c419_c423/:

| Input | Extent and SHA-256 |
| --- | --- |
| continuation_round9/charp_alternatives/PROOF_DRAFT.md | All 209 lines; 75cb7f6fe2abb7b77cc721b1354003c3416d34f5525823a6bb9806c38ebb73e4 |
| continuation_round9/charp_review/REVIEW.md | All 357 lines; f05a9e4f44165bbe242d25e10a60390b9eedfaaf921ddf5d4d7557b4b7170675 |
| continuation_round9/CP9_ADMISSION_REVIEW.md | All 142 lines; cb5536a61e331624ac5679b5768695aceb17c57989d4c0b29dd5ab3b10920044 |

The complete 41-line C423 PAPER_PLAN.md was also read. The actual
production text, rather than an assumed correspondence between old
proof and new theorem labels, was checked against this evidence.

The previous proof review's two optional clarifications are already
implemented in the manuscript:

1. The witness really has least period two, because equality of its
   two points would make the marked point constant
   (sections/3_witness.tex:42).
2. Equal f-values imply sufficiency by applying the one-point lemma to
   the fixed mark a and then joining b's orbit after one iteration,
   not by treating a parameter-dependent image as a fixed mark
   (sections/4_classification.tex:48).

These observations are checks of what is actually printed, not an
assumption that the old review automatically establishes the new one.

## Mathematical and transcription checks

### 1. Statement, constants and scope

Theorem 1.1 quantifies over every characteristic-three field L and
every pair a,b in L. The set of allowed parameters lies in the chosen
algebraic closure, not necessarily in L. The constant field k is
defined inside that algebraic closure, so saying that the two marks
are constant is meaningful even if L does not contain all of k.
The two alternatives are both retained: both marks constant, or equal
f-values. No quotient by an orbit relation replaces the actual pair.

The degree decomposition gives equal weights 3 and 3. The manuscript
therefore does not apply a strict-weight classification to this
binomial. Its scope table and conclusion concern the stated source
regimes and this one residual polynomial. They do not claim a theorem
for arbitrary equal-weight binomials, finite exceptional-set bounds,
or infinitely intersecting orbits for two fixed maps.

### 2. External inputs and their use

The specialized necessary relation, the separate universal local-height
statement and their attributions are consistent with the selected
source passages checked below. The constant/nonconstant distinction is
kept when the reduction is invoked. The displayed arithmetic for the
nonzero difference has exponent two and right-hand side one in
characteristic three, leaving exactly the two signs.

Crucially, Proposition 2.2 concludes equality at every parameter in
the completed algebraic closure at every relevant place; it is not
limited to the originally assumed common-preperiodicity set. Thus
applying it at the deliberately separating parameter is legitimate.
The polynomial is fixed, monic, degree six, defined over k and has
zero constant term. Its equal weights do not add an unavailable
strict-weight premise to the height input.

The later proof constructs a finite extension of a perfect closure
and places the entire assumed infinite set in its algebraic closure
before invoking Proposition 2.2. It does not silently apply a
one-variable function-field theorem to an arbitrary high-dimensional L.

### 3. Exact orbit and escape calculation

The three translation/evenness identities in (3.3) are correct in
characteristic three. Substitution of the printed parameter

    lambda_* = 1 - a - f(a)

gives precisely the two printed paths:

    a -> 1-a -> a,
    b -> -a-1 -> 0 -> lambda_*.

The second path uses the positive difference assumption; no additional
root choice or hidden relation on b is needed. For transcendental a,
the first path has least period two, not merely period dividing two.

At a pole with C = |a|_v > 1, the sixth-power term uniquely dominates
at a and in lambda_*, so both relevant absolute values are C^6.
For |z|_v > C, its sixth power strictly exceeds both the fourth-power
term and the parameter term. Consequently the escape identity is an
equality for every subsequent iterate, with no cancellation or
discreteness assumption.

The indexing is also correct: b first reaches lambda_* at iterate
three, but that value already has absolute value C^6. Thus

    |F^n(b)|_v = C^(6^(n-2))  for n >= 3,

and normalization by 6^n gives log(C)/36, not log(C)/216. This is
an exact infinite-time height calculation, not a finite numerical
orbit sample. The first path is finite and has height zero.

### 4. Arbitrary-field reduction

Under a nonzero difference and the assumption that the marks are not
both constant, neither mark can be constant: otherwise the other
would satisfy a polynomial over the algebraically closed k and would
also lie in k. Therefore swapping the marks handles the negative
difference using the same pole construction.

For the positive difference, b is algebraic over k(a). The printed
union K_0 contains all unique purely inseparable roots of a; since k
is perfect, this is the perfect closure of k(a). Adjoining b gives
a finite extension K/K_0 of exactly the required type.

If a is preperiodic at a parameter lambda, some iterate difference
F_T^n(a)-F_T^m(a), n>m, vanishes there. For m>=1 the two degrees
in T differ; for m=0 the second term is constant. The leading
sixth-power term at each stage prevents cancellation of the larger
degree. Hence the equation is nonzero and lambda is algebraic over
k(a).

It follows that every parameter in the assumed infinite set belongs
to the relative algebraic closure of K inside the chosen algebraically
closed ambient field. That relative closure is an algebraic closure
of K: any root of a polynomial over it is algebraic over K by
transitivity. No separability, finite generation of the original L,
or replacement of the original infinite set by an unproved subset
is involved.

A place above the pole of a can be extended through the stated
algebraic extensions and still has |a|_v>1 with constants units.
The constructed lambda_* belongs to K. Universal height equality
therefore contradicts the exact witness heights. Both signs are
removed, leaving the equal-value conclusion.

### 5. Single-mark infinitude and sufficiency

For a constant mark, any constant parameter lies with it in a common
finite field preserved by the map. There are infinitely many such
geometric parameters.

For a nonconstant mark, P_n(T)=F_T^n(a)-a is monic of degree
6^(n-1). The unique fixed parameter T_0=a-f(a) is a simple root
of every P_n: the chain-rule recurrence uses f'(a)=a^3 and gives
the printed nonzero polynomial sum in the transcendental a.
This remains nonzero when n is divisible by three.

For each prime integer ell>=2, P_ell has degree greater than one.
Simplicity of T_0 forces another geometric root; its least period
divides ell and is not one, so it equals ell. Different primes
cannot select the same parameter. This proof needs neither
separability of every root nor a claim that all parameters for
different n are distinct. It explicitly includes ell=3.

Finally, equality of f(a) and f(b) makes the two forward orbits
coincide after one iteration. Applying the lemma to the original
fixed mark a proves simultaneous preperiodicity for infinitely many
parameters. The manuscript gives both directions of the classification.

### 6. English, references and presentation

The article defines its family in the abstract, defines the iteration
clock and geometric parameters before the theorem, states its two
external propositions separately, and includes all remaining proofs
in the body. No central proof is replaced by a link to the research
record. The abstract's height factor, the theorem, the orbit display,
the lemma's prime quantifier and the concluding scope agree.

The bibliography has two actually relevant entries rather than an
artificial citation quota. The text distinguishes original attribution
from the source in which the precise height statement was inspected.
The AI-assistance and internal-review disclosure is explicit.

No unresolved reference or obvious malformed mathematical statement
was observed in the complete PDF text. The following two local
suggestions would make an already correct argument easier to read.

## Mandatory corrections

None.

## Optional suggestions

### O1 — keep the nonconstant qualification local in the abstract

Location: sections/0_abstract.tex:8, especially lines 9–12.

The theorem correctly retains every constant pair. The following
sentences then say that both nonzero differences are eliminated and
that the second point escapes at a pole of a, without locally
restating that these assertions concern the nonconstant case.
The full abstract and theorem make the intended restriction
recoverable, so this is not a contradiction in the theorem or proof.

Suggested wording:

    We eliminate both in the nonconstant case by an explicit two-cycle
    test. For a nonconstant pair with positive difference, ...

This prevents an isolated reading of those sentences as excluding
constant pairs with nonzero f-value difference.

### O2 — one explanatory clause for the relative algebraic closure

Location: sections/4_classification.tex:85.

The statement that the relative algebraic closure is an algebraic
closure is correct. Since passage from an arbitrary ambient field
is a highlighted feature of the article, the author could append
a short reason:

    ... is an algebraic closure of K, since algebraicity is transitive.

No new field hypothesis or additional lemma is required. This is an
optional reader aid, not a missing argument on which the verdict depends.

## Primary-source access during this manuscript review

No fresh search-engine queries were issued. A direct arXiv HTML open
and follow-up finds failed and are not counted as content access.
The fallback [Lee–Nam version-2 PDF](https://arxiv.org/pdf/2509.15079v2)
was accessible as extracted text. I read the selected introduction
and setup statements, Section 2 through Theorem 2.1 and its following
explanation, and Theorem 4.4 with Remark 4.5. These confirm the two
input applications and the specific residual example. This was not a
complete rereading of all source proofs.

The [version-specific arXiv record](https://arxiv.org/abs/2509.15079v2)
was also opened and confirms the 11 October 2025 version date.
A source-PDF screenshot request failed; no visual source-PDF read
is claimed.

The original Ghioca–Hsia body was not opened in this review. Its
[publisher DOI](https://doi.org/10.4064/aa241119-28-10) and journal
metadata are carried from the coordinator's primary-metadata receipt;
the precise height statement was checked in Lee–Nam. The manuscript
discloses that same access boundary.

## Action and review boundary

The only authored output of this task is this report. Initial
read-only path lookups from an abbreviated directory failed and were
corrected by resolving the actual manuscript path; they produced no
mathematical result or file change. A combined log-search/metadata
command stopped after the expected no-match search exit, so metadata
were subsequently obtained in a separate successful command.

No source text, bibliography entry, build artifact, mathematical
certificate, global ledger or Git state was changed. The prior proof
review is explicitly reused as comparison evidence, while this
round's TeX/Bib and complete PDF-text reading are new work. The
coordinator should preserve this raw report and record the disposition
of O1 and O2 before the second manuscript review.
