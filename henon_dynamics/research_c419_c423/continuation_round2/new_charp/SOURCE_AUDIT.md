# Source and collision audit: NC1 / NC2

Checked 2026-09-07 UTC. This is a bounded source-first screen of the two
[frozen contracts](FROZEN_CONTRACTS.md), not a systematic review, global
priority certificate, human peer review or formal Route-A evaluation.
The conclusion is **zero new admissible contracts**; see the complete
screening certificates in [SCOUT_REPORT.md](SCOUT_REPORT.md).

## Actual primary-source reading and hypothesis matching

### P1 — Artin–Schreier trace quadratic forms

Irene Bouw, Wei Ho, Beth Malmskog, Renate Scheidler, Padmavathi Srinivasan
and Christelle Vincent, *Zeta functions of a class of Artin-Schreier curves
with many automorphisms*, [arXiv:1410.7031v2](https://arxiv.org/abs/1410.7031v2),
revised 26 June 2015; original submission 26 October 2014.

Actually read: official metadata; introduction/notation; full
[Section 0.2](https://arxiv.org/html/1410.7031v2#Ch0.S2), including its
radical reduction, Theorem 0.2.1 and Proposition 3 with proof; and Section
0.8, with the complete Theorem 0.8.1 and proof. HTML mathematics was
also inspected through its LaTeX alternative text after browser timeouts.

Applicable: odd characteristic, additive `R`, and any finite extension
of its coefficient field in Section 0.2. The choice `R=X^p+aX`,
`a in F_p`, meets these conditions for every extension degree. The
nondegenerate zero formula is credited there to Joly, whose original
text was not independently obtained. Radical-zero handling in our
certificate is explicit.

Not applicable without an extra condition: Theorem 0.8.1's specialized
L-polynomial formulas require the field to contain the splitting field
of the source's `E(X)`. They are not an all-extension black box for NC2.

Deduction: NC2's remaining arithmetic is this classical trace-form
calculation. The short native-return identity is derived in our report.

### P2 — invariant forms do not bypass wild ramification

Alexandru Buium, *Complex dynamics and invariant forms mod p*,
[arXiv:math/0505037v2](https://arxiv.org/abs/math/0505037v2), revised
31 May 2005; original submission 2 May 2005.

Actually read: official metadata; [Theorem 1.2 and the Section 2
hypotheses](https://arxiv.org/html/math/0505037v2); Lemmas 2.2–2.3,
including the proof of Lemma 2.3. The search also identified the IMRN
publication; no separate publisher full-text audit is claimed.

Theorem 1.2 concerns one characteristic-zero rational map over a number
field whose reductions at infinitely many places admit nonzero invariant
forms. NC1 is a fixed-characteristic family whose degree changes with
`p`; those hypotheses have not been supplied.

Lemma 2.3 requires tame ramification and a semi-invariant weight-one
form. NC1 is wild at `x=-1`: writing `x=-1+z` gives
`f_lambda(-1+z)=lambda(-1+z)z^p`, of local degree `p`. Therefore the
lemma cannot identify NC1 with a power map. Its setup also excludes
characteristics two and three for the later arguments. The invariant
logarithmic differential alone is not a complete-count theorem.

### P3 — dynamically affine rational maps require their defining structure

Andrew Bridy, *The Artin-Mazur Zeta Function of a Dynamically Affine
Rational Map in Positive Characteristic*,
[arXiv:1306.5267v2](https://arxiv.org/abs/1306.5267v2), revised
24 February 2014; original submission 21 June 2013.

Actually read: official metadata and abstract, and
[Section 2's Definitions 2.1–2.2 and family discussion](https://arxiv.org/html/1306.5267v2).
No new full-proof verification of its zeta theorems is claimed.

Its scope requires a finite quotient of an affine morphism of a connected
commutative algebraic group, with the stated dense-open identification.
The discussion distinguishes power, Chebyshev, Lattes, additive and
subadditive families. The existence of `f^*(dx/x)=dx/x` is not itself
the dynamically affine definition. No such quotient structure for NC1
was established here, so no theorem from this source is falsely applied
to settle NC1. This is a checked near-owner, not the reason for rejection.

## Actual local collision checks

The decisive local sources were read, not inferred from filenames.
No old computation was executed.

1. [wild_ordinary / PROOF_PACKAGE.md](../../../continuation_c407_c408_round3/wild_ordinary/PROOF_PACKAGE.md)
   and its [source audit](../../../continuation_c407_c408_round3/wild_ordinary/SOURCE_AUDIT.md):
   read the whole package and audit. The hypotheses permit general
   nonconstant `H` in `x H(x)^q`. Thus `H=lambda^(1/p)(1+x)`, `q=p`
   is an exact NC1 inclusion. The old all-geometric-point ordinary count
   remains unclosed; its proved finite-field degree-lifting replacement
   cannot be rebranded as that count. Its `p=3`, least-period-12
   counterexample is old evidence, not a rerun.

2. [wild_dynamics / PROOF_PACKAGE.md](../../../continuation_c404_c408_round2/wild_dynamics/PROOF_PACKAGE.md):
   read the whole package. It owns an intersection-weighted observable
   under `H(0)=1`, not arbitrary distinct counts. It directly overlaps
   NC1 at `lambda=1`; it is not cited as an all-parameter ordinary theorem.

3. [PC-C closed-chain screen](../../../research_c409_c413/positive_characteristic/CANDIDATE_SCREEN.md):
   read the full PC-C subsection. It uses a correspondence over the
   algebraic closure of `F_p(c)`, transcendental `c`, and shift-period
   closed chains. It is **not** the NC2 finite-set skew permutation.
   Its short degree/transversality result is not reused or recounted.

4. [PC414-S skew inverse screen](../../../research_c414_c418/positive_characteristic/SCOUT_REPORT.md):
   read the exact inverse question and full elementary refutation, plus
   its source-audit context. That map is `(x^2,y^p+P(x))`; its question
   is forcing recovery from a two-axis count ledger. NC2 does not solve
   that inverse problem and is not an exact copy of that contract.

5. [earlier arithmetic candidate screen](../../../continuation_c407_c408_round3/arithmetic_candidate/SCOUT_REPORT.md):
   read the report. Its common-Frobenius and mixed-clock skew entries
   are nearby filtering history, not blanket no-go theorems. We reject
   NC2 on the displayed trace-form deduction, not this proximity alone.

The new two-cycle certificate in this lane is an author-derived exact
screening calculation. It has no worldwide priority claim and is not
large enough, by itself, to replace the frozen all-period NC1 question.

## Actual fresh search record

The following twelve distinct formulations were actually submitted on
2026-09-07 after freezing the contracts. The first ten are the bounded
lane screen; the last two are source-title follow-ups. They include at
least three NC2 formulations and multiple NC1 map, invariant-form and
periodic-point formulations, exceeding the five-fresh-query lane floor.

1. `polynomial dynamics positive characteristic "x(1+x)" "periodic"`
2. `"rational maps" "invariant differential" "characteristic p" multipliers`
3. `"Artin-Schreier" "skew" "finite fields" dynamics`
4. `"x+x^{p+1}" dynamics`
5. `"z+z^{p+1}" periodic`
6. `"rational maps" "invariant differentials" positive characteristic`
7. `"Artin-Schreier" "cycle structure"`
8. `rational dynamics characteristic p invariant differential forms Buium`
9. `polynomial dynamical zeta positive characteristic multiplier one Bridy`
10. `Artin Schreier curves finite fields trace quadratic forms x p+1 zeta functions`
11. `"Zeta functions of a class of Artin-Schreier curves with many automorphisms" arxiv`
12. `"Complex dynamics and invariant forms mod p" theorem degree characteristic`

Numerous keyword hits were unrelated PDE, characteristic-zero or other
arithmetic problems; they do not establish ownership. Search dates or
crawler recency labels were not substituted for publication dates.
Only the primary sources and the explicit local collisions above support
the substantive decisions. No claim that the entire modern literature
has been exhausted is made.

## Execution and authority limits

The only new files in this assignment are the frozen contracts and these
two reports. Complete rejected-candidate certificates are embedded in the
scout report; no separate paper-sized proof package is claimed. No
third candidate was opened. No Git, global-state, manuscript, evaluator,
accepted-contract or old-check mutation was performed. The team remains
an AI-assisted internal research process, not external peer review.

Source arithmetic, trace counts and finite permutation zetas supply no
target Euler factors, root numbers, zero correspondence or Hilbert–Polya
realization. `NO_BAD_EULER_OR_ROOT_NUMBER` is preserved; this lane assigns
no formal A1/A2 grade and changes no admitted-contract count.
