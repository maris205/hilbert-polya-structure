# P162 Hostile Review A — original report

**Review date:** 2026-09-03 UTC  
**Calibration:** `NOT_CALIBRATED`  
**Execution boundary:** role-separated internal cold read; the reviewer did not
author the Round-0 manuscript and did not import or call its verifier. No
external manuscript transmission, author contact, or release occurred.

## Verdict

**REVISE — 0 Critical / 0 Major / 1 Minor.**

The span statistic, finite-field rank law, sharp witness, all-target
source-size/history polynomial, one-step boundary, and stabilizer recovery
survive independent derivation and 1,654,331 reviewer-owned assertions. The
sole repair is a scope qualifier in the abstract: the full source `V` never
empties, so “worst-source absorption clock” should explicitly say
“worst-non-full-source emptying clock.” The theorem body already has the
correct exclusion and no formula changes.

## Strongest counter-argument

Most of the forward engine is owned background. Translation erosion and its
composition law belong to mathematical morphology, and the rank distribution
and full-rank waiting time belong to finite-field random-matrix theory. Once
those are subtracted, the paper must stand on a narrowly defined residual:
the exact conjunction of the witness `V\{0}`, arbitrary-target stabilizer
filter, proper-subset coset polynomial, and one-step recovery law. A future
direct source for that conjunction would materially reduce the paper.

This objection does not refute the present result. The inverse polynomial is
not obtained from the rank marginal: it distinguishes targets through their
translation stabilizers, counts every source size and every ordered history,
and has a separately proved boundary at trivial stabilizer. The manuscript
already gives the owned erosion and rank ingredients zero contribution credit
and describes its source screen as bounded.

## Independent theorem audit

| Interface | Adversarial derivation / test | Verdict |
|---|---|---|
| history compression | Expanding two literal updates gives intersections over subset sums; induction and characteristic two identify these with `span(v_1,...,v_t)`. Exhaustive literal and compressed iterates agree. | PASS |
| rank law | For each fixed `r`-space, a history is an onto map from `F_2^t`; multiplying the independent-row choices gives `S(t,r)`. Brute history ranks agree. | PASS |
| recurrent boundary | Invariance under every translation forces either the empty or full subset. These are exactly the universal fixed states through the exhaustive boxes. | PASS |
| sharp clock | Directly, `E_H(V\{0})=V\H`; hence this non-full witness empties if and only if the history span is full. Every subspace through `d=6` passes. | PASS |
| mean | Backward solution of the rank-chain hitting-time equations gives the displayed exact sum, including `d=0`. | PASS |
| fixed-span fibre | `E_H(A)` is precisely the union of those `H`-cosets wholly contained in `A`; therefore `H<=Stab(B)` is necessary and sufficient, with independent proper choices on all outside cosets. | PASS |
| all-target formula | Summing fixed-span polynomials over the subspaces of `Stab(B)` and the onto histories reproduces every observed target/source-size coefficient. | PASS |
| one-step boundary | The zero vector supplies the rank-zero term; each nonzero stabilizer vector supplies a two-point-coset term. Odd targets with `s=0` never evaluate a half-integral exponent. | PASS |
| recovery | At fixed `(d,b)`, the positive branch is a fixed power of three times `2^s-1`; exhaustive feasible cells through `d=4` are strictly ordered. | PASS |

The statement “by time sigma” is correctly an upper bound for every non-full
source and an equality only for the displayed witness. The paper does not
claim that every non-full source has the same absorption time.

## Boundary and inverse-direction attacks

- At `d=0`, the unique history symbol is zero, the two states are fixed, the
  empty rank sum and the `t=0` formula have their stated values.
- At `t=0`, only rank zero contributes and the inverse polynomial is the
  singleton monomial `z^|B|`.
- At `B=V`, all `2^(dt)` histories have the sole source `V`; the rank sum
  evaluates to that number.
- At `B=empty`, every admissible outside coset must be a proper subset, exactly
  matching the displayed factor.
- If `s>=1`, `B` is a union of stabilizer cosets and `2^s` divides `|B|`; if
  `s=0`, the separate value one is used. The reviewer checked 32,907
  odd-cardinality trivial-stabilizer targets.
- Necessity and sufficiency of `H<=Stab(B)` were both rederived. In
  particular, the proof does not confuse invariance of the target with
  invariance of the source.

## Exact-control and artifact audit

The author verifier was replayed and ended with 1,712,974 assertions and
`STATUS PASS`. Its transcript matched the frozen paper-local canonical file.
The reviewer-owned program is
`docs/papers162_166_sequence/reviews/p162_a/verify_p162_review_a.py`; it shares
no imports with the author implementation. It performs 1,654,331 assertions,
including the full literal `d=3,t=4` atlas, all target/source-size cells,
subspace witnesses through `d=6`, exact rank-chain means, and recovery cells
through `d=4`. Two fresh runs matched `CANONICAL.txt` byte for byte.

```text
reviewer verifier SHA-256:
49d78ba9d4714bc4c227ddccd2dfce476ba5f79b496851cb45edaa3a8d776738
reviewer canonical SHA-256:
79b7c29720d5cc766294c0155fe7c021b0b12355b0bdf3260fd0351c023ac69e
```

Two fresh source-only builds using
`pdflatex -> bibtex -> pdflatex -> pdflatex` were byte-identical to each
other, `main.pdf`, and `main_round0_original.pdf`, at SHA-256
`e496ce1be3084e61616494cab2ca405238adfa575a6484db93029f8dae01de46`.
The artifact has four A4 pages, blank identifying metadata, and 30/30 fonts
embedded, subsetted, and Unicode mapped. The settled log has no build,
reference, citation, box, or rerun warning. All pages were independently
rasterized and inspected; no clipping, overlap, malformed equation, bad glyph,
or identity leak was found.

## Provenance and collision audit

The cited Heijmans--Ronse paper directly owns the complete-lattice and
translation-invariant erosion framework. Balakin directly owns finite-field
random-matrix rank distributions. These are correctly subtracted. The bounded
search found no primary source displaying the paper's exact
target-stabilizer/source-size/history polynomial. That non-hit is not a
novelty, priority, ownership-completeness, or freedom-to-publish result.

Internally, P109 supplies deterministic subspace-image dynamics, P115 supplies
a different finite-linear operator, and P158 supplies random graph-cut history
signatures. None transfers the affine-coset proper-subset fibre or the target
stabilizer filter. Within the current batch, P163 is a deterministic
union-preserving set-family shadow system and P164 is a nonlinear word rule;
there is no literal-map or proof-engine collision.

## Finding

### Minor M1 — abstract omits the non-full-source qualifier

- **Evidence:** abstract: “a sharp worst-source absorption clock, witnessed by
  `V\{0}`”; theorem: “Every `A_0 != V` is empty by time `sigma`.”
- **Confidence:** 5/5.
- **Why it matters:** `V` is itself universally fixed and never empties, so an
  unqualified “worst-source emptying” phrase is literally false if the full
  phase is included.
- **Minimum repair:** change the abstract phrase to “a sharp
  worst-non-full-source emptying clock.” Optionally use the same qualifier in
  the theorem's summary sentence. Do not change the clock formulas.

After M1 is repaired and a Round-1 PDF is frozen, Review A supports
`ACCEPT_INTERNAL / HOLD_EXTERNAL`, subject to a fresh Review B. This report
does not authorize posting, circulation, submission, or author contact.
