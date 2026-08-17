# Independent devil's-advocate handoff

## Reviewer role

Treat every claimed theorem, source attribution, type distinction, and
novelty boundary as hostile input.  Do not infer correctness from package
hashes.  Do not write to authority while reviewing.

## Mandatory independent recomputation

Without importing package calculations, recompute from

```text
L = [[1,1],[0,1]]
R = [[1,0],[1,1]]
h(w) = [1,1] M_w [1,0]^T
```

all of:

```text
h(epsilon), h(0), h(1), h(01), h(10), h(11), h(001), h(010)
lambda(h(1)), lambda(h(11)), lambda(h(001)), lambda(h(010))
```

Verify word-product order explicitly.

## Logic attacks

1. Does `w -> w0` exactly represent the source direct-system embedding?
2. Is constancy of `h` on colimit classes sufficient to prove
   `[1] != [01]`?
3. Are cyclic invariance and the clock power law genuinely necessary for the
   typed scalar primitive/repetition ledger claimed, or did the package add an
   unstated convention?
4. Could a root-dependent orbit convention evade T2 without ceasing to be a
   cyclic primitive ledger?
5. Does T3 overreach from a scalar phase to arbitrary cocycles?  Reject any
   wording that does.
6. Is the diagonal determinant domain correct for complex `s`, including
   trace class, entire dependence on `u`, and the `|u|<1` log expansion?
7. Does the eigenvalue-one state force `Delta_K(s,1)=0` under the exact
   multiplicity convention?
8. Does Corollary 5 claim exhaustiveness only for the declared repair list?

## Provenance attacks

1. Resolve all 22 typed IDs in `SOURCE_HASHES.sha256` under the portable
   contract in `SOURCE_LOCK.md`, then recompute every SHA-256.  Reject a
   host-absolute path, unknown ID, missing dependency, duplicate, non-C-sorted
   ID list, root escape, or mismatch; direct `sha256sum -c` is not sufficient.
2. Confirm terminal P39 commit and manifest integrity independently.
3. Confirm P39 explicitly performs no successor ranking/authorization.
4. Confirm the Paper-40 research lock has 11 immutable research files and is
   not being mistaken for integrated authority status.
5. Confirm the six-card selection rule is unique without using paper order,
   P39 ordering, or P40 corrections.
6. Confirm the rule is explicitly retrospective over known cards, results,
   and witnesses; reject any prospective, outcome-independent, novelty, or
   priority claim.
7. Confirm only the final corrected package input bytes were frozen before
   independent DA.
8. Confirm proposed `SD-C43` remains preauthority and no repository file was
   modified by this package.

## Collision attacks

Repeat primary-source citation chaining from:

- Knauf 1998 plus erratum;
- Kleban--Oezluek's Farey fraction spin chain;
- Fiala--Kleban's generalized chain;
- Prellberg--Fiala--Kleban's explicit trace model;
- Technau's trace-product count.

Search exact formulas and conceptual synonyms, not only the working title.
Compare internal Papers 1, 33, 35, and the Paper-40 final research seal.  If
the exact four-witness result is already explicit, recommend `STOP_DUPLICATE`.

## Route attacks

Evaluate every coordinate from the strict v0.2 obligations.  In particular:

- do not inherit `A1_FAIL` merely from `SD-C06`; assess whether T1--T3 prove
  it under the narrowed contract;
- do not award A2 for `det(I-uQ_s)` unless the same operator has the required
  primitive return ownership;
- do not lower A0 or A3 merely because A1/A2 fail;
- do not award A4 for an `s`-dependent diagonal inventory;
- keep Route B false unless the same object passes all prerequisites.

## Acceptance gates

Return `DA_ACCEPT_PREAUTHORITY` only if all are true:

1. exact witnesses independently pass;
2. no theorem exceeds its explicit quantifier boundary;
3. direct-limit, necklace, trace-word, and diagonal-operator types remain
   separate;
4. the retrospective selector is unique and independent only of P39 ranking
   and P40 authorization, with no prospective or outcome-independent claim;
5. no exact literature or internal-paper duplicate is found;
6. the expected Route tuple is defensible;
7. `sha256sum -c SHA256SUMS.txt` passes and the portable source-ID resolver
   verifies `SOURCE_HASHES.sha256` 22/22;
8. the report records its own SHA-256 outside this package.

Otherwise return one of:

```text
DA_REVISE_CONVENTION
DA_REVISE_QUANTIFIERS
DA_REVISE_OPERATOR_DOMAIN
DA_REVISE_SELECTION
DA_REVISE_ROUTE
STOP_DUPLICATE
STOP_SOURCE_MISMATCH
```

## Required report contents

- independent calculations;
- theorem-by-theorem verdict and counterexample attempts;
- source/hash verification;
- literature collision matrix;
- strict Route tuple;
- exact requested corrections, if any;
- final acceptance/stop code and report SHA-256.
