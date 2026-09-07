# Last-seat legacy proof triage

2026-09-07 UTC. Owner: `/root/thirty_third_finite_scout`.
Decision support only; **NO_PROMOTION / NO_NEW_PROOF / NO_SCIENTIFIC_RUN**.

## Decision

Of the six bounded legacy subjects below, ORR is the sole conditional
next-proof priority. This is a relative ranking, **not** a finding that its
remaining proof is tractable. It already has two closed unsuccessful clock
attempts. If a new full-branch representation cannot be specified without
repeating their false charges, this triage recommends reopening none of the
six. It does not authorize reopening, admit a reserve, create an alias or
paper number, or treat an old HOLD as an independent gate acceptance.

The other five require multiple unresolved obligations or a source-first
decision; their partial results do not justify another generic proof pass.
No new theorem, example, counterexample, pilot, larger box, source search,
independent review or code contribution to any candidate is supplied here.
Root owns central integration and Git. External actions remain HOLD_EXTERNAL.

## Scope and original evidence

Exactly six pre-admission subjects were assessed: HVD, NCC, ORR, NED, CTM,
and GCF+. GCF0's proofs were read only to determine what does **not** carry
to its recorded positive invariant restriction GCF+; it is not a seventh
opportunity. Historical comparison names inside source notes are deductions,
not additional triaged candidates. LNR is excluded because root has a
separate source recheck. No protected numbered-paper scientific, source,
review, QA, freeze or build body was followed or read for this task.

All paths in the table are under `docs/papers204_208_sequence/scouting/`.
The linked native receipts retain literal argv/cwd, exact path sets,
before/after SHA256, exit, and complete raw stdout/stderr. Raw outputs are
new documentary reads of original notes, not new execution of their science.

| Subject | Exact original notes consumed | New documentary receipts |
|---|---|---|
| HVD | `word_local/HVD_PROOF_WORK/{PROOF_AND_DISPOSITION,SOURCE_AND_REPLAY,WORK_CONTRACT}.md`, complete | [10](commands/10_hvd_full/receipt.json) |
| NCC | `word_local/{NCC_INTAKE,NCC_PROOF_BOUNDARY}.md`, complete | [11](commands/11_ncc_full/receipt.json) |
| ORR | `finite_systems_twenty_second/ORR_FIBRE_PROOF.md`, `ORR_ROOT_CLOCK_BOUNDARY.md`, `ORR_SECOND_CLOCK_ATTEMPT/{PROOF_PACKAGE,ATTEMPT_REPORT,SOURCE_READS}.md`, complete; exact ORR portions of original intake, pre-code proof and primary-source boundary | [13](commands/13_orr_deduction_full/receipt.json), [14](commands/14_orr_precode/receipt.json), [15](commands/15_orr_primary_boundary/receipt.json), [16](commands/16_orr_intake/receipt.json) |
| NED | `finite_systems_twenty_first/{INTAKE,PROOF_PACKAGE,SOURCE_AND_HISTORY,SOURCE_SUPPLEMENT}.md`, complete; non-NED desk mentions are context only | [17](commands/17_ned_full/receipt.json) |
| CTM | `finite_systems_twenty_eighth/{INTAKE,PROOF_PACKAGE,SOURCE_AND_HISTORY}.md`, complete | [18](commands/18_ctm_full/receipt.json) |
| GCF+ | GCF0/GCF+ portions of `finite_systems_twenty_seventh/{INTAKE,PREPILOT_PROOF,PROOF_PACKAGE,PREPILOT_SOURCE,SOURCE_AND_HISTORY}.md`; literal line limits are in the receipts | [20](commands/20_gcf_intake/receipt.json), [21](commands/21_gcf_preproof/receipt.json), [22](commands/22_gcf_finalproof/receipt.json), [23](commands/23_gcf_primary_initial/receipt.json), [24](commands/24_gcf_primary_final/receipt.json) |

Primary boundaries below mean **what those original notes say was read**.
This task has not freshly downloaded or read their primary bodies and does
not re-certify their historical access, novelty or review eligibility.

## Only conditional opportunity: ORR's full-carrier clock

### Literal and surviving proved components

On labelled permutations $S_n$ with linear positions, compute all maximal
strictly increasing runs of the old word. Simultaneously reverse every
odd-length run and hold every even-length run. Singletons and the empty
permutation are held. No cyclic boundary, changed run selection or
restricted carrier is proposed.

Let $H_n$ be the maximum number of nonfixed epochs before a fixed point.
The already-proved independent mathematical components are:

