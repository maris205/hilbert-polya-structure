# Independent hostile gate: C02 record-block reversal

**Reviewed object:** COMB_RECORD_BLOCK_REVERSAL_REPORT.md and both exact
implementations/canonical outputs.  
**Reviewer role:** nonauthor; no participation in the proof spike.  
**Decision:** **REWRITE**.  
**Mathematical core:** survives.  
**Paper gate:** not yet cleared.  
**External status:** **HOLD_EXTERNAL**.

## 1. Bottom-line verdict

I did not find a counterexample to the literal map, lexicographic Lyapunov
argument, sharp depth \(n-1\), fixed-point formula, or one-step fibre DP.
The independent fibre verifier was rerun and its stdout matched the canonical
file byte for byte:

~~~text
record-block reversal fibre verifier: PASS
assertions=1636476
~~~

The earlier scouting implementation independently contributes 1,821,399
assertions through \(S_9\). Thus this is not a KILL_FALSE outcome.

It is nevertheless not ready for GO. Two nontrivial implications are
compressed in the prose, the claimed \(O(n^2)\) running time is unqualified,
the owner audit omits a close left-to-right-maxima fibre paper and a current
2026 record-fibre neighbor, and the P1--P121/internal silhouette subtraction
does not yet confront the combination

~~~text
permutation carrier + simultaneous block update + sharp depth n-1
+ exact target-local fibre algorithm.
~~~

After zero-credit subtraction, the fibre theorem is the only clearly
paper-scale residual. The clock is correct but elementary, and the
fixed-point EGF is classical. The candidate should be rewritten at the
proof/owner/value level before any paper number is considered.

## 2. Literal normalization used in this review

For \(\pi\in S_n\), insert a cut before each left-to-right maximum. Write the
resulting record blocks as

\[
\pi=B_1B_2\cdots B_k.
\]

Each \(B_r\) starts at its unique maximum, and these starting maxima strictly
increase. The map \(\Phi\) reverses each even-length \(B_r\), leaves each
odd-length \(B_r\) unchanged, and concatenates the results synchronously.

The empty permutation must be declared fixed. Every statement below is
valid on an arbitrary finite totally ordered label set after transporting
the labels order-isomorphically to \([n]\); this equivariance is used by the
depth induction and should be stated rather than left implicit.

## 3. Equation-by-equation proof audit

