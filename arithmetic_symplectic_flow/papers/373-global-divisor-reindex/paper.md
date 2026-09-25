# Global divisor exchange: full invertibility does not imply measure admission

Paper373; candidate `ANG-20260922-GDR01`;2026-09-22.
Status **NEGATIVE; SOURCE OWNED / IMAGE SINGULAR; STOP / FORK**.
Batch `MEASURED-HISTORY-20260922-E`, round4/5. Internal NOT_CALIBRATED.
Classical A0/A1/A2 NOT APPLICABLE; formal Route UNASSIGNED; B NOT INVOKED.

## Abstract

The frozen two-track system exchanges proper-divisor-related symbols at every
site, then shifts the entire rails in opposite directions. Its inverse exists
on the full source. Nevertheless its own asymmetric product probability is
singular under the dynamics. Exact cylinder IMAGE ratios on two full constant
configurations tend respectively to infinity and zero; a Borel frequency
argument proves the failure is not merely a chosen null-point version.
Thus no clock or physical packet is admitted under this ID. Equal rail laws
and exchange-off controls are measure preserving, but their clocks vanish;
reindex-off remains singular. All source histories are retained throughout.

## 1. Identity, lineage and question

The [frozen card](candidate-card.md) fixes X=({2,3,...}^2)^Z and its product
Borel structure. Write x_i=(a_i,b_i), chi(a,b)=1 when a!=b and one divides
the other; otherwise chi=0. R swaps a pair precisely when chi=1. C applies
R at ALL sites, S shifts the left rail from i-1 and right rail from i+1,
and F=S C. Only actual F iterates, with integer lag retained, are arrows.
The prime-symbolic arrow is proper-divisor witness -> arithmetic-dependent
exchange -> full reindexing -> next encounter. This is a stated deformation,
not a claimed conjugacy to a sieve or a finite-dimensional geometric lift.

| Owner field | Definition / boundary |
| --- | --- |
| Carrier | Full two-sided countable-alphabet pair shift |
| Action | F=S C, unique inverse C S^-1 |
| Probability | mu=product_i(p times q), p(n)=2^(1-n), q(n)=2*3^(1-n) |
| IMAGE version | J_k(x)=lim_N mu(F^k C_N(x))/mu(C_N(x)) |
| Clock / height extension | Conditional on admission; NOT DEFINED below |
| Symplectic form / classical suspension | NOT APPLICABLE |
| Operator / trace / determinant | NOT AUDITED; no borrowed object |

Here C_N fixes both entire local rails on[-N,N]. These are design laws,
not prime-derived weights. No positive roof, prime table, cutoff, selected
run, spatial quotient or period data is inserted. The question is admission
of this probability and version before any clock or target-period discussion.
Strong naturalness and nonconjugacy to prior owners are not established.

## 2. Full source, probability and exact inverse

The two geometric series sum to1, and every p(n),q(n) is positive.
Kolmogorov product construction gives a probability with full support.
Every C_N has mass at most(1/3)^(2N+1), so every singleton has zero mass.
The predicate chi is symmetric; swapping twice returns the same pair and
preserves chi. Hence R^2=id and C^2=id on ALL X. The rail shift S is a
homeomorphism with (S^-1x)^L_i=a_(i+1), (S^-1x)^R_i=b_(i-1).
Consequently (C S^-1)(S C)=id=(S C)(C S^-1) on the full source.
All maps and their inverses are continuous: each output coordinate depends
on only finitely many input coordinates, although infinitely many may change.

Shifting the two independent iid rails separately leaves mu invariant.
This first holds on every finite-coordinate cylinder by product independence,
then on every Borel set by uniqueness of probability measures. In particular
mu(S E)=mu(E), not merely equality for centred cylinders.

## 3. Two exact all-point failures

Let x^+=(2,4) at every site and x^-=(4,2) at every site. Both belong to
the FULL carrier, including their null singletons. Their paired probabilities
are p(2)q(4)=1/27 and p(4)q(2)=1/12. C swaps all the fixed pairs of
C_N(x^+), and S merely moves the fixed-coordinate intervals of each rail.
Thus, for every N>=0, exactly

    mu(F C_N(x^+))/mu(C_N(x^+))=(9/4)^(2N+1),
    mu(F C_N(x^-))/mu(C_N(x^-))=(4/9)^(2N+1).

Their limits are infinity and0. Positive finite all-point admission fails
already for k=1. No evaluation of further k can repair this failed universal
condition. Neither point can be deleted under the frozen full-source rule.
These computations are exact formulas, not finite experiments extrapolated
to a global law; the following argument also proves actual singularity.

## 4. Borel singularity and impossibility of every-Borel IMAGE

Let P(a,b)=p(a)q(b). Since C is coordinatewise, C_*mu is an iid pair
product with marginal P_R(a,b)=P(R(a,b)). Let B be the Borel set on which
the frequency of pair(2,4) in sites1,...,n tends to1/27. Then

    mu(B)=1,       (C_*mu)(B)=0,

because the respective probabilities of that pair are1/27 and1/12.
For completeness the needed indicator law follows without an external
ergodic assertion: Chebyshev bounds for averages at n=j^2 are summable,
so Borel--Cantelli gives convergence there; the at most2j+1 intervening
bounded summands then give convergence at every n. Apply this separately
to each iid indicator law. Thus C_*mu and mu are mutually singular.

As S_*mu=mu, F_*mu=S_*C_*mu is also mutually singular with mu.
Specifically mu(S B)=1 but (F_*mu)(S B)=0. Put E=F^-1(S B), a Borel
set. Then mu(E)=0 but mu(F E)=1. Any positive finite every-Borel IMAGE
density J would give mu(F E)=integral_E J dmu=0, a contradiction.
This is stronger than the two selected cylinder-version failures: no
Radon--Nikodym IMAGE version for this owner can satisfy that equation.
No post-failure symmetrization or truncation is allowed under this ID.

