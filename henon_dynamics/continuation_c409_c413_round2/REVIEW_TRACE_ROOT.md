# Independent internal review: complete integral Fibonacci trace dynamics

Reviewer: root coordinator, not the proof author. Date: 2026-09-06.
This is a mathematical and substantive contract review, not human peer review,
a journal decision, a priority certificate, or a formal Route-A evaluation.

## Decision

**The stated integral classification is proved, and its residual complete
question is sufficiently independent to be admitted as the fifth research
contract of this batch.** The admission concerns the exhaustiveness theorem
over all of `Z^3`, not discovery of the map or of its periodic curves. A
manuscript must credit those classical inputs and preserve the bounded scope
of the literature audit. Five complete papers have not yet been written.

The proof uses one ordinary map and one ordinary iteration clock. It covers
every integer initial point, every height, every integer invariant level,
both signs, and every period. No finite-period cutoff or numerical escape
guess supplies an unproved quantifier. The full classification yields finite
return counts on each level even though the unrestricted lattice has infinite
fixed-point sets at some times. This is an intrinsic arithmetic source result;
it supplies no target Euler factor, root number, or zero correspondence.

## Materials actually inspected

- The complete [proof package](nonlinear_geometry/PROOF_PACKAGE.md), initially
  390 lines, with the subsequent three-line factor-positivity clarification
  checked directly. Reviewed final proof SHA256:
  `db8143d09154c21fe70f4c84f59b14524d451753784b9faa6d4521c2c3bc2afd`.
- The complete [source ledger](nonlinear_geometry/SOURCE_LEDGER.md), first
  193-line version, and [scout report](nonlinear_geometry/SCOUT_REPORT.md).
  Later provenance-only additions are not silently included in that scope.
- All 175 lines of [the verifier](nonlinear_geometry/verify_trace_contract.py)
  and the complete [author execution receipt](nonlinear_geometry/VERIFICATION.md).
  Verifier SHA256:
  `41b4145cf8368e792e0e41d8b08184b711736560be054516609005721efc3106`.
  I reviewed code and output but did not rerun the author's unchanged census.
- The old [C13 project overview](../fibonacci_trace_map_clock_obstruction/README.md)
  in full and its candidate-registry entry. Its spectral-section and
  short-clock obstructions are different contracts; no old proof or test was
  reopened or changed.
- The primary-source passages listed below were accessed by the reviewer,
  independently of the author's description.

## 1. Proof audit, including potential failure points

**Object and completeness of the clock.** Substitution gives the stated
polynomial inverse and invariant. The scalar recurrence is genuinely
two-sided. A shift to a maximal scalar coordinate remains an ordinary iterate
of the same map. Reversing a scalar solution preserves its recurrence; this
is a legitimate way to handle left/right cases and is not a quotient by sign
or an unexplained replacement of `T` by `T^3`.

**Cycle existence, exact period, and disjointness.** The three cyclic scalar
words satisfy the recurrence. I checked the twelve successive triples and
their final return, including the signs at positions 4, 6, 8, and 11. For
`m >= 2`, the positive entry `m` occurs once per scalar word, so no proper
divisor of the displayed period can be a period. At `m = 1` this uniqueness
argument would fail, but the proof separately checks distinct triples and
does not apply the generic argument. Heights separate different parameters;
different exact periods separate the three families and the special orbits.

**Maximum lemma.** With `|u| = M >= 2`, the two neighbour relations imply
`|a|,|b| <= 2` without dividing by a potentially zero neighbour. If `b = 2 eta`,
equality in the triangle inequality forces both summands to be `eta u`.
The other relation then gives `M^2 <= M+2`, hence `M=2`. The resulting triple
has all coordinates of modulus 2 and positive product, precisely the fixed
point or 3-cycle already verified. The argument also handles `u<0`.

**Zero branches.** Two zero neighbours give an axis orbit for either sign of
`u`. With exactly one zero neighbour, the listed six further recurrence steps
give `t(1-u^2)`; its modulus exceeds `M` even at `M=2`. Reversal handles the
other placement of the zero. No exceptional height escapes this contradiction.

**Nonzero neighbours.** Once the modulus-2 branch is removed, the neighbours
are signs. Negative product `abu` forces the next coordinate to have modulus
`M+1`. Positive product leaves exactly four triples. Their identification
with `B_M`, `C_M`, `T^4 C_M`, and `T^8 C_M` agrees with the complete itinerary.
In particular the proof does not conflate the 4- and 12-cycles by sign symmetry.

**Unit cube.** Four nonzero triples of negative product immediately reach
modulus 2. The remaining 23 triples partition as `1+6+12+4`; the already
verified distinct `B_1` and `C_1` points occupy exactly the final 16. This is
a counting proof of the entire remainder, not a reliance on a program.

**Boundedness and proper escape.** On a bijection of `Z^3`, repetition in a
forward orbit implies that the initial point was periodic. More strongly, a
nonperiodic two-sided orbit is injective, so it visits any finite cube only
finitely often. This proves both proper-escape limits. No estimate of the
coordinatewise growth rate is needed or claimed. A merely unbounded sequence
would not suffice, but the proof correctly uses injectivity and discreteness.

