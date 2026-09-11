# CRC3 independent candidate gate

2026-09-05 UTC. Reviewer: `batch197_fifth_scout`.

**Verdict: MATH_VALID / GO_INTERNAL_NARROW / OWNER_AMBER / HOLD_EXTERNAL.**

This is a candidate-admission gate, not either of the two manuscript reviews.
It permits consideration of the pinned ternary all-length package only. It
does not certify external priority, an arbitrary-alphabet inverse theorem,
or completed paper status. No formal paper number is assigned here.

## 1. Independence and pinned inputs

Root authored `../CRC_TERNARY_PROOF_PACKAGE.md` and its author verifier.
The reviewer did not contribute to that proof package or edit author files.
The reviewer read them to audit their claims; the verifier here was written
from independent first-occurrence, orbit-walk, and record-set representations.
It imports no author code. Future manuscript review would require disclosure
of this candidate familiarity and a fresh, suitably distinct review task.

Input SHA256 values, checked before and after mathematical inspection:

| Input | SHA256 |
|---|---|
| CRC_TERNARY_PROOF_PACKAGE.md | `2a843e89f628197e31c1548597311780bfa0f6fa0d7a32903b86a5940d987634` |
| verify_crc3.py | `8665dfa7342247a8dac651476b3c7ab9c134873fbc6e366f7bfae3a61eadc354` |
| CRC3_CANONICAL.json | `1b035b1fc2036e2e1b237c3aeaeb5cefa9af3a830f2f76cf0b43cf75ac8fb9be` |

## 2. Exact mathematical ceiling

For every n >= 1, the carrier is the entire labelled cyclic box
`{1,2,3}^n`, including constant words. The update simultaneously replaces
each coordinate by the number of strict records in its length-n forward
cyclic scan. Equal letters are not new records. The direction and cyclic
root labels are retained; no quotient by rotation is used.

The following author claims are valid.

1. The exact first image is D: minimum one and no cyclic edge 31.
2. The exact second image and recurrent set are C: minimum one and neither
   edge 31 nor edge 13. On C the update is `c -> max(c)+1-c`.
3. `R^4=R^2`; the sole fixed state is `1^n`. Every other recurrent state
   has exact period two. The full-carrier sharp tail is one for n=1,2
   and two for n>=3.
4. The image and core populations are respectively `L_n-2^n` and
   `P_n+1-2^n`, with the two recurrences in the input. Their trace proofs
   also cover loops at n=1 and the doubled adjacency condition at n=2.
5. Every target has exactly the stated one-step fibre Psi. Invalid targets
   have no sources. Empty root-terminated runs have factor one.
6. The maximum fibre is three for n=1,2 and `1+J(n)` for n>=3; the
   stated labelled equality targets are exhaustive, including the
   alternative one-4/two-2 cases and both small-length exceptions.

There is no all-time fibre formula, transient-layer census, n=0 contract,
maximum-fibre claim for larger alphabets, or external novelty certificate.
The exploratory general-alphabet spike is not part of this gate.

## 3. Proof audit, not inference from finite computation

For the first image, the global maxima of a source are exactly its output
ones. Comparing adjacent scans can lose at most the old initial record,
giving the downward-unit constraint. Conversely, `x=4-b` has upward
steps at most one, so its record levels visit every integer up to three;
this supplies every b in D.

For a D-input, an old unit descent can add at most one record to the
scan beginning at the lower letter. An old ascent gives an exact
one-record difference, and equality gives equal counts. Thus the next
image is in C. Unit upward steps on C give every intervening record
level, yielding the reflection. The reflection is an involution preserving
C, proving exact second-image surjectivity and recurrence. The displayed
`1^(n-2)23` witness reaches a D-state outside C, proving sharpness for
n>=3. The n=1,2 witnesses were checked separately.

