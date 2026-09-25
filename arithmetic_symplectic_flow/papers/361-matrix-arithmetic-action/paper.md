# Full matrix Haar action: paired rank defects force packet multiplicity

**Paper:** `361-matrix-arithmetic-action`; candidate `ANG-20260921-MAA01`.
**Date/status:** 2026-09-21; **OWNED MATRIX CLOCK; PAIRED PACKET MULTIPLICITY — STOP / FORK**.
Owner-level T0 and Haar-clock T1 established; T2 target fails at the frozen test.
Classical A0/A1/A2 NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.

## 1. Abstract, identity and boundary

The full partial GL2 arithmetic action on M2(Z-hat) owns its Haar IMAGE
clock, including the prescribed values at null matrices. Its paired rank
defects give at least two distinct primitive packets of time 2 log p for
every prime p. No common change of time units removes that multiplicity.
All idempotents in the frozen diagnostic and three separate controls are
handled below. No classification of all matrix orbits, analytic trace,
strong naturalness or literature novelty is claimed.

The [card](candidate-card.md) fixes K=product Z_p, the finite arithmetic
ring R=union N^-1 K, W=M2(R), X=M2(K), additive nu(X)=1, mu=nu|X,
Gamma=GL2(R), U=GL2(K), ALL actual parameters (g,u), and gAu^-1.
The physical extension uses the REAL line ℝ, not the arithmetic ring R.
No rank stratum, null matrix, action kernel or incoming is removed.
There is no classical symplectic/contact object, roof or quantum owner.

The exact symbolic lineage interface is A_n=diag(n,1):
diag(1/d,1) A_n is integral iff n/d belongs to K, equivalently d|n
for integers n,d>=1. The actual output is diag(n/d,1). Matrix changes
deform this interface, not preserve one preferred row. More generally the
readouts 1[lambda A in dK²] for all integral row lambda transform by
lambda->lambda V under left V in U; right units preserve the divisibility
of a row. Thus the prime/composite admissibility family is explicit, not
the false claim that full-matrix divisibility on diag(n,1) detects d|n.

## 2. Full action and every-Borel measure owner

R identifies with the restricted product of Q_p relative to Z_p: a common
integer denominator clears the finitely many nonintegral components and
conversely. Its topology makes K compact open. A matrix and its inverse
in M2(R) have integral entries simultaneously at all but finitely many p;
there they lie in GL2(Z_p). This proves the restricted-product description
of Gamma, with the frozen matrix-and-inverse topology.

Each L_(g,u):A->gAu^-1 is a continuous additive automorphism of W.
Its full domain in X is D=X intersect L^-1 X, a compact-open additive
subgroup. All incoming to B are precisely g^-1Bu in X, for ALL parameters.
The displayed composition and inverse follow by multiplication; restricting
the full action to X gives the frozen groupoid. No etaleness is inferred.

Let |a|_f=product_p p^-v_p(a_p) for a in R^times. This is a finite product.
For a local matrix g_p, integral unit row/column operations preserve local
Haar, and reduction of a 2 by 2 invertible matrix over Q_p to diag(p^r,p^s)
by such operations shows that its vector Haar multiplier is p^(-r-s).
For completeness, take an entry of least valuation, swap it to the first
pivot, clear its row/column by integral elementary operations, and absorb
unit factors; the remaining pivot is nonzero. This gives the asserted form
without a chosen orbit quotient. Two independent matrix columns square
that multiplier. Right multiplication by u^-1 preserves X and its normalized
Haar. All but finitely many local multipliers are one. Therefore

```text
J(g,u)=nu(g X u^-1)=|det g|_f^2,
mu(L_(g,u) E)=J(g,u) mu(E), for EVERY Borel E subset D,
c(g,u)=-log J(g,u)=2 sum_p v_p(det g_p) log p.          (1)
```

The every-Borel assertion follows from uniqueness of additive Haar under
the automorphism (or normalized Haar on compact-open lattices), not only
from testing cylinder counts. J is positive finite and multiplicative;
c is a continuous homomorphism of parameters and hence an actual groupoid
cocycle. Its frozen all-point version applies even at zero/singular matrices;
measure-a.e. uniqueness alone would not have specified those values.

The full arrow kernel is exactly v_p(det g_p)=0 for every p, by unique
factorization of a positive rational. This includes many nonidentity arrows.
The globally ineffective action parameters are exactly (aI,aI), a in K^times:
testing A=I gives g=u, and commuting with matrix units forces a scalar;
invertibility in U makes a a unit. They remain actual arrows.

## 3. Full stabilizers, phases and every idempotent

For ANY f in X, its entire stabilizer is g f=f u, and its complete source
orbit is O_f={g f u^-1 in X: (g,u) in Gamma times U}. These formulas include
all incoming, including arbitrary chains, since chains compose in the same
group. On the extension, if B=g f u^-1, its phase relative to f is
h-c(g,u) modulo H_f=c(Stab f). Two choices differ by the whole stabilizer;
extension isotropy is exactly ker(c|Stab f). Conjugation preserves H_f.
Thus incoming cannot create a smaller hidden primitive or merge source orbits.
All height classes in one source orbit form one physical translation orbit.

At 0 the stabilizer is the whole Gamma times U and H_0=2 log(Q_+^times).
At I the stabilizer is exactly (u,u), u in U; H_I=0, with this full zero-time
isotropy retained. To describe every other tested core, an idempotent e has
components 0 or 1, since each Q_p is a field. Write S={p:e_p=0}.

For A_e=diag(e,1), the ENTIRE local stabilizer has g_p=u_p if p notin S.
At p in S write E=diag(0,1). The equation g_p E=E u_p is exactly

