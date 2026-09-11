# Fresh28 — previous-occurrence encoding and sparse inverse controls

2026-09-11. **ZERO_NEW_LITERALS / NO_PROMOTION / NO_PILOT / HOLD_EXTERNAL.**
Two structural directions were screened, not two newly nominated maps.
No central/manuscript/Git/host/source-program/child operation occurred.

## Word direction: exact old PD, no temporal re-entry

The opening 48 lines of the original
`docs/papers204_208_sequence/scouting/word_local/SCOUT_REPORT.md` were read.
PD already recomputes the distance to the previous equal letter, using zero
for a first occurrence, on the closed inversion-sequence carrier. Its old
finite observations are not rerun or treated as an all-parameter theorem.
No new recurrence spine was proved here, and no changed offset convention
was proposed to disguise this old literal.

Fresh primary inspection of [Set Parameterized Matching via Multi-Layer
Hashing, §2.2](https://drops.dagstuhl.de/storage/00lipics/lipics-vol369-cpm2026/html/LIPIcs.CPM.2026.36/LIPIcs.CPM.2026.36.html)
reached Definitions 3/5 and Lemma 6, explicitly attributing prev-encoding and
its equality-pattern characterization to Baker. This is a fresh reading of
that author's exposition, not of Baker's original paper. On unrestricted
words over an alphabet of size $q$, an admissible encoding with $k$ equality
classes has $(q)_k$ label assignments. That static argument cannot be silently
used on the position-bounded inversion-sequence carrier, whose labels have
additional restrictions. Neither version gives a new temporal theorem.

## Singular-matrix direction: universal shallow inverse-block control

Theorem 5 and its complete displayed proof were read in Fampa–Lee,
[*On Sparse Reflexive Generalized Inverse*](https://arxiv.org/html/1807.03074),
published in Operations Research Letters 46 (2018), 605–610.
It constructs a generalized inverse by inverting a full-rank nonsingular
submatrix in the transposed row/column positions and filling the rest with
zeros. The published theorem is over the reals; its block identities extend
over any field, but its norm optimization conclusions do not thereby extend
to finite fields. No Moore–Penrose inverse is asserted to exist universally
over a finite field.

### Hand lemma: no choice of that minor yields a deep clock

**PROVABLE AS STATED**, a control about the known construction, not a selected
new candidate. Fix any deterministic choice of an invertible rank-sized
minor for each nonzero $A\in M_n(\mathbb F_q)$. If its row/column index sets
in increasing order are $I,J$ and its block is $B=A[I,J]$, let $H(A)$ be
zero except for $H(A)[J,I]=B^{-1}$; set $H(0)=0$.
Then
$$H^3=H.$$

Proof. The output has rank $r$ and exactly $r$ nonzero rows, indexed by $J$,
and exactly $r$ nonzero columns, indexed by $I$: no row or column of an
invertible block is zero. Any invertible rank-sized minor must therefore use
all these rows and columns. At the next step the choice is forced, giving
$H^2(A)[I,J]=B$ and zeros elsewhere. This output again has unique such
row/column sets; the third application gives precisely $H(A)$. Zero is fixed,
covering rank zero. Thus every state reaches a fixed point or two-cycle in
at most one step. No selector refinement changes this bound. QED.

For structural subtraction, let $Y$ be the zero matrix and all matrices
supported on one invertible block, put $\pi=H^2$, and let $g=H|_Y$.
The lemma gives $\pi|_Y=\mathrm{id}$ and $g^2=\mathrm{id}$, while
$H=g\pi$ (with inclusion of $Y$ understood). This is exactly the generic
canonical-section/involution wrapper already proved in
`scouting/finite_algebraic_normal_form_fresh_desk/PROOF_PACKAGE.md`, Step 1.1,
actually read with its surrounding first 120 lines. No identity with Drazin
or companion matrices themselves is claimed.

Source fibres would only count matrices selecting a prescribed minor and
block; a selector-specific evaluated extremum was not asserted or developed.
The available clock is already mechanically shallow. No lexicographic or
other selector was fixed as a fresh literal, and no static rank-factorization
count was promoted as a new independent dynamical mechanism.

## Evidence limits and stop

Local search was targeted, not a complete history audit. Primary searches and
opens were bounded; the DOI open for Fampa–Lee failed with Internal Error,
then its arXiv HTML supplied the theorem/proof. The previous-encoding source
was read through selected find excerpts, not as a complete paper. Incidental
search results are navigation only. Native requests/returns remain in the
conversation; no extra receipt machinery or numerical artifact was generated.

This continuation uses the already-read project workflow and literature/proof
skills. Result: no theorem pair ready for a candidate gate; zero new literal,
reserve, admission, or denominator increment recommended. This does not rule
out other singular-matrix or word transformations.
