# Paper Citation Audit

**Audit date:** 2026-08-14  
**Input boundary:** `notes/CITATION_VERIFICATION.md` and
`notes/NOVELTY_AUDIT.md`, followed by DOI/arXiv/publisher metadata checks  
**Policy:** cited claims use only the safe-use column of the existing audit;
no negative search is converted into a historical priority claim.

## Selected records and safe manuscript use

| Manuscript key | Verified record | Stable identifier | Permitted use |
|---|---|---|---|
| `kook1989periodic` | Hyung-tae Kook and James D. Meiss, “Periodic orbits for reversible, symplectic mappings,” *Physica D* 35, 65--86 (1989). | DOI `10.1016/0167-2789(89)90096-1` | Periodic variational/generating action for symplectic maps. |
| `mackay1984transport` | R. S. MacKay, J. D. Meiss, and I. C. Percival, “Transport in Hamiltonian systems,” *Physica D* 13, 55--81 (1984). | DOI `10.1016/0167-2789(84)90270-7` | Dynamical role of action differences; not absolute normalization. |
| `meiss1992symplectic` | J. D. Meiss, “Symplectic maps, variational principles, and transport,” *Reviews of Modern Physics* 64, 795--848 (1992). | DOI `10.1103/RevModPhys.64.795` | Standard discrete variational/generating formalism and Hénon context. |
| `delshams1997melnikov` | Amadeu Delshams and Rafael Ramírez-Ros, “Melnikov Potential for Exact Symplectic Maps,” *Communications in Mathematical Physics* 190, 213--245 (1997). | DOI `10.1007/s002200050239` | $F^*\phi-\phi=dS$ and additive-constant ambiguity. |
| `ginzburg2009action` | Viktor L. Ginzburg and Başak Z. Gürel, “Action and index spectra and periodic orbits in Hamiltonian dynamics,” *Geometry & Topology* 13, 2745--2805 (2009). | DOI `10.2140/gt.2009.13.2745` | Action spectra and iteration background; no algebraicity attribution. |
| `mazzucchelli2013degenerate` | Marco Mazzucchelli, “Symplectically degenerate maxima via generating functions,” *Mathematische Zeitschrift* 275, 715--739 (2013). | DOI `10.1007/s00209-013-1157-6` | Discrete symplectic action/average-action context. |
| `bialy2023locally` | Misha Bialy and Daniel Tsodikovich, “Locally maximising orbits for the non-standard generating function of convex billiards and applications,” *Nonlinearity* 36, 2001--2019 (2023). | DOI `10.1088/1361-6544/acbb50` | Current example of a summed generating action. |
| `friedland1989dynamical` | Shmuel Friedland and John Milnor, “Dynamical properties of plane polynomial automorphisms,” *Ergodic Theory and Dynamical Systems* 9, 67--99 (1989). | DOI `10.1017/S014338570000482X` | Generalized-Hénon polynomial-automorphism background only. |
| `moser1994quadratic` | Jürgen Moser, “On quadratic symplectic mappings,” *Mathematische Zeitschrift* 216, 417--430 (1994). | DOI `10.1007/BF02572331` | Quadratic symplectic/Hénon normal-form context. |
| `dehenon2024open` | Julia Xénelkis de Hénon, “Hénon Maps: A List of Open Problems,” *Arnold Mathematical Journal* 10, 585--620 (2024). | DOI `10.1007/s40598-024-00252-x` | Current real/complex/algebraic/arithmetic Hénon questions. |
| `kim2024many` | Hyeonggeun Kim, Holly Krieger, Mara-Ioana Postolache, and Vivian Szeto, “Hénon maps with many rational periodic points” (2024 preprint). | arXiv `2412.01668` | Active arithmetic periodic-point context; explicitly a preprint. |
| `baker2022transcendental` | Alan Baker, *Transcendental Number Theory*, Cambridge Mathematical Library edition (2022), with a foreword by David Masser. | DOI `10.1017/9781009229937` | Authoritative Hermite--Lindemann/transcendence background. |
| `berry1999riemann` | M. V. Berry and J. P. Keating, “The Riemann Zeros and Eigenvalue Asymptotics,” *SIAM Review* 41, 236--266 (1999). | DOI `10.1137/S0036144598347497` | Motivation for hypothetical periods proportional to prime logarithms. |

## Metadata repair relative to internal shorthand

The existing novelty note calls the 2024 Hénon survey “Berger et al.”  The
publisher page and DOI metadata list the author as the collective name
**Julia Xénelkis de Hénon**.  The manuscript and bibliography use the
publisher record and do not propagate the internal shorthand.

Crossref's BibTeX record for the 2022 Cambridge edition lists David Masser as
an author, but the publisher page identifies Alan Baker as the author and
David Masser as the writer of the foreword.  The bibliography follows the
publisher page.

## Claim-level restrictions

- None of the action papers is cited for an arithmetic-action theorem.
- None of the Hénon papers is cited for the present $3\mathcal A_G$
  certificate or prime-logarithm exclusion.
- Baker is cited for a classical theorem, not for the paper-specific
  application.
- Berry--Keating supplies motivation only; no trace formula, zero data, or
  successful Riemann dynamics is imported.
- The phrase “no direct checked collision was located” is permitted only as a
  recall-limited literature-audit statement.  “First,” “novel theorem,” and
  equivalent priority claims are forbidden.

## BibTeX integrity policy

The production bibliography contains only keys actually cited by the
manuscript.  DOI entries were retrieved through DOI content negotiation and
normalized to ASCII-safe LaTeX; the two ambiguous author records were
corrected from publisher pages.  The arXiv entry remains explicitly typed as
a preprint.  No `[VERIFY]` entry is permitted in the compiled snapshot.
