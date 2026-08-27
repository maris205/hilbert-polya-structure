# Hostile audit

## Repaired-hash attacks

The mutation suite changes semantic content, recomputes the canonical payload
hash, and asks the independent checker to reject the result.  All 74 attacks are
rejected.  Coverage includes:

- candidate/date/commit/evaluator/scope drift;
- DOI, author, locator, oriented-matroid, and strict-SST source overclaims;
- changes to every theorem-lock sentence and attribution field;
- every Route-A qualification, tuple, overall verdict, and Route-B flag;
- every forbidden-claim boolean;
- every aggregate count;
- family/profile, hyperplane, covector, weight, separation, component, flat,
  matrix, polynomial, trace, sampler, and mixing mutations.

One additional semantic mutation retains the old payload hash; it is rejected
as stale.

## Mathematical attacks

| Attack | Resolution |
|---|---|
| merge equal numeric eigenvalues and lose flat multiplicities | retain the flat-indexed factorization; aggregation is only numerical |
| use the number of vanishing hyperplanes as geometric codimension | rejected; codimension is reconstructed as the intersection-poset chain rank, which matters for braid flats |
| infer self-adjointness from diagonalizability | rejected; the chains are generally nonreversible |
| call stationary output at a stop a strict SST | rejected; independence from the stopping time is neither source-locked nor generally valid |
| reduce the nonseparating boundary to “nonunique” | replace with the exact closed-component simplex classification |
| treat finite fixtures as proof | rejected; all-family ownership stays with Brown--Diaconis |
| enlarge Section 6 beyond oriented matroids as stated | rejected by exact source-lock map |
| identify the finite determinant with a target divisor | rejected; `A4_FORMAL_HINT` only |

No local/Euler/root-number, automorphy, Hilbert--Pólya, global novelty, external
review, or Route-B claim survives the release gates.
