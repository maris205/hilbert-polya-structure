# Evidence record — Fermat congruence register

**Candidate ID:** `ANG-20260918-FCR01`  
**Status:** `STOP — PRIME SEPARATION, INFINITE REGISTER MULTIPLICITY AND NON-LOG CLOCK`  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Inputs, method and limits

The version-1 [candidate card](../candidate-card.md) was created before
the [paper](../paper.md). Its exact inputs are all n>=2, all phases
1<=a<n, all k in Z, the congruence-failure bit Delta_n(a), the cyclic
phase scan, the reversible register increment and the roof
tau=1+1/(n+a). No prime table, fitted parameter, zero datum, finite
enumeration, numerical precision or cutoff was used.

The proof method is elementary and exact:

1. Compose the predecessor/subtraction inverse with the skew map in
   both orders; use tau>=1 for non-Zeno completeness.
2. Define the groupoid elapsed-time cocycle from this same roof and
   form its endpoint-glued suspension.
3. Prove the prime Fermat congruence by multiplying a permutation of
   nonzero residues; use a proper divisor as a composite nonunit
   witness. No external theorem is needed as an unproved premise.
4. Sum the register increments over the entire phase cycle. Any return
   must have m=r(n-1) and register change rD_n, which classifies every
   state before any register selection.
5. Sum the frozen roof over the surviving cycle. The harmonic sum and
   integral comparison give the exact period and its linear-scale
   bounds; actual traversal gives the repetition law.

There is no computed table, generated dataset, PDF, LaTeX artifact,
transfer operator or numerical evidence file. The symbolic proofs
support the all-n claims; the later mechanical check is only a file
and link consistency check.

## Lineage, parent and controls actually examined

The [prior-work guide](../../../docs/prior_work/README.md) supplies the
source/symbolic lineage frame. The new arithmetic predicate replaces
the prime/composite observable with an explicit all-residue
congruence scan; no historical Logistic/Hénon theorem is imported.
The author read the card and definition/proof portion of
[228](../../228-gcd-defect-cocycle/paper.md) as the nearest local
monotone-cocycle comparator. This candidate changes the predicate,
removes the real plane and changes the roof, so it receives its own
ID and no parent geometric or Route credit. Static n and naturalness
remain OPEN.

The paper proves the nonunit-indicator control, the qualified
single-cycle phase shuffle, the exponent-n control, the k-projection
ownership failure, the zero-defect comparison and unit-roof comparison.
The general nonnegative-defect argument is explicitly flagged as a
PROVES_TOO_MUCH risk. No control is silently installed as a repair.

## Bounded model checking and writing discipline

A separate native checker received the frozen formulas and proposed
statements, without filesystem writes or further delegation. It
confirmed the inverse, zero-defect classification, full prime
multiplicity, period sum and p=2 boundary. It identified two control
qualifications, both retained in paper section 6: phase reorder
invariance requires one cycle through all phases, and the nonunit
indicator agrees only on the periodic sector rather than on complete
composite dynamics. This is bounded same-family model checking, not
human peer review, cross-model replication or an independent
certificate.

Root's separately assigned `candidate231_review` then read all five
package surfaces, including the complete paper. It reported no
mathematical correction to the inverse/cocycle, all-residue criterion,
register multiplicity, clock or controls, and confirmed that the
parent/comparator relation does not claim a full conjugacy or inherited
geometry. Its reviewed paper SHA-256 was
`0a91d017eafbcdb1d5f2621b731bc29e0b54ba693eaebfe1625a633b5d316978`.
It made no file edits. This second native check has the same
model-review limitations just stated and is not external peer review.

ARS academic-writing guidance was used for claim/evidence/reasoning
separation and explicit counterarguments under the already fixed
research frame. No publication pipeline, venue assessment, external
model upload, source-expansion campaign or model switch was run.

## Mechanical verification

At `2026-09-18T11:36:46.875Z`, the author ran a bounded read-only Node
stdin verifier from the ASFS workspace. It read exactly README.md,
candidate-card.md, paper.md, claim-ledger.md and this evidence file;
tested each for the candidate ID, the exact final status string, a
final newline and absence of control bytes; then resolved every local
Markdown file-link target. The command exited 0 and returned
`{"files":5,"links":20,"errors":[]}`. This receipt records a mechanical
consistency check, not a mathematical or Route certificate. The only
subsequent author changes were replacing the pending-verification
paragraph with the actual receipt and appending the returned read-only
review result above; no definitions, proof inputs or link targets were
changed by those evidence-only additions.

Root integration owns any registry or root README change; this author
wrote only the package directory. The final candidate decision is
STOP / FORK, not a Route result.
