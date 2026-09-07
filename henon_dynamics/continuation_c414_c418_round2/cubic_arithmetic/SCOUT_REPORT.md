# Full integral conservative cubic: bounded scout

Status: `FULL_PROOF_PACKAGE_READY_FOR_NONAUTHOR_REVIEW`. No admission, manuscript,
paper number, formal Route A evaluation or PDF is asserted.

## First contract (frozen before diagnostics)

- Object: every map `H_(a,b,c)(x,y)=(y,y^3+b*y^2+c*y+a-x)`, with
  `(a,b,c) in Z^3`; determinant of the Jacobian is `+1`.
- Domain: all `Q^2`; clock: ordinary forward iteration by this one map.
- Observable: actual rational periodic points and their least periods, with
  unit point weights, no orientation quotient and no scheme multiplicities.
- Desired independent increment: an exhaustive all-parameter classification,
  a sharp uniform full-family bound, or a comparably complete global theorem.
  A finite coefficient scan, mere integrality, a root-neighborhood necessary
  condition and degree substitution into C412 do not meet this contract.
- Candidate mechanism: an integral translation normalizes the quadratic
  coefficient to `-1,0,1`; separated three-branch integer recurrence rigidity
  might close the remaining arbitrary cubic coefficients.
- Classical ownership to deduct: monic integral periodic-point integrality,
  escape/height bounds, bounded-orbit encoding and the sealed C412 quadratic
  classification. Literature ownership is being checked in `SOURCE_AUDIT.md`.
- Decisive cheap check: prove or refute a coefficient-uniform finite alphabet
  or branch-rigidity lemma; a small exact CPU scan may falsify a proposed
  lemma, but cannot certify a universal classification.
- Replacement boundary: if no such complete mechanism survives the proof and
  ownership checks, record the precise missing step and admit nothing. At
  most two materially different, separately frozen backups may be screened.

## Scope and workflow

Only this new `cubic_arithmetic/` directory is writable by this scout. The
39-file earlier C414–C418 checkpoint, its three admitted contracts and all
previous proof checks are frozen. The earlier SL2 companion is not reopened.
The batch still has three of five admissions and no new manuscripts/PDFs.

The repository batch workflow governs theorem scouting. `research-lit` and
`idea-creator` support bounded discovery; ARS is used only for fact-checking
and source-verification records, not as the author of a proof or admission
decision. Pure theoretical CPU diagnostics do not stand for an ML GPU pilot.
Discovery and eventual team checks are AI-assisted, not human attestations.
No target Euler factors, root numbers, automorphy, target zero/divisor
correspondence or Hilbert–Pólya operator is claimed. All A1/A2 separation
boundaries and `NO_BAD_EULER_OR_ROOT_NUMBER` remain in force.

## Outcome of the first contract

The first question survived the decisive check; no backup question was
opened. The [proof package](PROOF_PACKAGE.md) proves, with an explicitly
bounded exact finite graph certificate, the following full-family claims:

- Every rational periodic point is integral.
- Every cycle uses at most three coordinate values and has least period
  in $\{1,2,3,4,6\}$; every allowed period is realized somewhere.
- Seven exact polynomial/word templates classify every cycle, at every
  original integer coefficient triple, with all degeneracies excluded by
  explicit ranges.
- The total periodic set has at most eleven points, with equality exactly
  for $f(t)=(t-h)^3-5(t-h)+2h$, $h\in\mathbb Z$.

The key independent step is the integer third root of the global secant
polynomial, not a coordinate-radius estimate. After translating the
entire periodic set's coordinate extrema to $0,D$,
$$g(t)=A+qt+t(t-D)(t-r),\qquad q\in\{-2,-1,0,1,2\},\quad r\in\mathbb Z,$$
and every periodic symbol satisfies
$|t(t-D)(t-r)|\le2D$. For $D\ge16$ this gives either a three-root
affine recurrence or ninety genuinely symbolic $\mathbb Z[D]$ graphs.
For $2\le D\le15$, existence of an interior symbol forces
$-3\le r\le D+3$, leaving precisely $9373$ endpoint-compatible
parameter tuples. The remaining zero/one-diameter and two-symbol cases
are analytic. No original coefficient cutoff is imposed.

The distinction between per-cycle symbols and the global alphabet is
substantive. For example the large-diameter row $r=2,A=2,q=0$ supplies
$(1,1,D)$ and $(0,0,2,2)$ simultaneously, so four global symbols really
occur. Both cycles are retained. A graph containing both endpoints is
only a necessary filter, not a claim that it has no periodic points
outside that graph's interval. Full coverage instead follows because
the proof starts with the actual extrema of the entire periodic set.

## Diagnostics versus proof certificates

The initial [coefficient diagnostic](scan_cubic.py) checked $7497$ maps
with $b\in\{-1,0,1\}$, $-25\le a\le25$, $-40\le c\le8$. It
found no cycle with four symbols and a maximum of eleven points at
$f(t)=t^3-5t$. This scan supplied hypotheses only, not any universal
claim. It was not expanded after the parent requested a decisive proof.

[certify_cubic.py](certify_cubic.py) instead evaluates the finite families
deduced in the proof, with no period cutoff or floating-point arithmetic.
It computes the maximum and every maximizing tuple rather than testing
against a supplied value of eleven. The sole maximizing normalized
tuple is $(D,r,A,q)=(4,2,6,-1)$.

The [second author implementation](crosscheck_cubic.py) uses the entire
square $\{0,\ldots,D\}^2$, without the secant alphabet restriction,
and removes escaping vertices by exact inverse propagation. It agrees
with path traversal in all $9373$ small cases and verifies the exact
seven-template identities for all $3474$ cycles encountered. This is
an author cross-check, not nonauthor review or a proof-assistant claim.

## Ownership and next gate

[SOURCE_AUDIT.md](SOURCE_AUDIT.md) records four directly accessed primary
sources, actual section access, DOI/API date discrepancies and the
targeted C412/old-cubic/discrete-sine comparisons. Pezda's general period
set and Ingram's finiteness/height context prevent a claim that mere
uniform boundedness is new. C412's integrality, bounded encoding and
finite-complement method are explicitly deducted. The proposed
independent increment is the full nonconvex cubic closure, seven exact
cycle types, sharp eleven points and the complete equality locus.

The next required step is independent reconstruction of the proof and
exact graph arithmetic, plus a bounded primary-source check. Only the
coordinator can decide admission and update the batch count. This report
does not assign a paper number, reopen an old companion, start drafting,
write global state, modify Git, or fill the remaining slot by a corollary.
