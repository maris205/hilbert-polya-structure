# P166 paper plan — Hamming-weight translation dynamics

**Status:** `ROUND-2 INTERNAL ACCEPT / REVIEWS A-B 0C-0M-0m / HOLD_EXTERNAL`  
**Type:** short finite-dynamics theorem paper  
**Format:** `amsart`, A4, 10pt  
**Page budget:** 4–6 pages including references  
**Section count:** 6

## One-sentence contribution

For the state-dependent diagonal translation
`x -> x+wt(x)1` on `(Z/nZ)^n`, the paper derives the complete period and
preperiod census from an `n`-phase occupancy map and, independently, gives
an exact arbitrary-target one-step inverse atlas with its marked exponential
generating function and sharp maximum.

## Claims–evidence matrix

| Claim | All-parameter evidence | Executable falsification | Section |
|---|---|---|---|
| A diagonal orbit is conjugate to `g_m(j)=j+m_j`, and every iterate gives an exact target-local `n`-phase oracle | direct calculation from target multiplicities | every state through `n=7`; every target/time through the stated finite boxes | §2 |
| A nontrivial phase cycle consumes all occupancy mass and is a clockwise gap cycle | cycle-increment sum is a positive multiple of `n` bounded by `n` | all weak compositions through `n=10`, plus deterministic larger-modulus tests | §3 |
| Exact-period points are `1+(n-1)^n` at period one and `k!S(n,k)` at period `k>=2`, giving the zeta product | positive gap compositions lifted by multinomial weights | complete functional graphs through `n=7` | §3 |
| The complete exact-depth census is a Stirling sum, with sharp maximum `n-2`, full equality structure, and last shell `(n-1)n!/2` | no-wrap transient paths and ordered-surjection summation | all depth layers through `n=7`; all profile tails through `n=10` | §4 |
| Every one-step target fibre is determined by marked symbol multiplicities; the global marked EGF and sharp maximum follow | enumerate the `n` possible diagonal shifts of a fixed target | every target through `n=7`; independent EGF expansion and boundary witnesses | §5 |

## Section architecture

### §1. Literal system and subtraction boundary — 0.75 page

- Define `H_n`, integer Hamming weight, the self-map, period, and preperiod.
- State the complete theorem package before technical detail.
- Assign zero contribution credit to Hamming-weight terminology, diagonal
  group actions, Stirling/Fubini identities, finite-map zeta conversion, the
  `n=2` Meyer–Pommersheim map, and the one-ball siteswap slice.
- Say that the source search is bounded and supports no novelty claim.

### §2. Diagonal phase map and target-local iterates — 0.65 page

- Prove the free diagonal orbit and exact conjugacy.
- State `T^t(y-j1)=y-g_m^t(j)1` and
  `|(T^t)^{-1}(y)|=#{j:g_m^t(j)=0}`.
- Scope it explicitly as a target-local `n`-phase oracle, not a closed
  global all-time fibre census.

### §3. Recurrent structure, periods, and zeta — 1 page

- Prove mass exhaustion and the gap-cycle converse.
- Lift anchored gap compositions with multinomial weights.
- State exact period points, cycles, recurrent count, fixed iterates, and
  Artin–Mazur zeta function.

### §4. Complete transient census — 1.1 pages

- Derive the strictly increasing no-wrap phase path.
- Sum free histogram mass, then collapse positive compositions with
  Stirling numbers.
- Prove `n-2` sharpness and the complete equality profile/phase description.
- Count the last shell and isolate `n=2`.

### §5. Every-target one-step fibres — 1 page

- Enumerate the integer weight branches `0,...,n` without double counting
  the identical residue shifts at weights zero and `n`.
- Derive the exact image/fibre condition, marked EGF, image extraction, and
  sharp maximum fibre with equality criterion.

### §6. Controls, limitations, and declarations — 0.35 page

- Summarize the independent standard-library verifier and exact boxes.
- State the scope guards and `HOLD_EXTERNAL` visibly.
- No appendix and no reliance on computation for proof.

## Figure and table plan

No figure or table is needed.  The diagonal conjugacy and the two independent
proof axes are shorter and clearer as displayed formulas.  Omitting a hero
figure preserves the 4–6 page short-note budget.

## Citation plan

- §1: Hamming for terminology; Meyer–Pommersheim for the exact binary
  boundary; Buhler–Eisenbud–Graham–Wright for siteswaps; Konheim–Weiss and
  Lackner–Panholzer for occupancy/parking and mapping-functional-graph
  context; Meyles et al. for the Fubini/ordered-Bell parking connection.
- No citation is used as proof of a theorem stated here.
- Every cited record must be checked against an author, publisher, DOI, or
  arXiv record and recorded in `SOURCE_VERIFICATION.md`.

## Gate-A feedback incorporated

Independent Gate A returned `GREEN`, with `0 Critical / 0 Major / 2 scope
minors`.  The outline implements both before drafting:

1. the exact `n=2` parity-complement map receives explicit zero credit; and
2. the every-time statement is named only a target-local `n`-phase oracle,
   never a closed global all-time fibre census.

The plan also keeps direct siteswap ownership and classical ordered-Bell,
Stirling, Hamming, multinomial, group-action, and zeta ingredients outside
the contribution boundary.
