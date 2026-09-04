# P193 hostile Review A

**Reviewer relation:** process-separated internal reviewer; did not author
P193 and did not import its implementation.  
**Frozen input:** Round-0 sources and PDF pinned in `PINNED_INPUTS.sha256`.  
**Decision:** `PASS`.  
**Historical findings:** `0 Critical / 1 Major / 0 Minor`, all closed.  
**Open findings:** `0 Critical / 0 Major / 0 Minor`.  
**Mathematical decision:** `PASS`.  
**External state:** `OWNER_AMBER / HOLD_EXTERNAL`.

## Outcome first

The literal dynamics and every claimed theorem survived independent
rederivation and a fresh complete functional-graph reconstruction through
`S_8`.  The independent program checked 46,233 transitions and 917,780
predicates, including every labelled target fibre, and reproduced the stated
`n=8` depth row exactly.  The author verifier independently replayed byte for
byte through `S_9`.

Round 0 originally needed one source-boundary repair.  A contemporary paper
uses *mutual optimal/best blocking pairs* inside a decentralized matching
dynamics.  The repaired manuscript now cites and subtracts it while clearly
distinguishing P193's literal map.

## Closed finding P193-A1 — Major — closest matching-dynamics owner omitted

The bounded exact-term query located Burkhard C. Schipper and Tina Danting
Zhang, *Matching, Unanticipated Experiences, Divorce, Flirting, Rematching,
Etc*, arXiv:2504.01280 (2025).  That work defines mutually optimal/best
blocking pairs and studies a stochastic decentralized process that prioritizes
one such pair.  P193 instead freezes common master orders, encodes a matching
as one permutation, computes every nomination from the old state, and swaps
all mutual pairs simultaneously.  Its direct-sum refinement, clock recurrence,
and fibre product are not transferred by the located source.  Thus this is a
source/terminology owner, not a demonstrated literal-map collision.

The required repair was:

1. add the Schipper--Zhang arXiv record to `references.bib`;
2. cite it in Section 1 beside the matching interpretation;
3. say explicitly that mutual-best blocking-pair dynamics are zero-credit,
   and distinguish sequential/stochastic one-pair satisfaction from P193's
   deterministic simultaneous all-pair exchange under fixed common orders;
4. update `SOURCE_VERIFICATION.md` with the query result and retain
   `OWNER_AMBER / HOLD_EXTERNAL`; and
5. do not turn the bounded search into a novelty, priority, or
   freedom-to-operate statement.

**Acceptance:** `CLOSED`.  The repaired `main.tex` cites
`SchipperZhang2025`, distinguishes stochastic/sequential one-pair satisfaction
from fixed-order deterministic all-pair exchange, assigns the neighbouring
terminology zero credit, and retains the exact owner gate.  The bibliography
contains arXiv:2504.01280 and the source ledger records the hit without novelty
language.  Both verifiers and the cold PDF pass after the delta.

## Hostile mathematical attacks

- **Active-pair overlap:** rebuilt nominations directly and compared them with
  prefix-sum direct-sum cuts on every source through `S_8`; no overlap or
  classification exception exists.
- **Clock convention:** counted the first hit of the identity, including
  `n=1`; the maxima are `n-1`, with `(n-1)!` sources at that depth.
- **Depth recurrence:** independently expanded ordered block sequences and
  the marked terminal block.  All `A_t` and `B_t` coefficients in the
  complete range agree with orbit depths.
- **Fibre orientation:** accumulated literal incoming arrows before evaluating
  the component-size product.  Garden states are exactly the targets not
  beginning in `1`.
- **Singleton group boundary:** tested the parent weight `1` and all optional
  cuts before singleton target blocks.  Fibre mass is `n!` in every box.
- **Maximum equality edge case:** explicitly allowed equality
  `c_s=2` in `c_s<=2^(c_s-1)`; the exponent-budget inequality is then strict
  unless all later components are singletons, so the identity remains the
  unique maximizer.

## Verifier and build record

```text
author replay: PASS, byte-equal, S_1..S_9
reviewer replay: PASS, byte-equal, S_1..S_8
reviewer transitions: 46,233
reviewer checks: 917,785
reviewer digest: eaec02e654c02452ec757536456a3743a9ba333a78d2641dc61c5002fb5e7827
cold repaired PDF: 5 pages, 390,196 bytes
cold repaired PDF SHA-256: b5b2f4e77bada6229a0716d9780a871f95b8e6ba75fa2c9e6794b5bf524ad0d9
```

All five pages were rasterized and inspected.  Fonts are embedded, subsetted,
and Unicode mapped; no warning, bad box, unresolved citation/reference,
clipping, overlap, broken formula, or unintended blank page was found.

P193 now passes Review A with zero open findings.  This internal pass does not
authorize an external release or any novelty claim.
