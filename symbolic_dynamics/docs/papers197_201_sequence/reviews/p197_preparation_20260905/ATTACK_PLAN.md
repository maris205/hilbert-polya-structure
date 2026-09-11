# P197 independent preparation — not a manuscript review

2026-09-05 UTC. **PREPARATION_ONLY / NOT_REVIEW_A / HOLD_EXTERNAL**.
There was no frozen Round 0 when this preparation began. No author draft
was edited, and this file is not an acceptance decision. The reviewer did
not author TCSD; its earlier LFAS authorship excludes it from reviewing
P200 independently.

## Evidence inspected and live issues

The central five-seat freeze and the TCSD theorem, local, fibre, exact-gap,
sharp-junction, primary-source and collision supplements were read. The
later `TCSD_SMALL_WITNESS_ERRATUM.md` was also checked independently.
The proof-writer and research-lit workflows guided hypothesis/boundary
separation and primary-source checks. This is a single-process bounded
preparation, not the multi-persona panel or two paper reviews.

1. **Historical strict-merge wording is false, but the new proof repairs it.**
   The earlier fibre certificate's assertion that each extra doubled-run
   pair forces a strict Fibonacci merge fails for the cyclic target
   `++--`: two doubled runs, both gaps zero, and `F1 F1 = F1 = 1`.
   The exact-gap supplement does not need that assertion. Its non-strict
   product bound followed by the strict Lucas comparison is sufficient.
   A Round-0 manuscript must use the repaired argument, not the old wording.
2. **Historical universal one-exception witness fails at n=2,3.**
   Independently following all six ordered pairs a!=b gives tail zero for
   the two pairs with |a-b|=2 and tail one for the other four pairs, at both
   sizes. Root independently found this boundary and added the explicit
   erratum. The specific witness `0^(n-1)1` is safe at all n>=2.
   All six pairs attain the claimed sharp bound in the checked n=4,...,8
   box. The erratum's all-size proof route is the first-difference
   zero-run trajectory with strict-block length at least two.
3. **The junction supplement requires l>=2.** Applying its generic
   core-entry wording to a single letter would be false. The supplement
   states the restriction, and n=1 has its separate H1=1 boundary.

No new mathematical counterexample to the repaired all-size claims was
found. That statement is neither paper acceptance nor owner clearance.

## Independent finite pressure already implemented

`probe_preparation.py` imports no author code. It checks the 96 no-equal-
adjacent windows and 1,344 no-constant-triple windows, 1,104 signed junction
instances with zero-run lengths 1,...,24 and strict-block lengths 2,...,24,
all one-exception pairs at n=2,...,8, and every source and target at n<=8.
Its direct preimage histogram is compared with the cyclic-sign-run gap
product without multiplying the author's comparison matrices.

A separate two-bitplane update agrees with every literal transition in
those full boxes. All 216 independent input-left/input-right/output symbol
permutations were tested for associativity; none yields a semigroup law.
This is a local-table test, not an arbitrary block-conjugacy exclusion.

## Adversarial plan once Round 0 is frozen

- Pin manuscript, bibliography, code, canonical output and all claimed
  supplements before giving a paper-specific decision. Do not inherit
  Stage-1 approval, old assertion counts or pre-review issue closure.
- Use the two-bitplane transition and indegree peeling followed by reverse
  propagation of depths and periods. This differs from a tuple map followed
  by per-start orbit tracing. Compare peeled recurrent vertices with the
  D^4=rho^2 identity, including wraparound n smaller than a local window.
- Attack both directions of the recurrent-core claim, invariance and the
  inverse rho^(-2) D^3. Check that period divisibility is not upgraded to a
  claim that every divisor occurs.
- Separate nonconstant longest-run descent from constant configurations,
  the R=1 and R=2 local lemmas, and exceptional one-long-run sharp witnesses.
  Require an actual first-entry argument, not only reaching a recurrent
  endpoint. Check parity and all n=1,2,3 boundaries explicitly.
- Reconstruct the core de Bruijn graph from open local identities. Use
  independent closed-walk counting or graph trace identities for the
  recurrent recurrence and depth/period trace claims. Finite matrices whose
  dimensions grow with depth are not efficient fixed-dimension formulas.
- Count indegrees directly for every target in the finite box, compare
  matrix-free cyclic run-gap products, and check every maximum equality
  target: two at even n>=4, 2n at odd n>=5, plus the all-zero ties at n=2,3.
  Preserve the sole n=1 image and the zero-length strict skeleton.
- Subtract P164's exact one-step equality shadow and classical comparison
  transfer matrices/Fibonacci algebra. Revisit the actual Fukś local class;
  neither nonassociativity nor a bounded search non-hit proves novelty.

This preparation does not implement all of the future review plan. Formal
Review A must disclose its eventual exact executed scope and replay pins.
