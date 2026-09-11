# Claims and Evidence Matrix

Gate: `OWNER_RED_AMBER/HOLD_EXTERNAL`.

Evidence labels used below:

- **A**: analytic proof in `main.tex` / `PROOF_PACKAGE.md`;
- **S**: external classical source, audited in `SOURCE_VERIFICATION.md`;
- **C8**: exact Python exhaustion for (2\le n\le8);
- **C9**: independent exact C++ stream at (n=9);
- **N**: no novelty or owner-clearance inference permitted.

| ID | Claim | Status | Evidence | Exact boundary |
|---|---|---|---|---|
| C1 | (T_n) maps \(\mathcal F_n\) to itself. | Proved | A, C8 | Right Hurwitz move and frozen product convention only. |
| C2 | Adjacent equal transpositions cannot occur in a minimal (c_n)-factorization. | Proved | A | Uses transposition length (n-1) of an (n)-cycle. |
| C3 | Executed scheduler indices are strictly increasing. | Proved | A, C8 | Least lower-endpoint collision, right Hurwitz, numeric lower endpoint. |
| C4 | Every recurrent state is fixed. | Proved | A, C8 | Consequence of C3; no claim for altered conventions. |
| C5 | Every tail is at most (n-2). | Proved | A, C8 | Consequence of C3. |
| C6 | The tail bound (n-2) is sharp. | Proved | A, C8 | Explicit witness in Theorem 2.1. |
| C7 | Minimal (c_n)-factorizations are counted by (n^{n-2}). | Classical input | S, C8 | Zero contribution credit. |
| C8 | The lower-endpoint word bijects \(\mathcal F_n\) with parking functions of length (n-1). | Classical input | S, C8 | Zero contribution credit; orientation/convention fixed. |
| C9 | Fixed states are exactly adjacent-unequal lower words. | Proved | A, C8 | Immediate from the stopping rule. |
| C10 | \(|\operatorname{Fix}(T_n)|=(n-1)^{n-2}\). | Proved | A, S, C8 | Uses C8 and Pollak's circular model. |
| C11 | The reverse-admissibility test lists every nonself predecessor of every labelled target. | Proved | A, C8 | Exact one-step atlas; target labels retained. |
| C12 | The displayed indegree formula is exact for every target. | Proved | A, C8 | Includes the self-predecessor exactly for fixed targets. |
| C13 | Maximum one-step indegree is (n-1). | Proved | A, C8 | One-step fibres only. |
| C14 | The unique labelled maximizer is the adjacent-transposition chain. | Proved | A, C8 | Uses parking inequalities plus the classical bijection. |
| C15 | Iterating the atlas gives a finite reverse dynamic program for higher fibres. | Proved consequence | A | No uniform closed form or basin formula asserted. |
| C16 | For every (I\subseteq[n-2]), the exact history count is ((n-1)^{n-2-|I|}). | **Conjecture** | C8, C9 | Verified only for (n\le8) by exhaustion and separately for (n=9) by streaming. |
| C17 | Exact depth-(t) count is \(\binom{n-2}{t}(n-1)^{n-2-t}\) for all (n). | **Conjectural consequence** | C8, C9 | Not a theorem. |
| C18 | There is a unique deepest state for all (n). | **Conjectural consequence** | C8, C9 | Not a theorem, despite finite unique counts. |
| C19 | The scheduler package is novel or externally unowned. | **Not claimed** | N | Bounded non-hit is not evidence; external owner search remains open. |
| C20 | Conditional Hurwitz-string constructions, including Campion Loth--Rattan's equal-lower-endpoint case, are part of P192's contribution. | **Not claimed** | S, N | Their reversible monotone/string reordering mechanism is zero-credit; P192 retains only its exact literal scheduler/tail/fibre contract under `HOLD_EXTERNAL`. |

## Computational evidence ledger

### Python exhaustive verifier

`code/verify.py` generates the entire right-Hurwitz orbit from the canonical chain for (2\le n\le8). It checks:

- the Cayley cardinality and product of every state;
- the lower-endpoint parking property and injectivity over the orbit;
- strict, collision-free terminal histories and the sharp maximum tail;
- the fixed count;
- every finite history mask against the conjectural formula;
- every target's actual indegree against the analytic atlas;
- maximum fibre and its unique canonical maximizer;
- finite depth histograms.

Frozen totals: 280,392 states/transitions and 1,962,920 assertions. The canonical record digest is `67cc231e1e1ad859aca4c6de30f7a3dd76f81358ff2753b48bbdac06662cad24`.

### Independent (n=9) stream

`code/verify_n9.cpp` does not reuse the Python orbit generator. It streams all (9^7=4,782,969) Prüfer words, reconstructs a labelled tree, applies the rooted-tree inverse to obtain a factorization, scans the scheduler, and compares all 128 mask counts with (8^{7-|I|}). The transcript ends with:

```text
conjecture_status=n9_verified_not_claimed_all_n
status=PASS
```

This is evidence only for the finite slice (n=9). It does not promote C16--C18.

## Evidence exclusions

- Computation is not used to establish C3--C15.
- Classical Hurwitz, parking, Prüfer, and located conditional Hurwitz-string results are not credited as contributions.
- The absence of a located literal scheduler paper is not encoded as a novelty claim.
- `main_round0_original.pdf` is the immutable three-page Round-0 pin (SHA-256 `aa0ade6d64cb2cbd87545bde50ed15ba2b9729e3235aa7395b4be892b1cb76f1`). Current repaired `main.pdf` is four pages (SHA-256 `e06aac2579f0d90a15c1a7a2c8fa09ce57286f15818a10c2466cd06d210d6b57`) and is intentionally different. `main_pre_metadata_audit.pdf` remains a provenance-only comparison snapshot whose bibliography is superseded.
