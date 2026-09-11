# Paper plan — receiver-limited cyclic transfer

Status: SOURCE_AUTHORING_ONLY. No new scientific execution, canonical,
build, page view, Round0 or manuscript review exists for this paper.

Title: Terminal states and one-step fibres of receiver-limited cyclic transfer.

One-sentence contribution: For labelled fixed-mass cycles with current
$\min(a_i,a_{i+1})$, original zero-separated endpoints determine every
terminal state and the sharp worst fixation time, while a disjoint
comparison-word interval parametrization determines every one-step source
and the exact largest-fibre growth exponent $\lfloor n/3\rfloor$.

Type: anonymous mathematical short note. No venue selected.
Editorial length target: approximately 8–12 pages including complete proofs;
this is an estimate, not a measured page count or submission limit.
Five numbered body sections, plus one abstract include, all in main.tex.
No appendix, decorative figure or imported conference template is planned.

## Controlling scope

The sole admission contract is
[the P213 theorem contract](../../docs/papers211_215_sequence/P213_THEOREM_CONTRACT.md),
SHA256 e57437d154adc18fe04033026db221b63b06fdadb910d727f31498c35330ed92.
The [root reception](../../docs/papers211_215_sequence/scouting/root_reception/fresh07_candidate01/RECEPTION.md)
accepts a narrow theorem conjunction, not global priority or a completed paper.
Carrier: all labelled nonnegative integer cyclic vectors of length $n\ge1$
and sum $N\ge0$, without rotation quotient. All currents use the old state.

## Structure and proof roles

### Abstract — sections/00_abstract.tex

Open with the complete terminal/inverse problem. Explain the distinction
between receiver mass and receiver vacancy. Preview the sharp clock:
zero for $n\le2$ or $N=0$, $\lceil\log_2 N\rceil$ for $n=3,N\ge1$,
and $N-1$ for $n\ge4,N\ge1$. State the all-target interval formula
and $\Theta_n(N^{\lfloor n/3\rfloor})$ growth result. Evidence is deductive;
do not report the planned verifier as executed.

### 1. The rule and the questions — sections/01_introduction.tex

Define the full carrier, cyclic indexing, current and update immediately.
State two connected questions: where every state ends, and which sources
produce a specified labelled target. Preview the three retained conclusions.
Compact related-work paragraphs deduct conservation/flow and distinguish
the actual Burgers receiver-vacancy current. A small comparison table is
unnecessary: two exact current formulas and a scope paragraph are clearer.
No new-current priority or arbitrary-conjugacy exclusion is asserted.

### 2. Terminal states and sharp fixation time — sections/02_temporal.tex

Define minimum, residual, maximal positive runs and fixation time.
Prove translation, minimum invariance and permanent zeros.
Prove that only a run's first positive site can disappear, that its
original right endpoint increases by at least one until fixation, and that
the endpoint receives precisely the original run mass.
Derive all fixed/recurrent states and the global bound. Prove the doubled
endpoint formula for $n=3$, all sharp witnesses, and the $N=0,1,2$ and
$n=1,2$ boundaries. All details stay in the body.

### 3. Every one-step source — sections/03_inverse.tex

Use bit 1 exactly for weak ascent, with equality assigned only to 1.
Display and derive the four local equations. Separate constant words.
For every mixed word unwrap each valley–peak–next-valley block without
quotienting labels. Force valleys and descending interiors backwards;
handle a one-edge ascent with a forced peak; handle a longer ascent with
shifted target tests and one prepeak interval.
Prove necessity, sufficiency, automatic mass, independence and disjointness.
Explicitly treat one/two-edge ascents, empty descent interiors, empty
intervals, parity failure, ties and wraparound. Bound arithmetic operations
by $O(n2^n)$ without claiming bit-cost independence of $N$.

### 4. Fixed-target fibres and largest-fibre degree — sections/04_fibres.tex

For a fixed target subtract its minimum and define spike masses and
preceding zero-gap lengths, including a sole spike's gap $n-1$.
Prove that every source run has length at most two and classify all optional
heads. Derive the exact product, including uniform targets.
Pack two ascent edges plus one descending edge per free interval.
Use $k=\lfloor n/3\rfloor$ spaced spikes to attain the degree, with the
contract's explicit upper/lower constants and $N\ge2k$ threshold.
No exact finite-$N$ maximum or maximizer theorem is stated.

### 5. Finite verification and limits — sections/05_verification.tex

Describe the independently written comparison-word author verifier and
fixed box $1\le n\le6$, $0\le N\le4$: 461 states, 30 full carriers.
At this source-only milestone execution is pending. Archive references
remain separate from a paper canonical. State the excluded claims:
general pointwise clocks for $n\ge4$, all-time fibres, basin census,
exact finite-parameter maxima/all maximizers, linear-time image tests
and numerical proofs of asymptotic statements.

## Evidence plan

[CLAIMS_EVIDENCE.md](CLAIMS_EVIDENCE.md) is the claim-level ledger.
[PROOF_PACKAGE.md](PROOF_PACKAGE.md) carries the complete author proof
and dependency map; the TeX will contain the same mathematical scope.
The new standalone verify.py must not import or copy the gate's
flux-complementarity implementation. Its literal forward graph and
comparison-word reconstruction must agree on full source sets, not counts
alone. Parameters, output schema and complete scientific/runtime dependency
roles are declared before any scientific parsing or execution.

## Bibliography plan

Three published records are selected, with primary-source scope audited:
Boccara–Fukś (2002), Nishinari–Takahashi (1998), and
Fukuda–Segawa–Watanabe (2023). The last article's published title differs
from the 2021 preprint title. The Nishinari–Takahashi author PDF's 2001 front
date is not its 1998 publication date. Only verified cited entries belong
in references.bib. SOURCE_AUDIT.md records actual access and limitations.

## Skills and review status

paper-plan and paper-write are used in that order; the complete shared
writing-principles reference and citation-discipline fallback were read.
proof-writer supplies an explicit dependency map and boundary audit.
The project's short-note contract overrides generic ICLR page, natbib,
one-page related-work, hero-figure and API-provider defaults.

The named cross-model MCP reviewer is unavailable; no such call or outline
review is fabricated. Actual later process-separated reviews under the
project contract are still required. The candidate gate is not review A/B.
The author is a candidate proof/pilot contributor and cannot review the
manuscript. Source/parameter/runtime acceptance comes before execution;
canonical adoption, strict author pair, initial build/view and physical
Round0 come before A. Round1/B/Round2 and terminal gates remain later.

## Author checklist

- [x] Exact contribution and five-section roles fixed.
- [x] Claims separated from archive checks and pending paper execution.
- [x] Complete TeX and standalone verifier written and text-audited.
- [ ] Root-reviewed source/parameter/runtime gate.
- [ ] Actual initial stdout and canonical adoption.
- [ ] Separate strict author replay pair.
- [ ] Initial source-only build, all-page view and physical Round0.