| Spike item | Verdict | Hostile check |
|---|---|---|
| Literal record-block decomposition | **PASS WITH BOUNDARY REPAIR** | The decomposition is unique for \(n\geq1\). State separately that the empty word has no blocks and is fixed. |
| Lexicographic descent, equation (1) | **PASS** | Let \(B\) be the first even block. All earlier blocks are odd and unchanged. The first entry of \(B\) is its strict maximum, while reversal places its strictly smaller last entry at the first changed position. Later synchronous reversals cannot affect the lex comparison. Hence every changed state strictly decreases. |
| Acyclicity | **PASS** | Strict descent in a finite total order excludes every nontrivial cycle. Recurrent states are therefore exactly fixed states. |
| Maximum-entry split, equation (2) | **PASS WITH EXPLICIT EQUIVARIANCE NEEDED** | Writing \(\pi=\alpha n\beta\) is unique. The last record block is \(n\beta\), of length \(|\beta|+1\). The proof must say that the induced map on a word with an arbitrary label set depends only on relative order. |
| Depth induction, equation (3) | **PASS AFTER EXPANSION** | If \(|\beta|\) is even, \(n\beta\) has odd length and remains inert at every later step; the evolution is exactly that of \(\alpha\). If \(|\beta|\) is odd, the first image is \(\Phi(\alpha)\operatorname{rev}(\beta)n\); the terminal \(n\) is thereafter an inert singleton and the prefix is an \((n-1)\)-letter instance. This yields \(D_n\leq1+D_{n-1}=n-1\), with the empty-prefix cases handled separately. The spike states this correctly but too tersely. |
| Sharp family, equation (4) | **PASS** | For \(\omega_n=(2,3,\ldots,n,1)\), the only even block is \((n,1)\). One step gives \(\omega_{n-1}n\); the terminal \(n\) stays a singleton. With \(\omega_1=(1)\), induction gives depth \(n-1\). This works also for \(n=2\). |
| Fixed criterion | **PASS** | A reversal of an even block of distinct entries cannot equal that block. Therefore a word is fixed exactly when every record block has odd length. |
| Foata transfer and equations (5)--(6) | **PASS / ZERO CREDIT** | In standard cycle form with each maximum first and cycles ordered by increasing maxima, erasing parentheses gives exactly these record blocks. Thus all-odd blocks correspond to all-odd cycles. The EGF and double-factorial formulas are correct, but classical and not contribution mass. The \(n=0\) convention for \((-1)!!\) should be avoided or stated. |
| Forward direction of the fibre theorem, equations (7)--(8) | **PASS** | An odd source block stays in place, so its maximum is at the first image endpoint. An even source block reverses, so its maximum is at the last image endpoint. Because source block maxima strictly increase, that value is the maximum of the entire image prefix ending at the segment. |
| Converse fibre construction | **PASS AFTER EXPANSION** | For an admissible segment ending at \(j\), condition (8) places \(M_j\) at the first entry of the reconstructed segment: directly for odd length, and after reversal for even length. Since the entries are distinct and \(M_j\) occurs inside the new segment, successive segment maxima are strictly increasing. Every other entry in that segment is smaller, so no extra record cut occurs inside it. Hence the chosen cuts are exactly the reconstructed word's record cuts. These strictness/no-extra-cut steps are essential and are currently hidden in one sentence. |
| Fibre bijectivity/uniqueness | **PASS AFTER ONE EXPLICIT SENTENCE** | Applying \(\Phi\) to the reconstructed record blocks restores the target. Conversely, every literal preimage supplies its unique record cuts. Distinct admissible cuts cannot reconstruct the same preimage, because a permutation has a unique record-block decomposition. State this explicitly. |
| DP, equations (9)--(10) | **PASS** | Let \(h_j\) count admissible cuts of the prefix ending at \(j\). Choosing the previous cut \(i\) and an admissible final segment partitions those cut sequences disjointly, giving (9), and \(h_n\) is the fibre size. The image test \(h_n>0\) follows. |
| “\(O(n^2)\) exact fibre algorithm” | **REWRITE** | This is \(O(n^2)\) **integer additions/indicator tests** once prefix maxima are precomputed. Since the integers can have \(\Theta(n)\) bits (there are at most \(2^{n-1}\) cuts), an unqualified bit-runtime claim is not justified. Say “\(O(n^2)\) arithmetic operations,” or supply a bit-complexity bound (naively \(O(n^3)\)). |

## 4. Independent mechanical attack

I reran:

~~~bash
python3 docs/papers122_126_sequence/proof_spikes/comb_record_block_fibre_verify.py \
  | cmp - docs/papers122_126_sequence/proof_spikes/comb_record_block_fibre_verify.out
~~~

The comparison passed. The verifier exhausts every target and every source
in \(S_n\) for \(0\leq n\leq9\), and checks:

1. every reconstructed candidate maps to the target;
2. the number of distinct reconstructed candidates equals the DP;
3. that number equals the literal indegree;
4. \(h_n>0\) exactly on the literal image;
5. the fixed count and total fibre mass.

The independent scouting program separately checks lex descent, fixed
criterion, every exact depth layer, the sharp witness, and maximum indegree
through \(n=9\). These are strong falsification controls, but they do not
replace the missing prose steps above and do not license an all-\(n\) layer
formula.

One verifier limitation should be recorded: both implementations ultimately
use the same literal record-block definition. They are independent in their
inverse enumeration/DP route, not independent formalizations of what a
record is.