For inverses, output roots force the source global maxima. The three
possible source maxima are disjoint cases, contributing the two indicators
and the maximum-three product. In the latter case, each root-terminated
source run is binary. Before the last target 3, a target 3 forces source
1 and a target 2 forces source 2. After it, the source is a nonempty
2-prefix followed by 1s. If the run has no target 3, the source is any
weakly decreasing binary word. This proves all choices, their necessity,
and their independence between fixed maximum positions.

Replacing target threes by twos strictly increases at least one positive
run factor and introduces the maximum-two source. Therefore all maximizers
are binary. For a nonconstant binary target the fibre becomes one plus the
product of root-terminated block lengths. The subsequent integer-product
optimization is entirely classical and receives no independent credit.
The constant target is compared separately, avoiding incorrect n=1,2
equality statements.

No unresolved proof gap or counterexample was found in the pinned package.

## 4. Value after explicit deductions

`SOURCE_AND_ADAPTERS.md` gives the source-level and occupied-paper details.
The gate deducts all of the following completely: strict record statistics,
first-occurrence reduction, nearest-greater pointers, static depth encodings,
finite-language transfer matrices, binary chain counts, multiplying
independent factors, and the 2/3/4 integer-product optimum. Neither the
trace populations nor the maximum product is counted as an extra axis.

The residual is modest but two-sided: the exact image-to-unit-Lipschitz
feedback theorem for this recomputed cyclic record map, and its every-target
ternary source decoder with the maximum-symbol cases and all labelled
extremizers. The latter is not the power-of-two independent-site decoder
of P202 or the two-global-rotation decoder of P176. The reviewed external
record theorems do not directly evaluate this simultaneous cyclic profile.
No exact full adapter removing either residual was established in the
bounded review. This is an internal retention judgment, not evidence that
such an owner or adapter cannot exist.

The prior NS gate is a caution: there, an exact scaled descent-set formula
later removed an axis. That failed evidence remains intact. Here ordinary
tools are explicitly deducted, while a kill would still require a precise
formula, literal owner, or deduction covering the present joint profile.
The gate does not award value merely because a map or formula uses a
different carrier or different notation.

## 5. Independent computational evidence

The checker uses earliest occurrences of each possible letter for forward
record counts, cross-checked against all-earlier-letter comparisons through
n=7. It determines tails by walking each full functional graph orbit until
its first repeat, not by the author's Kahn peeling.

For each possible maximum M, the inverse lane fixes target-one positions
to M. It processes each intervening target run right to left, carrying the
SET S of record values in the already-constructed suffix. Prepending v<M
updates `S -> {v} union {s in S:s>v}` and accepts exactly when the new set
size equals the required output. The accepted run words are joined across
roots. This lane does not use a last-3 position or terminal-2 length.

Every target in all ternary boxes n=1..10 is compared with its actual
complete source SET. There are 88,572 targets and the same number of sources
across those boxes. Counts alone are not substituted for source equality.
Every maximizing target is compared with independently enumerated optimal
composition-part lists; all compositions through total 14 are checked.
There are 721,397 assertions per completed run. These finite tests are
regression/falsification evidence, not the all-length proof.

Two actual fresh subprocesses both exited zero with empty stderr; their
entire 3,163-byte stdout streams were byte-identical. SHA256:
`6ead393b4a0c46d641f0ce7a7d83381ad4e0ae704afca21cb81b11f2e1fe1a01`.
The saved `CANONICAL.json` is that exact stream; `REPLAY_LOG.md` records
the actual invocation and outcomes. No unnecessary cutoff growth was used.

## 6. Handoff conditions

Proceed only to ordinary manuscript authorship and two independent paper
reviews if root accepts this narrow gate. Re-open the value verdict if a
source evaluates the full cyclic record-profile fibres, if an occupied
literal mechanism supplies them by an exact adapter, or if the temporal
theorem is found as an existing iteration theorem. External release,
uploads, specialist contact, and priority claims remain HOLD_EXTERNAL.
