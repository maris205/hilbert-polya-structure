# Fresh55 — coupled local-ring feedback, bounded proof desk

Date: 2026-09-11 UTC. Status: `ONE_LITERAL / DEDUCTIVE_TWO_AXIS_PACKAGE /
CANDIDATE_GATE_PENDING / NO_SCI_EXECUTION / NO_ADMISSION`.

This is the one instantiated literal in a root-authorized scout allowing at
most two. No second literal was instantiated. It is not P212 work. The author
has not read or changed P212 mathematical manuscripts or manuscript reviews.
No central index, paper number, Git state or external release is changed.

## Literal and established results

Let q be any prime power, m >= 2, R = F_q[t]/(t^m), and I = tR. The autonomous
map on the full, prescribed carrier I² is

    F(x,y) = (y, x(t+y)).

Write v(0)=m and use the truncated t-adic valuation otherwise. For a=v(x)
and b=v(y), the first hitting time of (0,0) is exactly

    tau(x,y) = max{2(m-b), 2(m-a)-1}.

The unique recurrent state is (0,0). The maximum depth is 2m-2, attained
exactly when v(y)=1. For 0 <= h <= 2m-2 the number with tau <= h is q^h;
the number at exact depth h>=1 is (q-1)q^(h-1).

For any target (u,w) in I² put d=min(v(t+u),m-1). It has a preimage exactly
when w belongs to t^(d+1)R. Every nonempty fibre is an explicitly given
annihilator coset with q^d elements. The complete target census is:

| Nonempty fibre size | Number of targets |
| --- | --- |
| q^d, 1 <= d <= m-2 | (q-1)q^(2(m-d-1)) |
| q^(m-1) | q |

Thus the image size is q+(q-1) sum_(j=1)^(m-2) q^(2j). The largest fibres
are precisely the q targets (-t+c t^(m-1),0), c in F_q. The missing targets
are the complement of this image in the q^(2m-2)-element carrier.
The empty sum convention covers m=2; that whole control case is linear.

All these claims are proved in [PROOF_PACKAGE.md](PROOF_PACKAGE.md), with no
pilot, enumeration, verifier execution or measured scientific result.

## Exact ownership subtraction and limits

1. The old MFR polynomial is M(a,b)=(b,ab), studied on F_p² in
   `docs/papers147_151_sequence/scouting/algebraic/SCOUT.md`, lines 287–317.
   On the present I², let P(x,y)=(x,y+t), Q(u,w)=(u-t,w). Both are
   bijections and **F=Q M P**. All one-step inverse, image and maximal-fibre
   results are consequently multiplication/annihilator results in translated
   coordinates. They receive zero claim to a new inverse mechanism. The old
   source's finite-field census is not itself a proved local-ring census;
   the ring formula is derived explicitly here from the same primitive.
2. This two-sided equivalence is not a claimed conjugacy: Q is not P^-1.
   It does not transport iterates. No full-carrier conjugacy or old-factor
   obstruction consuming the displayed temporal theorem has been established
   in this bounded check. Absence of such a finding is not proof of absence.
3. Increasing adic precision by one under a contracting multiplier is old
   background (the WCF desk identified by the collision checker below).
   The temporal residual here is the sharp interleaved full-state clock,
   including the cancellation branch v(y)=1, and its exact depth census.
   It is not a new general valuation method.
4. The linear map L(x,y)=(y,tx) has exactly the same pointwise valuation clock
   and depth census. Equal depth census is not a conjugacy certificate.
   For m>=3, F has unequal nonempty fibre sizes, so it is not conjugate to
   any endomorphism of a finite group, in particular not any finite linear
   map. For m=2, F=L; this boundary subfamily is explicitly deducted.
5. The source author and root have discussed the cancellation example
   (t,-t). It does not refute the clock: it reaches zero at 2m-2 because the
   surviving odd chain controls the full state. No assertion that every
   coordinate valuation rises by exactly one is used. Root's challenge and
   clarification are proof-contribution background, not an independent gate.

The parent's stated candidate criterion permits known mechanisms on one or
both axes, but disallows an old occupied/rejected literal or factor disguised
by renaming. This desk therefore does not self-kill solely because the inverse
axis is primitive-owned, and also does not self-admit from a negative search.
An unconflicted candidate gate must decide the remaining literal/old-factor
and value questions. No scientific execution is requested or authorized here.

## Actual search and reading scope

The author read the current recovery entry, current batch entry and project
workflow before this scout. Literal/mechanism searches covered original
repository Markdown/scouting paths across historical batches, the artifact
index, and the current residual desks; historical QA/copy hits were not
mistaken for fresh systems. This is a bounded retrieval, not full reading of
all historical files. Directly inspected author originals include:

- P127 algebraic scout section 2.1 (nilpotent Jordan clock, Frobenius,
  dual-number squaring and other primitive controls); the large combined
  display was partially truncated, so no whole-file reading is claimed.
- P132 algebraic scout lines 1–240 (local polynomial and Henon controls).
- P147 algebraic scout lines 270–327, especially the actual MFR rule above.
- `finite_residual_fresh09/FIBONACCI_PROOF_AND_SUBTRACTION.md`, the full
  proof/subtraction note for (y,xy+1); output translation is distinguished
  there too from dynamical conjugacy.
- Current `finite_nonlinear_residual_desk01/PROOF_PACKAGE.md` and Fresh54's
  desk, for already rejected coupled rules and immediate duplicate controls.

An assigned process-separated collision checker searched the same one literal
and read additional old originals and primary sources. Its scope/results
will be in [COLLISION_NOTE.md](COLLISION_NOTE.md). The checker contributed the
explicit P/Q subtraction; it is not a noncontributor candidate gate reviewer.

The author issued three batches of four broad web queries for the bilinear
recurrence, local-ring dynamics and finite linear dynamics. Most were
irrelevant; query failure to find F is not novelty evidence. The directly
read primary baseline was Alexander Bors, *On the dynamics of endomorphisms
of finite groups*, published online 17 September 2016, volume 28 (2017),
205–214, [publisher full text](https://link.springer.com/article/10.1007/s00200-016-0304-9).
The viewed introduction and Sections 1–2, including the displayed Fitting
decomposition/rigid-procreation statements, concern endomorphisms. They do
not prove the present nonlinear theorem. Its arXiv abstract was also opened,
but is the same source, not independent evidence. The local unequal-fibre
argument here is elementary and does not depend on a theorem being quoted.
The twelve exact author queries and four actual saved tool responses are
preserved in [AUTHOR_WEB_RECORDS.json](AUTHOR_WEB_RECORDS.json); its source
response includes sections beyond the selected passages actually read.
The child's separate readings are reported only in its attributed note.

Operational limitations preserved: an initial overly broad `rg --files`
display was truncated; a nonexistent `literature` search path failed; a later
guessed P161 WCF path failed and was resolved by `rg --files` to P204. These
are retrieval failures, not scientific negative results. No old evidence was
overwritten. The final handoff will identify the exact files actually sealed.

## Authorship and handoff boundary

- Main scout: literal choice, temporal proof, fibre derivation, depth census,
  nonuniform-fibre obstruction and this desk.
- Root: explicit cancellation challenge and clarification; therefore not an
  independent proof gate for this candidate.
- `fresh55_local_ring_collision`: bounded collision/source research and
  explicit two-sided multiplication equivalence; proof familiarity disclosed.

Open: independent literal/factor/value gate. Closed deductively within this
desk: the stated temporal and one-step formulae. Not claimed: global novelty,
acceptance, numerical validation, manuscript review, a paper seat or completion.
