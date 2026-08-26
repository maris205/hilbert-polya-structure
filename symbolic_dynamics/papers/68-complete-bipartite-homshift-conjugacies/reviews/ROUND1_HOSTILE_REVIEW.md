# Round 1 hostile review

## Provenance and scope

**Provenance:** independent cross-agent review.  The requested GPT-5.4 child
reviewer was unavailable because the agent tree had reached its structural
thread cap.  This report does not claim GPT-5.4 provenance.  The reviewer did
not author P68 and read the manuscript, proof/source ledgers, bibliography,
control source and receipt, build instructions, prior internal review, and QA
artifacts before proposing any edit.

**Release posture:** external release remains **HOLD**.  No priority or
worldwide-novelty conclusion is made.

## Overall verdict

**Verdict:** **MAJOR REVISION; one headline finite-pattern theorem and its
control are false as written.**

**Score:** **4.5/10** at round 0.

The intrinsic dimer conjugacy and the finite-dependence phase argument appear
sound, but Proposition 2.2 confuses local admissibility on an induced graph
with global extendibility to a hom-shift configuration.  Because the abstract,
introduction, evidence ledger, QA report, and deterministic control all call
this an exact all-shape result, it is not a cosmetic defect.

## Strengths

1. The dimer anchors are detected from target-part membership rather than an
   absolute parity origin, which is the correct mechanism for odd-translation
   equivariance.
2. The inverse code uses the same intrinsic matching and `f^{-1}`, so the core
   sufficiency proof is genuinely local and two-sided.
3. The finite-dependence proof isolates a remote copied phase bit and correctly
   derives `p=p^2` without assuming stationarity.
4. The source boundary is unusually explicit: the public checkerboard/MME
   picture, the four-cycle-free obstruction, and the one-sided category are
   all returned to named owners.

## CRITICAL issues

### C1. The claimed globally extendible finite-shape formula is false

**Evidence.** In `sections/2_phase_counts.tex`, Proposition
`prop:patterns` states

```text
N(F)=product_C (m^(e_C)n^(o_C)+n^(e_C)m^(o_C))
```

for patterns on `F` that extend to the full hom-shift.  Its proof lets each
connected component of the induced graph choose its phase independently.
But Lemma `lem:phase` itself proves that every global configuration has one
phase on the whole lattice.  For

```text
F={(0,0),(2,0)},  m=2, n=3,
```

both sites are even.  The manuscript formula gives `(2+3)^2=25`, whereas a
globally extendible pattern has both symbols in `A` or both in `B`, so the
correct count is `2^2+3^2=13`.  A pattern placing one site in `A` and the
other in `B` is locally admissible on the edgeless induced graph but cannot
extend globally.

**Required fix.** Replace Proposition `prop:patterns` by the following exact
statement:

```text
N(empty)=1;
N(F)=m^|F cap E| n^|F cap O| + n^|F cap E| m^|F cap O|
for nonempty finite F.
```

Prove it directly from the two global phase components.  Remove
`C(F), e_C, o_C` wherever they exist only for the false product formula.
Retain the entropy conclusion, which follows unchanged from connected
Følner boxes.  Update every dependent artifact, including
`sections/0_abstract.tex`, `sections/1_introduction.tex`,
`sections/5_pressure.tex` if the scope of the weighted count is described,
`sections/7_scope.tex`, `ARGUMENT_BLUEPRINT.md`, `CLAIMS_EVIDENCE.md`,
`PAPER_CONFIGURATION.md`, `PAPER_PLAN.md`, `PROOF_PACKAGE.md`,
`CONTROL_RESULTS.md`, and `FINAL_QA.md`.

**Control failure.** In `code/verify_complete_bipartite.py`,
`brute_patterns` checks only edges induced by `F`; therefore it enumerates
locally admissible patterns, not restrictions of global points.  The
disconnected test was a false positive for the erroneous component product.
Rename the function or change it to enforce a single global phase, replace
`formula`, and add explicit regression assertions for two remote even sites
and two remote opposite-parity sites.  The frozen receipt must be regenerated.

## MAJOR issues

### M1. The radius-one theorem claims the wrong fixed pair of input sites

**Evidence.** Theorem `thm:classification` says that both local rules inspect
only `v` and `v+e_1`.  Equation (3.2) shows that at a `B`-site the output at
`v` uses `(v-e_1,v)`.  The code is radius one, but it does not always inspect
the fixed pair `{v,v+e_1}`.

