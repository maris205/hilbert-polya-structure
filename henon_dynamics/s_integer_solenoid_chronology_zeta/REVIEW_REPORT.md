# Independent review report

Date: 2026-08-06

## Scope

Three adversarial passes independently audited the exact algebra and code, the
theorem chain, and the primary-source positioning.  Reviewers were instructed
to look for fatal or major defects rather than to optimize prose.

## Algebra and computation

The matrix convention, fixed-index formula, mod-2 language, period-five
witnesses, global generating function, and continuation radius were checked
against the generated artifacts.  Earlier audit comments about a stale PDF,
an imprecise archimedean-expansion sentence, and missing artifact hashes were
resolved before release.  The final exact suite has 10/10 passing unit tests,
an implementation-independent checker, and seven passing SHA-256 checks.

## Theorem audit

The final theorem review returned `FINAL ACCEPT`.  Corrections made during the
review include:

- writing the archimedean sum as
  \(2^n+16^n-\operatorname{tr}(A+B)^n\);
- distinguishing the finite places above two rather than speaking of one
  undifferentiated place;
- specifying the fair Bernoulli measure in the Koopman obstruction;
- keeping the finite-state recurrence variable
  \(q_n=8^n c_n\) explicit;
- retaining chronology in every product and trace calculation.

The Bell--Miles--Ward hypothesis audit was then expanded once more: the paper
now identifies the full \(\mathbb Z[1/2]\)-lattice, its induced place set,
the Hensel-split unit direction, and the fact that the odd-trace branch is
necessarily irreducible.  A final narrow theory recheck after this
strengthening returned `FINAL ACCEPT`.

## Source and novelty audit

The final literature review returned `FINAL ACCEPT`.  It verified that:

- Paper 5 is described as an unpublished numerical/heuristic source rather
  than as a proved Hilbert--Pólya construction;
- the Bell--Miles--Ward theorem is applied only to individual return
  automorphisms, not to the full infinite primitive product;
- the Chothi--Everest--Ward and Miles results are not overstated;
- nearby rank-two-solenoid and finite-adelically-distorted work is cited;
- the Carvalho--Rodrigues--Varandas comparison is limited to its
  Ruelle-expanding setting;
- the novelty verdict remains scoped `YELLOW`, not a priority claim.

There are 11 citation keys and 11 bibliography records, with no missing or
unused entries.

## Release ruling

No critical or major issue remains.  The arithmetic-dynamical theorem package
is release-ready.  Its Hilbert--Pólya status remains a negative Route-A result:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
ROUTE_A_REJECTED
```

This distinction is intentional: a sound dynamical-zeta theorem is not being
presented as a Riemann spectral construction.
