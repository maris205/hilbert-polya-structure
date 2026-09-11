# Cyclic sliding-AND erosion — strict exact scout

**Decision: `KILL`.**  The literal system is correct and unusually clean, and
the proposed gap-resolved weighted inverse formula survives every finite
test.  It nevertheless fails the current paper-allocation threshold after
mandatory subtraction.  The forward formula is already the standard explicit
solution of elementary cellular automaton Rule 136 (Rule 192 after reflection),
the dynamics is binary mathematical erosion by an interval, and arbitrary-word
preimages of Rule 136 already belong to the classical run-factorized CA
preimage literature.  The residual cyclic/all-time/weight-refined fibre
identity is a useful specialization, but it is only one short axis built from
standard forbidden-run transfer matrices.  P90, P117, and especially P147
also consume too much of the proposed finite-dynamics architecture.

This is a value decision, not a failed calculation and not a novelty claim.
External status is **`HOLD_EXTERNAL`**.

## 1. Literal object and orientation

For `n>=2`, let `X_n={0,1}^{Z/nZ}` and define

```text
E(x)_i = x_i x_{i+1}.
```

With the usual Wolfram lookup order `111,110,...,000` for a radius-one rule,
the truth table is `10001000_2=136`: the output ignores the left neighbour
and ANDs the centre and right neighbour.  Thus the literal orientation is
**Rule 136**, not Rule 192.  Reflection sends it to Rule 192,
`x_i -> x_{i-1}x_i`.  Any future record must state this distinction rather
than call the displayed map Rule 192.

The map is also the erosion of the cyclic set `{i:x_i=1}` by the directed
two-point structuring element `{0,1}`.

## 2. Cold temporal derivation

### Proposition 2.1 — every iterate

For every `t>=0`, including `t>=n`,

```text
E^t(x)_i = product_{j=0}^t x_{i+j mod n}.                 (2.1)
```

Proof is induction.  If (2.1) holds at `t`, then the two adjacent products
for `E^{t+1}` cover `[i,i+t]` and `[i+1,i+t+1]`.  Their overlap is harmless
because binary coordinates are idempotent.  This last observation also makes
the formula valid after the window wraps around the ring.

### Proposition 2.2 — fixed points and sharp clock

Coordinatewise `E(x)<=x`.  A fixed word must satisfy
`x_i=1 => x_{i+1}=1`; cyclicity therefore makes it either `0^n` or `1^n`.
For every other word, let `L(x)` be its longest cyclic run of ones.  Equation
(2.1) says exactly that a run of length `a` has length `max(a-t,0)` at time
`t`.  Consequently

```text
depth(x)=0                       for x in {0^n,1^n},
depth(x)=L(x)                    otherwise.              (2.2)
```

The maximum depth is `n-1`, attained by `0 1^{n-1}` and its rotations.  This
also audits the indexing: depth means the first time at a fixed point, not the
number of nonfixed states.  At depth zero there are two states, not one.

### Proposition 2.3 — exact depth CDF

Let `Q_t(z)` have states `0,...,t`.  From every state `r` there is a zero edge
to state `0` of weight `1`, and from `r<t` there is a one edge to `r+1` of
weight `z`.  It is the suffix-run automaton forbidding `1^{t+1}`.  Then

```text
# {x in X_n : depth(x)<=t} = 1 + tr(Q_t(1)^n),            (2.3)
```

and the coefficient of `z^w` in the trace counts the non-all-one words of
weight `w` in this CDF.  A cyclic avoided word containing a zero has one
closed state path; the all-one word has none and supplies the extra `1`.
For `d>=1`, the depth-`d` shell is

```text
tr(Q_d(1)^n)-tr(Q_{d-1}(1)^n).
```

At `t=0`, (2.3) gives the two fixed words.  At `t>=n-1`, the trace is
`2^n-1`, so the CDF is the whole carrier.

## 3. Cold every-target weighted inverse atlas

For a target `y`, define

```text
Phi_{y,t}(z) = sum_{x:E^t(x)=y} z^{|x|}.                 (3.1)
```

The two uniform targets must be split off:

```text
Phi_{1^n,t}(z) = z^n,
Phi_{0^n,t}(z) = tr(Q_t(z)^n).                           (3.2)
```

For the nonconstant case, write the cyclic run/gap profile of `y` as

```text
(a_1,b_1),...,(a_k,b_k),
```

where `a_i>=1` is a one-run length and `b_i>=1` is its following zero-gap
length.  Define, for `m>=1`,

```text
G_{m,t}(z)=(Q_t(z)^{m-1})_{0,0}.                         (3.3)
```

Equivalently, `G_{m,t}` is the weight polynomial of length-`m` binary words
whose first and last letters are zero and which avoid `1^{t+1}`.

### Proposition 3.1 — reachability and factorization

A nonconstant target is in `im(E^t)` exactly when

```text
b_i >= t+1 for every i.                                 (3.4)
```

When (3.4) holds,

```text
Phi_{y,t}(z)
  = z^{sum_i(a_i+t)} product_i G_{b_i-t,t}(z).           (3.5)
```

If (3.4) fails, its fibre is empty.

