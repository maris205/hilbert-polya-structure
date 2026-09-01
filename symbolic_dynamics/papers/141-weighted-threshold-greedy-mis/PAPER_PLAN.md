# P141 paper plan

## Status

`ANONYMOUS_ROUND2 / OWNER_SUMMARY_REPAIR_COMPLETE /
GO_INTERNAL_OWNER_THIN / HOLD_EXTERNAL`

This is a specialized exact-law note on fully owned threshold-graph support,
the fully owned RSA/random-greedy process, and the fully owned
Plackett/exponential weighted order. It assigns all three inputs zero
contribution credit and does not claim a new greedy-MIS process.

## One-sentence residual

For positive-rate exponential random-greedy MIS on a labelled threshold graph,
derive the weighted reverse-stick endpoint law, invert it as a hazard/open-
simplex parametrization, and obtain the accepted-size PGF and all one-vertex
and nested zero-vertex inclusion laws.

## Formal claim spine

1. **P141-C0, owned support.** State Klivans's maximal-independent-set support
   first and assign it zero credit.
2. **P141-C1, weighted endpoint law.** Read the creation string from the right:
   a terminal zero is forced, while a terminal one either wins its prefix race
   or is deleted. Iterate to obtain reverse stick breaking.
3. **P141-C2, hazard/simplex inversion.** Recover every dominant hazard from
   endpoint masses, prove the open-simplex bijection, and state precisely that
   original vertex rates remain nonidentifiable.
4. **P141-C3, size and marginals.** Mix the owned support sizes to get the
   accepted-update PGF; derive dominant and zero marginals and nested zero
   inclusion.
5. **P141-C4, clock firewall.** Separate full-order inspections, accepted
   active-set updates, the numerical span of all priority labels, and
   continuous completion time. Give only the valid state Laplace recursion.

## Owner subtraction, before novelty language

- Klivans explicitly owns the support of maximal independent sets of a
  threshold graph in creation order. Support gets zero credit.
- Pippenger owns graph random sequential adsorption/random-order occupation.
  Krivelevich--Meszaros--Michaeli--Shikhelman own modern general random-greedy
  MIS framing. The process, maximality, and generic greedy validity get zero
  credit.
- Plackett owns the weighted permutation model. Size-biased order and the
  independent-exponential representation get zero credit.
- Theorem 3.1's weighted endpoint law and its inverse/simplex, PGF, and
  marginal consequences are **owner-thin and folklore-risky** because they are
  short consequences of the fully owned support/process/order inputs.
- A bounded search found no direct printed owner for that exact package. This
  bounded direct-owner non-hit is not novelty, priority, or owner clearance,
  so external status stays on hold.

## Hypotheses that must remain visible

- `b_1=0`; later creation bits are zero (isolated from earlier vertices) or
  one (dominant over earlier vertices).
- Every vertex rate is fixed and strictly positive.
- Endpoint masses are indexed by Klivans's support, including possible equal
  endpoint sizes but distinct endpoint sets.
- The endpoint law identifies dominant hazards, not the full rate vector.
- Only `K=|I|` has the displayed size PGF.
- Full scan count, accepted update count, priority-label span, and elapsed
  completion time are distinct objects.

## Paper architecture

1. Lead with owner subtraction and define the weighted process.
2. Quote and reprove the owned support for self-containment.
3. Prove the reverse-stick law by the rightmost-vertex recursion.
4. Prove hazard inversion, simplex surjectivity, and nonidentifiability.
5. Derive size PGF, inclusion marginals, and nesting.
6. Isolate the four clock/count vocabularies and state the CT recursion.
7. Record exact controls and the external hold.

## Evidence contract

The paper-local verifier uses exact rational arithmetic. It independently
enumerates the literal active-set dynamics for every creation string through
`n=6` and all weights in `{1,2,3}^n`, then every creation string through
`n=10` under four nonuniform profiles. It checks endpoint masses, PGFs,
hazard inversion, every marginal, and every ordered zero pair. A second lane
constructs rate vectors from positive simplex points. A bounded permutation
lane independently checks the continuous-time Laplace recursion. Symbolic
proof, not finite enumeration, carries arbitrary positive real rates.

## Review and closure criteria

- Klivans support and generic RSA/MIS are visibly zero-credit before the
  residual theorem.
- All residual claims have complete proofs in `main.tex`.
- Canonical verifier stdout replays byte for byte.
- The stable build and PDF/log/font/text checks pass.
- No formula for `K` is presented as a priority span or completion-time law.
- External status remains `HOLD_EXTERNAL`.

Hostile review A returned PASS with no repair item. Round-A closure therefore
freezes the unchanged manuscript as `main_round1.pdf`; it does not create a
fictitious theorem, source, bibliography, or verifier modification. Round B
and the independent owner-repair review required documentary owner-summary
synchronization only. That package-wide repair is now complete; all theorem,
source, bibliography, verifier, canonical stdout, and PDF bytes remain
unchanged, and status is `GO_INTERNAL (OWNER-THIN) / HOLD_EXTERNAL`.