## 5. Direct-owner and nearest-mechanism residual

### 5.1 Material that receives zero credit

- Foata's fundamental correspondence owns the record-block/cycle transfer.
  The cited primary source is
  [Foata and Han, *Signed words and permutations, I: A fundamental transformation*](https://doi.org/10.1090/S0002-9939-06-08436-X).
- Weighted cycle enumeration and, in particular, the all-odd-cycle EGF are
  existing machinery; the cited primary record is
  [Lugo, *Profiles of Permutations*](https://doi.org/10.37236/188).
- Generic lexicographic termination, prefix-max computation, segmentation
  DP, finite functional-graph language, and exhaustive permutation search
  are tools, not contributions.

### 5.2 Exact-map search result

Current searches covered literal and translated phrases including
“record block reversal,” “reverse even record blocks,” “left-to-right maxima
block reversal,” “Foata-block dynamics,” “reverse even cycles under Foata,”
and synchronous/iterated variants. I found no primary source stating this
literal self-map, its sharp clock, or equations (7)--(10). This is only
**BOUNDED_NO_DIRECT_HIT**; it is not a novelty or priority finding.

### 5.3 Missing close neighbors that must be subtracted

1. [Bouvel, Cioni, and Ferrari, *Preimages under the bubblesort operator*](https://arxiv.org/abs/2204.12936)
   gives a pointwise preimage description for another permutation operator
   in terms of left-to-right maxima and studies its functional trees and
   heights. It does not own \(\Phi\), but it owns much of the nearest
   “records determine fibres and tree geometry” genre. A final owner ledger
   must compare the two fibre constructions claim by claim.
2. [Huang, *Greedy Records and Bernstein Transfers for Fence and Circular-Fence Order Polynomials*](https://arxiv.org/abs/2607.22767)
   is a current 2026 primary neighbor involving greedy record blocks and
   endpoint-refined fibres/record posets. Its abstract does not state this
   dynamics, but it is too close in record/fibre language to omit from the
   current gate.
3. Distributional papers about records, cycle parity, genome block reversal,
   or ordinary permutation inverses do not own the literal update. They
   should not be used to inflate either the owner list or the residual.

Owner risk after this audit is **medium**, not low: there is no direct hit,
but the residual lies in a dense permutation-record/fibre neighborhood.

## 6. P1--P121 and internal collision attack

| Neighbor | Collision | Real separation | Gate consequence |
|---|---|---|---|
| **P105, cycle-minimum pruning** | Same carrier \(S_n\), acyclic dynamics, sharp global depth \(n-1\), classical Foata/cycle environment, and exact target-local fibres. | P105 edits cycle notation by deleting successive minima into fixed points; C02 preserves rank and reverses one-line record blocks. P105 has a full iterate normal form and exact depth layers; C02 has an admissible-cut fibre DP but no all-\(n\) layer theorem. | **Highest paper-silhouette risk.** A manuscript must contain a four-axis separation table and cannot market “permutation dynamics + depth \(n-1\) + fibres” as the residual. |
| **Earlier R3 maximal bond-run contraction spike** | Permutation blocks are processed simultaneously; exact maximum depth \(n-1\); the main inverse theorem is a target-local block-assignment/DP fibre law. | R3 contracts monotone consecutive-value runs and changes rank; C02 preserves rank, uses prefix-record cuts, and reverses rather than contracts. | Even though R3 was not the final P117, it is a project-local mechanism collision. C02 needs an output that is not merely the same short-paper silhouette on a new block rule. |
| **P117, odd-run reversal on cyclic binary words** | Synchronous parity-selected maximal blocks, reversal language, and sharp linear transients. This sits directly behind the new-round “local parity variants of P117” firewall. | P117 flips values on cyclic constant runs and has monotone boundary loss plus 1/2-cycles. C02 reverses order inside linearly ordered record blocks, has strict lex descent, and creates/rearranges record cuts rather than eroding a fixed boundary set. | Mechanisms are not conjugate, but the introduction must state this distinction explicitly; parity/reversal alone earns zero credit. |
| **P120, odd-fringe mirror** | Parity selects simultaneous reversals. | P120 acts on child lists of a fixed tree topology and is an involution; C02 reparses record blocks and is a terminating noninvertible map. | Low mathematical collision, moderate naming/narrative collision. |
| **P112, tournament upset reversal** | Synchronous reversal plus a Lyapunov termination proof. | Different carrier, selector, invariant, and fibre theory. | Low risk; generic “synchronous reversal” language receives zero credit. |

No literal conjugacy to P105, P117, or P120 was found. The problem is
residual mass, not equality of maps.

## 7. Short-paper value after strict subtraction

The current package contains:

1. strict lexicographic termination — correct but elementary;
2. maximum depth \(n-1\) with a recursive witness — exact but short;
3. fixed points/all-odd-cycle EGF — classical and zero credit;
4. exact one-step fibres by admissible cuts and DP — the main residual.

This is borderline for the stated “two substantial dynamical outputs” rule.
The pointwise fibre theorem was the precommitted C02 proof-spike gate and it
does pass mathematically; therefore an immediate kill would move the
goalposts. But comparison with P105, the R3 spike, and the bubblesort
preimage literature shows that a note containing only the present four
items would look like a thinner repetition of an already occupied paper
shape.

Minimum value repair: derive **one all-\(n\), theorem-level consequence of
the admissible-cut DP that is not already a restatement of \(h_n\)**. Any one
of the following would qualify:

- a recurrence or generating function for the total one-step image size;
- an exact characterization/census of Garden-of-Eden permutations;
- an exact maximum-fibre formula with its extremizers;
- an all-\(n\) depth-layer recurrence; or
- a nontrivial iterated-fibre/basin theorem.

If none of these closes without prolonged casework, the correct next verdict
is **KILL_VALUE**, not manuscript inflation.

## 8. Allowed claim ceiling

After the mandatory proof and owner repairs, the strongest currently allowed
claim surface is:

- the literal self-map \(\Phi:S_n\to S_n\), including the empty convention;
- strict lexicographic descent for every changed state, hence recurrence
  equals fixedness;
- the maximum-entry induction giving the universal depth bound \(n-1\);
- the uniform sharp family \((2,3,\ldots,n,1)\);
- fixed points as all-odd record blocks, with the Foata/all-odd-cycle count
  explicitly labelled classical and zero credit;
- the bijection between one-step preimages and admissible cuts;
- the DP for every one-step fibre and the one-step image test;
- finite verification through \(n=9\), identified only as falsification
  evidence.

Not currently allowed:

- “first,” “novel,” “new,” priority, or exhaustive-owner language;
- an exact all-\(n\) depth-layer law;
- a formula for maximum indegree or its extremizers;
- iterated-fibre or complete basin geometry;
- asymptotics;
- treating the fixed EGF, Foata correspondence, lex order, or the DP paradigm
  as contribution mass;
- claiming separation from P105/P117 merely because the literal carriers or
  block definitions differ.

## 9. Mandatory repairs before re-review

### M1 — proof completeness

Expand the maximum-\(n\) induction to state order-equivariance, the exact
first image in the even-block case, persistence of the terminal singleton,
and the empty-prefix/base cases.

### M2 — fibre inverse

Replace the one-paragraph converse with a lemma proving:

1. the reconstructed maximum is at the first position of every segment;
2. successive reconstructed block maxima increase strictly;
3. no extra record cut occurs inside a reconstructed segment;
4. the chosen cuts are the unique record cuts; and
5. the two constructions are inverse.

Then prove (9) explicitly by last-cut decomposition.

### M3 — complexity wording

Change \(O(n^2)\) to \(O(n^2)\) arithmetic operations after prefix maxima are
known, or supply a bit-complexity analysis.

### M4 — owner and collision ledger

Add claim-level subtraction against Foata--Han, Lugo, Bouvel--Cioni--Ferrari,
and the 2026 Huang record-fibre neighbor. Add an explicit P105/P117/P120/R3
collision matrix. Search misses must remain bounded no-hits.

### M5 — paper-value increment

Prove one all-\(n\) aggregate or iterated consequence listed in Section 7.
This is the substantive condition separating REWRITE from GO.

### M6 — boundary and contribution language

State \(n=0\) separately, avoid an unstated \((-1)!!\) convention, and keep
the fixed-point EGF in a zero-credit background corollary rather than the
headline contribution.

## 10. Re-entry rule

- **GO** if M1--M6 are completed, the new all-\(n\) consequence survives an
  independent verifier, and the updated owner gate still has no direct hit.
- **KILL** if the fibre theorem collapses to an owned record/bubblesort
  specialization, if the new value theorem fails, or if no second
  owner-subtracted dynamical output can be closed cheaply.
- Until then: **REWRITE / HOLD_EXTERNAL / NO PAPER NUMBER**.

---

## 11. Re-entry review after the all-size image repair

**Re-entry date:** 2026-08-30 UTC.  
**Material reviewed:** equations (11)--(16) in the revised proof spike,
comb_record_image_automaton.py, and its canonical output.  
**Final gate verdict:** **GO_INTERNAL / HOLD_EXTERNAL**.  
**Reason for status change:** the five-bit record-position transfer closes
M5 with a genuine all-\(n\) image/Garden-of-Eden recurrence. It is not a
numerical fit and is not a reformulation of a single target's \(h_n\).

The earlier prose, complexity, owner, collision, and boundary repairs remain
mandatory manuscript work. They no longer block internal selection because
they are local statement repairs rather than missing mathematics.

### 11.1 Reduction of admissibility to record positions

Let \(r_j\) indicate that position \(j\) is a left-to-right maximum, let
\(\ell_j=\max\{a\leq j:r_a=1\}\), and let \(d_j\) indicate that the prefix
ending at \(j\) has an admissible cut sequence. The reduction underlying
(11)--(13) is correct:

- An even final segment \((i,j]\) requires
  \(\sigma_j=M_j\), so \(j\) must be a record, and even length is equivalent
  to \(i\equiv j\pmod2\).
- An odd final segment requires
  \(\sigma_{i+1}=M_j\). Since the entries are distinct, the unique position
  of \(M_j\) in the prefix is \(\ell_j\); hence \(i=\ell_j-1\). Its length
  \(j-\ell_j+1\) is odd exactly when \(j\equiv\ell_j\pmod2\).

Therefore \(d_j\) depends only on the record-position set, not on the actual
record values or the nonrecord ordering. This is the key all-size reduction,
and it is valid.

### 11.2 Five-bit state sufficiency

The state in (11) retains exactly the information needed by the two cases:

\[
(E_j,O_j,Q_j,L_j,D_j),
\]

where \(D_j=d_j\), \(E_j/O_j\) record whether any reachable cut of the
specified parity has occurred, \(L_j=\ell_j\bmod2\), and
\(Q_j=d_{\ell_j-1}\).

No older information is needed:

- a future even segment queries only whether a reachable cut of its endpoint
  parity exists, supplied by \(E/O\);
- a future odd segment queries only the cut immediately preceding the most
  recent record and the parity of that record, supplied by \(Q,L\);
- \(D\) is needed both as the terminal acceptance bit and to update \(Q\) at
  a new record.

Thus five bits are sufficient. Minimality is neither proved nor needed and
must not be claimed.

### 11.3 Audit of the record transition (12)

At a record position \(j\), the new last-record parity is

\[
L_j=j\bmod2,
\]

and the cut immediately before that record is reachable exactly when

\[
Q_j=D_{j-1}.
\]

There are precisely two ways to end an admissible final segment at \(j\):

1. the length-one odd segment, available when \(D_{j-1}=1\);
2. an even segment beginning after any earlier reachable cut with the same
   parity as \(j\), detected by \(E_{j-1}\) for even \(j\) and \(O_{j-1}\)
   for odd \(j\).

Their Boolean union is exactly (12). After computing \(D_j\), OR-ing it into
the matching parity accumulator preserves the stated meaning of \(E_j,O_j\).
Equation (12) passes.

### 11.4 Audit of the nonrecord transition (13)

At a nonrecord position, \(\ell_j=\ell_{j-1}\), so \(L\) and \(Q\) remain
unchanged. An even final segment is impossible because \(j\) is not a
record. The only possible odd final segment starts at \(\ell_j\), and is
admissible exactly when

\[
Q_{j-1}=d_{\ell_j-1}=1
\quad\text{and}\quad
j\equiv L_{j-1}\pmod2.
\]

This is (13). Updating the appropriate parity accumulator afterward is also
correct. Equation (13) passes.

### 11.5 Initial and terminal states

The empty cut gives

\[
d_0=E_0=1,\qquad O_0=0.
\]

The proof should not pretend that \(Q_0,L_0\) have intrinsic meanings before
a record exists. Start the transfer after the forced record at position one,
where the state is explicitly

\[
(E_1,O_1,Q_1,L_1,D_1)=(1,1,1,1,1).
\]

Handle \(I_0=1\) separately. With this wording, all boundary lanes are
correct.

### 11.6 Record-set weight in (14)

For a uniform permutation, the record indicators are the classical
independent Bernoulli variables with probabilities \(1/j\). Equivalently,
for every \(S\subseteq[n]\) containing \(1\),

\[
\#\{\sigma\in S_n:\operatorname{RecPos}(\sigma)=S\}
=\prod_{j\notin S}(j-1).
\tag{17}
\]

This also follows directly by multiplying

\[
n!\prod_{j\in S}\frac1j
\prod_{j\notin S}\left(1-\frac1j\right).
\]

Hence a record decision at position \(j\) has multiplicative weight \(1\),
while a nonrecord decision has weight \(j-1\). The transfer factor

\[
R_j+(j-1)N_j
\]

is exact. Summing all terminal state weights gives \(n!\), and restricting
to \(D=1\) gives the image size. The record-indicator independence and
weight formula are classical and must receive zero contribution credit.

### 11.7 Matrix-product and image formulas (14)--(15)

With column-state convention, the chronological product must be written
unambiguously as

\[
v_n=
\bigl(R_n+(n-1)N_n\bigr)\cdots
\bigl(R_2+N_2\bigr)v_1.
\tag{18}
\]

The bare product notation in (14) is ambiguous about order; this is a
mandatory wording repair, not a mathematical failure. Each deterministic
transition matrix has one outgoing \(1\) per source state, and the weighted
sum accumulates exactly the record-set multiplicities (17). Therefore

\[
I_n=\sum_{s:D(s)=1}v_n(s)
\]

is the exact one-step image size, and \(n!-I_n\) is the exact
Garden-of-Eden count. Equations (14)--(15) pass after the product-order
clarification.

### 11.8 Independent mechanical re-entry evidence

The new verifier was rerun as

~~~bash
python3 docs/papers122_126_sequence/proof_spikes/comb_record_image_automaton.py \
  | cmp - docs/papers122_126_sequence/proof_spikes/comb_record_image_automaton.out
~~~

The comparison passed:

~~~text
record-block image automaton: PASS
assertions=551
~~~

Its 551 assertions comprise:

- factorial-mass checks for every transfer lane through \(n=30\);
- literal image comparison for every permutation through \(n=9\);
- literal verification of the record-set multiplicity formula for every
  record set occurring through \(n=9\).

As an additional reviewer-side control, I independently enumerated all
\(2^{n-1}\) record-position sets through \(n=15\), evaluated admissibility
directly from its last-cut definition rather than the five-bit transition,
weighted each set by (17), and recovered the automaton values exactly.

The verifier establishes exact agreement, not an asymptotic claim or a
minimal-state claim.

### 11.9 Value and collision re-assessment

After zero-credit subtraction, the residual now has three mutually useful
outputs:

1. a sharp all-\(n\) transient clock;
2. every target-local one-step fibre via admissible cuts;
3. an all-\(n\) finite-state recurrence for the total image and
   Garden-of-Eden census.

The third output is structurally different from P105 and the R3 spike:
it aggregates record-position sets with classical record multiplicities,
rather than using cycle-minimum deletion or signed interval inflation. This
does not eliminate the shared permutation/fibre silhouette, but it supplies
enough independent residual mass for a short theorem note under a strict
collision paragraph.

The current owner status remains **BOUNDED_NO_DIRECT_HIT**. The automaton
does not change the need to subtract Foata--Han, Lugo,
Bouvel--Cioni--Ferrari, the classical record-indicator law, and the 2026
Huang record-fibre neighbor.

## 12. Final allowed claim ceiling

The candidate may enter paper planning with only the following contribution
surface:

- the literal synchronous even-record-block reversal map;
- strict lexicographic descent and the sharp maximum depth \(n-1\);
- the admissible-cut bijection and pointwise one-step fibre DP;
- the five-bit weighted recurrence for \(I_n\) and \(n!-I_n\);
- exact finite controls through the stated ranges.

The fixed-point characterization may be included to close the functional
graph, but Foata's transformation, odd-cycle enumeration, (5)--(6), and the
record-set weight (17) are classical zero-credit inputs.

Still forbidden are claims of firstness, novelty, priority, minimal automaton
size, a closed form for \(I_n\), maximum-fibre formulas, all depth layers,
iterated fibres, basin asymptotics, or exhaustive ownership.

## 13. Paper-stage mandatory wording and repairs

The **GO_INTERNAL** verdict is conditional on implementing all of the
following in the manuscript:

1. **Definition and boundary:** define the empty permutation separately and
   state order-equivariance on arbitrary finite ordered label sets.
2. **Depth proof:** expand the maximum-entry induction, including the exact
   first image, the persistent terminal singleton, and base/empty-prefix
   cases.
3. **Fibre inverse:** prove strict increase of reconstructed block maxima,
   absence of extra record cuts, uniqueness of cuts, and the last-cut DP in
   a named lemma.
4. **Complexity:** say \(O(n^2)\) arithmetic operations, not unqualified
   bit time.
5. **Automaton initialization:** start from the explicit state
   \((1,1,1,1,1)\) after position one; do not assign semantic \(Q_0,L_0\)
   values.
6. **Matrix convention:** replace the ambiguous product in (14) by the
   ordered product (18), and define whether state vectors are columns.
7. **Record weights:** prove (17), call the record-indicator theorem
   classical, and assign it zero contribution credit.
8. **Owner subtraction:** compare claims explicitly with Foata--Han, Lugo,
   Bouvel--Cioni--Ferrari, Huang (2026), P105, P117, P120, and the R3 spike.
9. **Contribution language:** headline only the rule-specific conjunction
   of sharp clock, pointwise fibres, and image/Garden recurrence. Do not use
   “new,” “novel,” “first,” or priority language.
10. **Verification language:** report the exact finite ranges and assertion
    counts as falsification evidence, never as proof of all-\(n\) claims.

## 14. Final re-entry decision

**GO_INTERNAL / HOLD_EXTERNAL.**

The M5 value blocker is resolved by a correct all-size transfer theorem.
The remaining repairs are mandatory expository, boundary, complexity, and
owner-subtraction work that can be audited during paper review. Any failure
to implement the claim ceiling in Sections 12--13 reverts the candidate to
REWRITE; a later direct owner hit reverts it to KILL.
