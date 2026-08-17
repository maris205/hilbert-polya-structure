# Independent devil's-advocate handoff

## Reviewer role

Treat every theorem, source claim, selector clause, type distinction, and hash
as hostile input. Do not infer correctness from package seals. Do not write to
authority during review.

## Mandatory independent recomputation

Without copying the package's arithmetic, recompute for each `q` in
`{2,3,5}`:

1. `#Fix(sigma^r)=q^r` and `D_q(s,z)=1-zq^(1-s)`;
2. `N_q(1)=q` and `N_q(2)=(q^2-q)/2`;
3. primitivity of `[01]`;
4. the forced clock label `exp(2 log q)=q^2` and its composite status;
5. the source and target first `z` coefficients;
6. the large-real-`s` limits used in Theorem 3.

## Logic attacks

1. Is `z` genuinely a free marker per original source symbol, rather than a
   specialization hidden inside `q^(-s)`?
2. Is one `z` per rational-prime primitive loop the declared target marker?
3. Does the clock theorem require totality, and is totality truly necessary
   for the claimed full factor ledger?
4. Is `[01]` a valid primitive orbit for every frozen alphabet convention?
5. Does `log p=n log q` force `p=q^n` without a branch ambiguity?
6. Does the multiplicity proof distinguish based words from cyclic classes?
7. Is the first-coefficient comparison performed on a valid common analytic
   domain and with the correct reciprocal/determinant orientation?
8. Does the repair corollary quantify only over its explicit finite list?
9. Does any wording incorrectly say the function-field ledger itself fails?
10. Does any wording silently generalize from `q=2,3,5` to all finite fields
    or all function-field/number-field correspondences?

## Positive-control attacks

- Confirm the same primitive ledger is correct for monic irreducible
  polynomials over `F_q` and norm `q^n`.
- Confirm a separate diagonal rational-prime operator really owns the target
  Euler product on `Re(s)>1`.
- Confirm selecting one length-one orbit yields one correct local factor but
  is non-total.
- Reject a proof that obtains the negative result by damaging cyclicity or
  repetition on the source itself.

## Provenance attacks

1. Resolve every ID in `SOURCE_HASHES.sha256` using `SOURCE_LOCK.md`; reject
   absolute paths, `..`, symlink escapes, unknown IDs, duplicate IDs,
   non-C-sorted IDs, missing dependencies, and mismatches.
2. Independently verify terminal P39's 91-entry manifest, research Route,
   sealed Route, and no-ranking/no-selection fields.
3. Independently verify the final P40 research lock and its 11 immutable
   files; do not treat it as P42 authorization.
4. Independently verify the frozen P41 dependency lock and its 14 immutable
   files; do not treat it as an integrated Route record or P42 authorization.
5. Parse all six exact Session-4 cards and reapply the retrospective selector.
6. Confirm the selector and witnesses were known before the package and earn
   no prospective, outcome-independent, novelty, or priority credit.
7. Confirm no authority, mirror, Git, README, registry, or paper-manifest file
   was modified by this Phase-1 package.

## Literature attacks

Repeat primary-source and citation-chain searches from:

- Bowen-Lanford's finite-shift zeta article;
- current necklace-polynomial work, especially arXiv:2605.11445 and its cited
  counting literature;
- finite-field closed-point/norm treatments of the affine-line zeta;
- rational-prime marked Euler-product or prime-zeta literature.

Search conceptual synonyms: `closed point`, `prime polynomial`, `degree`,
`norm`, `necklace polynomial`, `full shift`, `marked zeta`, `orbit code`,
`prime Euler factor`, and `clock preserving`. If the exact typed theorem is
already explicit, return `STOP_DUPLICATE`.

## Route attacks

- Do not inherit the historical tuple without re-evaluating the narrowed
  object.
- Do not lower A1 or A2 because the rational-prime projection fails; both
  remain exact for the source's function-field species.
- Do not raise A0 above weak: rational primes do not emerge.
- Do not raise A3 using the separate target comparator or a function-field
  functional equation.
- Do not raise A4 from a finite weighted adjacency alone.
- Keep Route B false unless the same object satisfies every prerequisite.

## Acceptance gates

Return `DA_ACCEPT_PREAUTHORITY` only if all are true:

1. all three negative witnesses and all positive controls pass independently;
2. no theorem exceeds its stated quantifiers;
3. source necklace, finite-field prime polynomial, and rational prime remain
   distinct types;
4. marker, clock, multiplicity, and operator ownership remain explicit;
5. the six-card rule is unique but openly retrospective;
6. P39/P40/P41 are used only for governance and collision boundaries;
7. no exact literature or internal-paper duplicate is found;
8. the strict Route tuple is defensible;
9. `sha256sum -c SHA256SUMS.txt` passes and the typed source resolver verifies
   every `SOURCE_HASHES` entry;
10. the independent report records its own SHA-256 outside this package.

Otherwise return one of:

```text
DA_REVISE_SOURCE_CONVENTION
DA_REVISE_MARKER
DA_REVISE_QUANTIFIERS
DA_REVISE_SELECTION
DA_REVISE_ROUTE
STOP_DUPLICATE
STOP_SOURCE_MISMATCH
```

## Required report contents

- independent exact calculations;
- theorem-by-theorem verdict and counterexample attempts;
- positive-control verdicts;
- portable source/hash verification;
- P39/P40/P41 boundary audit;
- literature collision matrix;
- strict Route tuple;
- exact requested corrections, if any;
- final acceptance/stop code and report SHA-256.