## 5. Entire retained-lag source ledger, without a fictitious clock

Represent an arrow by(x,k), source x and range F^k x. Even if endpoints
coincide different k are distinct. Composition adds k. The lag kernel is
exactly the units k=0. All incoming arrows into y are

    (F^-k y,k), k in Z,

with no extra scattering-only or shift-only arrows. For EVERY full x,

    I_x={k in Z: (F^k x)^L_i=a_i and (F^k x)^R_i=b_i for ALL i}.

This exact full-state criterion is either{0} or rZ, with r the least
positive point-return lag when one exists. It covers all states without
asserting a global cellular-period census. For a constant pair(a,b), F
acts as R because S fixes constant rails. Thus r=2 if chi(a,b)=1 and
r=1 otherwise, including every diagonal constant pair(a,a). The two
precommitted tests each have r=2 and remain distinct source points on the
same two-point source orbit. Nonconstant configurations use the full criterion.

For MAIN c, its kernel and its intersection with the lag kernel, the height
extension, extension isotropy, H, physical phases, primitive physical packets
and their repetition law are all **NOT DEFINED**, not zero or vacuous.
A discrete source return of2 does not supply a physical time. No route
inference can be made from the full inverse alone.

## 6. Three independent owner controls

### 6.1 EQUAL-LAW

Keep X,F but use mu_eq=product_i(p times p). The pair marginal is symmetric
under R, so C_*mu_eq=mu_eq. Independent rail shifts preserve mu_eq as well.
The finite-cylinder proof extends to every Borel set as above. Hence for
every integer k, every cylinder and every x, J_k=1 exactly. The law has
full support and no atoms by the cylinder bound(1/4)^(2N+1).
The unique inverse remains C S^-1; its source histories and I_x are those
of section5, including all constant-pair tests. Its admitted clock is c_k=0.

Thus the full clock kernel is ALL G; the lag kernel and their intersection
are exactly units. On X times R, extension isotropy is the ENTIRE I_x,
not only its zero lag. H_x=c(I_x)={0}. The physical orbit set is exactly
the pairs([x]_F,h): translation in h has no nonzero return. Every incoming
inverse iterate has the same h. For each entire source orbit, all h in R
are retained distinct phases; no positive primitive physical packet exists,
even if the source is periodic. Repetitions of any source return still
have zero clock, not a positive roof inferred from r.

### 6.2 SWAP-OFF

Keep mu and X but use S alone, with unique inverse S^-1. Its probability,
atom status and full support are section2. Every-Borel invariance gives
J_k=1 for ALL k,x and c=0. Let Per(a)={k:a_(i+k)=a_i for every i} and
define Per(b) similarly. The complete source isotropy is

    I_x=Per(a) intersection Per(b).

If either rail is aperiodic it is{0}; otherwise it is lcm(r_a,r_b)Z for
their least positive periods. Constant pairs, including both tests, have
I_x=Z. Incoming arrows are(S^-k x,k), with both full rails retained.
Clock kernel ALL G, lag kernel/intersection units, extension isotropy I_x,
H={0}, all phases R per entire S orbit and no positive physical returns
follow by the same direct zero-clock argument, now for this own source.

### 6.3 REINDEX-OFF

Keep mu,X but use C alone, inverse C. For the same full constant-pair
cylinders, IMAGE ratios are exactly(9/4)^(2N+1) and(4/9)^(2N+1).
The Borel test in section4 gives C_*mu singular to mu directly. Hence
clock admission fails; none of its physical objects is defined.
Source isotropy IS fully classified: I_x=Z if chi(a_i,b_i)=0 at EVERY
site, and I_x=2Z otherwise. This uses the actual global involution, not
a finite exchange. All incoming are(C^k x,k); endpoints alternate x,Cx
but every integer lag remains. Lag kernel consists of units. Its undefined
clock kernel/H must not be identified with EQUAL-LAW's zero clock/H.

## 7. Gate and decision

| Owner-level question | Result / limit |
| --- | --- |
| T0 carrier and source ownership | PROVED for the full action and law |
| T1 owned positive finite clock | FAIL: actual measure singularity |
| T2 source/physical convention | Full source ledger proved; physical NOT DEFINED |
| T3 trace / operator | NOT AUDITED |
| Classical A0/A1/A2; formal Route; B | NOT APPLICABLE; UNASSIGNED; NOT INVOKED |

Portfolio **STOP / FORK**. The decisive reason is singular IMAGE for this
global all-site exchange, not a finite-write obstruction or a missing inverse.
Equal-law controls show that preserving the source action can instead force
a zero clock; they are not a repaired MAIN. No target prime time, symplectic
realization, universal no-go, new external theorem or priority claim follows.
Any later measure/source change needs a fresh card and authorization.

## Reproducibility and integrity

Primary evidence is the exact proof above: no floating-point calculation,
orbit cutoff, data download, prime/zero fitting or outside source citation.
Inputs were the entire86-line frozen card and repository template. Root's
prior private expectation of an infinite-product risk is disclosed in the
card; this was not blind discovery. The raw reviewer works separately from
that card. See [scope](evidence/scope-review.md),
[independent derivation](evidence/independent-proof.md),
[review](evidence/review.md), [claims](claim-ledger.md) and
[batch record](../370-divisor-renewal-clock/batch-log.md).
Proof-reading/model agreement does not constitute external peer review.

EOF — full source retained; singularity stops clock admission.
