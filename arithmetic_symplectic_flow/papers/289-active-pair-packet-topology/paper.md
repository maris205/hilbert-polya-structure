# Closed prime circles and non-Hausdorff limits in the active-pair owner

Audit ID: `ASFS-AUDIT-20260920-APT01`.
Candidate ID: `ANG-20260920-APR01` (unchanged 288).
Paper ID: `289-active-pair-packet-topology`. Date: 2026-09-20.
Status: `CLOSED PRIME-CIRCLE SUM; FULL QUOTIENT NON-HAUSDORFF — SCOPED ADVANCE / STOP`.
Result type: exact same-object topology and separation theorems.

## Abstract

For the complete active-pair profinite residue owner of 288, every
primitive prime packet is a closed embedded ordinary circle in its full
coarse real-extension quotient. The entire returning part is a closed
topological disjoint sum of these circles. This uses rootwise finiteness,
an open-quotient restriction argument and an explicit phase inverse; it
does not assume the ambient quotient is Hausdorff. Indeed the full
quotient is non-Hausdorff. Two actual three-step branch mergers, preceded
by long zero-digit inverse words, yield equivalent pairs with inequivalent
profinite limits. All nonreturning and terminal states are retained.
The result advances T2 topology but stops Hausdorff-ambient promotion.
Arithmetic naturalness and analytic ownership remain unresolved.

## 1. Frozen identity, source and limits

The [audit card](candidate-card.md) was frozen before these new claims,
with SHA-256

    bbed510affbe5f7a7ded025f7b1bb36e3a85ceba7dd9e0b437dda7375048e82d

It audits the unchanged [288 candidate](../288-active-pair-residue-flow/candidate-card.md)
and [288 proofs](../288-active-pair-residue-flow/paper.md), with respective
source hashes

    cb48100913138d23d66b89e91c0502e5920337cc0c9969f31d33d9cf441fdc78
    b20fa7e047eabcb036e95b60a6a2255f60bb11419ef9d588df7c5d86d86c78b8

No source, clock, topology or equivalence is replaced. The lineage is
proper-divisor prime/composite admissibility -> current second-order
integer feedback -> coupled full residue evolution. The exact witness
rule is internally evaluated, but its naturalness is not established
by a topological theorem. This is not a classical symplectic lift.

| Same-object item | Unchanged definition / owner |
|---|---|
| Source and measure | Y=coproduct_(a,b>=2) K², K=Z_hat, joint Haar mass one per root |
| Arithmetic witness | w(b)=#{d:1<d<b,d divides b}; no supplied prime table |
| Actual partial map | j=x mod b; c_pair=2b-a+w(b)+j; T=(b,c_pair,y,(x-j)/b+y), only if c_pair>=2 |
| Arrows | Full retained-lag partial-tail groupoid; only defined iterates, all terminal units |
| Clock | c_G=log D_alpha-log D_beta on actual beta-to-alpha branches |
| Real extension | M=Y x R; (w,t)->(z,t+c_G(g)); all phases retained |
| Coarse space | Q=M/G_c with quotient topology, without quotienting real translation |
| Classical / analytic fields | Classical base/roof/mapping torus NOT APPLICABLE; T3 NOT SUPPLIED / NOT PURSUED |

Here D_alpha is the product of the consumed second-root indices along
an actual finite prefix. The sign is inverse-prefix insertion. Its
joint Haar IMAGE law, continuous all-point version and full étale
owner are proved in 288, not reselected here from an a.e. version.

288 also proves: the only periodic states are z_p=(p,p,0,0); every
full basin B_p is a single source orbit with time group (log p)Z;
there is exactly one abstract packet per prime and no others. Each
B_p is finite at every root. A state initially at (a,b) can belong
to B_p only if p<=b, and its first-hit time is zero or at most b-1.
These are dependencies for this SAME candidate, not other-object credit.

## 2. Returning topology in the source

Set B=union_p B_p, retaining every finite preimage of every core.

