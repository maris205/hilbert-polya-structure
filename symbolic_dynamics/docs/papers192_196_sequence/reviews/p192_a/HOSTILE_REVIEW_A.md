# P192 hostile Review A

**Reviewer relation:** process-separated internal Reviewer A; did not author
P192 and did not import or reuse either author implementation.  
**Frozen input:** accepted-repair sources/current PDF and the immutable
Round-0 PDF baseline are pinned in `PINNED_INPUTS.sha256`.  
**Decision:** `ACCEPTED_REPAIR` (`0 Critical / 0 Major / 0 Minor open`; four
findings resolved).  
**Mathematical decision:** `PASS`.  
**External state:** `OWNER_RED_AMBER / HOLD_EXTERNAL`.

## Outcome first

All four proved axes survived independent reconstruction: the product and
right-Hurwitz convention, strictly advancing scheduler indices with sharp
tail, Pollak fixed-state count, and every-target inverse atlas with its unique
maximum fibre.  The reviewer generated the small carrier by direct Cartesian
enumeration of transposition sequences and a literal product filter, rather
than from a Hurwitz orbit or a tree code.  Every functional graph through
`n=6` was reconstructed, every labelled inverse set was compared, and an
independent parking/circular-parking control reached `n=8`.

The conjectural history-set law is not needed anywhere in these derivations.
The manuscript and claim ledger keep it, the binomial depth census, and the
general unique-deepest consequence explicitly outside theorem status.

Round 0 nevertheless required two exact manuscript/source changes: it had
omitted one close 2025 deterministic Hurwitz-algorithm neighbour, and it had
not stated the lower parameter bound even though its displayed sharp witness
needed a separate `n=2` interpretation.

The first repair resolved both defects.  A follow-up provenance repair also
synchronized the companion QA records with the new source/PDF while retaining
the immutable Round-0 baseline.  The final package sweep caught and repaired
two remaining plan-level page/status descriptions before the pins froze.

## Finding P192-A1 — Major — close conditional-Hurwitz neighbour omitted — RESOLVED

