# Source audit and ownership boundary

## Locked primary and modern sources

1. Michel Hénon, “L'amas isochrone I,” *Annales d'Astrophysique* **22** (1959), 126–139. ADS bibcode [`1959AnAp...22..126H`](https://ui.adsabs.harvard.edu/abs/1959AnAp...22..126H/abstract). This is the original isochrone-cluster construction.
2. Michel Hénon, “L'amas isochrone II: Le calcul des orbites,” *Annales d'Astrophysique* **22** (1959), 491–498. ADS bibcode [`1959AnAp...22..491H`](https://ui.adsabs.harvard.edu/abs/1959AnAp...22..491H/abstract). This is the original orbit-calculation source.
3. Paul Ramond and Jérôme Perez, “New Methods of Isochrone Mechanics,” *Journal of Mathematical Physics* **62** (2021), 112704, DOI [`10.1063/5.0056957`](https://doi.org/10.1063/5.0056957), preprint [`arXiv:2104.05643`](https://arxiv.org/abs/2104.05643). This provides a modern action-angle and Hamiltonian treatment.
4. Jean-Baptiste Fouvry and Simon Prunet, “Linear response theory and damped modes of stellar clusters,” *Monthly Notices of the Royal Astronomical Society* **509** (2022), 2443–2456, DOI [`10.1093/mnras/stab3020`](https://doi.org/10.1093/mnras/stab3020). Its official Appendix C records the isochrone frequency ratio used here.

The source-owner tokens are frozen in both evidence and evaluation files.  The two 1959 papers own the classical construction and orbit mechanics; Ramond–Perez owns the cited modern action-angle treatment; Fouvry–Prunet supplies a directly inspectable modern record of the frequency map.

## What this package does and does not claim

This package does **not** claim that the isochrone potential, radial action, isochrony, or frequency map is new in the literature.  Its contribution is narrower: a reproducible theorem-and-certificate closure that keeps the allowed energy domain and degenerate faces explicit, validates exact formulas independently, and freezes a conservative Route-A verdict.

The proof is self-contained.  Literature sources establish provenance and prevent a false priority claim; they are not used as substitutes for missing steps.  The finite grid is regression evidence only and is not presented as an all-parameter proof.

## Claim-to-source ledger

| Claim | Ownership / support | Status in this package |
|---|---|---|
| Isochrone potential and orbit mechanics | Hénon I–II | Classical; rederived |
| Action-angle Hamiltonian | Ramond–Perez | Classical/modern literature; rederived |
| \(\Omega_\phi/\Omega_r=\tfrac12(1+L/\sqrt{L^2+4\mu b})\) for \(L\geq0\) | Fouvry–Prunet Appendix C; compatible with Ramond–Perez | Reproved |
| Energy-boundary and degenerate-face bookkeeping | Algebra in `THEOREM_PACKAGE.md` | Package-level certificate organization |
| Route-A tuple | Frozen evaluator contract | Conservative evaluation, not a literature claim |

No searched or cited source is construed as providing arithmetic local data, a target Euler product, root numbers, a target functional equation, a target zero match, or a Hilbert–Pólya realization.