**Lemma 1.** Each B_p and the whole B are closed and discrete in Y.

*Proof.* At any fixed root (a,b), only finitely many primes p<=b
can occur. Each contributes finitely many states by 288 Proposition 7.
Thus B meets that copy of K² in a finite set. A finite subset of
the Hausdorff profinite space K² is closed, and each of its points
can be isolated from the other finitely many by an open neighborhood.
Because the root copies form a topological disjoint union, the same
closedness and relative discreteness hold globally. The identical
argument applies to B_p. No common finite bound over ALL roots is
needed or asserted. QED.

Every B_p is saturated for G, and B is saturated as their union.
Consequently A_p=B_p x R and A=B x R are closed saturated subsets
of the complete extension-object space M. This is a statement about
subsets of the existing owner, not a replacement of that owner.

## 3. The full quotient versus a restricted quotient

Let pi:M->Q be the full quotient map, P_p=pi(A_p) and P=pi(A).

**Lemma 2.** pi is open. For any saturated subset C of M, its
restriction pi|C is an open quotient map onto pi(C) with the ACTUAL
subspace topology from Q.

*Proof.* Every extension bisection is a homeomorphism between open
subsets of M. The saturation of an open U is a union of their images
of open restrictions, hence open. Since pi^(-1)(pi(U)) is that
saturation, the quotient definition implies pi(U) is open in Q.

If O=C intersect U is relatively open in C, saturation of C gives

    pi(O)=pi(C) intersect pi(U).

Indeed an orbit meeting C lies wholly in C, so any representative
in U of an image point from pi(C) also lies in C. The displayed
identity proves relative openness. Restriction is continuous and
surjective, hence an open quotient onto this subspace. No ambient
Hausdorff hypothesis was used. QED.

Closedness now also follows directly: pi^(-1)(P_p)=A_p and
pi^(-1)(P)=A are closed, so P_p and P are closed in Q by the
definition of quotient topology.

## 4. Phase inverse and ordinary circle sum

For z in B_p choose its first actual prefix to z_p and let
S_z=log D_z be its inverse-insertion clock, with S_(z_p)=0.
Every other prefix to z_p extends this by fixed-core steps and
adds an integer multiple of log p. Thus the following phase is
independent of that choice:

    f_p(z,t)=[t-S_z] in R/(log p)Z.

**Theorem 3.** The canonical map

    kappa_p:R/(log p)Z -> P_p, [t] -> pi(z_p,t)

is a homeomorphism onto a CLOSED subspace of the full Q, for every
prime p. Moreover P is homeomorphic to the topological disjoint sum
of these ordinary circles. Real translation restricts to ordinary
circle translation, with least period log p and repetitions r log p.

*Proof.* B_p is discrete, so f_p is continuous on each open component
{z} x R and hence on all A_p. The prefix arrow sends
(z_p,t-S_z) to (z,t). Any two states in A_p are equivalent exactly
when these core phases differ by the complete isotropy clock
(log p)Z. Thus f_p is constant on extension orbits and separates
them. Lemma 2 implies it descends to a continuous bijection
P_p->R/(log p)Z.

Conversely t->pi(z_p,t) is continuous and invariant under adding
log p, hence descends continuously through the ordinary circle
quotient. The two maps are inverse by their formulas. This proves
embedding without the invalid compact-to-non-Hausdorff shortcut.
Closedness was proved in Section 3.

For the total returning part, B is discrete, so each B_p is open
in B. Apply the same phase construction to the disjoint sum of
the circles, defining it on each {z} x R in A. It is continuous,
orbit-constant and complete. Lemma 2 applied to A gives its continuous
inverse on P, while the sum of the kappa_p maps is continuous by
the disjoint-sum topology. This proves the claimed homeomorphism.
The phase formula intertwines real translation with addition of
the same real amount, proving the periods and repetitions. QED.

