# Round 4 arithmetic scout: two closures, zero new admissions

Date: 2026-09-08 UTC. AI-generated internal screen; not a paper,
evaluation, referee report, or priority claim. Only this lane's
directory was written. The batch remains at its inherited **3/5**
from this lane's perspective: **0 new admissions, 0 manuscripts/PDFs,
0 C-numbers, 0 mathematical programs and 0 mathematical executions**.
The coordinator alone owns the global state.

## Decision

| Frozen candidate | Mathematical status | Substantial-paper decision |
| --- | --- | --- |
| DH1: $H_c=(y,y^2+c-2x)$, every $c\in\mathbb Z$, every periodic point in $\mathbb Q^2$ | PROVABLE AS STATED: exact all-parameter classification complete | Stop: short classical local contraction application |
| DH2: fixed $H_0$, $P=(0,1)$, $D_n=\gcd(|u_n|,|u_{n+1}-1|)$, every native $n\geq1$ | PROVABLE AS STATED: $2^{-n}\log D_n\to0$, unconditionally | Stop: short inverse-congruence proof; broader question and a recent general theorem already sourced |

Only these two different arithmetic observables were deep-screened.
No third Jacobian/degree variant, parameter table, changed clock,
finite field expansion, or numerical prefix was substituted.

## DH1 outcome

The complete periodic locus is:

- If $c=2-k(k+1)$, $k\geq0$, the two fixed points are
  $(1-k,1-k)$ and $(2+k,2+k)$.
- If $c=-7-k(k+1)$, $k\geq0$, the unique two-cycle is
  $(-k-2,k-1)\leftrightarrow(k-1,-k-2)$.
- Otherwise there are no rational periodic points.

The even and odd parameter sets do not overlap, and no least period
above two occurs. The proof first forces integrality by a minimum
valuation argument valid at every prime. It then shows $H_c^2$
improves shared parity-class precision by one power of two, making
reduction injective on all periodic points. The exact mod-two cycles
and two quadratic equations finish the full classification.

The inspected C412 theorem has Jacobian $+1$; C109 is a fixed
Jacobian-$1/2$ witness map. The concrete Ingram period family has
Jacobian $-1$, and the two Hutz sources concern other objects. Those
are not literal ownership of this table. Even so, the residual proof
is too short/classical to supply the missing paper-level contribution.
It must not be padded with counts or zeta notation into a new slot.

## DH2 outcome and the corrected source boundary

All $u_n$ for $n\geq1$ are odd, so $D_n$ is positive and odd.
An explicit escape induction gives $\log u_j\leq C2^j$ with fixed
$C$ and $u_j\to+\infty$. For any fixed backward shift $k$,
$H_0^{-k}(P)$ has a first coordinate $B_k/A_k$ with $A_k$ a power
of two. Inverse reduction modulo the odd $D_n$ gives

$$
D_n\mid A_ku_{n-k}-B_k.
$$

The right side is eventually nonzero. Consequently
$\limsup_n2^{-n}\log D_n\leq C2^{-k}$; letting $k\to\infty$ proves
the entire frozen limit. Constants depending on $k$ disappear only
after fixing $k$ and letting $n\to\infty$. There is no unproved
uniformity assumption, use of an even-modulus inverse, or hidden
Vojta/genericity requirement.

Source-first verification also found the applicable unconditional
Matsuzawa theorem from July 2025 and the genuine Barrios correction
from July 2026. Their exact roles, access limits, and map-specific
hypotheses are documented, not inferred from snippets. The larger
theorem is not needed for the elementary proof. Thus an earlier
possible “only Vojta conditional / non-split gap” diagnosis would be
incorrect and is not the final status.

This note does not assert a complete solution of Question 47's two
separate parts or expand the contract to all number fields. In
particular, the bounded-ideal infinitely-often subquestion is untouched.
The portable inverse mechanism is recorded only through this exact
fully proved instance, with no priority claim.

## Deliverables and actual activity receipt

- [FROZEN_CONTRACTS.md](FROZEN_CONTRACTS.md): object, all quantifiers,
  forward clock, observable, classical deduction, success and stop
  for exactly two candidates; no mathematical-test authorization.
- [COMPLETE_SHORT_PROOFS.md](COMPLETE_SHORT_PROOFS.md): complete
  elementary proofs, assumptions, dependency map, boundary cases,
  and optional recent-theorem hypothesis mapping.
- [SOURCE_AUDIT.md](SOURCE_AUDIT.md): 20 actual fresh queries including
  four roughly six-month-filter queries; eight primary-source entries
  with concrete access scope and two local nearest-owner routes.

Actual mathematical run receipt: **none**. The seven initial values
in the escape proof were obtained by hand substitution as a proof
base case, not by a script or experimental census. No old execution,
accepted item, prior round's proof, or pre-existing program was rerun.
Read-only shell discovery/source reading and file writes with
`apply_patch` are not mathematical executions.

Author-side equation and quantifier checking found no remaining
mathematical gap in these two short proofs. No independent reviewer
certificate is claimed.

Final author-side static receipt: all four Markdown files were read
back. One simple local-link scan over those four files found **10 local
link occurrences, 6 unique existing local targets, 12 external links
not re-requested by the scanner, and 0 broken local targets**. This
was a documentation-only Perl scan, not a mathematical execution or
independent mathematical reproduction. Subsequent wording/receipt
edits added or changed no links; the scan was not repeated.

## Stop and scope

Both frozen stopping conditions have been reached. Do not continue
these contracts by changing a Jacobian, scanning larger $n$, or
writing a manuscript. This lane supplies zero new substantial
admissions and leaves the other lanes/coordinator decisions untouched.

The directory label `dissipative_henon` is historical: the forward
Jacobian here is $2$, so the map is not forward area-dissipating.
The inverse clock was not substituted. `NO_BAD_EULER_OR_ROOT_NUMBER`
is unchanged; nothing here identifies target Euler factors, root
numbers, automorphy, target zeros, or a Hilbert–Pólya realization.
