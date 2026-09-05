# C392 source and provenance audit

Frozen baseline `0c877206d202f732e21ea0b194f9c7fdf30467ee`;
evaluator v0.2.0 SHA256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
Date 2026-09-05. Scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Verified primary owners and actual access

- Barrionuevo, Burton, Dajani and Kraaikamp, *Ergodic properties of generalized
  Lüroth series*, Acta Arithmetica 74(4), 311–327 (1996),
  DOI [10.4064/aa-74-4-311-327](https://doi.org/10.4064/aa-74-4-311-327).
  The [publisher record](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/74/4/108990/ergodic-properties-of-generalized-luroth-series),
  author institution record and CrossRef BibTeX confirmed metadata. Publisher
  full-PDF download timed out; no claim of a successful current-turn full-PDF
  reading is made. Coding here is proved directly; this citation credits the
  classical source, not the meromorphic residue theorem.
- Bandtlow and Jenkinson, *On the Ruelle eigenvalue sequence*, ETDS 28(6),
  1701–1711 (2008), DOI
  [10.1017/S0143385708000059](https://doi.org/10.1017/S0143385708000059).
  CrossRef BibTeX and publisher record checked; the actual author
  [arXiv PDF](https://arxiv.org/pdf/0802.1468) was read at Theorem 4.2
  and its proof, printed pages 6–7 (PDF pages 6–7), for the general
  holomorphic trace/determinant framework. Ruelle and Mayer are explicitly
  credited through this history; our concrete rank-one proof does not
  claim to invent that framework.
- [NIST DLMF §25.11](https://dlmf.nist.gov/25.11): actual reference page
  checked for the Hurwitz zeta definition and meromorphic simple-pole
  continuation used in the centered expansion. This is an explicitly
  imported classical analytic theorem.

Bibliography values were programmatically fetched by DOI content negotiation,
then normalized to the verified journal publication year. No fabricated
author, DOI or journal field was inserted. Direct DOI browser redirects
sometimes failed; official records and author PDFs supplied the documented
fallback rather than an invented successful download.

## Collision and project increment

C241 owns positive Lüroth coding and the scalar word identity only in the
right half-plane. C380 owns a finite Blaschke Hardy-annulus family with
geometric eigenvalues, not a countable-branch meromorphic parameter family.
C132/C137 own finite nonlinear Möbius Bergman systems, not this residue
parity phenomenon. Searches included “Lüroth transfer spectrum”,
“Luroth eigenvalues”, “Lüroth Fredholm”, “Luroth Hardy operator” and
the general Ruelle eigenvalue literature. These searches found owners;
they do not certify absence of earlier special-case formulas.

The mandatory completion beyond C241 is the all-plane operator continuation,
nonzero square-zero residue theorem and exact determinant-pole obstruction.
Every infinite statement is proved in the proof ledger. The strict new
A1_WEAK does not inherit the older C241 A1 label automatically.

## Integrity and arithmetic boundary

Current-team C379 agent actually read the full proof and verified the
centered operator, Cauchy tail, all ranks and noncancelling determinant poles.
No external model or human peer review occurred.
The seven failure modes and actual phase-test repair are recorded in
review/FAILURE_MODE_AUDIT.md. Finite numerical values are not certified intervals.
Composite derivative slopes and a Hurwitz rewriting do not define target
prime carriers, local Euler data or a target functional equation.