- Temporal partial structure: fixed words have only singleton/even runs;
  position parity is invariant; inversion increase forces convergence.
  The second clock note proves for every $n\ge1$
  $$\left\lfloor\frac{n-1}{2}\right\rfloor
    \le H_n\le\binom{\lceil n/2\rceil}{2},\qquad H_0=0.$$
  Its lower bound has an explicit every-epoch pair-block trajectory and an
  even-size maximum-prefix extension. Its quadratic upper bound uses the
  capacity of cross-position-colour inversions, not finite extrapolation.
- One-step inverse/extremal structure: the nonredundant interval partition
  decoder has decreasing odd blocks, increasing even blocks and exact
  source-run maximality conditions. Injection into odd-part compositions
  yields sharp maximum fibre $F_n$ for $n\ge1$, with $F_1=F_2=1$.
  For $n\ge3$ the unique maximizing target is the decreasing permutation;
  the original proof handles $n=0,1,2$ separately.

These are independent *proof components*, not two accepted novelty axes.
Ordinary run-partition inversion, composition/Fibonacci enumeration and
generic inversion potentials are explicitly deducted in the originals.
The old package says the quadratic clock does not qualify as its intended
nontrivial temporal axis. A new sharp time proof would still need the
source/value gate; this triage does not pre-accept the inverse residual.

### Exact missing obligation

Prove on the unchanged full carrier
$$H_n\le\left\lfloor\frac{n-1}{2}\right\rfloor.$$
Together with the existing symbolic lower family this would give equality.
The old finite equality through seven, parity preservation, or a longer
potential calculation does not establish that upper bound.

### Preserved failures and the only bounded distinction worth considering

The first root note proves that a successor active run consists of one
whole old even run plus one active endpoint, or one old singleton plus the
two facing endpoints of old active runs. It does not prove that activity
consumes positions. Its preserved seven-label orbit reuses the initial
active position interval after two steps.

The second note strengthens the obstruction: along the valid parent chain
with label sets
$$\{1,4,7\}\longrightarrow\{2,5,7\}\longrightarrow\{2,4,6\},$$
the last node adds only one new label. Thus charging two fresh labels to
every chain step is false, even though individual label-pair inversions
are never deleted. The other parent supplies the seventh label to the
full ancestry. The scalar cross-colour inversion capacity only counts
events; it does not bound their sequential depth linearly.

If root elects another bounded diagnostic, its stated proof object should
therefore be the **entire merging/branching dependency structure**, retaining
both parents and individual inversion-creation information, rather than a
single ancestral chain, frozen positions, or the scalar statistic $J$.
The concrete decision question is whether that representation supports an
overlap-aware depth certificate on arbitrary permutations, strong enough
to force at least $2t+1$ total labels for activity at epoch $t$ (where the
first nonfixed epoch is $t=1$). This is a proposed obligation, not a lemma
proved or an invariant constructed by this triage.

There is a real representational difference from the failed single-chain
and scalar-capacity arguments: simultaneous branches and their overlap
must be retained rather than discarded. However, **full branching ancestry
is already named as the unresolved possibility in the second note**. It
would be inaccurate to call the direction itself new. No tractability
claim or estimate of success follows from this distinction.

Stop the proposed diagnostic if it cannot give a globally defined
certificate and its exact monotonicity/overlap obligation, or if it merely
reinstates either false fresh-label charge. Do not respond by enlarging the
pilot, proving another quadratic potential bound, or restricting to the
known lower-bound family. No such diagnostic was executed in this task.

### Nearest deducted mechanisms and primary boundary

The original source work identifies Asinowski–Banderier–Hackl,
*Flip-sort and combinatorial aspects of pop-stack sorting* (DMTCS 2021;
arXiv:2003.04912), which reverses all maximal decreasing runs. Value
complement gives all-increasing-run reversal; ORR's even-run hold is not
that literal. The original scout read the indicated early sections and
Theorem 3 proof. The second attempt additionally read the stated shadow,
path, word-order and bandwidth excerpts and complete Propositions 22–23
proofs from the pinned old source text. It records why the source's
wrong-order adjacent-symbol progress premise does not transfer unchanged
through ORR's even-run holds. These are recorded bounded reads, not a
full-paper or global-owner clearance. Ordinary pop-stack/run reversal,
inversion monotonicity, interval partitions and Fibonacci composition
counting remain deductions, not newly earned value.

## Deferred subjects: literal maps, proved boundaries, and reasons

### HVD — two substantial obligations remain

For $n\ge1$, the carrier is $\{0,\ldots,n-1\}^n$. Join $i<j$ when
$x_k<\min(x_i,x_j)$ for every $i<k<j$, and replace $x$ by the ordered
undirected degree sequence. Ties and endpoints are part of the map.

