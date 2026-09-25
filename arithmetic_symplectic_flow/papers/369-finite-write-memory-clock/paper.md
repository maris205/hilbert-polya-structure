# Finite product-memory rewrites: every source return has zero IMAGE time

**Paper:** `369-finite-write-memory-clock`.<br>
**Candidate:** `ANG-AUDIT-20260921-FWM01`; date 2026-09-21.<br>
**Status:** **FINITE-WRITE CLOCK CANCELLATION — CONDITIONAL STOP / FORK**.<br>
T0/T1 statements are conditional owner statements; no arithmetic candidate is
constructed. Strong naturalness OPEN; T3 NOT AUDITED. Classical A0/A1/A2
NOT APPLICABLE; formal UNASSIGNED; Route B NOT INVOKED.

## Abstract

Fix exactly the full product-memory owner in the [card](candidate-card.md):
a Borel bijection with a countable partition into actual finite-rewrite charts,
positive finite head weights and strictly positive coordinate probabilities.
Its forward IMAGE density is the finite image/source pattern-weight ratio.
For every integer history this telescopes to an actual-endpoint relative
product, even with repeated writes and arbitrary Borel tail restrictions.
Every entire-source return therefore has clock zero. All source isotropy
survives in the extension, but every physical return group H_x is zero.
This stops positive-period promotion for this class, without deleting source
cycles. Two own finite-write controls and a separate nonatomic prefix owner
give complete contrasting ledgers. No infinite energy or arithmetic fit is used.

## 1. Frozen identity, lineage and hypotheses

| Field | Same frozen owner |
| --- | --- |
| Full source | X=Q times Omega, Omega=product_(s in S) A_s; product Borel |
| Measure | mu=sum_q m(q) delta_q times product_s pi_s |
| Actual update | ONE supplied Borel bijection F with the stated chart partition |
| History owner | Full retained-lag Z action x->F^k x, k in Z |
| Clock/time | Forward negative-log IMAGE; real height translation on extension orbit SET |
| Arithmetic interface | Admissibility may choose rewrites; no specific arithmetic F supplied |
| Classical/operator objects | No symplectic form, roof, determinant or operator supplied |

Q is nonempty countable, 0<m(q)<infinity; S is countable, possibly empty.
Each A_s is nonempty countable, with a strictly positive probability pi_s.
The product probability exists, and mu is sigma-finite through its Q slices.
Each actual chart has source C={q} times {a} times B and sends (q,a,eta)
to (r,b,eta), where D is finite and B is an arbitrary Borel outside-tail set.
The full source pieces AND their images partition X by hypothesis. This is
not inferred from a guessed inverse: it is a condition on the supplied F.
The inverse chart swaps q,a with r,b on the actual image and retains B.
Empty products are one; all head states, configurations and null pieces remain.

The lineage is divisor/admissibility execution -> full symbolic storage and
local update -> its own measured history. This conditional implication does
not establish that a proposed arithmetic algorithm meets these hypotheses,
that all such product sources are nonatomic, or that the weights are canonical.

## 2. Forward IMAGE on arbitrary Borel subsets, including null charts

Write nu_(D^c) for the outside product probability and
W_a=m(q) product_(s in D) pi_s(a_s), W_b=m(r) product_(s in D) pi_s(b_s).
Both weights are finite and strictly positive. For ANY Borel E subset C,
the fixed-pattern tail identification gives a Borel E_tail subset B and

```text
mu(E)=W_a nu_(D^c)(E_tail),   mu(F E)=W_b nu_(D^c)(E_tail).
J(x)=W_b/W_a on C,           mu(F E)=integral_E J dmu.       (1)
```

This uses finite pattern weights, never division by nu_(D^c)(B) or by mu(E).
It remains valid when B or E_tail has measure zero; (1) fixes the prescribed
positive finite version at EVERY point of that chart. Countable additivity
over the source partition and disjoint image partition gives (1) for every
Borel E subset X. The inverse charts have reciprocal densities at F x.
Thus F and its inverse are nonsingular, without assuming invariance of mu.