```text
g_p = [[a,0],[b,d]],  a in Q_p^times, b in Q_p, d in Z_p^times;
u_p = [[r,s],[0,d]],  r in Z_p^times, s in Z_p.         (2)
```

These local pairs, subject ONLY to g in Gamma and u in U globally, are the
full stabilizer; nothing is selected or quotiented. In particular det g_p
has arbitrary integer valuation at p in S and valuation zero outside S.
Each finitely supported assignment is attained by diagonal g, u=I.
For B_e=diag(e,e), at p outside S again g_p=u_p; at p in S both g_p and
u_p are arbitrary in GL2(Q_p), GL2(Z_p) respectively. Consequently BOTH have

```text
H_(A_e)=H_(B_e)=2 {sum_(p in S) k_p log p: k_p in Z, finite support}. (3)
```

Their full clock kernels are the displayed stabilizers with every determinant
valuation zero. If S is empty, both cores equal I, counted ONCE. If S={p},
H=2 log p Z and the least positive time is 2 log p, repetitions k times it.
If S has at least two primes, H has no least positive element: irrationality
of log p/log q follows from unique factorization; the pigeonhole argument
on fractional parts of its first N multiples gives nonzero group elements
of arbitrarily small absolute value. Thus this is not a primitive circle.
This handles infinite S too; only finite-support sums are attainable, not
arbitrary convergent sums or all of ℝ. At 0 use the same reasoning on all primes.

Invertible left and right actions preserve rank over EACH Q_p. For nonempty
S, A_e and B_e differ in rank at every p in S, so NO actual arrow, incoming
chain or height translation identifies them. Different S also have different
rank profiles within either family. Coincident parametrizations such as
B_0=0 or A_1=B_1=I are not extra packets. For S={p}, however, the two distinct
cores give at least TWO primitive packets at the SAME time 2 log p.
These are null-stratum witnesses retained by contract. The conclusion is a
lower bound, not an exact census of all packets. In the frozen units 2 log p
is log(p²); even rescaling all time by one half retains the multiplicity.

## 4. Three own controls

UNIT-ONLY. Both parameters are integral units. Their additive automorphisms
preserve X and its Haar; J=1 on every Borel set, c=0. Its full stabilizers
are g f=f u with g,u in U (in (2), g must additionally be integral unit).
Full orbits and phases use this restricted parameter group, not Gamma.
H=0 everywhere; the whole source isotropy is extension isotropy and every
arrow is in the clock kernel. No positive primitive is available.

ONE-COLUMN. The actual vector automorphism v->g v a^-1 has Haar multiplier
J_1=|det g|_f, since scalar a in K^times is a unit. This is one column, NOT
the matrix square. Its full domains/incoming are the frozen ones, and the
same Haar argument proves the EVERY-Borel law. For every vector v, its
entire stabilizer is g_p v_p=a_p v_p at each p, with the restricted-product
condition on g and a in K^times. Where v_p is nonzero, choose a Q_p basis
with first vector v_p: g_p is [[a_p,b],[0,d]], b arbitrary, d nonzero.
Where v_p=0, g_p is unrestricted. This is a description of all parameters,
not a quotient of vectors by chosen bases. Fixing every other local parameter
to I and a=1, the free second direction realizes any determinant valuation
at ANY p, even for nonzero v_p. Thus H_v=log(Q_+^times) for EVERY vector.
There is no least positive time. Its entire kernel is det valuations zero
inside that stabilizer; orbits/phase are {g v a^-1 in X_1}, h-c_1 modulo H_v.
Globally ineffective pairs are (aI,a); they remain, with the other kernels.

CENTRAL-INDEX. The actual matrices g=aV form a subgroup: scalars commute
and inverses have the same form. A different factorization changes a by an
element of K^times, so its valuations are well defined without adding labels.
On TWO-column matrices its OWN Haar IMAGE is |a|_f^4 and c=4 sum v_p(a)log p.
All domains/incoming and every-Borel laws hold as above for this subgroup.
At 0, H=4 log(Q_+^times); at I, g=u and H=0. For A_e, outside S g=u;
inside S equation (2) with g=aV forces V_12=0, V_11,V_22 units and
a_p V_22=d a unit. Hence v_p(a)=0 there too, so H_(A_e)=0 for EVERY e.
For B_e there is no restriction at S, and g=u elsewhere forces a unit there.
Its ENTIRE H is 4 sum_(p in S) Z log p, finite support. These statements
use the whole local stabilizers (2), or arbitrary pairs at zero components,
intersected with the actual central-index subgroup. The kernel is precisely
their zero scalar-valuation subset; phases and incoming use this own subgroup.
At singleton S the B core has least 4 log p; at larger S no least; at empty S
zero time. Rank still prevents merging. None of these clocks substitutes for (1).

## 5. Decision, reproducibility and limits

T0 full carrier/action and T1 measure-origin clock are established; the
same-object ledger is intact. T2 fails the one-prime/one-packet target already
on the paired full diagnostic. Portfolio **STOP / FORK**, without deleting
singular states, selecting normal forms or changing time units. Strong
naturalness remains OPEN; no formal Route coordinate is evaluated.

Proof inputs are the clarified118-line [card](candidate-card.md), SHA256
67cbafaf771cbc6ae3849d21f8a13165ea9eb24863a98ded81fa49a66d0ab2f4.
Methods are exact Haar uniqueness, local elementary matrix reduction, source
stabilizers and unique factorization; no numerical cutoff or scientific code.
The declared full idempotent family, three controls and all inverse domains
were retained. Internal [scope review](evidence/scope-review.md),
[independent proof](evidence/independent-proof.md) and [analysis review](evidence/review.md)
are shared-history NOT_CALIBRATED, not external peer review or novelty evidence.

EOF — whole paired diagnostic; wrong multiplicity, not a normalization repair.
