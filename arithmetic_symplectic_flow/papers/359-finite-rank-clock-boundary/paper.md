# A finite-rank actual clock cannot carry all prime return times

**Audit:** `ANG-AUDIT-20260921-FRC01`.  
**Status:** `FINITE-RANK PRIME-RETURN BOUND ESTABLISHED; CONDITIONAL FILTER ONLY`.

## 1. Exact result and what it is not

Under the [frozen full-clock hypothesis](candidate-card.md), let d be the
rational dimension of the finitely many clock generators. For ANY one common
lambda>0, at most d distinct primes can have lambda log p as an exact return
anywhere in the full object. This bounds returns, not merely selected
primitives, and excludes realizing all prime times under any one global
choice of time units. The proof is elementary and conditional on the actual
clock representation; it is not a new arithmetic dynamics candidate.

The bridge covers finite-block positive roofs on complete finite-edge shifts
and explicitly cohomologous clocks on those same sources. It does not cover
every continuous roof or every finite-state-looking programme automatically.
Three full suspension controls exhibit exact ranks1,2,1. In particular the
third roof depends on infinitely many coordinates and takes infinitely many
values, yet its ACTUAL clock is cohomologous to an integer-valued one.
Infinite range alone is therefore not a way around the hypothesis.

No claim of global literature novelty, new Route credit or resolution of
the OPEN profinite candidate follows. This completes the fifth bounded
audit of the batch; a sixth round requires the user's next confirmation.

## 2. Full return groups and conditional rank bound

Let g:x->y be an actual arrow of the input G, and use its real extension
(x,h)->(y,h+c(g)). A height return t at the class of(x,h) means that
(x,h+t) and(x,h) are related. Every chain of arrows composes to an actual
arrow with both base endpoints x. Thus the ENTIRE return group is
H_x=c(G_x^x), up to reversing sign, which does not change this subgroup.
No incoming chain supplies another return outside that group. In particular
the kernel and ineffective lags need not be removed to calculate time.

For a loop g at x the single-valued coboundary cancels, so

```text
H_x subset Lambda=sum_j Z omega_j subset V=span_Q{omega_1,...,omega_r}
for EVERY x, with dim_Q V=d.
```

This is valid also when H_x is zero or nondiscrete; it assigns no primitive
to those cases. The same V works globally because the hypothesis fixed the
generators on EVERY actual arrow, not separately by orbit.

Distinct prime logarithms are linearly independent over Q. Indeed multiply
any finite rational relation by a common denominator, then exponentiate:
product_i p_i^(n_i)=1 with n_i integers. Moving negative powers to the other
side and using unique prime factorization forces every n_i=0. Multiplication
by a common nonzero lambda preserves this independence.

If N distinct primes appear as exact lambda log p returns, all N independent
numbers lie in V. Hence N<=d. If infinitely many appeared, already d+1
would contradict this bound. There are infinitely many primes (a prime divisor
of one plus a finite product is not in that finite list), so all-prime return
coverage is impossible for this owner. Every primitive target is a return,
making the corresponding primitive impossibility an immediate consequence.
The theorem does not require the return-generating loops to be primitive.

The conclusion holds separately for every common lambda>0. It permits no
prime-specific rescaling and says nothing about approximate returns: a
finite-rank subgroup may even be dense. No approximation is an exact equality.
Neither a converse nor a canonical-origin theorem is asserted.

## 3. The actual finite-block suspension bridge

Take all two-sided legal sequences of a finite directed-edge graph, and its
invertible left shift sigma. Retain all actual arrows(sigma^n x,n,x), n in Z,
including distinct isotropy lags of periodic sequences. A fixed finite-block
positive roof has finitely many values omega_1,...,omega_r. For n>0 count
occurrences of each value along x,...,sigma^(n-1)x; extend counts to negative
n by reversing sign along the negative history, just as for the roof sums.
Concatenating signed histories adds these counts, so their negatives are
integer-valued Borel cocycles a_j on the full retained-lag transformation
groupoid. The ACTUAL usual-roof cocycle is
c_tau(sigma^n x,n,x)=-R_n tau(x)=sum_j a_j(g)omega_j.
This proves the hypothesis with b=0 on all arrows, not only periodic tests.

If on the SAME source tau=f+u(sigma x)-u(x), with u a single-valued Borel
function and f such a finite-block roof, then telescoping for every signed
n gives c_tau=c_f-u(range g)+u(source g). Thus b=-u gives precisely the
frozen representation. No change of physical clock is made to apply the
theorem: this is an equality for the original full c_tau. Positivity of the
actual roof, not an unproved surrogate, supplies its suspension owner.

A finite-memory sequential rule is covered when the entire autonomous state
includes its memory AND all controlling phase, with finite transition graph
and a true finite-block roof as above. An unbounded counter or schedule is
not a finite graph merely because each update reads a finite window. Nor does
a finite graph automatically make an arbitrary continuous roof finite-block
or cohomologous to one. Those are real hypotheses, not missing words.

## 4. Common full-owner lemma for the three distinct controls

For EACH control the base is the entire compact binary two-sided shift,
with unique full inverse sigma^-1 and fair Bernoulli measure nu. Shifting
specified finite coordinates leaves every cylinder's mass unchanged; the
generating-cylinder measure argument gives invariance on all Borel sets.
No a.e. quotient deletes periodic sequences. The actual groupoid is the
retained-lag transformation groupoid, and signed roof sums are Borel additive
by direct concatenation. Their negatives define the specified extension.