For actual endpoints x=(q,omega), y=(r,omega') differing at finitely many
sites, define only a finite relative-weight calculator

```text
R(x,y)=[m(r)/m(q)] product_(s:omega_s!=omega'_s) pi_s(omega'_s)/pi_s(omega_s).
```

The one-step density is R(x,F x). Adding unchanged sites to a chart changes
nothing, so the all-point rule is consistent under chart refinements or
alternative descriptions of the same actual map. Its null-point values are
the frozen prescription, not a claim of uniqueness from a.e. measure data.
R is not an extra arrow relation and does not identify finite-difference states.

## 3. All finite histories and repeated-write cancellation

For k>0 let J_k(x)=product_(j=0)^(k-1) J(F^j x); put J_0=1 and
J_(-k)(x)=product_(j=1)^k J(F^-j x)^(-1). The inverse charts and the integral
change-of-variables consequence of (1) prove, by induction, for every Borel E,
mu(F^k E)=integral_E J_k dmu for every k in Z. This also covers infinite-mass E
by nonnegative integration; there is no division by that mass.

Along a finite history only a finite union of sites is written. Head-weight
ratios telescope. At each written site, successive probability ratios telescope
even when that site is written repeatedly. Hence, at EVERY point and every k,

```text
J_k(x)=R(x,F^k x),  c_k(x)=-log J_k(x),
c_(k+l)(x)=c_k(x)+c_l(F^k x),  c_(-k)(F^k x)=-c_k(x).       (2)
```

Negative histories use the same argument on actual inverse charts. The formula
depends on actual endpoints and is independent of the finite chart description.
No sum over all sites, infinite product of relative weights, infinite-history
limit or putative global energy potential is introduced.

## 4. Entire isotropy, kernels, incoming histories and physical phases

Use arrows (x,k,F^k x), retaining the integer label. For any x, its source
isotropy I_x={k:F^k x=x} is a subgroup of Z: either {0} or pZ for the least
positive source period p. Equation (2) gives J_k(x)=1 on ALL of I_x. Therefore
c_k(x)=0 on all source returns, H_x=c(I_x)={0}, and extension isotropy equals
I_x, not a quotient of it. Source cycles and all their repeated lag labels
survive, but there is no positive primitive physical time or positive packet.

The FULL clock kernel consists of all actual arrows with R(x,F^k x)=1;
it may include arrows between different states. The FULL lag kernel is k=0,
hence only identity arrows for this action. Their intersection is the identity
groupoid. These assertions are not merely lists of periodic-point stabilizers.
All incoming arrows to x are (F^-k x,k,x), k in Z, with unique complete
two-sided history through x. There are no additional tail-equivalence arrows.

In the extension (x,h)->(F^k x,h+c_k(x)), choose a reference f in ONE actual
source orbit O. For x=F^k f, phase theta(x,h)=h-c_k(f) is independent of the
choice of k, because two choices differ by a zero-clock source stabilizer.
Two objects over O have the same theta exactly when an actual extension arrow
joins them. Thus the quotient over O is a real phase line; height translation
acts freely and transitively on it. Different actual source orbits stay distinct,
even if their states differ finitely or have equal relative weight. Only this
orbit SET is used; no Hausdorff manifold or invariant physical measure is claimed.

## 5. Two complete finite-write controls

TOGGLE has its own two-atom probability pi(0)=2/3, pi(1)=1/3. F(b)=1-b is
its own inverse; the two singleton charts partition source and image. Its
forward densities are J(0)=1/2, J(1)=2, so c_1(0)=log2 and c_1(1)=-log2.
For every integer k, J_k(b)=pi(F^k b)/pi(b): even k has clock zero, odd k
has c_1(b). There is one source orbit, with I_b=2Z, H_b=0 and extension
isotropy 2Z. Its full clock kernel is the even-lag arrows; lag kernel and
intersection are identities. Every incoming arrow is retained. At reference 0,
the phases are h at 0 and h-log2 at 1. The physical orbit is a free real
line, not a period-two flow; the nonzero one-step clocks cancel on return.

MOVING-WRITE retains X=Z times {0,1}^Z and its own counting-times-biased-product
measure. Its inverse is (n,eta)->(n-1,flip_(n-1) eta). The charts indexed by
n and eta_n fix just site n, leave every other site unrestricted and have
images indexed by head n+1 and the flipped bit; both partitions cover ALL X.
The density is pi(1-eta_n)/pi(eta_n), so c_1=(1-2eta_n)log2. For any integer k,
F^k increases the head by k and flips exactly the finite interval R_k(n)
between n and n+k, including its lower endpoint and excluding its upper;
R_0 is empty. Thus J_k=product_(s in R_k(n)) pi(1-eta_s)/pi(eta_s) and
c_k=log2 sum_(s in R_k(n))(1-2eta_s), also for negative k at its actual source.

No k!=0 returns the head, so source and extension isotropy are trivial and
H=0 everywhere. Clock-kernel arrows are exactly those whose flipped interval
contains equally many zeros and ones; lag kernel/intersection are identities.
All incoming histories are the stated inverse iterates. In one actual orbit,
each head position fixes exactly the configuration obtained by the required
interval flip; other configurations at that head are not merged into the orbit.
For x=F^k f the phase is h-c_k(f), with all untouched infinite memory retained.
Each physical orbit is a real line, with no positive packet or repeated return.
Its product memory is nonatomic, since fixing arbitrarily many bits bounds a
singleton's mass by (2/3)^N; this does not turn it into a recurrent clock owner.

## 6. Separate NONATOMIC-PREFIX owner and full positive ledger

Here X={0,1}^N with its OWN fair Bernoulli probability and total left shift T.
Both inverses theta_a(eta)=a eta remain; cylinder probabilities and uniqueness
of Borel measures give mu(theta_a E)=mu(E)/2 for EVERY Borel E. More generally
the chart v eta->u eta has IMAGE 2^(|v|-|u|), including its prescribed version
at null points. Every singleton is null, by its length-N cylinder mass 2^-N.
The actual groupoid has triples (z,m-n,w), T^m z=T^n w, source w and range z.
Its clock is c=(m-n)log2; witness independence, inverse sign and composition
follow from the retained lag. No freely generated histories are added.

The FULL clock kernel equals the full lag kernel and their intersection:
all synchronous eventual-agreement arrows (z,0,w), not just identities.
The source orbit of f consists exactly of v T^m f for all finite words v
and m>=0, with all actual witness lags retained. These are all incoming
prefix/tail histories, not the unique inverse history of a bijection.

Non-eventually-periodic paths have source and extension isotropy {0} and H=0. An
eventually periodic path with least periodic-tail word length ell has source
isotropy ell Z, clock image H=ell log2 Z and trivial extension isotropy.
Indeed a nonzero shift equality is precisely eventual periodicity, and its
least tail period generates every possible isotropy lag. Thus the least
positive physical time is ell log2. Relative to any actual reference arrow
g:f->x, phase is h-c(g) modulo H_f; all choices differ by that full stabilizer.
At a fixed periodic reference hit T^N x=f this is h-N log2 modulo ell log2.

Two periodic cores share an orbit exactly when their primitive binary words
are cyclic rotations: equality of shifted infinite tails gives that condition,
and rotations supply actual arrows. Every primitive binary necklace therefore
gives ONE physical packet, with all incoming prefixes and phases; repetitions
are k ell log2 of that same packet. This covers every length and word, not just
the two distinct log2 constant packets and the primitive 01 packet of log4.
Non-eventually-periodic source orbits give free real phase lines and no positive packets.
This owner lies OUTSIDE MAIN: T is not bijective and prefix transport reindexes
the full tail, rather than retaining it under a finite-site rewrite. Its
positive packets neither contradict the conditional theorem nor transfer to MAIN.

## 7. Gate, provenance and evidence limits

Advance the conditional finite-write filter; STOP positive-period promotion
for this owner class, since its ENTIRE H_x vanishes. No source-cycle census,
weight retuning, alternate null-point version or selected subsystem repairs
this same contract. Arithmetic realization and strong naturalness remain OPEN;
the theorem supplies neither an arithmetic F nor a new geometric/analytic owner.
This explicitly generalizes the finite-write mechanism of 329 disclosed in the
card; it is not claimed as a new empirical discovery or literature-priority result.

Only the original 81-line card and the full 107-line paper template were newly
read. The card's measured SHA256 was
`8ca58d59d6498503a344e749c96bd28201e7c0684d3ad8022ce823bad3ce64a5`.
A failed guessed-path read returned no content before filename-only localization.
Shared history includes the author's earlier rotor-definition work; no 329 file,
author comparator paper, independent proof or peer report was read for this task.
Proofs are exact finite relative-weight identities, actual action algebra and
own control cylinder measures; no scientific code, cutoff or external search.
ARS/internal review remains shared-history NOT_CALIBRATED, not external peer review.
T3 NOT AUDITED; classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
This fifth round ends at evidence/review handoff; no sixth round is started.
