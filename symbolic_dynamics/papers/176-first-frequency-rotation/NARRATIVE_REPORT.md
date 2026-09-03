# Narrative report — first-frequency rotation

## Outcome first

For a binary word, rotate left by the multiplicity of the symbol currently
under the pointer.  After fixing the word's Hamming weight `k`, the two local
branches are the frozen rotations `+k` and `-k`.  The paper does not credit
either frozen branch, the generic cyclic-phase reduction, the sharp value
`n-2`, or indicator-style inverse notation.  Høyer--Špalek's quantum phase
rotation, Grošek--Hromada's fixed-weight coordinate-rotation classes, Gupta
et al.'s ordinary circular shifts, and the internal P166 cyclic phase
architecture are explicit subtraction boundaries.  None of those external
sources owns the adaptive first-symbol gluing or its functional graph.

The retained mathematical object is the adaptive gluing of the two branches
on a pointed binary necklace.  On a necklace of least period `d`, its phase
graph splits into `gcd(k,d)` Cayley cycles.  Reading the bits in generator
order completely classifies each component: a constant component is a long
cycle, while a nonconstant component flows into the directed `10` edges.
That one structural theorem gives the complete period inventory, the sharp
clock and deepest-state census.  A separate inverse argument gives every
target's labelled predecessor set and the full `0/1/2` fibre histogram.  A
Möbius sum supplies the fixed census.

## Literal system

Let `R` be left rotation and, for `a in {0,1}`, let
`m_a(w)=#{i:w_i=a}`.  The autonomous finite map is

```text
T_n(w) = R^(m_(w_0)(w)) w,       w in {0,1}^n.
```

It preserves the cyclic necklace and the Hamming weight.  If `|w|_1=k`,
then its two branches are

```text
w_0=1:  R^k w,
w_0=0:  R^(n-k) w = R^(-k) w.
```

## Retained theorem package

1. On a necklace of least period `d`, put `h=gcd(k,d)` and `L=d/h`.
   The pointed graph is the disjoint union of `h` generator cycles of length
   `L`.  For `L>=3`, a constant component is a directed `L`-cycle; a
   nonconstant component has exactly the cyclic `10` edges as recurrent
   two-cycles, and its maximum tail is its longest constant run minus one.
2. The possible periods are `{1}` for `n=1` and
   `{1,2} union {ell: ell|n, 3<=ell<n}` for `n>=2`.
3. The maximum preperiod is `0` at `n=1` and `n-2` for `n>=2`.  Exactly two
   states attain it for every `n>=3`; the boundary counts are two at `n=1`
   and four at `n=2`.
4. Every nonconstant target has at most two explicitly labelled inverse
   rotations.  At weight `k`, the fibre histogram is identically one when
   `n|2k`; otherwise the zero- and two-fibre counts both equal
   `C(n-2,k-1)`.
5. Fixed points are counted by summing primitive fixed-density blocks over
   divisors of `n`, using an explicit Möbius formula.

## Evidence and limits

Uniform proofs establish all five items.  The paper-local standalone
author/scout-derived regression control enumerates every binary word through
length 18, compares the literal functional graph with separate prediction
paths, and freezes a canonical transcript.  It is not implementation-
independent from discovery.  Hostile Review A adds a fresh bit-mask verifier
through length 19 as an independent cross-check.  Hostile Review B adds a
second fresh string-state/Brent/direct-component verifier with 19,758,014
assertions.  Enumeration is used only as a falsifier and regression control.

The lifecycle is exactly:

```text
AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL
```

A direct owner for the adaptive literal map, a literal conjugacy into P166,
or a derivation of the retained component theorem directly from P166's mass
exhaustion changes the internal decision to `KILL_INTERNAL_P166_PHASE_MAP`.
