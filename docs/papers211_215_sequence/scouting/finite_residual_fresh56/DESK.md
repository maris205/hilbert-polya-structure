# Fresh56 — one finite-path collision rule, no theorem handoff

Date: 2026-09-11 UTC. Author: current_round_independent_scout.
Disposition: **ONE_DEFINED_LITERAL / ZERO_NOMINATIONS / NO_PILOT**.
This is a bounded author proof-feasibility desk, not a candidate-gate verdict.

The parent permits bijective systems with substantive all-parameter orbit
classification and a separated enumeration/extremal axis. Invertibility is
not an exclusion criterion. This corrects any contrary implication in the
fresh53 chat: that desk supplied no nontrivial period classification, not
a universal argument that bijections are inadmissible. Its old file is
preserved unchanged as requested.

## 1. Archive-first navigation

Finite-word/tree searches located old Foata, Kreweras, Deutsch and tree
rotation controls. They were not instantiated as fresh literals. The
original Foata section was actually read at
`docs/papers152_156_sequence/scouting/combinatorial_replacement2/SCOUT.md`,
lines 286–320, native `14d046`: it defines precisely the cycle-to-word
transformation and already records iteration as a failed old lane.
No unproved global period formula is imported from its small-box data.

The particle search located old BA and the XXC source desk. The actual BA
definition/proof was read at
`docs/papers204_208_sequence/scouting/combinatorial_second/PROOF_NOTES.md`,
lines 100–143 (`be33b8`). It is cyclic ballistic **annihilation**; its
survivors keep their velocities. The candidate below conserves particle
number and reverses blocked velocities on a finite path. No equality,
conjugacy or general factor exclusion is claimed merely from that contrast.

The complete current XXC handoff (`d13878`) and correct
`finite_particle_residual_scout01/SOURCE_AND_VALUE.md` (`7c5628`) were read.
An initial lookup used the nonexistent filename `SOURCES_AND_LIMITS.md`
and returned exit 2 (`637ecd`); it supplied no evidence.

## 2. Literal PBR: parallel blocked reflection

Fix integers $n\ge1$ and $0\le k\le n$. The carrier consists of ordered
occupied positions $1\le p_1<\cdots<p_k\le n$ and velocities
$v_i\in\{-1,+1\}$. Set $O=\{p_1,\ldots,p_k\}$ and proposals
$q_i=p_i+v_i$. Declare $i$ successful if and only if

1. $q_i\in[1,n]$;
2. $q_i\notin O$ (old occupancy, even if that old occupant will depart);
3. no other particle proposes $q_i$.

A successful particle moves to $q_i$ without changing velocity. Every
unsuccessful particle stays at $p_i$ and reverses velocity. All decisions
use the same old state. The output is again ordered by position. There is
no priority rule, asynchronous sweep, source-dependent boundary, or
annihilation convention.

### Elementary claims and proof status

Status: **PROVABLE AS STATED** for totality, noninjectivity at $(n,k)=(3,2)$,
and the two exact cycles below. Strategy: check move admissibility and each
displayed transition directly. These statements do not supply the missing
all-parameter theorem contract.

**Totality.** Successful destinations are pairwise distinct by condition 3
and are old vacancies by condition 2; they cannot coincide with a staying
particle. Two ordered particles cannot cross: an adjacent crossing would
require landing in old occupied sites; separation two with inward motion
would give a common proposal and is blocked. Thus output order remains
strict, and the same finite carrier is invariant. Particle number is
preserved. The empty state is fixed.

Write $(p^+,q^-)$ for two particles at $p,q$ with the indicated velocities.
At $(n,k)=(3,2)$,
$$
(1^+,2^+)\longmapsto(1^-,3^+),\qquad
(1^+,3^-)\longmapsto(1^-,3^+).
$$
In the first source, the left particle proposes old occupied site 2 and
the right particle moves to vacancy 3. In the second, both propose site 2
and reverse. The sources are different, proving noninjectivity. Moreover
$(1^-,3^+)\leftrightarrow(1^+,3^-)$ is a two-cycle, so the first source is
a genuine transient state. This is not a reversible elastic-collision map.

At the **same carrier** $(n,k)=(4,2)$ there is an exact four-cycle
$$
(1^+,4^-)\to(2^+,3^-)\to(2^-,3^+)
\to(1^-,4^+)\to(1^+,4^-),
$$
and an exact six-cycle
$$
\begin{aligned}
(1^-,3^+)&\to(1^+,4^+)\to(2^+,4^-)\\
&\to(2^-,4^+)\to(1^-,4^-)\to(1^+,3^-)
\to(1^-,3^+).
\end{aligned}
$$
For the four-cycle the successive decisions are free inward motion,
mutual old-occupancy blocks, free outward motion, and boundary blocks.
For the six-cycle they are respectively left-boundary/right-move,
left-move/right-boundary, common proposal 3, left-move/right-boundary,
left-boundary/right-move, and common proposal 2. All listed states within
each cycle are distinct, proving the displayed minimal periods.

These are hand-verified finite examples, **not** a census, program run,
or all-size proof. They refute a uniform-period conjecture even with
$n,k$ fixed. They do not prove that a more structured classification is
impossible.

## 3. Precise mechanism subtraction and open proof obligations

The directly browsed primary source Tamás Gombor and Balázs Pozsgay,
*Superintegrable cellular automata and dual unitary gates from Yang-Baxter
maps*, [arXiv:2112.01854v2](https://arxiv.org/html/2112.01854v2), defines
XXC by alternating layers of an involution: vacancy/particle pairs swap,
particle/particle pairs stay (equation 7, lines 114–119). Thus that
whole-layer evolution is bijective. The noninjectivity above excludes a
whole-carrier conjugacy of PBR to that reversible XXC map. It also excludes
an autonomous surjective factor of a finite bijection: if $E$ is onto and
$E\circ F=T\circ E$ with $F$ bijective, then every target $E(x)$ is
$T(E(F^{-1}(x)))$, making $T$ onto and hence bijective on a finite set.
This argument is specific to finite bijective source maps; other old
nonbijective sources have not been excluded. The paper's broader
Yang–Baxter and large-system assertions are not independently audited here.

The occupancy-forgetting factor is also unavailable in the direct form:
for example $(1^+,4^-)$ and $(1^-,4^+)$ initially have the same occupancy
on $[4]$ but next occupancies $\{2,3\}$ and $\{1,4\}$ differ. A scalar
gap process cannot discard all headings without additional valid state.

No all-parameter transient bound sharper than finite-state finiteness,
recurrent-state characterization, orbit-period classification, evaluated
target-fibre formula, or orbit enumeration was established. Writing a
generic sum over all source velocity/position choices would not solve the
second axis. The next genuine proof would need a closed collision-history
or phase invariant handling both same-target and old-occupancy blocking,
then a separate evaluated counting mechanism. Neither is available in this
short desk. The rule is therefore **not nominated**, without spending an
enumeration box to manufacture a signal. No second literal was added.

## 4. Evidence and scope limits

The broad word/tree archive search was truncated (`913d0e`) and is only
navigation; no exhaustive collision clearance is claimed. Targeted
particle results (`540ac7`) led to the original reads above. Two external
searches returned mostly unrelated physical/stochastic particle models;
no matching owner theorem is inferred from these hits or their absence.
The direct arXiv opening and equation-7 lookup succeeded. Search freshness
is not global novelty, and source absence is not proof of ownership freedom.

Only this new desk was written. No scientific code was created, imported,
parsed or executed; no pilot/large box, manuscript, central index, paper
number, Git operation or external write occurred. This is an author-level
negative feasibility result, not a reserve or a new batch.