There is no accidental prime-circle accumulation inside P: its topology
is the ordinary disjoint-sum topology. This does not make Q Hausdorff.

Two explicit phase controls retain multiplicity correctly. For p=2,
the core phase is t modulo log 2. Its noncore predecessor
(3,2,1,0) maps to z_2 in one step and has S=log 2, so its phase
is the same t modulo log 2, not another primitive circle. In general
every (p+j,p,j,0), 0<=j<p, remains in the same P_p. A terminal
state has no nonzero source isotropy and is outside B, but remains
in Q; restricting a proof to A never deletes it from the owner.

## 5. Two actual mergers with fixed clock difference

We now test the entire Q rather than infer its separation from P.
Only the existing main owner is used, with p=3. Put

    L=[[-3,3],[1,0]],
    v_A=(-2,1), v_B=(20,-5).

The following two exact paths start at root (3,3), merge after three
steps at the SAME full state (7,10,0,0), and use all indicated digits:

| Path | Full states in order | Digits | Consumed-index product |
|---|---|---|---|
| A | (3,3,-2,1) -> (3,4,1,0) -> (4,7,0,0) -> (7,10,0,0) | 1,1,0 | 3*4*7=84 |
| B | (3,3,20,-5) -> (3,5,-5,1) -> (5,7,1,0) -> (7,10,0,0) | 2,0,1 | 3*5*7=105 |

All divisions and residues are ordinary exact integer operations:
w(3)=w(5)=w(7)=0 and w(4)=1. In particular negative seeds use
canonical residues: -2 mod 3=1 and -5 mod 5=0. All next roots
are at least 2. This table verifies a fixed proof device; it is
not a finite sample standing in for a global dynamical theorem.

The matrix L is precisely the zero-digit inverse branch at root
(3,3), defined on the entire terminal K². For every N>=0, the
states z_(A,N)=(3,3,L^N v_A) and z_(B,N)=(3,3,L^N v_B)
have N actual zero-digit steps followed by these respective paths.
They therefore have a common full tail, with prefix products
3^N*84 and 3^N*105. The beta-to-alpha clock is exactly

    c_*=log(84/105)=log(4/5), independently of N.

Thus (z_(A,N),c_*) and (z_(B,N),0) are equivalent in M for EVERY N.
Their clock need not be positive: general arrows are not primitive
periods, and the actual signed cocycle is retained.

## 6. Complete profinite limits are inequivalent

Let e in K have 3-adic component zero and all other prime-adic
components one. This is an existing point of the full source, not
an extra arithmetic selector in the evolution.

**Lemma 4.** For N=k!, L^N converges to e I in M_2(K).

*Proof.* Direct multiplication gives

    L²=3*[[4,-3],[-1,1]].

Therefore L^(2r) is divisible entrywise by 3^r, and L^N tends
to zero at every 3-power modulus. For a prime ell different from
3, det L=-3 is a unit modulo ell^a. Hence L is an element of
the finite group GL_2(Z/ell^a Z). Its order divides k! for all
sufficiently large k, giving L^(k!)=I modulo ell^a. Combining
the finitely many prime powers of any fixed modulus by CRT proves
convergence at EVERY finite modulus, not just selected coordinates.
QED.

The two equivalent sequences in Section 5 thus converge in M to

    m_A=((3,3,e v_A),c_*),
    m_B=((3,3,e v_B),0).

**Lemma 5.** The underlying source states (3,3,e v_A) and
(3,3,e v_B) are not G-equivalent.

*Proof.* Their two seed coordinates have zero 3-adic component.
This property is preserved under (x,y)->(y,x/3+y); exact division
by 3 exists in K on these states. Thus every digit is zero and
every future root is (3,3). All future iterates are defined.

On these seeds use the polynomial

    F(x,y)=x²+3xy-3y².

At prime 5 the divisor 3 is a unit. Direct substitution in the
forward seed map gives F(y,x/3+y)=-F(x,y)/3. The 5-adic valuation
of its nonzero value is therefore preserved at every iterate.
Because e has 5-adic component one, the two initial values there
are respectively

    F(-2,1)=-5, with valuation 1;
    F(20,-5)=25, with valuation 2.

