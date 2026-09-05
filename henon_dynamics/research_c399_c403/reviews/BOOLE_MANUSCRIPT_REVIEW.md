# Boole manuscript-to-proof and citation review

Date: 2026-09-05. Scope: the complete first unnumbered manuscript, not a
compiled PDF or a released paper. Reviewer: the separate current-team agent
that reviewed the original proof, not an author of this manuscript.

## Assessment and action

The manuscript preserves the reviewed mathematical contract. I found no
substantive compression error, omitted load-bearing argument, incorrect
citation context, or newly asserted natural transfer-operator result.
Theorems `thm:main` and `thm:critical` and Proposition `prop:divisor` remain
supported. The prior ownership amendment is substantively incorporated in
the introduction. One minor abstract wording correction is recommended
before the text is frozen: W1 below removes a possible uniqueness claim
about compensation that the theorem does not make.

This is a bounded internal recommendation to proceed with that wording
repair and the coordinator's build checks. It is not journal acceptance,
publication-novelty certification, a full ARS panel, formal Route-A
evaluation, or a completed C-series paper.

Calibration status: `NOT_CALIBRATED`.
Review-target status: `criteria_binding_unavailable`; no venue-fit judgement.

ARS reviewer guidance was used inline for anchored claims, source scope,
criterion-specific assessment and disclosure. The parent assignment limits
this to one actual review; no other personas or reports were simulated.
The current-team context and model-family relationship do not establish
independent error processes. No external manuscript upload, ARS runtime,
schema validator, citation API client, numerical checker, compiler or Git
operation was run in this manuscript review.

## Actual input coverage and byte binding

I read every line of all nine TeX files, all three BibTeX entries, and the
entire plan: 623 lines in total, including the plan and bibliography.
There are exactly seven included section files. I inspected all four
actual `\citep` occurrences, not a citation sample. Comparison used the
previously read and independently reviewed 593-line proof; its current hash
still matches that original snapshot. I did not repeat the all-parameter
proof review or the author's finite checker.

Paths in the following table are relative to `boole/`:

| Input | SHA256 |
|---|---|
| `PROOF_PACKAGE.md` | `9ef4c0d8e3beab75e95be19d5a835e4b491392ce1565589997fa213f0296f725` |
| `PAPER_PLAN.md` | `e633d0970318bbf3666866f2a2d9b9630d2ae37ec1656e71ce0f9c4a8036d8da` |
| `paper/main.tex` | `3c0ac8773f090e4128cf72ae472c641ae38e506eaaa8ad23bc33cf0e63e90d10` |
| `paper/math_commands.tex` | `146265b3722a829eb228c421706e8132f6a5b00e8e30fb0dbbab064d812e6ea2` |
| `paper/sections/0_abstract.tex` | `1f154604bf77c56e6f421bc2eb7486d44cf97326458d0c7acdf64377d1152edb` |
| `paper/sections/1_introduction.tex` | `394e1ff7d6f58c5f138ac70fafd4fabb097982397d94e8d6b7bfd5b7c2dce982` |
| `paper/sections/2_dynamics.tex` | `f3ea7b594e34bb57ac75906d724cd5364aadd96b00495db50993f82172b82255` |
| `paper/sections/3_indices.tex` | `6e3c79d7874a9358cddb3c478ee760e193924a5b2b88c06e20726eef2a1b206e` |
| `paper/sections/4_products.tex` | `148fd977b2b55a46d7b341d972d11ad7c755d631b4470f4223bbc72807861e57` |
| `paper/sections/5_critical.tex` | `e4bfceaaf89ddc36bec47d6ed8b7703406dc15b9e6bb424c85caf207fa33dcb5` |
| `paper/sections/6_scope.tex` | `ea86b39414523dc3d00a514b82dfd9801cf651581cd9d308fc2b469bf8913dec` |
| `paper/references.bib` | `5e151da1071901897c890144bca159ab50247e502abc583f5548f78fb18763d1` |

These hashes identify the reviewed content, not mathematical correctness.
The original `BOOLE_INDEPENDENT_REVIEW.md` remains a separate proof-snapshot
review; this report does not overwrite or retrospectively broaden it.

## Registered manuscript claim mapping

The following are this report's explicitly registered claim groups, each
checked against the source proof. This is a manually anchored review map,
not an ARS machine-readable `claim-registry/1.0` artifact or a claim that
semantic extraction completeness has been mechanically certified.

