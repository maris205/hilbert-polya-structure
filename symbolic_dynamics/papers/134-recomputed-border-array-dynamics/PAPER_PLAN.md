# Paper plan — P134

**Working title:** Whole-Array Recomputation of Border Arrays: Exact
Two-Cycles, Sharp Transients, and Factorial Fibres

**One-sentence contribution:** When an ordinary border array is treated as a
new integer word and its entire border array is recomputed synchronously, the
resulting self-map on inversion sequences has an explicit two-cycle atlas, a
sharp piecewise-linear transient clock, and exactly two factorial-maximal
one-step fibres.

**Type:** finite-dynamics theory short paper.  
**Author mode:** anonymous.  
**External status:** `HOLD_EXTERNAL`.  
**Stage:** Stage-2 final QA complete; Round 2 frozen.

## Claims--evidence matrix

| claim | deductive evidence | exact counterexample pressure | section |
|---|---|---|---|
| `Pi_n(E_n)` is exactly the valid border arrays | standardize any realizing word by order of first occurrence; equality patterns preserve borders | every state through `n=9`; fast/naive border comparison through `n=8` | §2 |
| recurrence is one fixed point at `n=1`, and `n-1` exact two-cycles for `n>=2` | explicit templates `A_r,B_(r+1)` plus strict canonical-prefix growth off the templates | complete functional graphs through `n=9` | §2--§3 |
| maximum depth is `0,0,1,2n-4` for `n=1,2,3,n>=4` | indexed mismatch lemma gives the upper bound; explicit `e_n,p_n` trajectories attain it | every state through `n=9`; enlarged witnesses through `n=32` | §3--§4 |
| every target fibre is at most `(n-1)!` | left-to-right exposure: a positive prescribed border forces one letter, while a zero prescribed border leaves at most `i` choices | all target cells through `n=9` | §5 |
| the only maximal targets for `n>=2` are `0^n` and `010^(n-2)` | equality in every exposure factor plus a proper-suffix-start proof for the two source families | all target cells through `n=9` | §5 |

Finite checks are falsifiers only.  Every all-length claim has a written proof.

## Section structure

### Abstract

- Define whole-array recomputation in the first sentence.
- State the exact recurrent atlas, piecewise sharp depth, and two factorial
  maximizers.
- Distinguish the map from classical failure-link composition.
- State the bounded-search and `HOLD_EXTERNAL` boundary.

### §1. Whole-array recomputation and the subtraction boundary

- Define borders, the ordinary border array `beta(w)`, and
  `E_n={(e_0,...,e_(n-1)):0<=e_i<=i}`.
- Define `Pi_n(e)=beta(e)` as a literal finite self-map.
- Put failure-link composition `beta^j[i]` next to whole-array recomputation
  `beta(beta(e))`; only the second is studied.
- Credit KMP computation, border-array validation, construction, realization,
  and census completely.

### §2. Image and canonical two-cycles

- Prove image equals the valid border arrays by standardization.
- Define `A_r` and `B_(r+1)` and prove they form exact two-cycles.
- Introduce depth to the recurrent set.

### §3. Indexed mismatch amplifier

- Select the unique canonical template using `p_1`.
- Define the first mismatch index `L(p)`.
- Prove the exhaustive indexed transitions
  `A1 -> B2 -> extension` and
  `B0 -> A1 -> B2 -> extension`.
- Count at most three iterations for the first extension and two thereafter;
  conclude the valid-state and whole-carrier upper bounds and exclude all
  other recurrent points.

### §4. Sharp trajectories and boundaries

- Define `p_n=(0,0,1,0^(n-3))` and
  `e_n=(0,1,0,2,1^(n-4))`.
- Prove both alternating trajectory formulas by inspecting equality blocks.
- Obtain exact depths `2n-5` and `2n-4` and state the full boundary table.

### §5. Every target fibre and its two unique maxima

- Prove the all-target `(n-1)!` upper bound, including invalid targets.
- Derive the equality condition.
- Use the correct proper-suffix-start argument for the `0^n` and
  `010^(n-2)` source families; do not use the false “nonzero last letter”
  shortcut.
- State the `n=1` boundary.

### §6. Exact control, scope, and limitations

- Report exhaustive and enlarged-witness checks from the paper-local verifier.
- Keep finite computation logically separate from proof.
- State the bounded owner non-hit and `HOLD_EXTERNAL` status.

## Figure and table plan

No plot or architecture figure is needed: the paper is a compact exact
classification.  One inline boundary table summarizes the sharp depth at
`n=1,2,3,n>=4`; the indexed mismatch automaton is displayed as mathematics,
not as a decorative figure.

## Citation plan

- §1: Knuth--Morris--Pratt for the failure/prefix function; Franek et al. for
  linear border-array validation; Duval--Lecroq--Lefebvre for validation,
  construction, generation, and counts; Gawrychowski--Jez--Jez for fast online
  validation and minimum-alphabet realization.
- No citation receives credit for the repeated whole-array dynamical results.
- Bibliographic metadata is taken from DOI records and the primary Franek PDF.

## Credit and collision firewall

- P112-C6 is ordinary failure-link descent and is not this map.
- P105 and P122 already occupy permutation/inversion-sequence and
  sharp-depth/fibre silhouettes; carrier and package shape receive no credit.
- Same-batch PR1 is killed by an exact owner and cannot coexist with P134.
- P134 is the sole inversion-sequence candidate in this five-paper portfolio.

## Stage-2 completion checklist

- [x] hostile-gate repairs transferred to the scout report
- [x] plan and claim--evidence matrix frozen
- [x] paper-local verifier and raw canonical transcript
- [x] complete LaTeX proof draft
- [x] four-stage build and `main_round0_original.pdf`
- [x] metadata, font, extracted-text, page, and settled-log QA
- [x] independent Hostile Reviews A/B and all requested repairs
- [x] final isolated build, all-page visual audit, and manifest freeze
