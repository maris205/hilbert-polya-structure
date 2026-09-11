# Narrative report — P196

## Question

What finite dynamics is created by applying Gödel implication synchronously
to consecutive letters of a cyclic finite-chain word?

## Answer

The map has a one-step transient layer but a nontrivial recurrent rotation
core. Its image consists exactly of cyclic words in which every nontop letter
has a strictly larger predecessor. On this image the logical rule becomes
ordinary left rotation. The temporal problem therefore separates cleanly
from the inverse problem: periods are transfer-matrix/necklace data, whereas
one-step fibres factor over the cyclic top-letter gaps into explicit binomial
differences.

## Concrete progress

1. exact image and pointwise depth (only 0 or 1);
2. every iterate-fixed count and exact-period cycle census;
3. corrected characteristic polynomial
   `lambda^q-(lambda+1)^(q-1)`;
4. exact fibre of every labelled target, including all boundary cases;
5. exhaustive, deterministic regression controls.

The old attractive `q`-bonacci guess was falsified at `q=3`; the coefficient
of `lambda` is `-2`. The manuscript records the repaired binomial recurrence.
