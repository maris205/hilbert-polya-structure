# HCS-C30 primary-source verification

Verification date: **2026-08-11 UTC**
Purpose: framework and claim-boundary audit, not verification of repository
matrix arithmetic.

## Protocol

Only primary papers, official publisher pages, author manuscripts, and an
official erratum are used for technical claims.  For each source we checked
the bibliographic identity, the relevant section or stated construction, and
whether its hypotheses actually match the C30 object.  The C25/C26 word
calculations are verified by the repository certificate and independent code,
not attributed to literature.

## Claim-to-source matrix

| Claim used by C30 | Primary source and locator | Audit result |
|---|---|---|
| Rauzy chronology has later matrices on the left | Avila--Gouëzel--Yoccoz, Section 3.1.3 | supported |
| Length data transforms by the inverse transpose; the cone is a genuine branch-domain condition | Avila--Gouëzel--Yoccoz, Section 3.2, Eq. (3.1) and the definition of \(\Delta_\gamma\) | supported |
| The invertible extension supplies past coordinates rather than new positive-time inverse tokens | Avila--Gouëzel--Yoccoz, Section 3.3.1; C30 semantic inference | supported as a scoped inference |
| The accelerated return construction uses a positive roof/return time | Avila--Gouëzel--Yoccoz, Definition 2.3 and Sections 4.1.1--4.1.3 | supported |
| A symbolic suspension begins with a positive roof | Parry--Pollicott, Chapter 6 | supported |
| Standard Anosov trace expansions use positive periods, primitive periods, and repetitions | Dyatlov--Zworski, Section 2.2, Eqs. (2.4)--(2.5) | supported |
| Anisotropic Banach and microlocal approaches can define traces/determinants without ordinary trace class | Gouëzel--Liverani; Giulietti--Liverani--Pollicott with erratum; Dyatlov--Zworski | supported; prevents overclaim |
| Stable--unstable analytic correspondences use cross maps/partial adjoints rather than compact same-space inverse composition operators | Fried; Baladi--Pujals--Sambarino, Definition 2.4 and Lemmas 3.7--3.8 | supported |
| Formal symmetric inverse Rauzy graph is the AGY natural extension | no primary support located | forbidden |
| A C29 kernel word is a positive AGY periodic orbit | no primary support; exact C30 certificate refutes it for the frozen words | refuted in scope |

## Verified records

1. A. Avila, S. Gouëzel, J.-C. Yoccoz, *Exponential mixing for the
   Teichmüller flow*, Publications Mathématiques de l'IHÉS 104 (2006),
   [arXiv:math/0511614](https://arxiv.org/abs/math/0511614).
2. W. Parry, M. Pollicott, *Zeta functions and the periodic orbit structure of
   hyperbolic dynamics*, Astérisque 187--188 (1990),
   [official SMF PDF](https://smf.emath.fr/system/files/filepdf/AST_1990__187-188__1_0.pdf).
3. S. Gouëzel, C. Liverani, *Banach spaces adapted to Anosov systems*,
   Ergodic Theory and Dynamical Systems 26 (2006),
   [arXiv:math/0405278](https://arxiv.org/abs/math/0405278).
4. P. Giulietti, C. Liverani, M. Pollicott, *Anosov flows and dynamical zeta
   functions*, Annals of Mathematics 178 (2013),
   [DOI](https://doi.org/10.4007/annals.2013.178.2.6), with
   [official author erratum on arXiv](https://arxiv.org/abs/2203.04917).
5. S. Dyatlov, M. Zworski, *Dynamical zeta functions for Anosov flows via
   microlocal analysis*, Annales de l'ENS 49 (2016),
   [arXiv:1306.4203](https://arxiv.org/abs/1306.4203).
6. D. Fried, *Meromorphic zeta functions for analytic flows*, Communications
   in Mathematical Physics 174 (1995),
   [DOI](https://doi.org/10.1007/BF02099469).
7. V. Baladi, E. R. Pujals, M. Sambarino, *Dynamical zeta functions for
   analytic surface diffeomorphisms with dominated splitting*,
   [arXiv:math/0307045](https://arxiv.org/abs/math/0307045).

The following primary graph-zeta records are used only to locate the finite
Hashimoto/von-Neumann construction historically; none is evidence for the
C30 source-dynamics no-go:

8. K.-i. Hashimoto, *Zeta functions of finite graphs and representations of
   p-adic groups*, Advanced Studies in Pure Mathematics 15 (1989),
   [DOI](https://doi.org/10.2969/aspm/01510211).
9. H. M. Stark, A. A. Terras, *Zeta functions of finite graphs and
   coverings*, Advances in Mathematics 121 (1996),
   [DOI](https://doi.org/10.1006/aima.1996.0050).
10. D. Lenz, F. Pogorzelski, M. Schmidt, *The Ihara zeta function for
    infinite graphs*, Transactions of the American Mathematical Society 371
    (2019), [DOI](https://doi.org/10.1090/tran/7508) and
    [arXiv:1408.3522](https://arxiv.org/abs/1408.3522).

## Integrity and limitation notes

- The Giulietti--Liverani--Pollicott erratum is carried beside the original;
  C30 does not rely on the corrected spectral claim for its exact no-go.
- No source is used as evidence for the repository-specific C25/C26 integer
  relations.
- The absence of a source identifying C29 with the AGY natural extension is a
  bounded search result, not a universal literature theorem.
- General clean-fixed-manifold regularization remains open; C30 rules out only
  the ordinary nuclear and standard isolated-hyperbolic trace promotion under
  its declared hypotheses.
