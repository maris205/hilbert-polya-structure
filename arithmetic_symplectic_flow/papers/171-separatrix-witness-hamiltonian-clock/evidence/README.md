# Evidence index — complete rational-barrier Hamiltonian

**Candidate ID:** ASFS-20260915-SWH01  
**Status:** ADVANCE — COMPLETE PRIME-ONLY HAMILTONIAN PACKETS AND PHYSICAL LOGARITHMIC CLOCK; NATURALNESS OPEN.

## Exact evidence and reproducibility

The [version-1 card](../candidate-card.md) was created before mathematical
claims or computations. No tuple, physical units, fixed energy or operator
owner changed after that freeze. The [paper](../paper.md) contains all
inputs and every proof; the [ledger](../claim-ledger.md) separates each
positive result from stronger OPEN claims.

| Check | Exact method / inputs | Output and limit |
| --- | --- | --- |
| Full completeness and regular energy | Differentiate rational W, bound abs(W')<=4, compare critical energies 0,c_n with 1 | Proposition 1; exact all-state argument, no integrator |
| Actual return and omitted states | Classify the even bounded well at E<0, E=0, 0<E<c_n, E=c_n and E>c_n; apply pdot<=-8 on composite components | Proposition 2; outer branches explicitly distinct from inner orbits at the same E |
| Full positive-dimensional owner | Differentiate variable-time return preserving I=QP; construct first-return suspension conjugacy | Proposition 3; return-saturation only, not the whole energy surface |
| Primitive ledger and repetitions | Solve Q=e^t Q, P=e^-t P on the full energy owner, then classify scalar E=1 | Proposition 4; exact multiplicity one per prime and every repeated transverse monodromy |
| Period asymptotics | Substitute y=(1-q^2)/(1+q^2), delta=1/sqrt(n^2+1); split the explicit integral at 1/2 | Proposition 5; uniform O(1), leading coefficient 2 sqrt2, no fit or prescribed roof |
| Ordinary product | Compare actual T_p against 2 sqrt2 log p within a uniform bound; elementary prime-reciprocal divergence | Corollary 6; exact absolute abscissa, not analytic continuation or a determinant |

There are no numerical observations, finite orbit censuses, precision or
cutoff claims, hidden script outputs, prime/zero datasets, LaTeX/PDF assets
or external-model uploads. No novelty claim or expanded literature review
is made: all mathematical claims are proved here.

## Bounded source and collision record

Read-only contextual inputs were the local AGENTS/plan/readme, the
[175 scope](../../175-six-lane-geometric-source-frontier/candidate-card.md),
[prior-work guide](../../../docs/prior_work/README.md), and the relevant
[164 card](../../164-witness-hamiltonian-return-clock/candidate-card.md)
and [full proof](../../164-witness-hamiltonian-return-clock/paper.md).
[155](../../155-derivative-roof-completeness-test/paper.md) supplies the
need to test full-state completeness, not a result for this new clock.
[160](../../160-source-geometric-return-clock/candidate-card.md) is only
the disclosed different dilation/reset comparator. No old package was
modified and no earlier trace, clock or result was transferred.

## Review provenance

A separate native invocation, `separatrix_clock_review`, was dispatched
after the card freeze with read access and sole write ownership of
[review.md](review.md). It received the candidate and inherited context;
therefore this is not blind review. Its mathematical findings and any
read-only helper checks are disclosed in the actual review receipt.
The current author must not replace a pending receipt with an assumed
pass. Model-assisted checking is not human peer review, not an
independent-error guarantee, and not proof certification.

ARS was used only for bounded claim/evidence/counterargument checks of
the approved lane. No publication workflow, journal criteria, runtime
installation, hook or external provider was invoked. All edits use
apply_patch and remain within the assigned Markdown package.

## Structural verification

Final verification was run on 2026-09-15 after the actual review receipt
existed. A read-only Node heredoc (`node -`) recursively enumerated only
this package's Markdown files with fs.readdirSync, read each as UTF-8,
and checked:

1. every inline Markdown local-file target resolves relative to its source
   file, after removing a fragment and decoding the path; external URLs,
   mail links and same-file fragments are excluded;
2. each of the five core files contains the literal candidate ID and full
   final status printed at the top of this index;
3. no UTF-8 text contains a control character below U+0020 other than
   line feed or tab;
4. each contiguous Markdown table has consistent pipe-separated column
   counts; only lines beginning and ending with a pipe are table rows.

Observed output: **6 Markdown files, 39 local-file links, 5 core ID/status
pairs, 9 tables, zero reported problems.** No persistent script or output
file was created. These are document-structure checks, not theorem checks.

The two actual review minors (two carriage-return bytes in equation 18
and an unescaped table-cell absolute-value delimiter) were repaired using
apply_patch and independently re-read as ADDRESSED. The first structural
precheck ran before the review file existed, so its four review links
were still unresolved. Its provisional table detector also mistook two
displayed absolute-value expressions for tables; the final detector above
corrected that scope. Neither preliminary observation was reported as a
final pass or used to alter a mathematical claim.

Final review state: NO MATHEMATICAL BLOCKER IDENTIFIED IN THE DECLARED
ENGINEERING CLAIMS; no unresolved Critical/Major findings and both minors
ADDRESSED. The reviewer stopped editing before this final verification.