**Required fix.** State that the rule at `v` uses `v` and one of its two
`e_1`-neighbours, selected by the visible target part; equivalently its
memory set is `{ -e_1,0,e_1 }` and its radius is one.  Make the same correction
in the abstract, proof package, figure decision, narrative report, and any QA
claim that says “the two sites `v,v+e_1`.”

## MINOR issues

### m1. The dimension range is inconsistent

The abstract restricts the finite-dependence theorem to `d>=2`, whereas
Theorem `thm:fd` and its proof work for every `d>=1`.  Use the proved range
consistently or explain a deliberate restriction.

### m2. The equilibrium uniqueness step should use the joint dimer marginal

In `sections/5_pressure.tex`, the proof applies separate Gibbs inequalities
to `p_A` and `p_B` and then invokes entropy subadditivity in one sentence.
For complete transparency, start with an arbitrary one-dimer marginal on
`A x B`, bound its Shannon entropy plus potential average by
`log(Z_A Z_B)`, state both equality conditions (independence within a dimer
and Bernoulli independence across `E`), and then divide the `E`-action value
by two.  The existing conclusion is plausible; the equality chain should be
written at the same precision as the headline conjugacy proof.

### m3. Corollary `cor:many-presentations` overstates the availability of
distinct factorizations

For a prime `q>=5`, all presentations with product `q` have the same
unordered pair `{1,q}`.  Retain the universal conjugacy statement, but phrase
the “different unordered pairs” clause conditionally and keep `(2,6)` versus
`(3,4)` as the explicit witness.

## Proof-dependency audit

```text
global phase lemma
  -> corrected all-shape restriction count
  -> rectangular entropy
  -> entropy necessity in product classification

global phase lemma + intrinsic A-anchor matching
  -> radius-one code and inverse
  -> product sufficiency

global phase lemma + finite dependence
  -> deterministic phase
  -> subgroup obstruction / iid sufficiency

phase full-shift model + joint Gibbs equality
  -> pressure and unique full-action equilibrium

global phase on finite quotient
  -> subgroup fixed-point formula
```

Only the first “all-shape count” node is mathematically false.  Its entropy
descendant survives after the formula is corrected.  The dimer, finite-
dependence, pressure, and periodic engines do not require component-wise
phase freedom.

## Source and ownership audit

- Chandgotia’s author-hosted Lecture 4 explicitly displays the complete-
  bipartite checkerboard mixture/MME picture (slides 26--32):
  <https://nishantchandgotia.github.io/Teaching/2019_Jagiellonian/coursekrakow/l4.pdf>.
- Chandgotia--Thorat, Corollary 8.4, proves nonexistence of shift-invariant
  finitely dependent processes for finite four-cycle-free targets in
  `d>=2`; complete bipartite targets with both parts at least two lie outside
  that hypothesis: <https://arxiv.org/html/2605.02226v2>.
- The one-sided category record is current and correctly separated:
  <https://arxiv.org/abs/2509.24754>.

No exact primary source for the product dimer classification was located in
the bounded search.  That is only a source-audit status, not evidence of
priority.  The external-release verdict remains HOLD.

## Control and reproducibility audit

- Baseline script exits zero, but its finite-shape check is semantically
  invalid for the theorem because it tests local admissibility.
- The 288-point torus dimer encode/decode check is exhaustive for the stated
  finite example and remains useful.
- The fixed-point, weighted-square, and scalar `p=p^2` checks are internally
  consistent, though the scalar test is illustrative rather than exhaustive.
- `SHA256SUMS` and `FINAL_QA.md` are stale immediately after this review and
  must be regenerated only after both improvement rounds.

## Actionable Round 1 checklist

1. Correct Proposition `prop:patterns`, its proof, and all ledgers.
2. Repair the control semantics and add the two disconnected global-phase
   counterexamples as positive tests.
3. Correct the dimer memory-set wording everywhere.
4. Tighten the joint-Gibbs equality chain and dimension-range wording.
5. Re-run the deterministic control and full LaTeX/BibTeX build before
   preserving `main_round1.pdf`.

## Release recommendation

**HOLD.** Do not circulate externally until C1 and M1 are fixed, controls and
claims ledgers agree with the corrected theorem, and Round 2 independently
audits the revised proof.
