# Narrative report — P139

## Research question

The Chen--Fox--Lyndon factorization is a canonical static decomposition.  What
finite dynamics appears when only its factor starts are retained as a binary
word and the operation is repeated?

## Mechanism

On the binary alphabet, every leading `1` is a singleton Lyndon factor.  The
first factor of the remaining suffix contributes one further start, so the
leading-one prefix of the mask grows strictly until the all-one word is
reached.  This simple amplifier controls all recurrence.

## Main progression

The static interface is imported first: Theorem 2.2 of
Mantaci--Restivo--Rosone--Sciortino identifies factor starts with left-to-right
minima of the suffix-rank permutation.  Its equivalent strict-suffix-record
form, the ordered-tail comparison, and the reproduced proof receive zero
contribution credit.

The residual progression is:

1. The leading-one amplifier gives one fixed point and depth at most `n`.
2. The alternating word factors into copies of `01`, with a final `0` at odd
   length, and maps to `1` followed by the shorter alternating word.  Reversing
   equality in the clock induction forces those same factors, proving that the
   deepest source is unique.
3. A target mask prescribes a composition of factor lengths.  Its fibre is
   exactly the set of nonincreasing chains of binary Lyndon words of those
   lengths.  Rectangular lex-comparison matrices count the chains and give a
   complete image test.  The one-factor and all-singleton targets reduce to
   the classical binary Lyndon census and `n+1`, respectively.

## Evidence discipline

The verifier exhausts functional graphs through length 18.  Its independent
Duval/suffix-record agreement is an integration test for the imported static
theorem, not a contribution claim.  An independent Lyndon-word generator and
comparison-matrix evaluator matches every literal target fibre through length
14; both special fibres are checked through length 18.  Computation is used
only as counterexample pressure.

## Credit boundary and status

Mantaci--Restivo--Rosone--Sciortino, *Journal of Discrete Algorithms* 28
(2014), 2--8, DOI `10.1016/j.jda.2014.06.001`, own the static suffix-rank
minimum/factor-start equivalence.  The ordered-tail comparison, CFL theorem,
Duval factorization, suffix/Lyndon arrays, binary Lyndon census, Möbius
inversion, and matrix multiplication are also zero-credit tools.  Only the
iterated mask dynamics, sharp unique clock, and target-wise ordered-Lyndon
inverse atlas remain in the residual.  External release remains
`HOLD_EXTERNAL`.
