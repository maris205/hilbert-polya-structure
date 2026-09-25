# ECD01 — manuscript comparison and final internal review

Candidate: **ANG-20260923-ECD01**.
Candidate outcome: **DEGREE-LOCKED CLOCK — GLOBAL STOP / FORK**.
Review verdict: **CP2 PASS / CP3 PASS** for the exact surfaces below.
No mandatory mathematical or presentation correction was found.
Internal shared-model/history review: **NOT_CALIBRATED**, not peer validation.

## 1. Complete access and version receipts

All four final surfaces were personally read through EOF:

- `paper.md` — 293 lines, 18987 bytes, SHA-256 `f2f4589d7464d35bcade6f3493ba4a871b6daa34d6c166b5833109fc9b32fdfc`.
- `candidate-card.md` — 117 lines, 6969 bytes, SHA-256 `e92fa087331548c70338cb512797c2627e78a5471232c672599898f6c2083dc4`.
- `README.md` — 19 lines, 1567 bytes, SHA-256 `62029fe9ea8800be9168f2be2df7a20c01b9bdda43c4706449d9b958138f4f6d`.
- `claim-ledger.md` — 23 lines, 2446 bytes, SHA-256 `2e7528e74268c3f02730d31d7c4e978f7340e92db8d4e25b552eed25b48b65f3`.

The paper read covered 1–180 and 181–293 EOF; the other reads covered all
117, 19 and 23 lines respectively. No truncated output was used as full access.
Two scientific-prefix hashes were remeasured after the appended outcome:

- Original card 1–91: `4164f4ff5863e0999125ce017d900f1ce8274d95d29301e7c6416427d9a4f4e9`.
- Clarified card 1–100: `af74a4508865d5a947ac2527abb97681615c580e878996c37d2428ae45558b74`.

The earlier reviewer records are preserved byte-for-byte:

- `evidence/scope-review.md` — 99 lines, SHA-256 `5194ae7402514af9b5c1262a49aee25818045b98014e890d47ec9ee04e5b65cd`.
- `evidence/independent-derivation.md` — 216 lines, SHA-256 `7f3f4fc7aa55eca009483f6835b19ff0961fb26ced990be800ce75a16e5d722f`.

Actual stages: CP1 read the original card and found the sector/clock notation
collision plus the missing explicit positive-length sums. Root appended the
pre-proof clarification; the reviewer read that delta and appended READY,
preserving the original observation. Only after root's full scope read and
separate mathematical release was the clarified-card-only raw derived,
self-read and frozen. Root then reported its full raw read and separately
unlocked the manuscript. Only then were these four surfaces read and audited.
No earlier manuscript version or peer proof was read, and no private draft
timing or authorship independence is inferred from this access order.
The paper's author-helper and design-source descriptions remain attributed
disclosures, not new source files read by this reviewer or extra review seats.
ARS staged workflow/DA/runtime boundaries remain in force. No auxiliary,
web, scientific code, numerical experiment, Git or model change was used.
Only this final review was written in CP2/CP3; raw and scope remain frozen.

## 2. CP2 — mathematical comparison

### Whole source, inverse domains and IMAGE

The integer interface, current-cell coefficient and full signed complex
carrier agree with the clarified card. MAIN/A exclude only zero from forward
legality but retain it as an object; L is total and keeps its fixed origin.
Nonzero coefficients prevent any nonzero source from entering the origin.
Thus MAIN/A's origin is an identity-only source component, not an absorbing
forward cycle. L's distinct origin component has all integer lags.

The complete root/cell/sector inverse construction retains all actual
predecessors with exact readout checks, not a principal-root selection.
Half-open cells and sectors assign each source uniquely even at cuts.
A has no redundant cell labels, and L imports neither square-root sectors
nor MAIN's terminal condition. The all-integer inverse domains are exact;
surjectivity or a uniform finite inverse bound is not asserted without proof.

The real-area derivative is `|2az|^2`, not `|2az|`. The displayed inverse
densities and all-point step clocks follow with the correct factor four.
The author's every-Borel proof was checked independently: partition each
injective source-sector piece into disjoint Borel sets subordinate to a
countable local inverse-chart cover. Their target images are disjoint and
change of variables applies on each chart; countable additivity gives the
full law, including infinite measure and assigned null faces. This is a valid
alternative to the raw's explicit cut-ray/slit-plane split. Neither proof
assumes a continuous globally assigned square-root formula across its cut.
Null-state versions are fixed by the frozen germs, not by a.e. uniqueness.
No global measure-invariance conclusion is substituted for branch IMAGE.

