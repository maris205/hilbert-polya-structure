# UGR independent candidate gate

2026-09-06 UTC. Assessor: `batch197_lzk_gate`, a nonauthor of UGR and
LNR's proofs, in a separate process from contributors root and
`batch197_fosp_gate`. Current configured model; not an external expert
or cross-model review. Verdict: **MATH_VALID / GO_NARROW_RANK_FAMILY**.

There are zero current open blocking findings for the narrow contract
below. There is no proved full prior adapter that kills its entire
residual. This gate supports at most one rank-family representative;
UGR is not yet root-admitted or numbered and does not create a second
LNR/UGR seat. LNR's existing source HOLD remains unchanged. This is
bounded candidate approval, not global novelty clearance. `HOLD_EXTERNAL`.

## Exact reviewed contract

The carrier is the labelled ternary cycle of length n >= 3 and
`U(x)_i = [x_(i-1) > x_i] + [x_(i+1) > x_i]`, with strict comparisons
and synchronous updates. The author proof, code, full canonical, source
boundary, handoff and preserved failure descriptions were actually read.
The complete LNR inverse proof and primary-source boundary, the original
LNR independent audit, and both TCSD original proof files were also read.
Their inputs are pinned, not replaced by this report.

The mathematical findings are as follows.

| Claim | Assessment and independent evidence |
|---|---|
| Permanent strict extrema | Correct local deduction: a strict minimum maps to 2 with neighbours at most 1; a strict maximum maps to 0 with neighbours at least 1. Hence E(x) is increasing along the trajectory. |
| Finite radius-six growth lemma | Correct as an explicitly computer-assisted finite lemma. New verifier checks every one of the 3^13 = 1,594,323 words individually, using direct height comparisons, not the author's 3^11 / nine-extension decomposition. All 166,536 unequal-center cases have a checked new-extremum witness. |
| All-size period bound | Correct deductive use of the finite lemma. Every repeated cyclic window is among those tested, including n < 13. Equality of E(a) and E(U^4 a) forces U^4 a = U^2 a. Among n+1 four-step inclusions one is equal, giving U^(4n+4) = U^(4n+2). |
| Exact recurrent core | Correct two-time-column classification, independently rechecked below. The only fixed point is 0^n; every other point of Fix(U^2) has exact period two. |
| Eight-role core enumeration | Correct after the proved bijection. Independently recovered through the 81-state height-overlap graph, not by reusing the eight roles or their determinant implementation. Graph trace and recurrence are standard consequences, not a separate novel axis. |
| Exact seed clock | Correct induction for seed 20^(n-1), whose fronts meet at floor(n/2). Thus h(01^(n-1)) = floor(n/2)+1 for n >= 4, and H(3) = 1. Witness-only checks through n=64 pressure the induction; these are not full boxes. |
| Shared all-target fibre theorem | Correct unchanged LNR proof, transported by the full source-set involution J(x)=2-x. The transport itself earns no new credit. The global mixed-target comparison is a possible shared rank-family residual, not a second independent copy. |

The bound H(n) <= 4n+2 is **nonsharp**. The exact full boxes n=3,...,10
give H(n)=1,5,5,5,5,5,5,6, respectively. No formula for the sharp global
clock beyond the stated H(3) is proved or admitted.

## Proof scrutiny beyond the finite atlas

The author's inner-window lemma covers 177,147 inner words: 158,643 have
equal time-2/time-4 centers, 18,300 have a witness that is independent of
the two outer letters, and 204 require all nine extensions. These numbers
account for the full carrier, but the independent checker does not use
them as a partition or assume that outer coordinates are irrelevant.
It checks the claimed implication on all 13-letter words directly.
Witness positions satisfy |j| <= 5-s and the original non-extremum test
is made on the same position, so the four-step set argument is valid.
The finite certificate is a proof dependency and must remain explicit.

For the recurrent language, a (0,0) temporal column forces adjacent
(0,0) columns, hence the all-zero state. Otherwise the possible columns
are (0,2),(2,0),(0,1),(1,0),(1,1). The neutral (1,1) column requires
opposite strong neighbours. In particular it cannot neighbour a weak
column; this uses the neutral site's own equation and fixes the domain
mistake preserved in the author's failed initial checker. Each weak
column has exactly one same-phase weak neighbour, giving unique dimers.
Strong neighbours have opposite phase, possibly separated by a neutral.
These local conditions are both necessary and sufficient in the literal
two-time equations. They give exactly the stated cyclic zero runs of
length 1 or 2 and positive runs 2,11,12,21,121, with the required singleton
zero boundary beside each neutral. The emitted single word determines
the roles uniquely; no rotation quotient or dimer orientation multiplier
is lost, even at n=3 or n=4.

The independent graph has a vertex for every four-height word abcd and
an edge abcd -> bcde exactly when
`U(U(a,b,c), U(b,c,d), U(c,d,e)) = c`.
Labelled closed walks are in bijection with U^2-fixed cyclic words by
overlap. Its 81 vertices and 137 edges are generated from that equation.
Exact Newton identities use all traces through degree 81 and obtain

