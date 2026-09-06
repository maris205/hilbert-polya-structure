# C407 paper plan

2026-09-06. Approved theorem contract: `../BATCH_PLAN.md`, C407.

**Working title:** Zero-dimensional Cantor limit sets for hyperbolic
finite-adelically distorted orbit counting.

**One-sentence contribution:** Every genuinely distorted positive-entropy
hyperbolic FAD system has a Cantor accumulation set for native normalized
prime-orbit counting, with covering number at most a fixed constant times
`(1+log(1/epsilon))^(2d)` for `d` active primes.

**Type and audience:** Pure mathematical research article for readers in
arithmetic/topological dynamics and p-adic analysis. No venue has been chosen.
English main text, anonymous author block; an independent Chinese abstract
will be supplied separately. No fabricated human identities, affiliations,
funding, journal-readiness claim, or publication-priority certificate.

**Scope:** The entire approved image theorem and its FAD corollary. All
proofs remain in the main text. Seven numbered sections plus abstract and
references. No appendix, experimental section, page quota, or length padding.

## Claims–evidence matrix

| Claim | Evidence | Status | Main-text location |
|---|---|---|---|
| Polylogarithmic image covers and zero upper box dimension | Adaptive center-dependent partition; exponential series and valuation tails | Complete proof, independently checked | Sections 2–3 |
| Positive finite-type radial sums are nonconstant | Exact negative Fourier coefficients, lexicographic type dominance, summable DCT | Complete proof, independently checked | Section 4 |
| Every detector cylinder has nonconstant image; no isolated image points | Local rescaling; CRT-compatible detector; classical negative-integer slice | Complete proof, independently checked | Section 5 |
| Hyperbolic FAD orbit limits obey the image theorem | Exact BCH v2 Theorem 12.4.3(ii), equation (12.4), and phase reduction | Classical input plus proved image theorem | Section 6 |
| Missing regimes are genuinely realized | Two-prime solenoid, wild additive map, product | Classical fixed counts and elementary parameter identification; not separate novelty | Section 6 |
| 2024 source-local problem resolution, without absolute priority guarantee | BCH v2 Problem 14.1.1; explicit 2026 book-version gap | Bounded verified scope only | Introduction and Section 7 |

## Section plan

### Abstract

Start with the Cantor/zero-upper-box conclusion, define the normalized
orbit-counting observable and the meaning of hyperbolic, state the
polylogarithmic estimate, and distinguish covering from perfectness. Name
the multiprime/wild scope without an undefined acronym or unqualified first
priority claim. Approximately 180–230 words, subordinate to accuracy.

### 1. Introduction and prior work

Motivate why a bounded oscillatory orbit count still needs a topology
classification. Locate the explicit BCH 2024 open hyperbolic regimes and
state the present conclusion early. Compare the older `S`-integer detector,
the abelian-variety one-prime result, and the full FAD cardinality result.
One compact comparison table should distinguish source hypotheses and
conclusions, not merely enumerate citations. Explain the two proof tasks:
thinness does not imply perfectness. Attribute the negative-integer slice
to BCH. Include the 2026 source-version qualification and a short roadmap.

### 2. A finite-adelic image theorem

Define `v_p(0)=infinity`, all radial kernels and their value at zero,
positive periodic `r`, finite nonnegative real exponent types with own-prime
coprime periods, common period `w`, and active primes. Define the closed
diagonal detector group `D` and uniformly convergent real function `Phi`.
State the complete finite-versus-Cantor theorem, covering convention and
zero dimensions. Make the quantifier order explicit: constants may depend
on all fixed data, not on epsilon. Explain which hypotheses are used only
for perfectness.

### 3. Adaptive valuation covers

Prove the `1+(p-1)LK` partition bound using occupied balls, including the
constant truncated valuation assertion. Prove exponential valuation-tail
control for every active finite type, including `s=0<t`. Choose explicit
truncation lengths and depths; telescope products and bound both series
tails. Deduce the covering estimate, empty interior and zero upper box and
Hausdorff dimensions. Do not replace the adaptive count with `p^K`.

### 4. Fourier nonconstancy of positive radial series

Specify Haar probability, the chosen high-conductor characters, and the
translation convention. Prove the uniform ball-indicator expansion,
coefficient sign, exact tame coefficient, and wild first-term asymptotic.
Prove the finite-type dominance in all cases, with `t` minimized first.
Use a summable majorant to pass the high-conductor limit through countably
many integer translations. Then state and prove the exact local rescaling
lemma, separating constant outside-ball and inactive terms. No hidden
uniformity in all centers or all balls is claimed.

### 5. Perfectness of the full detector image

