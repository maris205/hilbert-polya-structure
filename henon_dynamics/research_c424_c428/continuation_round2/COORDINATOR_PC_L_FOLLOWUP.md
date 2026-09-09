# Coordinator follow-up on the original PC-L radical gap

2026-09-08 UTC. Read-only review and a bounded complementary proof/source
attempt on [the positive-characteristic proof](positive_characteristic/PROOF_PACKAGE.md).
This is not a new candidate. All odd primes, all parameters and all
polynomial degrees remain in the original question.

## Mathematical reading and contribution

The coordinator read the complete original Steps 1–5, then the revised
Step 4 and the remainder after its insertion. The full cyclic-algebra
basis proof, binary-support coefficient argument, ordinary-root versus
nilradical equivalence, characteristic-three Jacobian counterexample,
and rational-pole proof were checked by hand. No required mathematical
correction was found in those claims. This is not an external-model
review or a formal paper evaluation.

The key binary argument really is uniform in `c`: local square reduction
preserves binary weight when selecting the next variable and lowers it
when selecting the constant term. The odd leading exponent selects the
two ends of a unique circular window once `n>2 floor(log2 D)`. No
assumption that the iterate quotient is reduced appears in this step.
That absence is essential: nonzero in the full algebra is not the same
as nonzero at an ordinary periodic point.

The coordinator supplied the Frobenius/multiplicity route now proved in
the author's Step 4. If `v` were a nonzero normal representative in
`K_c`, let `D=deg v`, let `M_n` be the largest root multiplicity of
`f_c^n-x`, and take the least `p`-power `q_n>=M_n`. Orbitwise vanishing
would give `H_n(v)^q_n=H_n(v^q_n)=0` in the full quotient. Since
`v^q_n` is still normal, of degree `D q_n`, the binary lemma forces

`D q_n >= 2^ceil(n/2)` and `M_n > 2^ceil(n/2)/(pD)`

for every `n`. In particular `liminf M_n/2^(n/2)=0` would prove the
original equality for that `p,c`. These inequalities and their logical
quantifiers were checked after insertion. Because this route is a
coordinator contribution, this file is **not an independent review of
that contribution**. No general multiplicity bound has been proved.

## Source check: the nearby theorems do not supply the missing bound

All accesses were ordinary browsing on 2026-09-08 UTC, with no local
PDF download, mathematical program or external manuscript upload.

- Nordqvist–Rivera-Letelier,
  [*Residue fixed point index and wildly ramified power series*, 1904.04494v3](https://arxiv.org/html/1904.04494v3),
  3 February 2020. Read metadata/abstract, the initial definitions and
  Section 1.2 through the exact statement of Theorem 2; selected
  lower-ramification statements were also inspected, not all proofs.
  Theorem 2 presupposes multiplicity `q+1` with `1<=q<=p-1` and
  characterizes minimal ramification by a nonzero iterative residue.
  It is not an upper bound on the maximal multiplicity over all
  ordinary periodic points of every quadratic map.

- Lindahl–Rivera-Letelier,
  [*Generic parabolic points are isolated in positive characteristic*, 1501.03965v2](https://arxiv.org/html/1501.03965v2).
  Read the introduction, Main Theorem, definitions of minimal
  ramification, and Theorems A, B, D with the adjacent explanation.
  Their generic/minimal-ramification hypotheses and local isolation
  conclusions do not establish the uniform global multiplicity estimate
  needed here. No proof or conclusion is extended beyond those scopes.

- Levy,
  [*The McMullen Map in Positive Characteristic*, 1304.2834](https://arxiv.org/abs/1304.2834),
  was inspected only through arXiv metadata/abstract after the author's
  KTH PDF timed out. Multiplier-spectrum rigidity is a related topic,
  not an imported multiplicity theorem. Search snippets of its full
  text are not recorded as a completed proof read.

An initial direct open mistakenly used arXiv `1501.03958`, which returned
an unrelated vegetation-pattern paper. It was discarded immediately.
A title query then identified the correct `1501.03965`; no mathematical
assertion or bibliography entry relies on the mistaken locator.

## Exact additional queries

```text
polynomial finite field iterates fixed points multiplicity bound characteristic p dynatomic
quadratic polynomial characteristic p parabolic cycles multiplicity bound periodic points
Livsic polynomial cohomology positive characteristic periodic orbit sums

"positive characteristic" "multiplicity" "periodic points" rational map
"finite field" "f^n" "squarefree" dynamics
"fixed points" "multiplicities" "finite fields" polynomial iteration
"positive characteristic" "Fatou" "Shishikura"

"Generic parabolic points are isolated in positive characteristic" arxiv
"McMullen map" "positive characteristic" arxiv
"multiplicity" "periodic" "quadratic" "finite field" dynatomic
```

Unrelated squarefree-value papers, complex quadratic results, informal
web questions and code-project issue descriptions were not proof inputs.
This bounded search found no applicable bound; that is not a claim that
none exists in the literature.

## Disposition

The conditional result strengthens the original attempt but does not
close `K_c=B_c` or classify a nonzero defect. The new source checks
do not remove the radical/multiplicity gap. The current status remains
`ORIGINAL_QUESTION_UNCLOSED / AUXILIARY_LEMMAS_ONLY / NOT_ADMITTED`.
No condition on `c`, no degree bound and no replacement by a generic
analytic germ is inserted into the original contract. No new paper or
target arithmetic assertion follows from this file.
