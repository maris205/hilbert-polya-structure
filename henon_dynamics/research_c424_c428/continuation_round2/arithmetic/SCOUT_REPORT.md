# Second-round arithmetic lane: AR2-1 final disposition

**Current result: AUXILIARY_ONLY; zero new admitted contracts in this lane.**
The parameterwise theorem is mathematically closed. This is not a report
of an unresolved proof gap, and it does not overturn the batch's existing
AM1 admission. The coordinator agrees with the independent substantive
review that the residual after C418 and external-source subtraction is
not enough for another independent paper under the present batch standard.

Only one of the allowed two questions was opened. No second title was
invented to fill a quota. No GPU, expanding census, old helper rerun,
manuscript, formal evaluation, shared-state edit, or Git mutation occurred.

## Completed mathematical result

For every field `k` with `char k != 2`, every nonzero constant determinant
`a`, and every nonconstant Laurent parameter `c`, ordinary iteration of
`H(x,y)=(y,y^2+c-a x)` is considered on **all** of `k(t)^2`.

* Periodic coordinates have precisely controlled principal parts at the
  two parameter poles: `y=eU+dV+b`, with signs `e,d` and a constant `b`.
* If sign products differ anywhere in the complete periodic set, even
  between coexisting orbits, then `UV` is a nonzero constant. This forces
  `U=u t^m,V=v t^-m` and a five-term parameter form.
* Outside that exceptional monomial-pair case, the whole periodic set
  reduces to the already-owned C418 seven-row atlas after square completion.
* In the exceptional case, 64 injective actual rational-point labels and
  two explicit if-and-only-if edge guards reconstruct every ordinary
  periodic point, its exact least period and all coexistence. The point
  and period bounds are 64, without a sharpness claim or period cutoff.
* A coordinator-proposed and author-verified hand strengthening shows
  that a genuinely mixed orbit requires `a^2=1`. Together with the
  inherited pure rows, any period greater than two in the entire frozen
  Laurent family requires `a^4=1`.

This is a complete parameterwise finite atlas. It is not a flattened
classification of every possible mixed word, sharp extremum or irreducible
parameter stratum; none of those stronger statements is claimed. Their
absence does not invalidate the theorem that was actually proved.

## Actual verification and independent assessment

The [independent review](../arithmetic_review/REVIEW.md) read and reconstructed
the full proof, global reduction, injective labels and both directions of
the edge criterion. It found no blocking mathematical defect. A separate
nonauthor also checked the label/edge algebra without running a program.
The stronger run-length proof in the separate addendum was independently
reconstructed by the reviewer and judged provable as stated.

The final addendum text additionally makes the counting convention
explicit: guards are evaluated in `k`, but the adjacency matrix is over
`Z`, its traces are ordinary integer counts, and its determinant is in
`Z[z]`. That last editorial delta was sent for exact readback at the
hash below. It does not change the mathematics or the admission judgment.
Neither internal AI-assisted review is represented as human peer review
or a formal evaluation.

The reviewer identified one genuine source-scope error: the initial
audit substituted degree two into Ingram's Section 3 numerical estimate,
although that section assumes degree at least three. The author verified
the section opening, removed the unsupported numerical comparison and
recorded the correction. The reviewer read back the corrected passages
and closed R1. The quadratic source route is Theorem 1.4/Section 4.
No replacement unsupported number is claimed. This error was never an
input to the hand proof.

Exactly one mathematical diagnostic ran, for approximately 0.465 seconds.
It stopped at its first mixed four-cycle after 11 linear systems, seven
consistent, and did not reach its frozen ceiling of period six. The
actual coordinate word is `(A,-P,-A,-P)` with
`A=t-1/(4t), P=t+1+1/(4t), a=1,c=-P^2`; direct residuals vanished.
This disproves the inherited-only shortcut but is not itself a novelty
claim. No follow-up probe or flattening census was run.

## Source subtraction and why no admission follows

The actual bounded source ledger deducts classical pole escape,
Ingram's appropriately scoped finiteness/height/bad-place mechanisms,
Gauthier--Vigny's broader characteristic-zero finiteness theorem,
Allen--DeMark--Petsche's local horseshoe, C418's entire one-pole and
pure-sign classification, the low-period witness, and elementary zeta
packaging. Search absence is not used to assert priority.

The residual global unit lemma and rational finite-graph extension are
real mathematical progress relative to the inspected predecessor. They
are nevertheless a short two-place compatibility extension of C418's
existing sign/offset architecture. Independent mathematical correctness
and independent paper-level materiality are separate gates. The
coordinator's **AUXILIARY_ONLY** decision follows the latter gate; the
result is retained without claiming another admission or a proof failure.
This disposition does not authorize a larger census to seek a different
answer.

## Frozen handoff files

| File | Role / frozen identity |
|---|---|
| [PROOF_PACKAGE.md](PROOF_PACKAGE.md) | Full theorem; SHA-256 `66bca7ae41a1fe409e8c7967f5b37e2ce0e1c05ddabf439272a70857bc22aeb3` |
| [ADDENDUM_MIXED_DETERMINANT.md](ADDENDUM_MIXED_DETERMINANT.md) | Stronger determinant condition and integer counting convention; SHA-256 `28de90b5dc90acf646cea981afc188078aa3194816664539b178cac96ef6cf93` |
| [SOURCE_AUDIT.md](SOURCE_AUDIT.md) | Actual primary access, local/source subtraction and acknowledged R1 correction; SHA-256 `414cca363464905ce4745d06faf69c245aa4206f0e4231c2f269899769302ced` |
| [EXECUTION_RECORD.md](EXECUTION_RECORD.md) | Chronology, single run, current auxiliary disposition; SHA-256 `1d1f508186c1b4f459f5daee61aae525239dd30d6d0f508670403984fafdb503` |
| [FROZEN_QUESTIONS.md](FROZEN_QUESTIONS.md) | One question and the pre-execution diagnostic boundary |
| [mixed_sign_probe.py](mixed_sign_probe.py) and [saved output](mixed_sign_probe_result.json) | The only mathematical diagnostic and its actual stopping result |
| [C418 preflight](c418_pdf_preflight.json) and [C417 preflight](c417_pdf_preflight.json) | Actual `UNAVAILABLE` PDF-structure checks; not claimed as validation |

The author proof bytes never changed after initial mathematical handoff.
The addendum was kept separate so that review did not silently replace
the frozen theorem. This report supersedes earlier provisional author
`HOLD` recommendations for current admission status. The lane stops after
handoff; no further question or computation is opened.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional. Nothing here asserts
target Euler factors, root numbers, automorphy, target-divisor matching,
or a Hilbert--Pólya realization.
