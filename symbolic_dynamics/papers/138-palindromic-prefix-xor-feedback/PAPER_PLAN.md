# Paper plan — P138

**Working title:** Palindromic-Prefix XOR Feedback: One Two-Cycle, a Sharp
Linear Clock, and Exact Fibres

**One-sentence contribution:** Feeding the complete palindromic-prefix
indicator vector back by coordinatewise XOR yields a complement-equivariant
binary system whose quotient synchronizes sharply in `n-2` rounds and whose
every-target fibres are counted by a left-to-right palindrome decoder.

**Type:** exact finite-dynamics short paper.  
**Author mode:** anonymous.  
**External status:** `HOLD_EXTERNAL`.  
**Stage:** Stage 2, Round 0.

## Claims--evidence matrix

| claim | deductive evidence | exact counterexample pressure | section |
|---|---|---|---|
| complement quotient has rule `Q(y)_i=y_i xor 1 xor pal(prefix_i)` | complement preserves palindromicity; the first output bit flips | literal/quotient equality for every word through `n=18` | §2 |
| the only recurrent class is `0^n <-> 1^n` | three-coordinate reset followed by the leading-zero amplifier | complete functional graphs through `n=18` | §2 |
| sharp maximum depth is `0,1,n-2` | quotient amplifier plus closed word with ones at `3 mod 4` and an alternating-tail trajectory | every state through `n=18`; closed witnesses through `n=64` | §3 |
| normalized target recursion counts every fibre | the last source bit affects the prefix-palindrome test only through the middle word and equality with the first bit | every target through `n=15` | §4 |
| original phase adds no multiplicity | the target first bit uniquely fixes the source first bit | literal fibres through `n=15` | §4 |

Finite checks are falsifiers only; all unbounded claims have written proofs.

## Section structure

1. **Definition and subtraction boundary.** Define the complete indicator
   vector and XOR feedback; credit palindrome algorithms and static word
   structure as background.
2. **Complement quotient and recurrence.** Prove equivariance, the exact
   quotient, the initial reset, the amplifier, and the unique strict
   two-cycle.
3. **Sharp clock.** Handle `n=1,2`; prove the `n-2` upper bound; analyze the
   `3 mod 4` witness and the alternating-tail chain.
4. **Every-target inverse decoder.** Give the normalized recursion, prove
   soundness/completeness by induction, and lift it to the original phase.
5. **Exact control and limitations.** State the verifier ranges, separate
   computation from proof, and retain `HOLD_EXTERNAL`.

## Figure and table plan

No figure is needed.  The exact quotient trajectory is more legible as two
displayed word families.  A compact boundary table records the maximum depth.

## Citation and credit plan

- Galil for real-time initial-palindrome recognition.
- Rubinchik--Shur for a modern all-palindrome data structure.
- Harju--Huova--Zamboni for static palindromic generation of binary words.
- Bathie--Ellert--Starikovskaya for recent prefix-palindrome encoding.
- All cited palindrome recognition, encoding, border, and word-combinatorial
  facts receive zero contribution credit.

## Round-0 checklist

- [x] frozen theorem contract transferred without broadening
- [x] deterministic paper-local verifier
- [x] canonical raw transcript
- [x] verified bibliography
- [x] complete LaTeX build and immutable Round-0 PDF
- [x] settled-log, font, text, metadata, and visual-page QA
- [ ] hostile Reviews A/B (later Stage-2 gate; not claimed at Round 0)
