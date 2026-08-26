# P22 Stage-2.5 reference and citation-context audit

Date: **2026-08-24**  
Final audited manuscript SHA-256:
`5976642a43907a3e01abdb586e9188c697d4a07e7137330a8f285538caaa02fc`

## Final subgate

**PASS after one bounded correction round.**

| Metric | Result |
|---|---:|
| bibliography entries verified | 3/3 |
| citation commands checked | 18/18 (100%) |
| citation contexts supported after correction | 18/18 |
| locators checked | 19/19 |
| orphan references | 0 |
| dangling/undefined citations | 0 |
| unresolved retrievals | 0 |

The initial audit found one `MEDIUM` compound-context deviation and one
`MINOR` locator-description deviation:

1. `CIT-01`: the old introduction made both Frobenius and Verschiebung sound
   like open lifting questions.  Deninger v1 constructs the Frobenius maps
   and asks the lifting question only for Verschiebung on the fp/fppf sites.
2. `CIT-08`: equation (20), p.14 was described too broadly as the power-series
   realization of Witt addition.  It specifically supplies the displayed
   Frobenius/Verschiebung formulas, including `V_N(f)(T)=f(T^N)`.

Both sentences were narrowed in `paper/manuscript.tex`, the PDF was rebuilt,
and an independent delta audit closed both findings.  No adjacent claim or
locator drift was introduced.

## Context ledger

| ID | Manuscript locator / source locator | Final result |
|---|---|---|
| CIT-01 | L121; Deninger p.25 | PASS after correction: constructed Frobenius maps and open Verschiebung question are now separated. |
| CIT-02 | L130; Deninger Secs.3--4 | PASS: noetherian-affine site owner and small-version context. |
| CIT-03 | L144; Deninger Thm.3.4 p.19 | PASS: fpqc sheaf condition. |
| CIT-04 | L146; Deninger Prop.4.3 p.21 | PASS: sheaf epimorphism. |
| CIT-05 | L166; Deninger Sec.4 | PASS: finite-flat/fp and fppf are not conflated. |
| CIT-06 | L216; Deninger Cor.4.6 p.23 | PASS: exact v1 sectionwise assertion reported. |
| CIT-07 | L228; Deninger--Mellit Thm.1.1 | PASS: related monoid-algebra kernel computation, different owner. |
| CIT-08 | L273; Deninger eqs.(4),(20) | PASS after correction: equation (20) is now described as the Verschiebung formula. |
| CIT-09 | L319; Stacks 03CN | PASS: cokernel sheafification and local exactness. |
| CIT-10 | L411; Deninger Ex.4.4 p.22 | PASS: full-Witt detection of the nilpotent class. |
| CIT-11 | L436; Deninger Prop.4.5 pp.22--23 | PASS: integral-domain refinement criterion. |
| CIT-12 | L445; Stacks 00HS | PASS: flat going-down. |
| CIT-13 | L448; Stacks 0AUW | PASS: torsion-free/flat and finite locally free over a Dedekind domain. |
| CIT-14 | L708; Deninger Ex.4.4 p.22 | PASS: `N=2` source control. |
| CIT-15 | L744; Stacks 010I | PASS: extension pullback and pushout. |
| CIT-16 | L746; Stacks 06XP | PASS: Yoneda extension classes and derived `Ext^1`. |
| CIT-17 | L846; Deninger Cor.4.6 p.23 | PASS: source statement is quoted accurately before independent testing. |
| CIT-18 | L904; Deninger Cor.4.7 p.24 | PASS: finer non-subcanonical topology comparator. |

## Bibliographic identity

- `Deninger2025Rational`: official arXiv record, title, author, arXiv ID,
  primary class, v1 date, DOI, and URL agree.  The exact local v1 PDF has
  SHA-256
  `19870cbdddbde82526939eb801c2ce14707dc7b48e54a7bc81f4a84400505002`.
- `DeningerMellit2019`: title, two authors, journal, volume 142, pages 93--102,
  year, and DOI `10.4171/RSMUP/32` agree with the publisher record; Theorem
  1.1 was located in open full text.
- `StacksProject`: the bibliography follows the Stacks recommended identity,
  including its fixed `year=2018`; all five cited stable tags exist.

An exact-hash PDF preflight recorded 31 declared/enumerated/reader pages and
`PASS`.  A later environment rerun recorded `UNAVAILABLE` because `pypdf` was
not installed; that advisory did not replace or rewrite the earlier exact-hash
receipt.  Page locators were additionally checked in local text and official
HTML.

No withdrawal or retraction notice was observed on the official records
checked.  This is a bounded observation, not a universal retraction-clean
certificate.  No bibliographic resolver API, author contact, or external
write was used.
