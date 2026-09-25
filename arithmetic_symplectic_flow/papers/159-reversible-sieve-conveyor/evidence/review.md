# Mathematical proof check: reversible sieve conveyor

**Candidate ID:** ASFS-20260915-RSC01  
**Paper ID:** 159-reversible-sieve-conveyor  
**Date:** 2026-09-15  
**Candidate status:** STOP — COMPLETE REVERSIBLE SOURCE CONVEYOR; NO INTRINSIC CLOSED ORBITS.  
**Review result:** No blocking mathematical defect found in the checked claims.  
**Calibration status:** NOT_CALIBRATED.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Provenance and actual scope

This is a separately delegated, same-session Codex model-family check of the
[actual paper](../paper.md) and [candidate card](../candidate-card.md), not
human peer review, cross-model verification, or an independent-error claim.
The reviewer inherited the session model configuration; an exact runtime
model identifier was not independently verified. No accountable human
reviewer or external journal criteria were supplied.

The reviewer was not blind: before the manuscript existed, this same checker
had inspected the proposed increment rule and returned the inverse, a height
formula, a register correction and the finite-closing consequence. The
present review checks those ingredients against their actual written use,
including the newly written suspension identification; it is not an
unrelated fresh discovery or a second independent source for the formulas.

The complete 362-line paper, 81-line candidate card and the three other core
Markdown files were read. Every proof in Propositions 1 and 2, Corollary 3,
and Controls A--D was checked algebraically, rather than sampled through
finite orbit data. The source-output argument and offset quantifiers in
Section 3 were checked as well. Thus this is a complete check of the package's
displayed mathematical arguments, with the external boundaries below, not a
global literature or novelty audit.

The prior-work guide and the specific local collision records 018, 025,
053, 054 and 011 were read to check the narrow historical comparison.
Their external literature dependencies were not revalidated, and no claim
from those external works is needed by the present proofs. No numerical
experiment, external model call, source upload, publication review or formal
Route evaluation was performed. The only file written by this reviewer is
this review receipt.

## Findings and coverage receipt

No Critical, Major or unresolved Minor defect was found in the assigned
proofs. The table records the checked surfaces and the basis for that result;
it is not a correctness certificate.

| Checked surface | Evidence anchor | Reconstruction and finding |
| --- | --- | --- |
| Phase indices and empty ranges | equation: paper (1); Section 5 Control A | Forward divisors run from 2 through n-1 and reverse divisors from n-1 through 2. For n=2 both ranges are empty, leaving the two distinct zero-increment phases. For n=4 the six increments are exactly (1,0,0,0,-1,0). No endpoint is omitted or double-counted. |
| Global inverse and smooth geometry | equation: paper (2)--(3); Proposition 1 | The discrete predecessor is inverse to the successor also at j=-1 to 0 and every connector. Subtracting the predecessor's increment undoes the register translation. Both maps are smooth on the countable disjoint-union manifold and pull back dq wedge dp to itself on every component. |
| Height and exhaustion of all labels | equation: paper (4)--(5); Proposition 2 | H(j+1)-H(j)=2 times the absolute value of j plus 2 for j less than -1, j=-1 and j nonnegative separately. The component intervals are adjacent and exhaust all integers. Thus h is a bijection, not merely an observable on the clean source trajectory. |
| Register correction and conjugacy | equation: paper (6)--(9); Proposition 2 | The partial sum C has successor difference w within a block; the full block sum is zero, so the identity also holds at the connector. The stated inverse of Psi is unique for every integer height and all real Q,P. The map is exactly translation on the full carrier. |
| Complete suspension coordinates | equation: paper (10); Corollary 3 | At t=1 the endpoint maps to (q-C,p,h+1). At its glued representative (Fx,0), C gains w and h gains one, producing the same coordinates. Any u in R can be written h+t with 0 less than or equal to t less than 1, uniquely apart from the identified integer endpoints. Local seam coordinates are related by the same constant translations, so this bijection and its inverse are smooth. The conjugated flow is global real translation, proving both completeness and absence of any positive-real-time closed orbit. |
| Actual output and arbitrary offsets | equation: Section 3 definition of a(n); Section 5 Control B | The top displacement equals a(n) after exactly n-2 test steps for every input offset. The pointwise zero-output test requires the explicitly stated clean entry register. The n=4, q_entry=-1 example correctly refutes extending that test to all states. Neither observable removes any state from the full proof. |
| Finite closing and full multiplicity | equation: Section 5 Control C, G raised to L equals identity | In the specified finite ordered list, each block occurrence retains its own phase positions and the phase permutation is one L-cycle. Cancellation returns every real register; no smaller iterate can return its phase. The first phase parametrizes distinct primitive cycles by all of R squared. Unit-roof primitive time is L, with repeats rL. For n=2 through N the sum of phase lengths is N(N-1). No primality filter appears. |
| Paired-data controls | equation: paper (4)--(9) with replaced C; Section 5 Control D | Zero increments and arbitrary fixed paired integer tables preserve the phase successor and total block cancellation. The same direct calculation applies to those changed-map controls, without borrowing their results as additional credit for RSC01. |
| Lineage and collision scope | text: paper Section 1, "not asserted to be conjugate"; Section 6, "no claim about all possible reversible sieve realizations" | The concrete lineage mechanism is ordered prime/composite divisor symbols transported by the real register map. It is not a claimed conjugacy to a historical Logistic/Henon system. Record 018 already supplies the elementary increasing-height obstruction, while 053/054 concern designated source trajectories. The current full-state construction is accurately kept distinct from a new universal no-go theorem. |

## Known wording correction

The author reported that the candidate card originally said positive j
performs the sequence beginning with n=2. That would omit j=0. The actual
card read in this review already says nonnegative j, matching n(j)=2+|j|
and the paper's explicit start at j=0. This was a **Minor wording issue,
ADDRESSED before the substantive manuscript check**; no formula, proof or
candidate identity changed. The full two-sided sequence still decreases
toward n=2 before increasing, exactly as the paper states.

## Decision boundary

The strong local conclusion is an exact full-state conjugacy, not numerical
nonrecurrence: the frozen unit suspension is complete and has no closed
orbit. The finite closed comparison is a different owner and has continuum
primitive multiplicity for prime and composite inputs alike. These claims
support the stated STOP / FORK decision without modifying RSC01.

Source computation is operationally established, but that is not full A0
prime-orbit or target-clock relevance. The empty A1 ledger is a scoped
failure of the proposed nonempty prime-packet chain, not a failure to define
the map or suspension. A2 remains NOT ADVANCED. No operator, nontrivial zeta,
exact prime-log clock, formal Route coordinate or later spectral conclusion
is created by this review. The same-object separation in the
[claim ledger](../claim-ledger.md) is intact.

The bounded ARS evidence-and-severity discipline informed this receipt; no
full journal review panel, numeric quality ranking or publication decision
is claimed. Residual risk is ordinary same-family model error despite the
explicit derivation, not an unreported mathematical gap identified here.