**Level arithmetic.** Both height-to-level parametrizations are strictly
increasing for positive integer parameters. The quadratic condition is exactly
that `4k-7` be a positive odd square. The only intersection with positive
squares comes from two positive factors with product 7; the added sentence
`r^2=(m-1/2)^2+7/4` makes their positivity explicit. It yields `r=m=2`.
The exceptional level `k=4` contains `1+3+4+6+12=26` points. The fixed-point
formula follows by retaining precisely cycles whose exact period divides the
ordinary time. Its zeta conversion is classical and correctly restricted to
one fixed level. A whole-lattice finite-count zeta would be invalid.

**Counterboundaries.** The displayed rational point has exact period 2, so an
extension from integers to all rationals would be false. The level-8 four-cycle
is non-axis and lies outside the whole-group finite-orbit classification.
These examples protect two material quantifier boundaries, not cosmetic caveats.

No blocking mathematical issue remains. The only requested edit was the
factor-positivity explanation, now verified. It changes no theorem or code.

## 2. Primary-source ownership audit

[Roberts–Baake (1994)](https://web.maths.unsw.edu.au/~jagr/RB94.pdf): I read the
map and normalization, the relevant boundedness and sign-symmetry statements,
Eq. (29), and the discussion on printed pp. 849–852. I also downloaded the
author-hosted PDF and visually inspected the actual Table I on printed p. 850,
after the web extraction failed to display it. Its period-4 representatives
are `(-1/2,a,-1/2)` and `(-1/2,1/2-a,-1/2)`, exactly the candidate's family
after scaling. The axis family and the period-4-to-12 sign relation are
classical. All their existence content is deducted. No complete half-integer
lattice intersection is stated in those inspected passages. Downloaded PDF
SHA256: `524d281026f0c763f6fda829ae63cb892cb7a53291539caa2a435a68f9f5f6ed`.

[Roberts (1996)](https://web.maths.unsw.edu.au/~jagr/R96.pdf): I read Proposition
4.1 and its proof, Theorem 4.1 and its proof, Remarks 4.1–4.2, Theorems
4.2–4.3, Corollary 4.1, and Extensions 5.1–5.2 with their arguments. These
provide the general escape regions and growth theory, including the
orientation-reversing Fibonacci case. They do not list the complete integral
periodic set on all levels. The present theorem closes the arithmetic
boundary/complement cases explicitly; it does not claim a new general escape
criterion or a stronger growth theorem.

[Humphries, arXiv:1611.02743v1](https://arxiv.org/html/1611.02743v1): I read the
definitions and Theorem 1 in their introductory context, the whole-group
interpretation, and the proof of Theorem 1. Its hypothesis is periodicity
under every group element, not under one chosen hyperbolic word. The
non-axis point `(-1,3,-1)/2` has half-trace invariant 2; the source excludes it
from its finite-orbit class, whereas it is periodic for our map. This is a
direct reason the cited theorem cannot replace the proposed classification.
The source is labelled by its 2016 arXiv version, not an HTML generation date.

[Ghosh–Sarnak, arXiv:1706.06712v3](https://arxiv.org/html/1706.06712v3): I read
the abstract and the introduction through the group definition and Theorem
1.1. The statement concerns integral-point sets and representatives modulo
the full Markoff group. Its introduction explicitly distinguishes finitely
many group orbits from their infinite size. It does not give single-word
cycle classification. I did not independently read its full analytic proof.

[Vishkautsan, arXiv:1504.07099v2](https://arxiv.org/pdf/1504.07099v2): I read
the abstract, Sections 1.1–1.2 and the two main statements. Its two-reflection
map and residual periodicity question differ from the one-map all-level
integer classification. The zero-level real-periodic exclusion is already
credited there to Cantat and Loray; our zero-level specialization is not
treated as an independent new theorem.

The author's wider ledger and my additional formula/normalization searches
did not locate an exact prior whole-lattice classification. Negative search
results cannot certify worldwide priority. The manuscript must state the
result without an unsupported “first” claim and distinguish this bounded
source comparison from proof of originality. There is no identified unread
near-owner explicitly claiming the same all-integer theorem in this lane.

## 3. Substantive independence and verification limits

This contract answers a complete arithmetic dynamical question: exactly which
integer initial conditions recur under a fixed nonlinear three-dimensional
automorphism, and therefore what the ordinary return law is on every level.
The deduction of a rational zeta is not the increment. Nor are the known
cycle formulas, the exceptional zero level, or a catalogue of small periods.
The unrestricted-period exclusion and all equality cases are the increment.

The four earlier contracts concern nonhyperbolic wild FAD natural boundaries,
a characteristic-three inverse tower, two-clock simultaneous returns, and
rational periodic points of a quadratic Hénon family. None implies this
single trace-map theorem. Reuse of an elementary maximum argument is not a
duplication of the mathematical object or the complete classified question.
The old C13 clock obstructions also do not supply this theorem.

The author's executable evidence independently extracts finite directed cycles
inside a specified cube and checks exact identities. Its level tests are
consistency checks against generated cycles, not independent proofs of global
exhaustiveness. The reported 445-point and 125-state checks have only their
stated finite scopes. My independent contribution here is the full proof and
ownership audit, not a second execution of unchanged code.

**Final internal verdict:** `PROOF_PASS; SUBSTANTIAL_INDEPENDENT_CONTRACT`.
Proceed to the five-contract paper plan, full manuscripts, applicable route
evaluations, manuscript-level non-author review, and actual release checks.
No paper/PDF completion or target-arithmetic success follows from this verdict.
