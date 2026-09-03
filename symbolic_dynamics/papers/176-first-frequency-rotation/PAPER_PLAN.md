# Paper plan — first-frequency rotation

## Format and lifecycle

- Format: anonymous `amsart` short note, A4, 10 pt.
- Target length: 4--6 pages including references.
- Working title: **First-Frequency Rotation on Binary Pointed Necklaces**.
- Lifecycle: `AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL`.
- Round: final Round 2; both hostile reviews closed and immutable Round 0
  remains preserved.

## One-sentence paper spine

The adaptive first-symbol gluing of the frozen rotations `+k` and `-k`
orients disjoint generator cycles of every pointed necklace, which yields a
complete component classification and, independently, an every-target
two-branch inverse atlas.

## Contribution boundary

The note assigns zero contribution credit to all of the following:

- Høyer--Špalek's Hamming-weight-controlled rotation construction and the
  two frozen `+k/-k` branch idea;
- the generic reduction of an invariant cyclic orbit to a phase map;
- P166's `j -> j+c_j` cyclic-phase architecture, its use of indicator-style
  target inversion, and the already occurring sharp value `n-2`;
- ordinary functional-graph facts, orientations of a cycle, binomial
  conditioning, primitive-necklace enumeration, and Möbius inversion.

Only the constrained `+/-k` generator-component theorem and its stated
consequences are retained.

## Section architecture

### Abstract

Define the literal map, state the subtraction boundary, then give the five
exact residual outputs: component theorem, period inventory, clock/deepest
census, every-target fibres, and fixed census.

### 1. Literal map and subtraction boundary

- Define `T_n` and conventions.
- Display the two frozen branches.
- Cite Høyer--Špalek precisely and distinguish their phase-rotation object
  from the present cyclic coordinate shift while assigning the common
  controlled-rotation idea zero credit.
- Cite and subtract Grošek--Hromada's fixed-weight coordinate-rotation
  classes and Gupta et al.'s adjacent circular-shift treatment; neither owns
  the adaptive first-symbol gluing or its functional graph.
- Compare FCR and P166 in a compact table: carrier, phase profile,
  recurrence, periods, inverse fibres.
- Display the amber/hold status and the strict kill switch.

### 2. Pointed-necklace component theorem

- Pass from a cyclic word of least period `d` to the exact phase map
  `j -> j+k` on a `1` and `j -> j-k` on a `0`.
- Decompose `Z/dZ` into `gcd(k,d)` generator cycles.
- Prove the four cases `L=1`, `L=2`, constant `L>=3`, nonconstant `L>=3`.
- Give a pointwise tail formula and the longest-run maximum.

### 3. Period inventory and the sharp clock

- Prove the exact possible-period set and realize every proper-divisor long
  period with an explicit aperiodic word.
- Prove maximum preperiod `n-2` and exactly two deepest states for `n>=3`,
  including `n=1,2` boundary counts.

### 4. Every-target fibres and fixed census

- Give the two labelled inverse rotations for every target.
- Derive the weight-layer `0/1/2` histogram and global image formula.
- Cite fixed-density necklace sources and derive the primitive-block Möbius
  formula for all fixed points.

### 5. Exact control and lifecycle

- Record the standalone author/scout-derived regression control through
  `n=18`, separately from the independent reviewer implementations.
- State assertion count and canonical transcript digest.
- Separate finite computation from proof.
- Restate the amber/hold boundary and immediate kill conditions.

## Claim-to-evidence map

| Claim | Formal evidence | Executable pressure |
|---|---|---|
| exact pointed-necklace phase reduction | Lemma 2.1 | every rotation class, `n<=18` |
| complete component dynamics | Theorem 2.2 | local/global orbit equality, component cycle/tail checks |
| exact possible periods | Theorem 3.1 | full functional graphs, `n<=18` |
| sharp clock and deepest two | Theorem 3.2 | every state, `n<=18` |
| every-target fibres and histogram | Theorem 4.1 | every target, `n<=18` |
| fixed Möbius census | Theorem 4.2 | exact fixed counts, `n<=18` |

## Figure/table decision

No figure is needed.  One comparison table materially clarifies what is
subtracted at the P166 boundary.  All other relationships are shorter and
clearer in theorem/proof form.
