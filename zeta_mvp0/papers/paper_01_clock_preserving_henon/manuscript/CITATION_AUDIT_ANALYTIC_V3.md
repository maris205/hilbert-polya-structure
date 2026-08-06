# Citation audit for analytic-v3

Verified on 2026-08-06.  The audit covers every source added specifically for
the strict ground-state and relative heat theorems.  Existing Round-2
references retain their prior audit.

| BibTeX key | Primary/authoritative record | Claim supported | Verification |
|---|---|---|---|
| `LiebLoss2001` | [AMS, *Analysis*, 2nd ed.](https://bookstore.ams.org/gsm-14-r/) | Standard Pólya--Szegő and rearrangement framework | Authors, edition, series 14, year, ISBN/AMS metadata checked |
| `BrothersZiemer1988` | [De Gruyter DOI record](https://doi.org/10.1515/crll.1988.384.153) | Equality classification for minimal Sobolev rearrangements | Authors, title, journal, volume 384, pages 153--179, DOI checked |
| `BrascampLiebLuttinger1974` | [Journal DOI record](https://doi.org/10.1016/0022-1236(74)90013-5) | Closest-work context for finite multiple-integral rearrangement | Authors, title, JFA 17(2), pages 227--237, DOI checked |
| `MorreyNirenberg1957` | [Wiley DOI record](https://doi.org/10.1002/cpa.3160100204) | Analytic elliptic regularity used in the equality-case audit | Authors, title, CPAM 10(2), pages 271--290, DOI checked |
| `ReedSimon1978IV` | [Duke bibliographic record](https://scholars.duke.edu/publication/1163835) | Standard positivity/simplicity context for scalar Schrödinger ground states | Authors, volume title, publisher and year checked |
| `Simon2005FunctionalIntegration` | [AMS authoritative book record](https://bookstore.ams.org/chel-351-h) | Brownian bridge and Feynman--Kac foundations | Author, second edition, Chelsea volume 351, year and ISBN checked; AMS description explicitly covers Brownian bridges and four Feynman--Kac proofs |
| `BoldtGueneysu2023` | [Springer DOI record](https://doi.org/10.1007/s40072-022-00269-3) | Modern noncompact Friedrichs/Feynman--Kac context | Authors, title, journal, volume 11, pages 1519--1552, issue year and DOI checked |
| `Fucci2018` | [Springer DOI record](https://doi.org/10.1007/s11005-018-1086-8) | Closest-work context for heat-trace expansions with confining potentials on unbounded domains | Author, title, LMP 108(11), pages 2453--2478 and DOI checked |
| `Wang2026HenonPreprint` | [Exact 17-page PDF at fixed Git commit](https://github.com/maris205/riemann_henon/blob/f86bf21a32ad5bcb21ba81d312cc68e91bcc7db0/paper/manuscript.pdf) | Provenance of the prior-frozen H\'enon value \(a=1.02\), not support for the new theorems | Public commit `f86bf21a32ad5bcb21ba81d312cc68e91bcc7db0` was cloned over SSH; its `paper/manuscript.pdf` and the local archive have identical SHA-256 `23dad812162728316f633081e1a1995d4c00614a70d0f5877d425c68d0c726b9`.  The PDF internal title, author, date, page count, affiliation, and email were checked. |

## Scope controls

- Fucci's polynomial-potential result is cited as context, not as a theorem
  from which the exponential Hénon result follows.
- Boldt--Güneysu and Simon support the Feynman--Kac framework; the moving
  main/tail remainder estimate is proved in the manuscript.
- Brascamp--Lieb--Luttinger is used only as closest-work context.  The
  manuscript makes no all-time heat-trace ordering claim from a Trotter
  limit.
- Brothers--Ziemer is used only after the manuscript checks finite-measure
  superlevel sets and the zero-measure intermediate critical set.
- The published `Wang2026PrimeChaos` paper supports only the broader
  low-dimensional deterministic-chaos context.  The H\'enon-specific
  \(a=1.02\) provenance is assigned only to the separately identified
  fixed-commit preprint; neither source supports the analytic-v3 theorems.
- Zenodo record `10.5281/zenodo.19084735` is a related, expanded 21-page
  manuscript titled *The Physical Topology of Riemann Zeros: Dual Evidence
  from Quantum Coherence and Macroscopic Dissipation*.  Its PDF SHA-256 is
  `a414cef5072126a67ff6b9089b19c00536ad31168e31b32095493ade36d0a46b`, so it
  is explicitly not used as the locator for the cited 17-page manuscript.
- No new reference is used to support a prime-power, zeta-zero, or RH claim.

## Final bibliography census

- BibTeX database entries: 77.
- Distinct entries printed in analytic-v3: 67.
- Unresolved citation keys: 0.
- Repeated BibTeX keys: 0.

BibTeX completed without missing entries, repeated keys, or unresolved
citations in the four-pass 45-page PDF build.  The older 69-entry/59-printed
census belongs only to the immutable Round-2 baseline.
