# Independent model review — ANG-20260915-SDC01

**Date:** 2026-09-15.  
**Review type:** independent model proof and ownership check, not human peer review.  
**Outcome:** no mathematical blocker found in Propositions 1--5; one claim-ledger
quantifier should be explicit as recorded below.  
**Candidate status reviewed:** STOP — EXACT MULTIPLICATIVE REPETITIONS; MIXED
PRIMITIVES AND INFINITE UNIT PACKETS.

## Scope and inspected inputs

The reviewer read the complete frozen [version-1 card](../candidate-card.md),
[paper](../paper.md), [claim ledger](../claim-ledger.md), and
[evidence index](README.md). The checks concern the all-rational cover source,
normalized action and inverse, full topology, multiplicative cocycle,
primitive-packet multiplicity, and ordinary unit-roof zeta obstruction.
No numerical experiment, external source, alternative roof, or selected
subcarrier supplies evidence for the conclusions below.

## Mathematical checks

| Item | Independent check | Finding |
| --- | --- | --- |
| Cover source | An intermediate z gives the factorization y/x = (z/x)(y/z), with both factors integers greater than one; any such factorization supplies an intermediate z | Prime cover ratios follow from the full divisibility order |
| Ratio bijection | Positive coordinates are finite products of ratios, and negative coordinates are reciprocal finite products; normalization fixes the sole scaling freedom | Equations (2)--(3) identify the full carrier, without selecting states |
| Topological conjugacy | Each output coordinate in either direction uses finitely many discrete coordinates; normalization cancellation shifts the ratio sequence | Homeomorphism and full-shift conjugacy hold |
| Action inverse | Substitution into F gives F inverse at coordinate t equal to y at t minus 1 divided by y at minus 1 | Equation (4) is correct and global |
| Local compactness | Any compact neighborhood would contain a finite-coordinate ratio cylinder; an unrestricted coordinate projects onto the infinite discrete prime set | The nowhere-locally-compact conclusion is correct |
| Full primitive ledger | A periodic ratio sequence is a repeated finite word; its least period excludes proper word powers; changing phase rotates the word | All mixed words are included with the stated cyclic multiplicity |
| Suspension time | At the same suspension height, a return time must be an integer and the corresponding iterate must return the base state | Primitive and repeated times are m and rm |
| Multiplicative cocycle | F raised to m has coordinate y at t plus m divided by y at m | Equation (5) and the return-conditioned repetition identity follow |
| Prime-power returns | A product of m prime ratios is a prime power only if all those ratios are that same prime; a return of length m repeats that block everywhere | Proposition 4 is correct with its return-time hypothesis |
| Mixed witness | The word (2,3) is not a proper word power; (3,2) is its other phase | Exactly one indicated primitive length-2 packet, not two |
| Ordinary zeta | The r = 1 contribution from constant-prime packets has infinitely many equal nonzero absolute summands; real positive subproducts contain arbitrarily large powers of the same factor greater than one | Proposition 5 correctly rules out absolute logarithmic convergence in every right half-plane |

The second-countability and zero-dimensionality assertions follow from the
countable collection of finite-coordinate clopen cylinders. The scalar
normalization does not impose an additional quotient on the ratio words.
In particular, reversals are identified only when already cyclic rotations,
not by an unstated orientation quotient.

## Essential quantifier and editorial precision

The exact prime-power statement is:

\[
F^m y=y\quad\hbox{and}\quad C_m(y)=p^k
\quad\Longrightarrow\quad
R(y)_t=p\ \hbox{for every }t,\quad k=m,
\]

for positive m and k. The least period is then one. This is the content of
Proposition 4's phrase "over a positive return time m", so the paper's theorem
already has the required hypothesis.

It would be false to drop that hypothesis and assume only that y is periodic:
the mixed period-2 word (2,3) has C at index 1 equal to 2. Claim SDC-06 should
therefore explicitly say **prime-power observations over return times**.
This is a scope clarification to the ledger, not a counterexample to the
paper's stated theorem. The author owns any resulting ledger edit; this review
does not claim to have made or verified that later edit.

## Ownership and decision

The exact source and cocycle results do not remove the mixed primitive
packets. The complete ordinary product must retain all of them and all
constant-prime packets. Its divergence is already forced by the latter.
The arithmetic cocycle is not a logarithmic roof or a replacement clock.

The proposed transformation groupoid remains non-locally compact on the
specified topology; no locally compact groupoid analytic framework is
implicitly available from this review. The paper correctly supplies no
operator, trace, determinant, or universal regularization obstruction.

The same-object ledger remains intact. The stated **stop/fork** decision is
supported for this frozen ordinary unit-roof product and prime-only primitive
target. It is not a no-go result for a new carrier or clock. No classical
Route coordinate was evaluated; Route B remains NOT INVOKED.