| ID | Actual manuscript anchor | Claim and scope | Proof dependency | Result |
|---|---|---|---|---|
| BM1 | `1_introduction.tex:7`, `eq:domain`, `eq:definition` | Real $a,b>0$, finite prepole-deleted domain, original clock, denominator $\Lambda-1$ and normalized germ | Steps 1 and 6 | Preserved; no extra state at infinity or time rescaling |
| BM2 | `2_dynamics.tex:13`, `eq:jacobian`, `eq:cauchy`, `eq:escape` | Invariant measures and exact initial-Lebesgue survival law | Steps 1–3 | Preserved; no new ergodicity, mixing or invariant probability on the repeller |
| BM3 | `2_dynamics.tex:42`, `eq:imaginary`, `eq:jet`, `eq:counts` | All-period positive simplicity, real census and critical multiplicity three | Steps 2 and 4 | Preserved; localization and repulsion precede counting distinct real roots |
| BM4 | `3_indices.tex:9`, `eq:critical-index`, `eq:finite-sum`; `eq:tau-main` | All-iterate finite-real weighted sums | Steps 5–6 | Preserved; coordinate correction and off-real subtraction retain their signs |
| BM5 | `4_products.tex:12`, `eq:primitive`, `eq:products-main` | Primitive product on the disk and explicit continuation | Step 7 | Preserved; absolute regrouping and nonzero product tails are present |
| BM6 | `4_products.tex:34`, `prop:divisor`, `eq:resonant`; `eq:entire-main` | Complete logarithmic commensurability divisor, entire iff family and one parameter per positive integer | Step 8 | Preserved, including $q=0$, negative numerator zeros and first-pole necessity |
| BM7 | `5_critical.tex:4`, `eq:fractional-order`; `thm:critical` | Non-meromorphic continuation through $u=1$ only | Step 9 | Preserved; no whole-circle natural-boundary inference |
| BM8 | `5_critical.tex:29`, `eq:reduced-tau`, `eq:uniform-plus`, `eq:unreduced` | Both locally uniform disk limits, specified full fixed-orbit reduction, failure of unreduced upper limit | Step 10 | Preserved in theorem/body; abstract ambiguity W1 does not change the proved statement |
| BM9 | `4_products.tex:69`, `6_scope.tex:5`, `eq:circle` and conclusion | Abstract diagonal realizability; classical circle factor; no natural finite-real transfer or arithmetic target identification | Steps 8 and 11 | Preserved; null-orbit deletion is expressly not an operator restriction theorem |

In particular, the shorter manuscript still supplies the cubic/quintic
recurrence instead of merely quoting the critical index. Its two uniform
bounds remain independent of both $n$ and the approaching parameter.
It still removes both fixed primitives at every repetition, not only their
first-iterate terms. It still distinguishes global geometric-product
continuation from global convergence of the primitive product. These are
the load-bearing compression checks, not conclusions inferred from matching
headlines or finite code output.

The omitted homogeneous-coordinate explanation for degree multiplication
is an elementary background compression, not a new assumption: composition
of relatively prime homogeneous coordinates has no common projective zero,
so the degree remains $2^n$. The paper states this fact before using the
fixed equation; the complete derivation remains in the proof supplement.
No substantive theorem depends solely on the existence of that supplement.

## Bibliography and all four citation contexts

All three references exist and match the stated authors, titles, journals,
dates, volume/issue, article/page identifiers and DOI. In this review I
reopened the official metadata and the relevant journal/author sources.
The earlier proof review had already inspected the specific Mendoza and
Blaschke theorem passages; those same-session primary passages were used
again for context matching.