Jesse Campion Loth and Amarpreet Rattan,
*Centrality of star and monotone factorisations*, *Bulletin of the London
Mathematical Society* 57(11), 3567--3585 (2025), DOI
[`10.1112/blms.70170`](https://doi.org/10.1112/blms.70170), gives a
deterministic bijection assembled from conditionally selected Hurwitz moves.
In the proof of its Theorem 7, Stage 1 scans contiguous strings, and Case 2 is
precisely triggered when adjacent transpositions have the same lower endpoint.

This is not the P192 map.  The located algorithm changes the defining order
for monotone factorizations, processes whole strings under its own left/right
move convention, and is reversible.  It does not select the least collision
of a fixed minimal `c_n` factorization at each epoch, nor prove P192's strict
clock, fixed census, or labelled inverse atlas.  It is nevertheless the
closest located deterministic conditional-Hurwitz mechanism and is too close
to the claimed subtraction boundary to omit.

Required repair:

1. add the Campion Loth--Rattan record to `references.bib`;
2. cite it in Section 1 beside the adaptive-Hurwitz subtraction;
3. assign its conditional Hurwitz/string-reordering mechanism zero
   contribution credit and state the exact separation above;
4. record the query and source in `SOURCE_VERIFICATION.md`; and
5. retain `OWNER_RED_AMBER / HOLD_EXTERNAL` and all denials of novelty,
   priority, completeness, or freedom to operate.

Acceptance result: all five items are visible in the repaired package, the
theorem statements must remain unchanged except for finding P192-A2, and both
author controls and this reviewer control replay bytewise.  `ACCEPTED`.

## Finding P192-A2 — Minor — domain and sharp-witness boundary unstated — RESOLVED

The paper never says `n>=2`, although the fixed formula and scheduler range
do not define the advertised family at `n=1`.  In addition, the displayed
witness

```text
((1,n),(1,2),(2,3),...,(n-2,n-1))
```

is an `n-1` factor factorization only for `n>=3`; read literally at `n=2`, its
first two displayed entries coincide.  The proof package handles `n=2`, but
the paper must be self-contained.

Required repair:

1. state `Fix n>=2` when the family is introduced;
2. qualify the displayed witness and its sweep proof by `n>=3`; and
3. state that for `n=2` the sole factorization `((1,2))` is fixed, so sharp
   tail `0` and maximum fibre `1` hold.

Acceptance result: the parameter domain, both branches of sharpness, and the
`n=2` self-fibre are explicit without changing the formulas for `n>=2`.
`ACCEPTED`.

## Finding P192-A3 — Minor — repaired build has stale companion QA — RESOLVED

After P192-A1/A2 were repaired, the live manuscript hash became
`30cd2c9b...`, the current PDF became the four-page `e06aac25...`, and the
bibliography grew to six records.  Four companion documents still describe
the old Round-0 state as current:

- `BUILD.md` records the old source/PDF hashes, calls `main.pdf`
  byte-identical to `main_round0_original.pdf`, and reports three pages;
- `SELF_QA.md` repeats the old source/PDF identity, three pages, and five
  citations;
- `README.md` calls `main.pdf` and `main_round0_original.pdf` a byte-identical
  set; and
- `CLAIMS_EVIDENCE.md` repeats that false byte identity.

Required repair: update these four records to distinguish the immutable
Round-0 baseline (`main_round0_original.pdf`, SHA-256 `aa0ade6d...`) from the
accepted-repair current source and PDF; record the six-reference source delta,
four-page build, current hashes, and Review-A repair state.  Do not overwrite
or relabel the Round-0 PDF.

Acceptance result: every inspected live path/hash/page/citation assertion now
matches the current files; the historical Round-0 facts are separately and
accurately labelled, including `file: main_round0_original.pdf`.  `ACCEPTED`.

## Finding P192-A4 — Minor — stale page/status text in two plans — RESOLVED

The final provenance sweep found that `FIGURE_PLAN.md` still called the live
manuscript a three-page theorem note, while `PAPER_PLAN.md` called the current
cold build three pages and treated four pages as a possible future state.
Those descriptions contradicted the accepted four-page PDF even though they
did not affect any theorem.

Required repair: make both plans distinguish the immutable three-page Round-0
baseline from the current four-page accepted repair, and keep the external
gate explicit.

Acceptance result: both plans now state the two statuses and page counts
accurately; `PAPER_PLAN.md` also explains that the fourth page results from the
nearest-source subtraction and explicit boundary cases.  `ACCEPTED`.

## Hostile mathematical attacks

- **Product convention:** permutations were represented by their images and
  composed as `left[right[i]]`.  The canonical chain multiplies to
  `(1 2 ... n)`, while reversing its factors gives the inverse cycle.  Every
  enumerated Hurwitz update preserves the frozen product.
- **Carrier independence:** all sequences in
  `binom(n,2)^(n-1)` were scanned for `2<=n<=6`; only literal products equal to
  the long cycle were retained.  Their sizes are `n^(n-2)`.  No author orbit
  traversal or Prüfer conversion generated this carrier.
- **Strict scheduler index:** after a collision `(a,b),(a,c)`, the new lower
  endpoints are `a,min(b,c)` with the second strictly larger.  The comparison
  at `i-1` is unchanged because the lower endpoint at position `i` stays `a`.
  Every direct history is therefore strictly increasing.
- **Sharpness:** for `n>=3`, the stated witness executes exactly
  `1,2,...,n-2` and terminates at the canonical chain.  The independent code
  handles `n=2` separately and confirms the zero-tail boundary.
- **Pollak census:** ordinary parking words were enumerated separately through
  length seven.  A second circular control constructs translation orbits,
  normalizes the unique empty spot, and checks freeness and adjacent
  inequality.  Counts are `(n-1)^(n-2)`.
- **Inverse orientation:** literal incoming arrows were accumulated before
  evaluating the formula.  For every target, the exact source set equals the
  fixed self-source when applicable plus `H_i^{-1}y` at precisely the
  reverse-admissible indices before the target's first collision.
- **Maximum fibre:** complete small graphs give maximum `n-1` with the
  canonical chain as sole maximizer.  Independently, equality forces a fixed
  target with strictly increasing lower word; parking inequalities then force
  `(1,2,...,n-1)`, and the classical bijection forces the chain.
- **Conjecture firewall:** finite depth histograms are printed only as
  regression observations.  The verifier prints
  `CONJECTURE_ONLY_NOT_USED_IN_PROVED_AXES`, and no all-parameter mask or
  depth formula is asserted by this review.

## Verifier and build record

```text
author Python replay: PASS, byte-equal through n=8
author C++ n=9 replay: PASS, byte-equal
reviewer replay 1: PASS, byte-equal
reviewer replay 2: PASS, byte-equal
reviewer sequences scanned: 769,601
reviewer factorizations/transitions/targets: 1,441 / 1,441 / 1,441
independent parking words: 280,392
reviewer assertions: 305,104
reviewer digest: 63cd3a6f4f86f054d128508f7cf399ef80b5bacb93f168d493325b5b577d1410
accepted-repair PDF SHA-256: e06aac2579f0d90a15c1a7a2c8fa09ce57286f15818a10c2466cd06d210d6b57
```

All four accepted-repair pages were rasterized and inspected.  The repaired
build is technically clean.  All four findings are closed;
`OWNER_RED_AMBER / HOLD_EXTERNAL` remains binding.