For a continuous roof with1<=tau<=C, the action of integer n on X times R
sends(x,h) to(sigma^n x,h-R_n tau(x)). It is free because a nonzero signed
roof sum has the sign of n. It is proper: if heights of both endpoints stay
in fixed compact intervals, |n| is bounded by their total height range,
since every step has length>=1. The full usual suspension quotient therefore
has a well-defined continuous height flow and the standard roof identifications;
no periodic subspace or representative selection replaces it.

Every class has a unique representative with0<=h<tau(x): successive signed
roof sums are strictly increasing and tend to both infinities. Use nu dh
on this fundamental domain. Its total mass is integral tau dnu, finite.
The integer generator preserves nu dh on all X times R: shift preserves nu
and the accompanying height translation preserves each Lebesgue fiber,
as seen by Fubini. For any fixed physical time, partition the fundamental
domain according to how many roofs are crossed. That count is uniformly
bounded for fixed time, as tau>=1. On each piece the translated return to
the domain is a restriction of a product-measure-preserving integer action
and height translation. The pieces and images partition their domains, so
the OWN finite suspension measure is invariant for every Borel set.

If x is nonperiodic its complete source isotropy is0 and H_x=0. Otherwise
let k be its least shift period. All fixing integers are kZ, and signed
roof sums on them are multiples of
L=sum_(i=0..k-1)tau(sigma^i x)>0. Thus ENTIRE H_x=LZ, least L, with zero
extension isotropy and all repetitions mL. Different shift-orbits cannot
merge through actual arrows; all heights over one periodic base orbit form
ONE physical packet. Equal durations in distinct shift-orbits do not merge.
These are full-owner statements, not a census of selected words.

## 5. U: unit clock on the full source

Its OWN roof tau_U=1 satisfies the preceding hypotheses with C=1.
Its full clock is c_U=-n, represented by generator1, and its suspension
measure has mass1. For every least-period-k word, L_U=k; all nonperiodic
points have H=0. The two constant sequences are distinct base shift-orbits
and hence two primitive packets of least1, not a single labelled packet.
The nonzero return1 forces rank at least1, while the displayed full
representation gives rank1. All source inverse and phase data are as proved
for this very roof. Its declared roof clock is not the source's IMAGE clock.

## 6. V: two genuinely independent clocks

Its OWN roof is1 at symbol0 and sqrt2 at symbol1; it is continuous positive
with C=sqrt2. If N_0,N_1 are full signed symbol counts, c_V=-N_0-N_1 sqrt2,
an all-arrow representation by two integer cocycles. The invariant suspension
measure has mass(1+sqrt2)/2. A least-period-k word with m_0 zeros and m_1 ones
has its OWN least period L_V=m_0+m_1 sqrt2, by the full isotropy proof.
Nonperiodic points have no positive return. Its two constant packets give
returns1 and sqrt2, rationally independent since sqrt2 is irrational (the
usual even/odd contradiction after squaring a reduced fraction proves it).
Therefore the minimal possible rational rank is exactly2, not merely at most2.
These are not U periods imported to the same symbolic words.

## 7. W: infinite-memory roof with exact rank one

The series tau_W=1+sum_(k>=1)2^(-k)x_k converges uniformly by the geometric
tail bound. Its summands are continuous cylinders, so tau_W is continuous
and lies in[1,2]. Changing a sufficiently distant digit changes the value
while leaving any prescribed finite window fixed. It is not finite-block,
and binary expansions supply infinitely many values. Its own full suspension
and invariant measure nevertheless follow from section4; its measure has
mass1+(1/2)sum_(k>=1)2^(-k)=3/2, by bounded convergence.

Put u(x)=sum_(k>=0)2^(-k)x_k, a uniformly convergent continuous function.
Shifting the series and subtracting gives, at EVERY point,

```text
u(sigma x)-u(x)=-x_0+sum_(j>=1)2^(-j)x_j;
tau_W=(1+x_0)+u(sigma x)-u(x).
```

Thus c_W=-R_n(1+x_0)-u(sigma^n x)+u(x) on all signed arrows.
The integer cocycle -R_n(1+x_0), generator1 and b=-u satisfy the exact
hypothesis. For a least-period-k word the telescoping term cancels, giving
its OWN least time L_W=k+m_1. Nonperiodic points still have H=0, and the
constant zero word supplies return1, making the minimal rank exactly1.
All incoming and phases remain in the full suspension; no actual roof or
source was replaced to obtain this identity. Infinite memory/range did not
remove this finite-rank obstruction. It is not a theorem that all infinite-
memory roofs reduce in this way.

## 8. Applicability, reproducibility and end of batch

Portfolio **advance** this proved conditional search filter; **stop** any
all-prime exact-return claim for an owner satisfying its full hypothesis.
Do NOT use it to reject every symbolic dynamics programme or every geometric
lift. A finite-state appearance is not an actual-clock representation.
The controls are symbolic roof boundary tests, not endogenous prime candidates.

In particular a zero IMAGE cocycle cannot describe a different commuting
geometric flow's returns, and unbounded content values alone do not decide
whether a profinite cocycle has a finite-rank representation up to coboundary.
For358 that representation is NOT ESTABLISHED; this theorem neither proves
nor refutes it and leaves its T2 OPEN. No new358 orbit search was performed.

Methods: exact full-arrow cancellation, unique prime factorization, signed
block counts, suspension-measure partitions and uniformly convergent series.
No numerical experiment, prime dataset, approximate match, literature novelty
claim or external analytic object is used. ARS CP1/2/3 and raw-contract
derivation are internal shared-history NOT_CALIBRATED, not peer verification.
Same-owner ledger intact; naturalness OPEN; no new formal T/Route coordinate;
classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
This is the fifth round: summarize and await confirmation, not a sixth search.

EOF — conditional finite-rank bound, full bridge and three own controls complete.