| Context ID | Actual occurrence and supported scope | Primary support | Result / limit |
|---|---|---|---|
| BC1 | `1_introduction.tex:74`, `umeno2016boole`: three statistical regimes and explicit Lyapunov analysis | [Umeno–Okubo journal article](https://academic.oup.com/ptep/article/2016/2/021A01/2461070), abstract and §§2–3 | Supported. Does not cite this work for the manuscript's weighted divisor or compensated limit |
| BC2 | `1_introduction.tex:75`, `mendoza2022boole`: shifted family, deleted-prepole domain, covered coding/count consequences and supercritical Cantor system | [Publisher PDF](https://revistas.utm.edu.ec/index.php/Basedelaciencia/article/download/4408/7355/27220), §3, Lemma 3.1, Theorems 4.2, 4.4, 4.5 | Supported. “Upper-subcritical” here means $1/2<a<1$; $2^n-2$ is the stated coding theorem's immediate corollary, not necessarily a displayed source formula |
| BC3 | `1_introduction.tex:83`, `bandtlow2017spectral`: the full-circle holomorphic transfer spectrum | [Primary journal PDF](https://www.numdam.org/item/AIHPC_2017__34_1_31_0.pdf), Theorem 5.4 | Supported. Scope is the analytic expanding circle map on an annulus Hardy space, not the punctured real-domain operator |
| BC4 | `6_scope.tex:14`, same Blaschke reference: the classical full-circle determinant mechanism | Same primary PDF, Theorem 5.4 and Remarks 5.5–5.6 | Supported. Equation `eq:circle` is derived in the manuscript; the citation acknowledges the established mechanism, not a claimed literal source formula for physical deletion |

No bibliography entry is orphaned and no citation key is missing. The
Numdam record's own BibTeX verifies the order Bandtlow, Just, Slipantschuk
used in the manuscript, along with the remaining bibliographic fields.
[Primary metadata](https://www.numdam.org/articles/10.1016/j.anihpc.2015.08.004/).
I did not repeat the coordinator's CrossRef content-negotiation request and
therefore do not independently attest its discrepant response.

The initial direct Umeno DOI open failed in the browser; the official OUP
article found by a domain-restricted search provided the journal metadata
and full relevant text. Its theorem numbering differs from the arXiv
version, but the manuscript does not supply conflicting theorem numbers.
The Mendoza publisher metadata and PDF agree with the bibliography,
including volume 7, the 2022 special issue and pages 300–310.
[Publisher record](https://revistas.utm.edu.ec/index.php/Basedelaciencia/article/view/4408).

The introduction now denies novelty credit for the deleted-prepole domain,
classical phase geometry, coding and covered unweighted counts. This
substantively addresses R1 from the proof review. Adding the exact theorem
locators already listed in BC2 would improve reader navigation, but the
current attribution is not misleading or mathematically incomplete.

## Review body

### Strengths

**S1 — compressed proof retains its decisive estimates.**
Evidence Anchor: equation: `eq:jet`, `eq:form-change`, `eq:uniform-minus`,
`eq:uniform-plus`.
The critical calculation and both all-period bounds survive the transfer
to TeX. Neither index nor uniformity is asserted on the strength of sampled
coefficients.

**S2 — correct ownership and operator boundary.**
Evidence Anchor: text: `1_introduction.tex:80`, “symbolic coding or those
counting consequences as new results”; `6_scope.tex:17`, “is a
periodic-product identity”.
The classical inputs are attributed and the source identity is separated
from a natural finite-real operator trace. The distinction is also present
in the abstract, not buried only at the end.

### W1 — avoid suggesting uniqueness among arbitrary renormalizations

Severity: Minor.
Evidence Anchor: text: `0_abstract.tex:12`, “supercritical germs have the
same limit only after deleting”.
Confidence: 5 — comparison with the exact theorem and an explicit alternative.

The proof establishes that the stated complete fixed-orbit deletion works
and that the unreduced family fails. It does not classify every analytic
renormalization. For example,
$$
\widetilde D_a(u)=D_a^{\mathrm{red}}(u)\exp((a-1)u)
$$
has the same locally uniform critical limit and is still normalized at zero,
but is not exactly the fixed-orbit deletion. Thus “only after” should not
be allowed to suggest uniqueness over such a larger class. This is not a
counterexample to `thm:critical`, which makes no uniqueness assertion.

Minimum remedy: say the supercritical germs have the same limit **after**
deleting those complete factors, and separately say the unreduced family
does not converge to the critical germ. No formula, proof, experiment or
source change is required. The author/coordinator owns the actual edit;
this review did not apply it.

## Seven scoped failure-mode assessments

These seven named checks are the requested task-level audit, not a claim
that an ARS seven-gate runtime or calibrated detector executed.

| Failure mode | Criterion source and actual surfaces | Scoped assessment | Limit / decision bearing |
|---|---|---|---|
| F1. Fabricated or mismatched bibliography | Parent's all-reference audit; three BibTeX entries versus primary metadata | MEETS: all three supported, including Blaschke author order | No retraction-history certification or database completeness claim |
| F2. Citation-context overreach | Parent's all-context audit; BC1–BC4 | MEETS: all four uses stay within the cited source scopes | Counts in BC2 are explicitly an inference from coding; no weighted novelty inferred from citations |
| F3. Mathematical compression loses domains, signs, exceptional cases or quantifiers | Proof-writer feasibility criteria; BM1–BM6 and the immutable proof | MEETS: the defining domain, positive weights, infinity correction, $q=0$, resonance necessity and multiplicities survive | No fresh all-proof rerun; the original substantive review remains the proof-level evidence |
| F4. Unsupported analytic continuation or interchange of limits | The stated mathematical contract; BM5, BM7–BM8 | MEETS for the theorem/body: nonzero tails and uniform all-$n$ bounds are retained | W1 is a minor headline precision issue, not a failure of the proved limit |
| F5. Classical reconstruction presented as new or research significance inflated | Parent's ownership remit; introduction and BC1–BC4 | MEETS for explicit ownership and bounded priority language | Publication originality and venue significance remain NOT_ASSESSED; no exhaustive literature search was repeated |
| F6. Invented experiments or code output promoted to proof | Pure-mathematical article type in the plan; §6 reproducibility paragraph and previously inspected exact checker | MEETS for evidence labeling; experiment/statistical efficacy criteria NOT_ASSESSED as inapplicable | Finite diagnostic code exists; no experimental result, statistical claim or new checker run is represented here |
| F7. Product promoted to natural PF/operator, target arithmetic or release approval | Original source contract and parent authority; abstract, BM9, §6 status paragraph | MEETS: these inferences remain expressly excluded | No operator-domain theorem, target-grade promotion, external referee approval, compilation or release judgement |

The relevant reviewer-guidance criteria are argument coherence, theoretical
definition precision, evidence sufficiency and bounded literature
integration. No claim depends on a missing experiment, a minimum reference
count, a presumed journal norm or a numerical review score. The most
important retained uncertainty is publication significance, not a discovered
gap in the current source-system proof.

## Handoff boundary

Only this report was written. The next relevant action is the coordinator's
minor wording adjudication and actual compilation/visual/reference checks.
The `.tex` source and its status paragraph cannot establish the existence,
legibility or deterministic rebuild of a PDF. No such check was performed
or claimed by this reviewer. Later source changes should be tied to their
affected review rows; a one-sentence abstract repair does not require another
full proof review or repetition of the finite checker.

## Targeted amendment receipt — 2026-09-05

I read the amended abstract in full and the revised introduction ownership
paragraph, then measured the actual two file hashes. This is an affected-text
check, not a repeated manuscript review. The original findings and snapshot
ledger above are retained as the historical review record.

| Amended file, relative to `boole/` | Actual SHA256 | Affected review rows |
|---|---|---|
| `paper/sections/0_abstract.tex` | `b84e3afb9584f29828acf478bb0a40d89ffb6e168bce83496c8d6668c43c5fd0` | W1, BM8, F4 |
| `paper/sections/1_introduction.tex` | `d8d34e93f82e3679a934ec4aa99f62c4a2885757e381d58f587275d2edc77d8c` | BC2, F2, F5 |

**W1: RESOLVED.** The abstract now states that the specified fixed-orbit
deletion gives the critical limit and separately states that the unreduced
family does not. It no longer suggests uniqueness among arbitrary analytic
renormalizations. Naming $\operatorname{Li}_2$ as the dilogarithm is accurate
and consistent with its series definition in §4. No theorem, branch
convention, domain or limit scope was strengthened.

**BC2 locator amendment: VERIFIED WITH THE SAME PRIMARY SCOPE.** The added
source §3 locator matches the deleted-prepole definition. Theorem 4.2 is
the critical $a=1$, $b>0$, zero-shift coding result; Theorem 4.4 covers
$1/2<a<1$, $b>0$, zero shift; Theorem 4.5 covers the supercritical binary
Cantor system. These are precisely the primary passages already inspected
for BC2, not new or broader source claims. The explicit upper-subcritical
interval improves precision. The unweighted counts remain identified as
consequences of coding, not as publication-new formulas.

No remaining text correction is required by this review on these amended
surfaces. Earlier judgements on the other inputs remain bound to their
original hashes; this receipt does not claim a new full-source or PDF check.
No TeX/BibTeX edit, compilation, exact-check execution, full proof rerun,
external-review operation or Git operation was performed by this reviewer.
