# Internal exact review — adjacent-factor parity flow

Candidate: ANG-20260920-AFP01.
Package: 300-adjacent-factor-parity-flow.
Status: OWNED PARITY IMAGE CLOCK; ALL POSITIVE RETURN PACKETS ABSENT — STOP / FORK.
Review verdict: PASS for the stated negative result and its bounded controls.
Calibration: NOT_CALIBRATED; no journal/venue criteria binding supplied.

## Inputs, access order and review provenance

The original 158-line version-1 [card](../candidate-card.md) was read
in full before any access to the [manuscript](../paper.md). Its SHA-256 is

    fe1dc06ce89644078e422659e0b99cf48b45bbd97dd6ae3baa74faaa2a6553d5

The raw owner, IMAGE, all-period seed argument, main obstruction and
both control conclusions were sent to root before manuscript access.
Root then supplied the 353-line manuscript; I read it in full and
verified its actual SHA-256:

    3fea72d3c21e436345a8344af96c7a9107973ecf9172a713921da2e7961b55ca

At manuscript review, the card had an administrative outcome appended.
Reading its first 158 lines and hashing that prefix recovered the
original hash above. The observed appended full-card hash was

    a805404d51bda80de0ef805d5ab5f67d9aca228b0fba89960c77869027881413

The appendix is not treated as a pre-result frozen input.
No other package theorem, clock or return classification was imported.
Historical design-provenance links are not independently re-audited here.

One inherited-model auxiliary, atomic_clock_scope, read only the raw
card and independently checked the two frozen controls, including
their own Haar calculation and the constant-index seed argument.
It did not inspect the manuscript or other review answers, write files,
perform a numerical census or use external sources. I independently
derived the general positive-index-word lemma and checked the controls.
The auxiliary results were integrated before the raw checkpoint closed.

The explicit finite four-root seed witness in manuscript Section 5 was
supplied by this reviewer during raw analysis, then checked and attributed
by root before manuscript review. It is not a blinded second discovery.
This is separate native execution with inherited model and substantial
shared historical context, not external peer review, formal verification,
cross-model corroboration or evidence of independent error processes.

ARS supplied the three-checkpoint and strongest-counterargument discipline.
The router, review/DA instructions, runtime policy and fallacy reference
were consulted; no criticism quota was used to manufacture a defect.
Only local reads, file hashes and the authorized report write were used.
No scientific code, numerical experiment, literature expansion or upload
was performed. The reviewer owns only this report.

## Checkpoint 1 — independent raw-card findings

**Scope verdict: PASS; candidate target: STOP / FORK.**

The full coproduct of positive root pairs with all profinite seeds is
locally compact, Hausdorff and second countable. Its specified measure
is sigma-finite, locally finite, nonatomic and full-support.
The forward domain is clopen, including the exact divisibility and
positive-numerator restrictions. Every valid branch is a homeomorphism
onto the parity-restricted target fibre stated in the card.
The inverse test forces a=b(b+epsilon)/c and retains every digit j.
Missing-image points and terminal points are not removed; T is not onto.

On an actual inverse branch, (u,v)->(v-u,u) preserves joint Haar.
Scaling its first coordinate by a has ambient IMAGE factor 1/a,
and translation by j preserves it. Restriction to the target parity
cylinder retains the same factor for every Borel subset: no factor 2.
The inverse clock is +log a, and the forward-arrow clock is -log a.

Finite inverse-branch pairs define the entire retained-lag groupoid.
Partial composition needs only the longer already-defined middle path.
Equal-lag presentations extend both sides by the same terminal history,
whose index product cancels. Thus J=A_k/A_m and c=log A_m-log A_k
are pointwise well-defined, multiplicative/additive and locally constant.
Full support on open bisections determines the continuous version even
at null seeds. Complete real translation on the extension is owned;
unit-index steps remain zero-clock steps, not an assigned positive roof.

The main raw proof used inverse integer matrices, rather than the
manuscript's forward rational matrices. Write

    B_a=[[-a,a],[1,0]],  v_i=B_(a_i) v_(i+1)+(j_i,0).

Double an odd period if necessary. With D=diag(1,-1),

    D B_a B_b D = [[a(b+1),ab],[b,b]].

The corresponding product P of these positive integer matrices has determinant
d=product a_i, P_11>d and P_22>=1. Hence
det(I-P)=1-tr(P)+d<0. The affine periodic equation has a unique
rational solution. Its profinite coordinates must be ordinary integers:
nonzero integers act injectively on K and Q intersect K=Z.
No cancellation by an arbitrary profinite element is used.