Proved temporal partial results include endpoint erosion to permanent 1s,
permanent interior 2s, and a decreasing active set $A=\{i:x_i>2\}$ after
the first step. Once endpoints are 1, the exact active reduction is
$$z\longmapsto\deg H(z)+b,\qquad
  b_j={\bf1}_{a_j-1\notin A}+{\bf1}_{a_j+1\notin A}.$$
Separated active sites have $b\equiv2$ and embed a smaller positive HVD
system; general adjacent active sites give mixed $b\in\{0,1,2\}^m$.
There is an exact maximum-degree-at-most-three fixed subfamily, but not
the complete recurrent core. The path-target fibre is exactly the weakly
unimodal words and has the evaluated count
$$\sum_{a=0}^{N-1}\binom{2a+n-1}{n-1}$$
on the alphabet $\{0,\ldots,N-1\}$.

Missing: an all-length weighted-active recurrent/convergence or sharp-time
theorem **and** a materially independent evaluated all-target inverse or
extremal residual. The path fibre is an explicitly deducted unimodality
count. The mixed weights cannot be removed by a common translation, and
eventual constancy of $A$ does not freeze its values. The original sentinel
creates an edge and raises square norm from 36 to 38, refuting those simple
monotonicities. Degree targets with ties need not reconstruct a unique HVG;
the original source sentinel gives two graphs with the same ordered degree
sequence. Summing over every compatible graph/order chamber is not an
evaluated inverse theorem.

Source boundary: the original note has detailed partial/full read limits
for canonical-HVG reconstruction, counting HVGs, externally generated
symbolic visibility dynamics, and merge-tree duality. Those static
reconstruction/merge-tree/order-polynomial mechanisms are deducted.
This triage has no bounded device overcoming both independent gaps, so
it does not prioritize a new HVD attempt.

### NCC — histogram/cohort closure does not close labelled time

On labelled words $\{1,\ldots,n\}^n$,
$$C(x)_i=\#\{j:|x_j-x_i|\le1\},$$
including self. These are numeric line positions, not cyclic neighbours
and not a rounded average. Equal-position cohorts never split.

Proved: fixed words have separated occupied positions $S$ with mass
$m_a=a$ at each $a\in S$; labelled allocations give the stated partition
sum. For a constant target $q^n$, every occupied source component has one
or two adjacent positions, total mass $q$, and is separated from the next
component by a zero. This gives the complete evaluated constant-target
fibre formula. The generic all-target occupancy-pushforward multinomial
decoder is explicitly the spent QHK/cohort adapter, with zero separate
credit.

Missing: full labelled recurrence/entrance structure, a substantive clock,
and an evaluated all-target maximum or separate qualifying inverse
mechanism. Genuine labelled two-cycles with an unchanged histogram already
occur in the old notes. A convergent histogram would not imply labelled
convergence; cohort coarsening gives no bound on waiting between mergers.
The old QHK proof that new occupied positions lie among the old positions
does not transfer to this cardinality rule. Even the target $n^n$ is not
always fibre-maximal: the original $n=6$ counts are 316 versus 3800 at
$3^6$. These are preserved old-box facts, not new execution.

Source boundary: old literal queries found no established direct owner
body; averaging, degree feedback, inventories, unit-interval graphs and
histogram allocation remain nearby mechanisms. No precise new bounded
proof route is present in the original notes or supplied here. Defer.

### NED — source-first, then an unresolved dense-carrier problem

On $X_{n,M}=\{x\in\mathbb Z_{\ge0}^n:\sum x_i=M\}$ with labelled cyclic
indices, hold an all-positive word. Otherwise every old positive site
sends one chip to the first old zero clockwise. Simultaneously positives
decrement and zeros receive the lengths of the preceding positive runs.

Proved: an exact full-target decoder uses the partial functional graph
$j\mapsto j-(y_j+1)\pmod n$ on sites with $y_j<n$. Each directed cycle
whose positive gaps sum to $n$ determines one zero-containing predecessor;
an all-positive held target has its separate self predecessor. For $M<n$
the cycle count yields at most one predecessor, hence finite bijectivity
and entrance time zero. These are two mathematical components, not a
certified two-axis literature advance.

Missing: full temporal/recurrent structure for $M\ge n$, a sharp clock,
and source clearance. The dense-only-all-positive recurrent core is already
false: the old note gives the zero-containing cycle of $(2,1,0)$ at
$(n,M)=(3,3)$ and the transient predecessor $(3,0,0)$. Low-mass bijectivity
cannot simply be extended across this boundary.

The original source record identifies Cannings–Haigh, *Montreal Solitaire*
(1992), DOI 10.1016/0097-3165(92)90037-U. Its primary body was not obtained;
metadata and a secondary description suggest the same run-dispatch
primitive on a trimmed line. The line/ring distinction alone earns no
novelty clearance. First obtain and compare the exact primary theorems if
root separately authorizes that source task; it is premature to prioritize
a new dense-carrier proof before knowing what survives that deduction.

