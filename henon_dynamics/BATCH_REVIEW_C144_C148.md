# Batch review: HCS-C144--HCS-C148

Date: 2026-08-25

System family: five separate Route-A dynamical subtypes under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

Recommendation: **retain four candidates as explicit source-structural
progress, retain C144 as a proved source rejection, continue Route A, and
keep Route B unauthorized**.

## Completed paper outputs

1. **C144** freezes the two-sided Thue--Morse language subshift.  A
   self-contained odd-popcount separation proves that it is nonempty,
   minimal, and uniformly recurrent but has no shift-periodic point at any
   positive period.  Every Artin--Mazur fixed count and primitive-cycle count
   therefore vanishes and the source zeta is exactly one.  Cyclic finite
   substitution words are retained only as approximant controls.
2. **C145** gives an all-size fixed-point theorem for cyclic Rule 90:

   ```text
   Fix(L,n)=2^deg gcd(x^L+1,(x^2+1)^n+x^n).
   ```

   The proof includes nonsquarefree even circumferences.  Möbius inversion
   recovers exact-period points and geometric temporal cycles, while labeled
   `L x n` space--time tori retain both clocks.  Frozen `24 x 24` minimum
   witnesses show that area and one fixed count each erase essential
   primitive-history data.
3. **C146** constructs an explicit lattice automorphism of the compact
   Heisenberg nilmanifold.  Its central circle is a clean fixed component for
   every iterate, with `ker(I-DPhi^n)` equal to the circle tangent; hence the
   ordinary isolated-orbit stability determinant is singular.  The
   invariant-form/Nomizu calculation gives Lefschetz number zero, while the
   horizontal torus has exactly `|det(A^n-I)|=L_(2n)-2` isolated fixed
   classes.  A period-two central-cocycle witness proves that this horizontal
   number is not a nilmanifold component count.
4. **C147** classifies square-billiard primitive positive directions by
   coprime pairs `(m,n)` with length `2 sqrt(m^2+n^2)`.  After vertex-hit
   offsets are removed, each direction has open clean cylinders of positive
   transverse length but zero ambient energy-shell measure.  The full
   reduced Poincare derivative is the shear `[[1,L],[0,1]]`; its
   family-tangent unit eigenvector makes the isolated determinant singular.
   The first global symmetry-inequivalent length collision is
   `65=1^2+8^2=4^2+7^2`, and the aspect `2^(1/4)` removes all distinct
   positive-direction collisions.  The Dirichlet half-wave supplies a
   natural target-free quantization and time reversal, not a trace bridge.
5. **C148** freezes a three-symbol open Walsh gate.  One tick has rank
   `2*3^(k-1)`, whereas a full factor cycle satisfies
   `B_k^k=A^(tensor k)` and has rank `2^k`.  Both subunitarity defects are
   rank-`3^(k-1)` projections, and for every `n,k>=1`, with `d=gcd(n,k)`,

   ```text
   Tr(B_k^n)=Tr(A^(n/d))^d.
   ```

   Newton recursion gives every exact coefficient through `k=5`, and the
   complex primitive-path product is absolutely regroupable in the proved
   disk `|z|<1/sqrt(3)`.  Closing the hole restores a unitary parent;
   projector order is isospectral, while hole location changes the secular
   data.

## Uniform release audit

All five deterministic producers, producer-independent checkers, separate
symbolic reconstructions, canonical byte replays, and hostile mutation suites
pass.  Their receipts are:

- C144: 172,437 checker assertions, 83 symbolic checks, and 37/37 mutation
  rejections;
- C145: 6,520 checker assertions, 1,177 symbolic checks, and 43/43 mutation
  rejections across the complete 576-cell replay ledger;
- C146: 687 checker assertions, 87 symbolic checks, and 31/31 mutation
  rejections across the iterate-20 exact ledger;
- C147: 1,082 checker assertions, 88 symbolic checks, and 36/36 mutation
  rejections across 979 primitive positive directions;
- C148: 748 checker assertions, 141 symbolic checks, and 41/41 mutation
  rejections, including 60 direct traces and 67 exact coefficient cells.

The batch totals are 181,474 checker assertions, 1,576 symbolic checks, and
188/188 rejected hostile cases.  The mutation split is 183 repaired-hash
semantic mutations plus five stale-hash controls.

Every release manifest has an exact 27/27 payload ledger with no missing,
extra, size-mismatched, or hash-mismatched file.  Each package therefore has
28 physical release files including its self-excluded manifest.  No Python
cache, bytecode, or LaTeX auxiliary/log/recorder artifact remains.

Fresh isolated fixed-epoch double builds reproduce all five checked-in PDFs
byte for byte.  The ten rendered pages use embedded/subset fonts and show no
clipping, collision, truncation, malformed formula, broken table, blank
content, or unreadably small text.  Final logs contain no warning,
overfull/underfull box, undefined reference or citation, or multiply-defined
label.

## Content-addressed release ledger