### Actual cocycle, kernels, stabilizers and phases

The exact radial identity yields, on nonzero MAIN/A arrows,
`c=k log 4+V(w)-V(z)`, where `V=2 log|z|`; L has just the potential difference.
The forward-arrow sign and finite-history density `exp(-c)` agree with the
actual inverse convention. Common legal histories, not free labels or an
extension through zero, determine the retained-lag Borel groupoid.
The all-depth inverse recursion covers every incoming arrow. Countability
follows from the inverse atlas; no enumerated finite full basin is claimed.

Full arrow kernels are correctly restricted to actual `G`: a radius equation
alone cannot create an arrow. Source isotropy is the entire `p Z` for an
eventual least-`p` cycle and is trivial otherwise. MAIN/A therefore have
entire `H=p log 4 Z` on such basins and trivial extension isotropy, including
ancestors; non-eventual sources and their terminal origin have `H=0`.
This rules out falsely extracting a smaller generator from inverse branching.

The phase discussion retains the anchor's actual lag coset and the full
`p log 4` modulus. In explicit raw coordinates this is
`h+V(z)-ell_z log 4 mod p log 4`, not simply radial height modulo `log 4`.
The manuscript's anchored description is consistent with this formula and
does not impose a new roof or alter physical height translation.
All quotient claims are set-level, without an unsupported nice measurable,
Hausdorff, symplectic or classical conservative-flow assertion.

L's origin is separately checked with `J=1`, zero step clock, source and
extension isotropy `Z`, full-component clock kernel, unit lag/joint kernels
and real phases. Its nonzero potential calculation then proves global `H=0`.
This does not make L's general arrow or step clock identically zero.
No logarithm of zero, terminal-clock value or MAIN origin loop is inserted.

### Global gate and comparison of scopes

The all-itinerary radial product and real-area derivative product give
`4^p` on ANY actual MAIN/A least-`p` cycle. The full isotropy calculation
makes `log(4^p)` the primitive time, not merely one possible loop time.
Its multiplier is composite for every positive integer `p`. Consequently
MAIN's joint target fails: any positive packet violates prime-only, while
absence of such packets violates nonemptiness. This logic does not decide
cycle existence, periods realized, basin counts or packet multiplicities.
The manuscript's exclusion of all-prime coverage is also a valid direct
corollary of no ordinary-prime primitive, not a hidden existence theorem.

The A and L arguments use their own transports, inverse versions and clocks;
neither control's conclusion is substituted for MAIN's derivation. The raw
additionally supplies per-target finite inverse bounds, A's root-of-unity
eventual-source classification and L's complete fixed-only cycle description.
Those optional structural control consequences are not represented as author
claims or required manuscript additions after this decisive global gate.

## 3. CP3 — strongest positive/adverse reading and surfaces

The strongest positive result is genuine: the frozen full-state arithmetic
execution has a coherent all-point Borel IMAGE and actual history clock.
Arithmetic can change motion and least source periods. It is its contribution
to the return multiplier that cancels, not the source dynamics themselves.
The decisive objection is the owned degree/area factor, not a failure to find
cycles in a sample. Halving the clock, selecting roots or reducing the period
group would change the owner or its primitive convention and cannot rescue
this result. No broader impossibility claim for complex/arithmetic dynamics
follows. MAIN existence/classification and strong naturalness remain OPEN.

All four surfaces agree on ID, GLOBAL STOP / FORK, controls, origin treatment,
full kernels/phases, the no-existence-claim boundary and the scope of coverage.
The original and clarified scientific prefixes are unchanged. The card's
scope clarification is documented as pre-proof, not retroactively present.
The equations, tables and local file references are readable and consistent;
no required surface repair was identified. No issue quota or numeric score
was used. Arithmetic T1 remains NOT PASSED, T3 NOT AUDITED, classical fields
NOT APPLICABLE, formal Route UNASSIGNED and Route B NOT INVOKED.
CP2/CP3 PASS is a bound internal review verdict, not a target pass, external
peer review or calibrated guarantee. A later change to any bound surface
requires proportionate delta review; this report does not authorize new work.