### CTM — an onto cubic trace factor is an obligation, not a clock

For every odd prime power $q$, on the whole $M_2(\mathbb F_q)$ in the fixed
basis, $T(A)=A^{\mathsf T}A^2$. There is no invertibility or normality
restriction. The original coordinate proof gives a full one-step inverse
with evaluated linear/conic branches and exact zero-target fibre $q^2$
when $-1$ is nonsquare, $3q^2-2q$ when it is square.

Temporal partials: determinant follows $d'=d^3$, skew follows $k'=dk$,
and trace follows $s'=s(s^2-3d+k^2)$. The singular sector reduces after
one step to ordinary matrix/scalar cubing. But the invariant $d=1,k=k_0$
stratum maps **surjectively** by trace onto
$s\mapsto s^3+(k_0^2-3)s$ on all of $\mathbb F_q$.

Missing: all-$q$ temporal structure of these full factors and their matrix
lifts, not merely the determinant or singular restriction. Global maximum
fibre and owner clearance are also absent. Scalar-root/conic counting,
Cayley–Hamilton and power maps are deducted. The original primary
finite-field-polynomial paper was read only through its stated introductory
text range and the beginning of a proof; no completed classification was
imported. This says what this desk lacks, not that the literature's cubic
problem is universally open. No bounded residual proof mechanism is
available here, so CTM is not prioritized.

### GCF+ — the recorded zero-boundary proof is outside this carrier

For $N\ge n$, on $X^+_{n,N}=\{x\in\mathbb Z_{>0}^n:\sum x_i=N\}$, set
$g_i=\gcd(x_i,x_{i+1})$ and
$$T(x)_i=x_i-g_i+g_{i-1}$$
using old cyclic coordinates. It is exactly the recorded invariant
positive restriction of GCF0, whose nonnegative version sets $g_i=0$ at
an edge incident to zero. It is not an independent renamed direction.

Proved on the positive carrier: positivity and total mass are invariant;
fixedness is equivalent to all currents being equal; $n=1,2$ are identity.
No qualifying full-positive temporal or evaluated inverse axis is present.
The nonnegative parent's permanent-zero cut gives an ordinary transport
potential, but no cut exists in GCF+. Its independent-support fixed-target
divisor-splitting inverse is likewise a zero-boundary theorem, not a
positive-target inverse. Circulating gcd currents are not decoded by it.

Missing: full-positive convergence or recurrence, a substantive sharp-time
result, and a full-target inverse/extremal residual. The initial global
gcd is not invariant, as the old displayed arrow $(2,3,4)\mapsto(3,3,3)$
already shows. Fixed-only finite cycles cannot supply the missing proof.
Conservation, totality repair, transport potential, divisor counting and
positive restriction are all deducted mechanisms. The original source
record found no exact direct primary owner body; general number-conserving
automata background does not transfer a theorem to this rule. Defer.

## Provenance, failures and handoff boundary

The three control files were physically copied and SHA256-pinned **before**
their body key-search. [CONTROL_ROLES.json](CONTROL_ROLES.json) maps exact
original paths to copies and initial hashes. Later root changes to live
central indexes are allowed; the audit checks archived before/after pins
against those exact immutable copies, not against today's live controls.

Commands 03–09 are bounded direct-directory filename discovery only.
The original guard falsely rejected the ordinary suffix `PROOFS` as the
identifier `OFS` and stopped discovery before candidate-body reads. The
original script and partial output are retained. A subsequent display
really failed on the not-yet-created 06–09 paths. Both outer failures are
honestly transcribed, not fabricated as native stdout packages, in
[SCOPE_REFUSAL_TRANSCRIPTION.md](SCOPE_REFUSAL_TRANSCRIPTION.md).
The additive token-aware adapter resumed only the missing metadata reads.
No prior receipt or failed artifact was overwritten. Candidate bodies
subsequently read are exactly those in the table and native path sets.

The project skill was used for the inherited-evidence/hold boundary:
partial all-size deductions and old finite checks do not by themselves
promote a final-seat paper. This task is not a new proof author or reviewer
for any subject. References to old source/scouting exposure failures in
the complete NED/CTM notes describe **those historical tasks**; reading a
disclosure does not establish that this triage opened their excluded paths,
nor does it repair or erase their failures.

Read [DOCUMENTARY_AUDIT.json](DOCUMENTARY_AUDIT.json) and the actual command
25 receipt for hash/scope results. `SHA256SUMS` seals every nonself package
file after this report and audit. No hash test is called a scientific replay
or an independent mathematical acceptance. Scout33 and Scout34 are unchanged;
root may use this sealed triage solely to select the next authorized task.