| paper | evidence SHA-256 | PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|
| C144 | `418d3f6f384adb06b8dda10e24a8d0a8254d3a89d6a840a183374e8231e0578d` | `7d226462a14e84e0f5ff36a84b96da659960b477e8fdaba1f7982d6c7e77754f` | `9508aa73d703350622484a9802e6ed0e9fb40df98d5b4e4544d73f22300c0109` |
| C145 | `635a952a8cb5d3b4fcae3eab69e5553bb1165e43c95dd8a345d3fbc93591d246` | `fdc23c119b84e093c0e8c26bf63d70da0cfd23f12a44f64a6d9945146cf9024f` | `0fdbe0b553590ce0e9a46e2a68bfba9c186d032d3a7f8404b797a51fe4881089` |
| C146 | `e6789ac7a8525d81d2cc0802896f83c57602c45e00ad8a89fef81a536228de72` | `8ee75e2e8e293cf3c65856d8c03056dcb52762d92629439170cdaa79e10c80c3` | `99353b6b71d919907049eade88433e869eef76026f7f3c3ddfabb8da6128364f` |
| C147 | `2df27380610e7e7f3c2460563d41213042e95b97b44ee8bacb1dac3c95f771ea` | `d3468d9cb6c2b35fa4034042c388ea1e8e2f6c36e76d9cc5e0b744c073895a1b` | `6e8195d2350647f96bf43556c481af46a88c735f78dabdcbd8bd81f99e1bd570` |
| C148 | `75e93a1253a7d2d51211ea50676b48f4382cd70b050da4db4df0d9837be92787` | `7d74eb952880972d2d73a87e32eb69bbcdd65f430c19aa1ab168bc1e3548dd89` | `fe73e089e5f2c6f796d74ca999de37a155095d0d3af3b4888c508f3452f7c4a4` |

## Internal cross-review and repair ledger

The reviews were evidence-anchored internal theorem/scope audits, not
external peer review.  No acceptance, novelty, model-independence, or
reviewer-independence score is claimed.  They produced the following
release-relevant repairs:

- C144 made its all-period aperiodicity quantifiers self-contained, kept
  finite cyclic approximants outside the subshift, replaced an unregistered
  evaluator status, and corrected its next-step proposal so that a nonempty
  periodic skeleton requires dropping minimality.
- C145 made the nonsquarefree polynomial-kernel argument explicit, separated
  the three bounded minimum domains, retained the divisor history before
  cycle division, and replaced an unregistered evaluator status.
- C146 withdrew the false conjecture that every horizontal fixed class lifts
  to a fixed circle.  It added the explicit period-two cocycle obstruction,
  the clean-kernel equality, and the precise invariant-complex/Nomizu
  Lefschetz calculation.
- C147 replaced a scalar multiplier shorthand by the complete reduced
  Poincare shear, distinguished family-tangent from angular directions,
  separated positive transverse length from ambient measure, proved the
  collision minimum globally, and completed the Dirichlet half-wave,
  principal-symbol clock, reflection phase, and antiunitary bridge.
- C148 corrected the tempting but false one-step rank `2^k` to
  `2*3^(k-1)`, reserved `2^k` for the full-cycle rank, strengthened the gcd
  trace proof and zero-multiplicity argument, separated projector order from
  hole location, and removed a layout overflow and empty third page.

## Academic failure-mode audit

The seven release failure modes were checked explicitly:

1. **Implementation errors:** mitigated by producer-independent checkers,
   separate SymPy paths, byte replay, and repaired-hash semantic mutations.
2. **Source traceability:** no external target table or literature-derived
   numerical claim enters any package; every imported mathematical
   convention is declared in the source audit and the operative computation
   is reproduced locally.
3. **Invented evidence:** all displayed counts, ranks, hashes, and finite
   witnesses are generated by canonical evidence payloads and independently
   reconstructed.
4. **Missing controls:** every paper includes an exact matched or negative
   control, and the controls are kept separate from the positive theorem.
5. **Suppressed surprises:** the periodic vacuum, two-clock collisions,
   false nilmanifold lift, billiard clean-family singularity, and one-step
   Walsh rank correction are reported as results rather than hidden.
6. **Methods/results drift:** theorem statements, evidence keys, checkers,
   paper text, evaluation YAML, compile reports, and manifests were compared
   after the final repairs.
7. **Confirmation bias:** five distinct dynamical subtypes were frozen in
   advance; failed conjectures and strict failed coordinates were retained
   rather than promoted.

## Route-A assessment

The strict tuples are:

```text
C144 (A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)
C145 (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
C146 (A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
C147 (A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)
C148 (A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)
```

C144 is `ROUTE_A_REJECTED`; C145--C148 are
`ROUTE_A_EXPLORATORY`.  C146's Haar--Koopman hint, C147's Dirichlet
half-wave, and C148's finite scattering subgate belong to different source
systems and are not combined.  No package has a frozen target divisor, zero
census, functional equation, counting-law comparison, arithmetic local
factor, Euler factor, root number, automorphy object, or Hilbert--Polya
operator.  Every package has `route_b_invocation_allowed=false`.

## Next gate

The next five-paper Route-A round should continue subtype diversification
while building on one exact boundary per paper: an almost-minimal symbolic
extension with a controlled periodic skeleton; a one-parameter or scaling
family extracted from the Rule-90 two-clock table; a character-resolved
Heisenberg fibre rotation; a rigorously regularized clean-family billiard
trace; and a controlled growing-`k` limit for the open Walsh gate.  Any
target-facing comparison remains a separately frozen protocol requiring
explicit authorization.
