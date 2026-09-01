# Paper plan — P139

**Working title:** Iterating Lyndon-Factor Starts on Binary Words

**One-sentence contribution:** Replacing a binary word by the start mask of
its nonincreasing Chen--Fox--Lyndon factors yields a system with one fixed
point, sharp depth `n` attained by a unique alternating word, and an exact
ordered-Lyndon matrix formula for every one-step fibre.

**Type:** exact finite-dynamics short paper.  
**Author mode:** anonymous.  
**External status:** `HOLD_EXTERNAL`.  
**Stage:** Stage 2, Round 3 owner repair.

## Residual claims--evidence matrix

| claim | deductive evidence | exact counterexample pressure | section |
|---|---|---|---|
| unique recurrent state is `1^n` | leading `1` letters are singleton factors; every nonfixed update extends the leading-one prefix | complete graphs through `n=18` | §3 |
| sharp maximum depth is `n`, uniquely at `0101...` | explicit `(01)` factorization; induction reverses equality and forces length-two factors | all states through `n=18` | §3--§4 |
| every target fibre is an ordered Lyndon chain | uniqueness of CFL factorization with prescribed factor lengths | every target through `n=14` | §5 |
| matrix formula and two special fibres | rectangular comparison matrices; one-factor and all-singleton compositions | special fibres through `n=18` | §5 |

Finite checks are counterexample pressure only.

## Owned static inputs — zero contribution credit

| imported statement or tool | owner | role in this paper |
|---|---|---|
| factor starts are exactly left-to-right minima of the suffix-rank permutation, equivalently strict new suffix minima | Mantaci--Restivo--Rosone--Sciortino, Theorem 2.2, DOI `10.1016/j.jda.2014.06.001` | fixes the intrinsic orientation of the mask; reproduced proof is background only |
| ordered-tail comparison for nonincreasing CFL factors | classical CFL/Lyndon comparison machinery | used only inside the reproduced background proof |
| CFL factorization, Duval algorithm, Lyndon census, Möbius inversion, matrix multiplication | cited classical sources | definitions and static counting tools |

The verifier's Duval-mask/suffix-record comparison through `n=18` validates
the imported interface; it is not evidence for residual ownership.

## Section structure

1. **Definition and owner subtraction.** Fix `0<1`, define binary Lyndon
   words, CFL factorization, masks, depth, and the zero-credit boundary.
2. **Owned static interface.** Cite Mantaci et al. Theorem 2.2, state the exact
   suffix-record orientation, and retain a clearly labelled reproduced
   background proof, including equal factors and positions inside factors.
3. **Leading-one amplifier.** Prove `L(1^r0s)=1^rL(0s)`, convergence, and the
   unique fixed state.
4. **Sharp and unique deepest source.** Factor the alternating word, derive
   `L(a_n)=1a_(n-1)`, and reverse the induction to force all `01` blocks and
   the odd terminal `0`.
5. **Ordered-Lyndon inverse atlas.** Prove the every-target count, express it
   as a rectangular matrix product, and derive the Möbius and `n+1` fibres.
6. **Exact control and limitations.** Report verifier ranges and preserve
   `HOLD_EXTERNAL`.

## Figure and table plan

No plot is needed.  The alternating trajectory and comparison matrices are
displayed algebraically; this avoids a decorative automaton.

## Citation and credit plan

- Chen--Fox--Lyndon for the classical factorization theorem.
- Duval for linear factorization, least suffix, and least rotation.
- Mantaci--Restivo--Rosone--Sciortino for the exact factor-start/suffix-rank
  left-to-right-minimum equivalence.
- Franek et al. and Badkobeh--Crochemore for Lyndon arrays/forests.
- The factorization theorem, suffix-record equivalence, ordered-tail
  comparison, Duval algorithm, binary Lyndon census, necklace Möbius
  inversion, and matrix multiplication receive zero contribution credit.

## Historical rounds

- [x] frozen theorem contract transferred without broadening
- [x] deterministic paper-local verifier
- [x] canonical raw transcript
- [x] verified bibliography
- [x] complete LaTeX build and immutable Round-0 PDF
- [x] settled-log, font, text, metadata, and visual-page QA
- [x] hostile Reviews A/B completed before the batch-level owner audit
- [x] Round-0/1/2 PDFs preserved as pre-repair historical artifacts

The batch-level final owner audit supersedes the earlier reviews on static
ownership and requires the present repair.

## Round-3 owner-repair checklist

- [x] official Mantaci et al. citation and Theorem 2.2 ownership verified
- [x] suffix-record and ordered-tail statements moved behind zero-credit gate
- [x] abstract, introduction, and limitations restricted to the residual
- [x] canonical verifier replay remains byte-identical
- [x] full settled build and isolated byte-identical rebuild
- [x] freeze repaired `main_round3.pdf`; preserve all earlier PDFs
- [x] citation/log/font/text/metadata/page and visual QA