No iterate of one source can equal any iterate of the other.
There is consequently no common full tail and no G arrow between
them, regardless of lag or real phase. They are also nonreturning:
neither nonzero valuation-bearing trajectory can reach a zero core.
QED.

**Theorem 6.** The full quotient Q is non-Hausdorff.

*Proof.* For N=k! the two sequences from Section 5 have the SAME
image in Q. Continuity of pi gives limits pi(m_A) and pi(m_B),
which are distinct by Lemma 5. A sequence in a Hausdorff space
cannot have two different limits: disjoint neighborhoods of the
limits would both contain every sufficiently late term. Hence Q
is not Hausdorff. Equivalently, the full orbit relation on M is
not closed. QED.

No prime-circle or returning seed was used to manufacture this
nonseparation. The initial finite paths already leave the zero-difference
root sector, while their limiting states stay forever in it without
returning. All these actual states remain part of the owner. The
result does not classify every orbit closure or the global T1 property.

## 7. Controls, significance and next decision

The positive controls check p=2, a genuine transient preimage, the
full clock sign and the subspace topology rather than a reduced quotient
alone. The negative control is an exact two-merger construction with
constant signed clock difference and an all-moduli limit. Its limiting
inequivalence is separately established by a conserved 5-adic valuation.
Neither finite numerical precision nor prime cutoffs occur.

The [author-side naturalness check](evidence/naturalness-check.md) keeps
two facts distinct: the witness is internally evaluated and the clock
is genuinely owned, but the current prime selection proof uses witness
nonnegativity and its zero set. The existing OFF/ON/SHIFTED controls
leave a generic integer-index clock in place while changing accepted
roots. Thus topology alone does not establish a deeper arithmetic
composition law linking admissibility, primitivity and index products.
This is a scope limitation, not a refutation of the engineered owner.

| Obligation | Result for unchanged APR01 | Boundary |
|---|---|---|
| T0 and scoped T1 | Prior 288 owner retained | Witness/completion/measure naturalness OPEN |
| T2 counts and repetitions | Unchanged, exactly one prime packet | No representative selection |
| T2 packet topology | Closed embedded ordinary circles; closed circle-sum returning part | Proved in FULL quotient |
| Full ambient separation | NON-HAUSDORFF | Stop Hausdorff/classical-ambient promotion |
| Other orbit closures / global T1 | NOT CLASSIFIED | Not needed for the stated negative result |
| T3 operator / trace / zeta / determinant | NOT SUPPLIED / NOT PURSUED | No analytic result inferred from circle topology |
| Classical A0/A1/A2 / formal Route / B | NOT APPLICABLE / UNASSIGNED / NOT INVOKED | No Route passage or symplectic lift |

Portfolio: **scoped advance / stop**. Preserve the positive full-circle
result and stop Hausdorff-ambient promotion of this unchanged object.
Continue architectural breadth using the source-composition admission
question recorded in the naturalness check. Do not delete the adverse
states, change the clock or attach a borrowed determinant. A new
architecture requires a new frozen card; any same-object analytic
proposal needs its own explicit contract. Neither is created here.

## Evidence and disclosure

The [claim ledger](claim-ledger.md), [evidence](evidence/README.md) and
[internal adverse review](evidence/independent-review.md) distinguish
new topology proofs, prior same-candidate dependencies and open scope.
The methods are exact residue algebra, finite-group orders, CRT,
quotient topology and explicit phase maps. No scientific numerical run,
new operator, external novelty claim, PDF/LaTeX or publication occurred.
ARS structured the freeze and three adverse checkpoints. AI-assisted
same-model/shared-context review is not external peer review, formal
verification or an independent-error guarantee. Old packages and source
mirrors remain unchanged; 241/242 paused; programme goal active.