`det(I-zA) = (1-z)(1-z^2-4z^3-2z^4+z^8)`.

All 72 coefficients after degree 9 vanish. The checked full degree is
essential: agreement of just eight or ten traces would not justify that
identity. GNU signed 128-bit additions and products in this computation
have explicit overflow checks. This is an independent verification
route, not a replacement author lemma or new candidate contribution.

The LNR global inverse comparison was read through every mixed A/J/B
case, the k>=2 length budget, the r=0,1 exceptions and the q=0,1 equality
classification. The standard multifactor Schatten inequality is used
with valid exponents r/s >= 1 and does not require the kernels to commute.
The source-set decoder and classical attainer counts are deducted. The
prior TCSD proof is an exact sign-stratum adapter for every target, but
does not alone provide the inequality for the union of compatible strata.
See the full deduction in [SOURCE_AUDIT.md](SOURCE_AUDIT.md).

## Actual independent execution

[verify_gate.cpp](verify_gate.cpp) is a standalone producer with no file
inputs and no imports or execution of author/old verifier code. The full
3^13 check, 81-degree graph identity, all 88,560 cyclic states for
n=3,...,10, every target's TCSD-stratum union, all maximizing targets,
and the declared seed profiles produced 2,638,324 assertions per run.
The complete canonical is 6,184 bytes, SHA-256
`6beafa58167d74b9db85ca8001b8a54043ad6ffbe493901a6046ead5485e2cb5`.
Two new executions and two actual raw `cmp` calls all exited zero.
See [EXECUTION_RECEIPT.md](EXECUTION_RECEIPT.md) and the complete streams.
The ordered FNV checksum in the canonical is merely a deterministic
diagnostic; the displayed SHA-256 is the cryptographic byte pin.

## Residual value and narrow allowed contract

After deducting the rank primitive, all static sign-stratum decoders,
all attainer source sets/counts, the trace identities and the standard
matrix inequality, two materially different claims remain together:

1. The UGR-specific temporal/core theorem: a complete fixed local-growth
   implication with a deductive nonsharp linear entrance bound; a necessary
   and sufficient recurrent block language; and an exact all-length seed
   clock. Enumeration of that proved core is a corollary, not another axis.
2. The shared rank-family extremal theorem: the sharp comparison of the
   **whole** inverse over every labelled target and the complete equality
   classification, including mixed kernels and the odd-length budget.
   This is the unchanged LNR mathematical theorem used once, not fresh
   inverse credit from the input-complement transport.

The second is not supplied by the full TCSD summand adapter: the old proof
controls one product of gaps, not a sum over a G_U fibre. The first is not
supplied by the inspected strict-lower rank definition or the binary
threshold theorem without an actual iteration adapter. The exact core
classification and global target comparison are substantive all-parameter
progress; the nonsharp global clock is accurately limited and need not
be advertised as a sharp classification. This satisfies the batch's two
mechanism threshold for **one** candidate. It does not support separate
LNR and UGR papers or reuse the same extremal theorem as a second seat.

## Finding census and disposition

Zero current proof, execution or admission-blocking source/value findings
remain in this bounded narrow contract. A source limitation remains:
the actual Mukherjee 2011 convergence body has not been read. Its retrieved
primary definition is strict lower rank; no retrieved primary statement
asserts the upper/reversed-order iteration or a general dual theorem that
would supply UGR's claims. U=FJ is not a conjugacy, and the literal
period-two example prevents transfer of LNR's all-fixed recurrence by
conjugacy. The missing body is consequently not promoted into a universal
blocker for related maps, nor described as positively cleared. Generic
symmetric-threshold sources likewise require an actual embedding, which
has not been established; same period bound alone is not an adapter.

This does not close or weaken LNR-S1, which concerns the paper's directly
matching strict-lower iteration. The primary contexts, nonblocking UGR
access limitation, and deducted contributions are fully recorded in
[SOURCE_AUDIT.md](SOURCE_AUDIT.md). A later applicable primary theorem or
complete internal adapter must reopen its affected UGR scope.

The compile-warning failure and the author's mathematical probe failures
are preserved; current PASS does not erase them. The bounded gate closes
as **MATH_VALID / GO_NARROW_RANK_FAMILY / NOT_ROOT_ADMITTED / HOLD_EXTERNAL**.
No larger complete cyclic cutoff or indefinite source search is required
by this gate. Root must inspect this actual evidence and perform its own
required replay pair before accepting the gate and assigning a number.

The rejected preclosure HOLD draft is preserved in `provisional_hold_01/`.
Its proposed UGR-S1 depended only on an unread related body, without a
primary applicability statement. Root challenged that evidentiary scope;
this assessor withdrew the unsupported blocking classification and
made the residual-value judgment above. This is not a claim to have
obtained the missing body. No scientific input or verification output
changed during that disposition correction.