To derive this without using a preimage algorithm, a target one-run forces
source ones on that run and on the first `t` positions of the following gap.
The forced regions are disjoint precisely under (3.4).  The remaining segment
of gap `i` has length `b_i-t`.  Its first position must be zero to kill the
window starting at the first target zero, and its last position must be zero
before the next forced one-run.  Every other zero target is equivalent to the
absence of `t+1` consecutive source ones.  Different residual gaps share no
variables, proving the product.

The boundary `t=0` is included: `G_{b,0}=1`, so every target has its singleton
identity fibre.  If `t>=n-1`, no nonconstant profile can satisfy (3.4), leaving
only (3.2).  For a concrete nonuniform checkpoint, the `n=12,t=2` profile
`(a,b)=((2,3),(1,6))` has

```text
Phi(z)=z^7(1+2z+z^2)=z^7+2z^8+z^9.
```

The stipulated domain begins at `n=2`.  At the excluded degenerate boundary
`n=1`, the neighbour is the site itself, so `E` is the identity on both words;
the window formula remains true by idempotence, but there is no nonconstant
run/gap profile and no positive-depth state.

## 4. Exact executable evidence

`verify_scout.py` is a standalone standard-library implementation.  It does
not import any other project code.  It checks:

1. literal iteration against (2.1), for every source, all `2<=n<=13`, and
   every `0<=t<=n+1`;
2. coordinate monotonicity, the two fixed points, (2.2), the sharp witness,
   and the full depth histograms;
3. (2.3), coefficient-refined trace polynomials, and saturation boundaries;
4. every coefficient of (3.2)--(3.5), for every source and every one of the
   `2^n` possible targets, including unreachable targets;
5. each small gap polynomial against direct filler enumeration; and
6. total fibre mass `2^n` at every tested time.

The frozen run has **737,743 assertions**, all passing.  Its displayed depth
histograms begin

```text
n=2  0:2,1:2
n=3  0:2,1:3,2:3
n=4  0:2,1:6,2:4,3:4
n=5  0:2,1:10,2:10,3:5,4:5
n=6  0:2,1:17,2:21,3:12,4:6,5:6
```

Two fresh replays are required to byte-match `CANONICAL.txt`; the final
receipt is recorded there and in the handoff, not used as evidence of
originality.

## 5. Strict subtraction ledger

| component | status after audit | reason |
|---|---|---|
| literal Rule orientation | zero credit | This is Rule 136, reflected Rule 192. |
| iterate (2.1) | directly owned / zero credit | Fukś's explicit Rule-136 solution gives exactly this product window. |
| erosion/composition interpretation | classical / zero credit | Binary translation-invariant erosion and its lattice formulation are standard mathematical morphology. |
| fixed points, longest-run clock, height | elementary consequence / zero credit | Immediate from the owned window solution. |
| trace CDF | classical ingredient / zero credit | Finite automata/transfer matrices for forbidden runs and pattern avoidance. |
| arbitrary-target reachability | heavy prior overlap | Classical CA preimage work treats arbitrary spatial words; Jen explicitly puts Rule 136 in a run/Fibonacci product class. |
| cyclic all-time weighted formula (3.5) | apparently not verbatim in inspected sources, but too thin | It is the only clean residual and is a direct independent-gap specialization of standard preimage and run-avoidance machinery. |

The bounded search found no inspected source that prints (3.5) verbatim with
cyclic boundary, arbitrary time, and source-weight variable `z`.  That
non-hit is **not** evidence of novelty or priority.  It only identifies the
maximum residual after subtraction.

## 6. Internal and same-batch collision gate

- **P63:** different infinite rank-one XOR carrier, but already occupies
  sliding-block inverse-radius language.
- **P90:** strong category collision: an elementary CA on binary rings with
  exact transients, weighted enumerators, and periodic data.
- **P105:** no literal collision, but it occupies sharp finite pruning clocks
  plus every-target fibres.
- **P117:** strong carrier/statistic collision: cyclic binary words, run
  evolution, exact recurrent census, and sharp preperiod.
- **P147:** decisive architecture collision: local run dynamics, a sharp
  clock, and an every-target product fibre factorized over gaps.
- **P149/P155:** their extraction maps differ; only the ranked-image/section
  packaging overlaps.
- **Same-batch RTI:** stochastic translation intersection is not conjugate to
  this deterministic local erosion.  Its history-span and stabilizer-weighted
  fibres do not transfer.
- **Same-batch CEF:** the equality-feedback front and subsequent additive
  Rule-102 tail differ literally.  Nevertheless it already fills the current
  cyclic finite-word CA slot with all-time clock/image/fibre and special-time
  target spectra.

Thus there is no hidden equivalence to RTI or CEF, but portfolio separation is
still inadequate once P90/P117/P147 and direct external owners are counted.

## 7. Threshold ruling

The requested three-layer mathematical package is true:

```text
temporal law + sharp census + every-target weighted inverse atlas.
```

After honest credit subtraction, however, the first two layers disappear and
the third reduces to one concise gap-factorization corollary.  There are not
two independently creditable theorem axes, no parameter-recovery theorem, and
no deformation that escapes the same preimage automaton.  Promoting it merely
to fill a slot would violate the batch threshold.

**Final decision: `KILL_DIRECT_RULE136_AND_PREIMAGE_OWNER`.**  Preserve the
exact formula and verifier as negative scouting evidence.  Do not allocate a
paper number, do not draft a paper, and retain `HOLD_EXTERNAL`.
