# Post-pilot MNA image enumeration and explicit bijection

This dated addendum was written after the ONE fixed `N=1..12` scientific
pilot completed. It does not change the rule, pre-pilot contract or proof,
and no second scientific execution was performed for it. The image
threshold was already proved before that pilot. Root subsequently derived
and first shared the closed enumeration from the threshold; main checked
the algebra and derived the explicit bijection below. These are
collaborative author contributions, not independent candidate review.

Let `T_k=k(k+1)/2` for `k>=1` and `Theta(z)=sum_(k>=1) z^(T_k)`.
If `i_N` is the number of distinct image compositions of total `N>=1`, then

`sum_(N>=1) i_N z^N = Theta(z)/(1-Theta(z))`.

## 1. Threshold-reset derivation

Use the exact right-to-left image scan in `MNA_PROOF.md`, Theorem 3.
The rightmost target part is arbitrary positive, with generating series
`S=z/(1-z)`, and sets the threshold to `1`. From threshold `r`, prepending
size `r+1` increases the threshold to `r+1`; prepending any size at least
`r+2` resets it to `1`.

Starting from `1`, a string of increments through threshold `k>=1` uses
parts `2,3,...,k`, of total `T_k-1`. Its series when it is the terminal,
possibly empty string is `E=sum_(k>=1) z^(T_k-1)=Theta/z`.
If it is followed by a reset part `k+2+u`, `u>=0`, the total mass of this
complete reset cycle is `T_(k+1)+u`. Hence the cycle series is

`C=(sum_(j>=2) z^(T_j))/(1-z)=(Theta-z)/(1-z)`.

Every accepted target has a unique rightmost part, a sequence of complete
reset cycles and one terminal increment string. Therefore its series is

`S * (1-C)^(-1) * E = Theta/(1-Theta)`.

All statements are formal-power-series identities: positive transition
weights make every coefficient finite, and `C(0)=Theta(0)=0`. No analytic
convergence or unverified asymptotic theorem is used. Root's full original
renewal proof was read in native command 18 and is copied with its source
boundary in `root_references/image/`.

## 2. Explicit mass-preserving bijection

This section is a new main-author deduction after root first shared the
closed series. It identifies the image class with nonempty compositions
whose parts are positive triangular numbers, without appealing only to
equality of generating functions.

Given an image target, read it right to left and use its deterministic
threshold scan. Let its rightmost part be `b>=1`. Begin a new list with
`b-1` copies of `1`. Each complete reset cycle has the unique read-order
form

`2,3,...,k, k+2+u`, with `k>=1`, `u>=0`.

For each such cycle, append `T_(k+1)` followed by `u` copies of `1` to the
new list. At the end, the remaining terminal increments have the form
`2,3,...,k` for a unique `k>=1`; append the final part `T_k`. Thus the
produced list is nonempty and every part is triangular. Its total is the
original total because the first part plus the last partial ladder has
mass `b+T_k-1=(b-1)+T_k`, and each reset cycle has mass `T_(k+1)+u`.
The order of emitted cycles is their scan order, not left-to-right target
order; this convention is part of the bijection.

For the inverse, take any nonempty triangular-part composition and reserve
its last part, uniquely `T_k`, for the final increment ladder. Parse the
remaining list uniquely as an initial string of ones and then successive
parts at least `3`, each followed by its maximal string of ones. (The only
positive triangular number smaller than `3` is `1`.) If the initial string
has length `b-1`, start a target read-list with rightmost part `b`. Every
following part at least `3` is uniquely `T_(j+1)` for `j>=1`; if it is
followed by `u` ones, append the scan-cycle `2,3,...,j,j+2+u` to the
read-list. Finally append `2,3,...,k`. Reverse the read-list to get the
target composition.

Each reconstructed increment and reset is legal, so the threshold theorem
places the target in the image. Its unique scan recovers exactly the
parsed blocks, while reserving the final triangular part recovers the
final ladder, even when it is `T_1=1`. Therefore the two constructions are
mutual inverses. Their mass calculation proves the claimed bijection.

Example: target `(2,3,2)` has rightmost part `b=2`, then reset part `3`
from threshold `1`, then final increment `2`. It encodes as `(1,3,3)`.
A one-part target `(N)` encodes as `N` ones. These are deductive examples,
not an additional scientific execution.

## 3. Exact source subtraction and numerical boundary

The triangular-composition class, its reciprocal series, and its recurrence
are already known. Main directly read the full author-contributed
[OEIS A023361](https://oeis.org/A023361), attributed to David W. Wilson
(1998), and [Robbins, *On compositions whose parts are polygonal numbers*](https://ac.inf.elte.hu/Vol_043_2014/239_43.pdf)
(2014), especially Theorem 1 with its proof on p. 240 and Theorem 4 on
p. 241. These consume all novelty credit for that count. The proposed
remaining connection is its identification with this MNA image class.
The source child's bounded three-query followup found no checked existing
connection; it opened no additional source in that followup. This is
owner-thin evidence, not global novelty clearance.

With the auxiliary empty count `i_0=1`, the known recurrence is
`i_N=sum_(T_k<=N) i_(N-T_k)`. The already archived pilot's image counts
for `N=1..12` are `1,1,2,3,4,7,11,16,25,40,61,94`. They match the cited
sequence, but this observation is post hoc documentary comparison, not a
new experiment, proof or independent replay. The carrier remains `N>=1`.

The extracted Robbins table on p. 242 instead reports `g_t(12)=93` and
some later discrepancies. Its own recurrence gives `61+25+7+1=94`, also
the value in OEIS and in the already archived pilot. Main's screenshot
attempt timed out, so this is recorded as an extracted-table discrepancy,
not certified printed typography. We use the proved recurrence and never
turn the inconsistent table or an uninspected asymptotic condition into
validation. Root's separate Robbins fetch timed out; main's successful
199-line extraction is a distinct preserved source return.

No maximum-fibre theorem, new sequence or global novelty is asserted here.
This is author-level theorem progress for a real independent candidate
gate: `OWNER_AMBER / HOLD_EXTERNAL`, not admission.
