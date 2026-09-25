# Raw-card source derivation — Global coprime memory

Screen: `ANG-SCREEN-20260921-GCM01`.
Result: **MAIN has no source recurrence or invariant probability: Pre-P0 STOP/FORK**.
All three source controls have periodic points and invariant probabilities.

## 1. Inputs and role

After separate mathematical release, reread only original card lines 1–67,
through its original EOF marker. The actual 67-line prefix SHA256 is
`21ef68fe27d0d8e08e8b6c6b517684b387ce972470919af8ac10b39f55d55141`.
No author paper, peer proof, scout or other new scientific input was read.
This reviewer previously performed CP1 here and reviewed 364; that shared
history is disclosed, not called blind discovery or external peer review.
The derivation below uses the raw source contract, not an imported theorem.
Retained ARS discipline; internal shared-history **NOT_CALIBRATED**.
No numerical computation, external literature, measure/clock fitting or source
selection is used. No owner-level clock or physical flow is constructed.

## 2. MAIN is a nonempty closed full source

For distinct i,j, the condition gcd(x_i,x_j)=1 is clopen in A^Z: it depends
on two coordinates in a discrete alphabet. The intersection over all such
pairs is therefore closed, hence Borel, with its stated subspace topology.
The exclusion is all-history, not the closure of a finite-window substitute.

For nonemptiness, set a_0=2 and a_(r+1)=1+product_(j=0)^r a_j. For s<=r,
a_(r+1) is congruent to 1 modulo a_s, so these integers are pairwise coprime.
Let b:Z->N_0 be the bijection b(0)=0, b(k)=2k-1 and b(-k)=2k for k>=1.
Then x_i=a_(b(i)) belongs to X. This is only a nonemptiness witness; the
owner remains ALL X, without selecting this orbit or assigning it a measure.

## 3. Actual action, full incoming and source isotropy

Write (Tx)_i=x_(i+1) and (T^-1 x)_i=x_(i-1). Translation of coordinate
indices preserves every defining pair condition; both maps preserve X and
are inverse homeomorphisms. There is no terminal or missing predecessor.
For every x and every k in Z the unique k-step predecessor is T^-k x.
Its full incoming action arrow is (T^-k x,k,x); all such lags remain.
The entire history through x is (T^n x)_(n in Z), not a collection of
arbitrarily prepended one-sided tails. Composition adds lags; inversion
negates them. No two different lag labels are identified at a return.

If T^k x=x for k!=0, then x_0=x_k=a>=2, contradicting gcd(x_0,x_k)=1.
Thus EVERY source isotropy group is {0}; there are no periodic points.
More strongly, U_x={y in X:y_0=x_0} is an open neighborhood of x which
T^k x never revisits for k!=0. No point is topologically recurrent.
Conditional statement only: if a real additive cocycle on this actual
groupoid were later supplied, the image of source isotropy would be {0},
since a cocycle vanishes on identity arrows. This supplies neither that
cocycle nor a measure, extension, clock or physical-return construction.

## 4. Separate obstruction to invariant probability

For a in A let C_a={x in X:x_0=a}. Distinct translates T^k C_a are disjoint:
a point in two would contain the same integer a at two different coordinates.
Suppose nu were a T-invariant Borel probability on ALL X. For every M>=1,
the M disjoint translates with 0<=k<M give M nu(C_a)<=1. Hence nu(C_a)=0.
But the countably many C_a partition X, so countable additivity gives
nu(X)=sum_(a>=2)nu(C_a)=0, contradicting nu(X)=1.
This proof makes no full-support or atomlessness assumption and does not
infer absence of invariant probability merely from absence of periodic points.
It excludes neither arbitrary nonsingular measures nor invariant sigma-finite
measures. No assertion about those different measure questions is needed.

## 5. Complete common ledger for the three controls

Each control's source is closed/Borel: its specified coordinate-pair conditions
are clopen; FREE is all A^Z. Each is invariant under both displayed shifts,
so it has its OWN inverse homeomorphism, no terminals, and the full incoming
history/retained-lag action of section 3 with that control's source substituted.
The MAIN witness belongs to every control, so all include aperiodic sources.

For an arbitrary point of ANY control, its isotropy is the subgroup
I_x={k in Z:x_(i+k)=x_i for all i}. It is {0} if there is no positive period;
otherwise, with ell its least positive period, division with remainder gives
I_x=ell Z. All these arrows, including every repeated lag, are retained.
There are no additional incoming arrows from merely eventually equal tails.

For a finite word w=(w_0,...,w_(r-1)), let w^infinity denote its two-sided
periodic extension. The rules below characterize ALL admissible periodic
points, not only the displayed witnesses. If w has a smaller cyclic period,
use the least period ell of its extension, not the displayed length r.
On its actual ell-point shift orbit, nu_w=(1/ell)sum_(j=0)^(ell-1)delta_(T^j w^infinity)
is a Borel probability on the full control source. T permutes these points,
so nu_w is invariant. This is a permitted existence test, not a canonical
full-support measure or a replacement of the full source by that orbit.

ADJACENT. The exact rule is gcd(w_j,w_((j+1) mod r))=1 for every j.
It follows by evaluating each neighboring pair in the periodic extension,
and conversely checks every such pair. There is no constant periodic point,
since gcd(a,a)=a>=2. The word (2,3) is admissible with least period 2;
its isotropy is 2Z and the corresponding uniform two-point law is invariant.
All other periodic and aperiodic points have precisely the general ledger above.

WINDOW-TWO. The exact rule is gcd(w_j,w_((j+s) mod r))=1 for all j and
s=1,2; symmetry supplies negative offsets. These conditions are necessary
and sufficient for the entire periodic extension. Periods 1 and 2 are
impossible because an offset 1 or 2 compares a symbol to itself. The word
(2,3,5) is admissible with least period 3, isotropy 3Z and an invariant
uniform three-point law. The stated rule covers every other periodic word,
and the common ledger covers every nonperiodic source and incoming history.

FREE. Every finite word over A is admissible, with its actual least period
determining isotropy as above. The constant word (2) gives a fixed source,
isotropy Z and invariant point mass. The full carrier still contains ALL
other periodic words and all aperiodic sequences, with their full incoming.
None of the three controls obtains a physical time or MAIN clock from this.

## 6. Splicing boundary and disposition

The return-word mechanism referenced in 364 needs nonempty closed words at
one actual graph state, whose concatenations/repetitions remain legal in its
full path language. Here no nonempty symbol block can occur twice: its first
integer would repeat at distinct coordinates. A putative local return cannot
reset the global divisor-exclusion memory. In particular repeating any finite
word violates MAIN, so the graph's repeatable-return premise is unavailable.
This is a direct language check, not an application of 364 to a selected proxy.

MAIN therefore stops BEFORE P0 on its full-history recurrence gate. The source
is nonempty, closed and fully invertible, but all isotropy is trivial and no
invariant probability exists. The controls show exactly that the stated local
or absent constraints allow source recurrence, not that any owned flow passes.
The unit-excluding alphabet is retained throughout; no repair or pruning occurs.
T1 remains NOT TESTABLE without an owned clock; T2 is source-only, T3 NOT AUDITED,
classical A0/A1/A2 NOT APPLICABLE, formal UNASSIGNED, Route B NOT INVOKED.
