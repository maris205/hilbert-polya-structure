# LY4 fifth continuation: explicit exceptional atlas, exhaustion still open

Date: 2026-09-08 UTC. Decision: **FULL CONTRACT NOT CLOSED; ZERO ADMISSIONS**.

## Original object and contract

For every $a\in\mathbb Z$, the object remains
$$L_a(x,y,z)=(y,z,(a+y+z)/x)$$
on ordinary two-sided orbits whose scalar coordinates are nonzero
integers. Time is one displayed map application. Orbits are identified
by cyclic rotation only. The observable is the complete integral orbit
classification with exact least periods, not a finite-alphabet count,
spectral determinant, or target-arithmetic assertion.

The original full question is unchanged. The new
[frozen analytic attempt](FROZEN_ATTEMPT.md) was installed before any
new mathematical program and proposed the precise closing lemma E:
outside $a=1$, every ordinary integral periodic orbit has least period
at most six. E remains **UNPROVED**, not refuted or silently weakened.

## What was actually proved

The [proof package](PROOF_PACKAGE.md) gives a necessary-and-sufficient
atlas for every least period at most six and for every orbit at $a=1$.
In addition, it excludes genuine period eight when $a\ne1$.

The full six-channel is, apart from periods dividing two, the family
$$W(r,s)=(r,-r-1,r,s,-s-1,s),\qquad
a=rs+1,\qquad r,s\in\mathbb Z\setminus\{0,-1\}.$$
Its least period is three for $s=r$, two for $s=-r-1$, and six otherwise.
Thus the previous unbounded counterfamily belongs to an exhaustively
classified stratum; it is not removed by another height cutoff.

There is exactly one least-five orbit,
$$(-2,-2,-3,-4,-3),\qquad a=13.$$
The proof reduces a genuine five-period word to the coefficient-one
second-order Lyness recurrence, proves positivity by the sign law,
and finishes with a two-divisor hand case.

At $a=1$ the complete ordinary integral locus consists, up to rotation,
of the two-cycle $(2,3)$, the four-family
$$(-1,b,-1,-b),\qquad b\ne0,$$
the eight-family
$$(-1,b,1,-b-2,-1,-b-2,1,b),\qquad b\notin\{-2,-1,0\},$$
and exactly four positive eight-orbits:
$$\begin{gathered}
(1,4,1,6,2,9,2,6),\qquad(1,2,1,4,3,8,3,4),\\
(1,2,2,5,4,5,2,2),\qquad(1,1,1,3,5,9,5,3).
\end{gathered}$$
The proof includes the entire singular plus-factor locus, forces
positivity off that locus, bounds an exact divisor parameter by nine,
and displays every remaining divisor case. This is an explicit
integral atlas, not merely the classical birational order-eight law.

## Classical inputs, source access, and increment boundary

The recurrence, alternating two-integral, QRT structure, and global
order eight at $a=1$ are classical, not new fifth-pass claims. The
integrality of the two-integrals and the complete $a\ne1$ stratum
meeting $-1$ are reused from the fourth-pass proof and its actual
non-author helper review. Neither accepted proof is rerun.

This author read the original contract, actual fourth-pass proof,
independent helper review and scout report, as well as the repository
entry instructions, batch skill/workflow, fifth-pass plan and the
proof-writer skill. The coordinator separately performs and records
primary-source access in `../lyness_sources/`; this author makes no
claim of independent web-source access or complete global novelty
verification. No external theorem is needed for the new elementary
case proofs beyond the precise reused local integrality result.

The proposed paper-level increment remains the full uniform integral
classification. The newly proved strata are useful progress toward it,
not a substitute independent contract. They are not assigned a C-number,
manuscript, PDF, formal grade, or fourth admission.

## Exact remaining gap and stop decision

It remains to rule out, or explicitly classify, ordinary integral
cycles with $a\ne1$ and native least period greater than six. Period
eight is now excluded, but no argument here excludes seven, nine,
ten, or the other possible larger periods. Integer alternating
coefficients, a six-period sign law, or an upper bound obtained from
rational torsion do not alone settle these integral channels.

If E is established, the displayed short-period atlas and the complete
$a=1$ exceptional atlas close the original question. If E fails, an
ordinary higher-period counterexample requires a new classification
branch, not an enlarged alphabet. No new uniform arithmetic mechanism
for E was found in this bounded attempt. The proof-writer instruction
to report an unclosed implication rather than fabricate a proof
therefore fixes the honest stopping boundary.

## Actual execution receipt

- Mathematical programs created, imported, or executed: **zero**.
- Old height-eight graph runs, IR1 reruns, enlarged parameter boxes,
  numerical orbit checks, GPU jobs and paid API calls: **zero**.
- The two finite divisor tables and the fifth-iterate identity are
  hand derivations contained in the proof, not outputs of a hidden run.
- Read-only shell calls read the above inputs, selected previously
  stored metadata, and the assigned directory's initial status. The
  initial path-specific `git status --short` was empty. No Git
  mutation, staging, commit or push was performed by this author.
- All three authored files were installed with `apply_patch` only:
  `FROZEN_ATTEMPT.md`, `PROOF_PACKAGE.md`, and this report.

The coordinator may obtain a separate non-author review of the new
strata; no future review result is prefilled here. Current-team review
is internal AI-assisted review, not human peer review. At handoff, this
lane adds no admission to the batch's existing three contracts.

`NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged. No source period atlas
establishes target Euler factors, root numbers, automorphy, target zeros,
or a Hilbert–Pólya realization.

## Subsequent separate review assignment

After this author's proof handoff, the coordinator assigned a bounded
non-author review of its own rational-period bound. That review is now
recorded at
[INDEPENDENT_PERIOD_BOUND_REVIEW.md](../lyness_sources/INDEPENDENT_PERIOD_BOUND_REVIEW.md).
It read the coordinator's full proof and frozen auxiliary scope and
independently opened two primary-source dependencies, with exact access
limits and input hashes recorded there. This subsequent source access
belongs to that separate review, not to the original author-strata
derivation described above. No mathematical program was run in either
assignment, and the author-strata proof was not changed.

The separate review finds no required correction to the coarse rational
native-period bound $N\le48$, including its singular/reducible-fiber
argument. This makes the remaining integral-period problem finite in
clock, not in coefficient or height, and does not establish E or close
LY4. The coordinator's separate non-author
[strata review](INDEPENDENT_STRATA_REVIEW.md) likewise reports no
mandatory mathematical correction to the actual short-period/$a=1$
proof. Both are internal auxiliary reviews only; neither adds an
admission.
