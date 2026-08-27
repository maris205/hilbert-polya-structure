# Stage 2 report — Papers 77–81

Status: **five manuscripts and five canonical PDFs generated**.
External release: **HOLD**.

## Artifact census

| Paper | Pages | Concrete landed advance | Deterministic control |
|---|---:|---|---|
| P77 | 9 | finite CB tower, full nilpotent endomorphism monoid, automorphisms, and arithmetic conjugacy rigidity | 266,067 reported check groups across limits, composition, bounded differences, and base separation |
| P78 | 4 | arbitrary-profile sandpile-translation period, localized corollaries, and full finite translation dynamics | 7,938 two-site + 1,176 arbitrary-profile cokernel checks; 23,346 literal burning/stabilization/orbit checks |
| P79 | 8 | delayed reversal onset plus persistent-phase entropy, recovery, nonmixing, and Markov-order classification | 309 grouped exact assertions |
| P80 | 4 | full cocktail-party majority functional graph, zeta/natural extension, and critical window | 87,380 states, 309,038 instrumented asserts; iterate counts through `k=12` |
| P81 | 5 | mixing/periodic gluing and exact scale-entropy coefficient for a continuum relation shift | 18,240 bridge, 192 Jacobian, and 208 Funk checks |

Total canonical manuscript length: **30 pages**.

## Paper packages

- [`papers/77-digit-weight-automatic-towers/`](../../papers/77-digit-weight-automatic-towers/)
- [`papers/78-complete-bipartite-sandpile-translations/`](../../papers/78-complete-bipartite-sandpile-translations/)
- [`papers/79-noisy-fkm-delayed-irreversibility/`](../../papers/79-noisy-fkm-delayed-irreversibility/)
- [`papers/80-cocktail-party-majority-zeta/`](../../papers/80-cocktail-party-majority-zeta/)
- [`papers/81-spherical-orthogonality-scale-entropy/`](../../papers/81-spherical-orthogonality-scale-entropy/)

Each package contains `main.tex`, `references.bib`, `main.pdf`, a README, and
an independently runnable script under `code/`.  LaTeX uses an internal
anonymous `amsart` format and names no target venue.

## Claim discipline

- P77 excludes `d=0` from arithmetic rigidity and treats `d=1` as an owned
  base case.
- P78 states explicitly that its result is a sink-relative loading-coordinate
  computation, not a new sandpile group, `K_{m,n}` classification, or generic
  finite-translation theorem.
- P79 gives Mohri et al. direct ownership of the uniform de Bruijn-context
  construction and separates emission noise from transition noise.
- P80 claims exact family-specific counts, not the general period-two theorem.
- P81 cites the Funk spectrum and restricts measure uniqueness to the
  homogeneous one-step Markov class.

Writing-level source details are in
[`phase2/SOURCE_VERIFICATION_REPORT.md`](phase2/SOURCE_VERIFICATION_REPORT.md).
