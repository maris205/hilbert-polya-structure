# Paper plan: totient--complement Pratt dynamics

**Working title:** Source Phases and Target Fibres for Totient--Complement
Dynamics on Squarefree Divisors  
**Type:** rigorous mathematical short note  
**Status:** `GO_INTERNAL / HOLD_EXTERNAL`  
**Target length:** 4--6 A4 pages, including references  
**One-sentence contribution:** For the literal map
`d -> gcd(n,(n/d)phi(d))` on the divisors of every squarefree `n`, prove an
explicit source-phase decoder for all recurrent states, a uniform `h+1`
entry bound, and an inclusion--exclusion formula for the fibre over every
target divisor.

## Claims--evidence matrix

| Claim | Proof object | Paper-local control | Credit boundary |
|---|---|---|---|
| The divisor map is statewise conjugate to `S -> (P\S) union N(S)` on the induced Pratt DAG. | Proposition 2.1, prime-by-prime Euler factorization | Literal integer update equals the support update for every state in four prime sets. | Euler's totient formula, squarefree support, and the Pratt relation are zero credit. |
| Source phases give every recurrent state, with exactly `2^s` recurrent states and `2^(s-1)` exact two-cycles. | Equations (6)--(7), Lemma 3.1, and the completeness paragraph after Proposition 3.3 | Decoder pairs equal the literal recurrent set in every box. | Generic feed-forward/AND--NOT propagation is zero credit. |
| Every orbit is two-periodic from time at most `h+1`. | Lemma 3.2 and Proposition 3.3 | Every literal orbit satisfies the bound, including the singleton and disconnected controls. | `h+1` is a bound, not a sharp clock. |
| Every target has the stated one-step inclusion--exclusion fibre. | Theorem 1.1(iv) and the derivation in Section 4 | Formula equals the literal fibre for every target, including zero-fibre targets. | Inclusion--exclusion as a method is zero credit. |

## Structure

1. **Scope and main theorem.** Define the arithmetic map, front-load the
   complete theorem, and state `HOLD_EXTERNAL`.
2. **Literal support conjugacy.** Prove the primewise identity and orient all
   Pratt edges explicitly.
3. **Source-phase decoder.** Pass to complemented bits, construct both phases
   in topological order, prove uniqueness, and count exact two-cycles.
4. **Entry bound.** Prove the two-step erasure identity and the level
   induction giving `h+1`, including boundary cases.
5. **Every-target fibres.** Derive the forced-one/forced-zero conditions and
   the target-wise inclusion--exclusion sum.
6. **Controls, ownership, and limits.** Separate proof from finite
   falsification; subtract Pratt-tree and Boolean-network ownership.

## Display plan

No decorative figure is needed for this short note.  The front-matter
substitute is a compact main-theorem display listing the decoder, bound, and
fibre law.  One small verification table reports only finite controls and is
captioned as falsification evidence.

## Citation plan

- Ford--Konyagin--Luca: prime chains and Pratt-tree height.
- Veliz-Cuba et al.: AND--NOT network/wiring-diagram framework.
- Aracena--Cabrera-Crot--Salinas: signed Boolean interaction and source/FVS
  propagation background.

All three records were checked against publisher or official arXiv metadata.
No uncited bibliography entries are retained.

## Writing review applied

The short-note override replaces the conference template: one theorem story,
no empirical-method section, no hero graphic, and complete proofs in the main
text.  The title, abstract, and first section expose the literal map and all
three residual outputs.  Independent hostile Reviews A/B are intentionally
deferred by the Stage-2 instruction.