For these integer coordinates the recurrence is
s_(i+2)=s_(i+1)+floor(s_i/a_i). Two adjacent nonnegative entries
force a nondecreasing future; periodicity makes it constant.
Two negative entries force strict decrease. In a remaining alternating
sign cycle, each next nonnegative term is strictly smaller than the
previous nonnegative term. Thus every periodic seed is (k,k), with
0<=k<a_i at every step, and all digits are k, not necessarily zero.

Consequently main periodicity forces constant parity and one fixed sign.
Multiplication of the cyclic root equations requires
product a_i=product(a_i+epsilon). The positive sign makes the right
side strictly larger; the negative sign, on its valid domain, makes
it strictly smaller. There are no periodic or eventually periodic
main states. All source isotropy, extension fixed-object isotropy
and time-return groups are trivial at every retained object.

The frozen mixed-root pattern is arithmetically admissible and has a
realizable finite seed path: initial (n(2n+1),0), digits (0,0,n,n).
Its four updated seeds are exactly those printed in Section 5.
The final pair differs from the initial pair. The uniform lemma
also excludes a return after any repeated traversal of this pattern.
A root cycle or its index product therefore is not a full packet.

PARITY-OFF has its own IMAGE factor 1/a and strictly increasing
consecutive-root ratio c/b=(b+1)/a>b/a; it has no return at any state.
ADJACENCY-OFF has its own factor 1/a and preserves b/a. A periodic
or eventually periodic root must already be (n,n). Its only periodic
seeds are fixed (k,k), 0<=k<n. Each finite-preimage basin is retained.
Distinct fixed cores cannot acquire a common tail through excursions.
For n>=2, each core basin has source isotropy Z, trivial extension
isotropy and H=(log n)Z: exactly n separate primitive packets.
For n=1 the only eventually periodic seed is (0,0), with source/extension
isotropy Z but H={0}. All other control states have trivial isotropy.
Composite-root packets are not relabelled as repetitions at other roots.

## Checkpoint 2 — complete manuscript comparison

**Verdict: PASS; no manuscript correction requested.**

Propositions 1–2 correctly prove the actual topology, Borel IMAGE law,
presentation independence and null-point continuous version. The proof
of open coarse quotient maps supports descended continuous translation,
but neither Hausdorffness nor embedded circles is asserted.

Lemma 3's different matrix proof is valid. For h=1, P_a has one
eigenvalue >1 and the other of absolute value <1. For h>=2 the
product is strictly positive with both row sums >1. Its positive
eigenvector gives lambda_+>=minimum row sum>1, while
abs(lambda_-)=abs(det M)/lambda_+<1 because abs(det M)<=1.
Thus I-M is invertible at every length, including words containing 1.
The localization and Q intersect K=Z step then justify integer seeds.
The subsequent sign argument handles negative integers and zero
without assuming that the profinite ring is an ordered domain.

Theorem 4 correctly excludes all full periods, then all eventual
periodicity and nonzero retained-lag isotropy. It does not extrapolate
from the single four-root family. The finite witness's digits, signs,
endpoint and reviewer attribution are accurate.
Section 6 keeps both controls separate, all finite preimages and the
unit zero-clock stratum. Its packet counts use distinct actual fixed
tails; equality or divisibility of lengths is not packet identification.

## Checkpoint 3 — strongest counterargument and final limits

The strongest objection would be that the root four-cycle is genuine,
so a longer or noninteger profinite seed cycle might still close even
though the exhibited integer seed does not. That objection would defeat
a family-only or finite-modulus test. Here it is answered by an
all-length nonsingular rational matrix equation, the exact intersection
Q intersect K=Z, and the complete integer recurrence argument. The
proof excludes arbitrary repeated root traversals, not just the example.
Its dependence on the frozen seed rule is explicit; it is not a general
no-go theorem for parity feedback or profinite arithmetic dynamics.

A second possible error would be to infer an absent or borrowed clock
from the empty packet ledger. The manuscript does not do this: the
full Haar IMAGE clock is established before the return obstruction.
Conversely, an owned clock and active arithmetic domain do not establish
source/measure naturalness, which remains OPEN.
Source isotropy, fixed-object extension isotropy and time image groups
are distinguished, especially at the unit core of ADJACENCY-OFF.

No critical, major or minor correction was identified in the bound draft.
This is acceptance of the scoped negative mathematical record, not
admission of AFP01 as a promising prime-packet candidate.
The same-object ledger remains intact. T3 is not supplied or pursued;
classical A0/A1/A2 are not applicable; formal Route is unassigned and
Route B is not invoked. Other orbit equivalences and coarse separation
properties were not classified. No new architecture or old-package
change is authorized by this review.