Prove the exact CRT description of `D`, not just a subgroup inclusion.
Given any nonempty relative open set, choose a product cylinder and fix
other coordinates at negative ordinary integers in their prescribed balls.
Credit this classical slice choice. Verify all sliced coefficients are
strictly positive and summable. Use the coprime exponent period to place an
active center in the varying ball. Apply Section 4 to every cylinder;
exclude an isolated image value by its open preimage. Finish the Cantor
characterization and the finite undistorted formula. Retain the independent
reviewer's outside-hypothesis period example only if approved as a scope
illustration; it is not needed for the approved proof.

### 6. Hyperbolic FAD dynamics and realized examples

Define confined systems, primitive orbits, `pi_f`, the FAD fixed-count
formula and gcd-sequence convention, and the exact unique-dominant-root
meaning used from BCH. State the source detector theorem precisely with
the trivial phase and identify all of its data with Section 2. Prove the
corollary by this named reduction. Present the two-prime `Z[1/15]`-dual
doubling system, odd-characteristic `x^p+x`, and their product at `p=7`.
Record the correct periods, active-prime counts, growth bases and resulting
logarithmic upper bounds. Counts, LTE and product closure are classical.

### 7. Scope and conclusion

State the distinction between topology, metric dimension and fibers. Do not
claim injectivity, nonatomic pushforward, sharp logarithmic exponents,
infinite-prime extension, signed-weight extension, nonhyperbolic topology,
or target-zero/arithmetic correspondence. Preserve the final EMS-book
priority gap. Close with concrete questions about optimal covering scales
and fibers, not an inflated general conclusion. Include concise provenance
and disclosure statements: proof-only data availability; no human subjects;
anonymous/unconfirmed human CRediT/funding/COI; actual AI-assisted research,
drafting and current-team checks, with no human peer-review claim.

## Figure and table plan

No figure is needed: numerical plots cannot prove the infinite topology
statement and a diagram would repeat the short proof roadmap. A small
Table 1 compares the known one-prime/no-wild result, the 2024 missing
hyperbolic regimes, the present theorem, and the excluded nonhyperbolic
setting. Its caption must state that the prior-work column is version-bound
to BCH v2. It is a theorem-scope comparison, not experimental evidence.

## Citation plan and ownership deductions

Use four verified primary works only, with exact locators in each substantive
context. An inline `thebibliography` is authorized; no unused entries or
placeholder citations are required.

1. BCH, arXiv:2209.00085v2, 19 April 2024: Definitions 7.1.1–7.1.2 and
   10.3.9; detector equation (12.4)/Theorem 12.4.3(ii); Theorems
   12.5.1–12.5.2, the proof of 12.5.1, Remark 12.5.3, Problem 14.1.1;
   examples and Proposition 9.1.4 for realized systems.
2. Byszewski–Cornelissen, ANT 2018, DOI 10.2140/ant.2018.12.2185:
   Proposition 9.4 and Theorem 9.5, earlier one-prime orbit-limit topology.
3. Everest–Miles–Stevens–Ward, JRAM 2007,
   DOI 10.1515/crelle.2007.056: Theorem 1.1 and Section 2/Lemma 2.4/
   Corollary 2.5 in the author preprint, earlier detector and injectivity.
4. Cornelissen–Park, arXiv:2605.24504v2, 19 June 2026:
   Theorem C/Section 4 for the distinct Cesàro observable, reference 6 for
   the forthcoming EMS book. Do not merge that unobtained book with v2.

The original Bridy proposition will not be an unread bibliography entry.
Its attribution, if mentioned, will explicitly be through BCH Example 7.2.7.
Proofs of elementary lemmas are supplied, so citations are not added solely
to decorate a self-contained argument. `SOURCE_AUDIT.md` records the actual
read scopes and bounded searches.

## Review feedback and authorized clarification

The independent nonauthor report
`../wild_ordinary/CROSS_REVIEW_ARITHMETIC_TOPOLOGY.md` gives
`PASS_MATH_AND_2024_SOURCE_SCOPE` and identifies no mathematical blocker.
Its sole minor attribution finding is accepted: BCH already owns the
negative-integer slice choice. Contract/proof/scout wording has been
clarified without changing any mathematical statement. The manuscript
credits that input explicitly. Root also independently checked the proof,
source definitions and realized examples before admission.

## Workflow and handoff

The `paper-plan` and `paper-write` claim-to-evidence, complete-argument and
citation checks are used, together with `proof-writer` and the relevant ARS
writing/integrity guidance. The authorized pure-mathematics batch overrides
ML venue, word/page quotas, external/old-model review defaults and redundant
approval interviews. No full ARS staged product, human-read attestation,
programmatic citation certification or calibrated journal recommendation
is claimed.

Create modular LaTeX under `paper/`. A draft compile, if performed, uses a
unique `mktemp -d` directory under `/tmp` with actual exit/log reporting.
Root owns the later nonauthor manuscript review, final dual fresh builds,
all-page PDF QA, formal Route-A evaluation and release/Git operations.
