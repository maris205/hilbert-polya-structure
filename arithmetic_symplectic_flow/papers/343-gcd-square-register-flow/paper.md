# An owned gcd clock produces composite primitives, not just prime repetitions

Candidate: `ANG-20260920-GSR01`. Package: `343-gcd-square-register-flow`.
Status: `OWNED GCD CLOCK; COMPOSITE PRIMITIVES — STOP / FORK`.
Date: 2026-09-20. Broadened arithmetic groupoid audit; no formal Route coordinate.

## 1. Question and exact same-object boundary

Can an actual gcd redistribution of integer registers induce a useful primitive
clock through its own geometric measure transport? The [frozen card](candidate-card.md)
defines all positive ordered triples with a whole real plane, the autonomous
register/plane map, its proposed inverse branches and retained-lag groupoid. We establish
that owner and its clock. However, EVERY integer n>=2 produces two
distinct primitive packets of least time log n. In particular the n=4
packet is not the second traversal of an n=2 packet. The bounded
product-eight sector supplies four distinct least-log2 packets, with all incoming states retained.

These are exact algebraic statements, not numerical observations or a global periodic
census. The clock is derived from the frozen inverse IMAGE determinant, never
inserted as a log-prime roof. Positive ownership does not establish strong naturalness.

| Frozen component | Actual owner / scope |
| --- | --- |
| Carrier and measure | ALL Y=N_(>=1)^3 x R²; counting triples times plane Lebesgue measure |
| Arithmetic step | g=gcd(a,b), R(a,b,c)=(b/g,c*g²,a/g) |
| Plane step | Phi_g(x,y)=(y,y²-g*x), on the whole real plane |
| Source map | T(r,q)=(Rr,Phi_(g(r)) q), total but not asserted bijective |
| Arrows | Actual triples (z,m-k,w) with T^m z=T^k w; all lags and predecessors |
| Clock / extension | Inverse IMAGE, its additive character, and ALL Y x R_h |
| Primitive identity | Actual source/height equivalence and time phase, not product or equal length |
| Classical fields | NOT APPLICABLE: no symplectic base, positive roof or physical Hamiltonian flow |

The lineage is the proper-divisor symbol (n,d) -> register input (n,d,1)
-> current gcd redistribution -> subsequent registers driving a quadratic plane map.
For a proper divisor d|n the actual update is (1,d²,n/d). This
is an exact symbolic-source deformation, not a Logistic/Henon conjugacy or conservative
lift. The square redistribution, quadratic geometry and measure are declared designs.
Geometry does not feed back into gcd selection. No prime table, per-prime
choice, zero data, von Mangoldt weight or external trace is supplied.

## 2. Complete inverse, groupoid and all-point IMAGE

Suppose R(a,b,c)=(A,B,C) and g=gcd(a,b). Necessarily a=gC,
b=gA, c=B/g², with g²|B and gcd(A,C)=1. Conversely those
conditions give gcd(gC,gA)=g and reproduce the target exactly. The complete
inverse family is consequently

    I_g(A,B,C,u,v)=(gC,gA,B/g²,(u²-v)/g,u),
    g>=1, g²|B, gcd(A,C)=1.

Distinct g give distinct register predecessors. This is finite at every target;
there is no inverse when gcd(A,C)>1. Each listed branch covers the
ENTIRE target plane. In particular a no-incoming state still has its actual
outgoing T step. Units, origins, signed coordinates and every inverse remain.

Direct multiplication proves P(a,b,c)=abc is conserved by R and every
actual inverse. Each integer-product sector is thus saturated under the full groupoid,
not merely forward invariant. It contains finitely many register triples, but still
the full planes; it is not the carrier substituted for Y.

The plane map Phi_g is a global polynomial diffeomorphism with determinant g.
Its displayed inverse has absolute determinant 1/g at EVERY real target,
including the origin and every null set. Counting-component weights do not change.
The finite-dimensional change-of-variables theorem, summed over the countable target components,
therefore gives for EVERY Borel E in the branch domain

    mu(I_g E)=integral_E (1/g) dmu, J_g=1/g, kappa=log g.

No a.e. representative or infinite determinant is needed. Compositions multiply their
actual Jacobians, so for T^m z=T^k w the branch-pair map from
w to z has IMAGE Jacobian exp(-c_G), where

    c_G=sum_(i<m) log g(T^i z)-sum_(i<k) log g(T^i w).

Here g(T^i z) means the gcd of that state's first two registers.
Two presentations of the same lag differ by increasing both iteration indices;
the additional sums are evaluated on the same common future and cancel.
Thus c_G is presentation independent. Refining composable arrows to a common
future proves addition of lags and characters; reversing endpoints negates both.

There is also a direct topology check, not an assumed germ completion.
Fix the source-register triple, target-register triple and lag. If any iteration
indices make their register futures coincide, the corresponding plane map is a
global diffeomorphism between those two planes. All other matching indices with
that lag give the same map, by cancellation of the common future
plane diffeomorphism. Therefore each nonempty discrete-label slice of G is ONE
global plane graph. G is a countable disjoint union of these graphs
in the inherited topology. It is Hausdorff, locally compact, second countable
and etale, with Borel/continuous groupoid operations. Distinct lags remain distinct arrows.
This says nothing by itself about Hausdorffness of the coarse orbit quotient.

The extension arrows are (w,h)->(z,h+c_G). Translation of h commutes
with all of them, hence gives the frozen set-level time action. Its
return subgroup at a source state is exactly c_G(G_z^z). Extension
isotropy is instead the kernel of that character; we keep both quantities.
No alternative density, roof, physical runtime or selected source core intervenes.

## 3. All global fixed states, entire isotropy and incoming packets

First solve Tz=z on the ENTIRE carrier. Register fixation gives b=ag
and c=a/g. Since gcd(a,ag)=a, one must have g=a, c=1
and b=a². Thus its full register list is r_n=(n,n²,1), n>=1.
On that component the fixed-plane equations are x=y and x²=(n+1)x.
There are exactly two roots:

    z_(n,0)=(n,n²,1,0,0),
    z_(n,1)=(n,n²,1,n+1,n+1), for EVERY integer n>=1.

Every integer in this family is admitted by the same original rule.
It is not a prime-labelled family of individually chosen maps.

At either fixed state every lag ell in Z is realized, and
every presentation has c_G=ell log n. Consequently the ENTIRE source isotropy
and character are

    G_z^z=Z, H_z=(log n) Z,
    ker(c_G|G_z^z)={0} for n>=2, and Z for n=1.

For n>=2 the least positive time is log n, not just an
exhibited return. The n=1 states instead have H={0}, despite nontrivial
zero-character isotropy. Their quotient-time orbits are lines, not primitive circles.

We specify ALL finite incoming states, not just the displayed centres. Let
B_n be the set of register triples r with product n³ whose
forward R sequence reaches r_n. For r in B_n let h_r
be its first hitting time and let Psi_r be the actual composition
of plane maps along these h_r steps (identity if h_r=0). Write
A_r=sum_(i<h_r) log g(R^i r), and q_(n,epsilon) for the fixed
plane point above. The full source orbit of z_(n,epsilon) is exactly

    O_(n,epsilon)={(r,Psi_r^(-1) q_(n,epsilon)):r in B_n}.

Necessity follows from T^m z=T^k z_(n,epsilon)=z_(n,epsilon); sufficiency
is the actual forward arrow after h_r steps. Each register contributes
exactly one plane point by invertibility. There are no outside-product ancestors.
This is a finite, reconstructible full-orbit description: if M_n is the
number of triples with product n³, a first hit has h_r<M_n,
since an earlier repeated register would already lie on a cycle not
first reaching r_n later. In particular M_n<=n^6 gives a finite
explicit bound. No numerical cutoff or unverified eventual-hitting assumption is used.

Every state in this full incoming orbit has source isotropy Z and
character ell->ell log n: presentations can be refined beyond its first hit.
For n>=2 the complete extension quotient over this orbit is parametrized by

    theta(r,q,h)=h-A_r modulo log n.

An arrow w->z has character A_z-A_w plus an integer multiple of
log n, so theta is invariant. Conversely every equality of these phases
is realized by an actual lag arrow, choosing sufficiently long common futures.
This proves the quotient is a single circle R/(log n)Z, with
the original translation time. Since the source orbit is finite and discrete,
this restricted quotient has its usual circle topology. It does not assert
global coarse-quotient separation. Repetition r log n is traversal of this
SAME circle, not selection of another fixed state or register product.

Different n have different conserved products n³ and cannot share an arrow.
At a fixed n the two roots remain distinct under every forward
iterate; their entire incoming source orbits are disjoint as well. Thus there
are at least TWO distinct primitive packets of least log n for
every n>=2. This is an exact lower bound on multiplicity, not
a claim that the displayed family exhausts all packets at that length.

## 4. Complete fixed and two-step gate in the product-eight sector

All ten positive register triples with product8 and their complete predecessor
lists are below. The lists follow the exact global inverse formula, so
they exclude no outside incoming point. A row's actual plane transport remains
Phi_g; the table does not replace it by a symbolic unit step.

| Register | Name | g | Successor | ALL predecessor registers |
| --- | --- | --- | --- | --- |
| (2,4,1) | C | 2 | C | C, C1 |
| (1,2,4) | C1 | 1 | C | C2 |
| (4,1,2) | C2 | 1 | C1 | none |
| (4,2,1) | A | 2 | B | B |
| (1,4,2) | B | 1 | A | A, D |
| (2,1,4) | D | 1 | B | none |
| (8,1,1) | Z0 | 1 | Z1 | Z2 |
| (1,1,8) | Z1 | 1 | Z2 | Z0 |
| (1,8,1) | Z2 | 1 | Z0 | Z1, E |
| (2,2,2) | E | 2 | Z2 | none |

A full fixed state must lie over C; its two plane roots are
(0,0) and (3,3). For a two-step return over C the equations
are y²=3x and x²=3y. They force x,y>=0, and give
only the same two fixed roots. Thus no distinct C two-cycle is missed.

Over A, Phi_1 composed with Phi_2 must fix (x,y). Its exact
equations are y²=3x and x²=2y. Hence either x=y=0 or
x=alpha=positive cuberoot(12), y=beta=alpha²/2. These exhaust all real roots:
substitution yields x(x³-12)=0, and the nonnegative constraints exclude no valid
additional root. The corresponding B phase is (y,x). The source least
period is2 even at plane zero because the register alternates A and B.

No other register in the table is fixed by R or R².
We have therefore solved ALL full-source fixed and two-step returns in this
sector. Their ENTIRE incoming source orbits, including the nonperiodic ancestors, are:

| Primitive packet | Every source object, written register:plane | Entire isotropy / character / kernel |
| --- | --- | --- |
| C-zero | C:(0,0), C1:(0,0), C2:(0,0) | Z; ell->ell log2; kernel0 |
| C-positive | C:(3,3), C1:(6,3), C2:(33,6) | Z; ell->ell log2; kernel0 |
| AB-zero | A:(0,0), B:(0,0), D:(0,0) | 2Z; ell->(ell/2)log2; kernel0 |
| AB-positive | A:(alpha,beta), B:(beta,alpha), D:(2alpha,beta) | 2Z; ell->(ell/2)log2; kernel0 |

The predecessor coordinates follow Phi_1^(-1)(u,v)=(u²-v,u); for example
beta²=3alpha gives D's first coordinate2alpha. The register predecessor lists
close each displayed source orbit, so no transient basin or unused real
coordinate has been silently removed. At an AB ancestor, equal future states
have even lag and every even lag is achieved beyond the first
hit; a full two-step circuit has gcd product2. These facts give
the entire character in the table, not merely its value on one loop.

All four packets have least time log2. Their extension/time quotients are
four distinct circles: different C versus AB futures cannot merge, and within
either register cycle the two plane solutions never coincide. Actual arrow
shifts on these four finite source orbits are integer multiples of log2,
so the phase can also be written simply h modulo log2.

The Z0/Z1/Z2/E component is retained on its entire planes. After
at most one step all its g-values are1, hence every isotropy
character is zero and H={0} throughout that component, whether or not
the plane is eventually periodic. At the origin the Z cycle has
source isotropy3Z and the whole group is its extension kernel. There
are also nonidentity zero-clock arrows between the different Z registers. The
E-to-Z2 arrow at the origin instead has clock -log2; zero isotropy
character must not be confused with a zero character on the entire groupoid.
Higher-period plane dynamics in the C/AB components remain unclassified and are
not needed for the decisive gate. No global census is inferred from this sector.

## 5. Primitive versus prime-power repetition: the decisive failure

The globally fixed n=2 states have least time log2. The globally
fixed n=4 states have least time log4=2 log2. Their products
are8 and64 respectively, so no actual arrow identifies their source packets,
even after including every predecessor and height shift. Since H_(n=4)=
(log4)Z, each n=4 packet is itself primitive. It cannot be
called the second traversal of either n=2 circle: that traversal stays
on its original product-eight packet and still has least time log2.

This is an exact composite-primitive obstruction to the frozen prime/primitive ledger.
Separately, the four least-log2 packets in Section4 already contradict one intrinsic
primitive for the prime2. Equal numerical lengths are not an allowed packet
quotient. Deleting the zero root, selecting a positive root, labelling packets
by their conserved product, or choosing one representative per prime changes the
object. Both zero and nonzero witnesses remain in the proof.

The positive part matters: actual current arithmetic evolves, the same inverse
Jacobian produces its clock, and real primitive circles exist. The proved
PROVES_TOO_MUCH statement is specifically that the uniform rule gives primitives for
ALL integers n>=2. It is not a claim that arbitrary prescribed
data can be encoded, nor an impossibility theorem for gcd dynamics generally.

## 6. Three separately owned controls

The full inverse/graph argument of Section2 applies after checking each control's
actual source rule. None borrows MAIN's missing branches or its determinant.

| Control | Complete inverse and own IMAGE | Entire clock conclusion |
| --- | --- | --- |
| GCD-OFF | Unique inverse (C,A,B,u²-v,u); all targets allowed; J=1 | kappa=0, c_G=0, every H_z={0}; all source isotropy retained as kernel |
| SQUARE-OFF | I_g=(gC,gA,B/g,(u²-v)/g,u), for g|B and gcd(A,C)=1; J=1/g | Own c_G=log P(z)-log P(w); every isotropy H_z={0}, despite possible nonzero arrow clocks |
| GEOMETRY-OFF | I_g=(gC,gA,B/g²,u,v), for g²|B and gcd(A,C)=1; J=1 | kappa=0, c_G=0, every H_z={0}; actual arithmetic cycles do not become time circles |

For SQUARE-OFF the source register product is P(Tz)=P(z)/g(z), not
MAIN's conserved product. Thus its own forward sums telescope to
log P(z)-log P(T^m z). At a common future this gives the
displayed coboundary, and every isotropy character is exactly zero. Its incoming
source trees are the stated own g|B branches and may cross product
sectors; MAIN's saturation or finite incoming tree is not transferred. A
strictly decreasing positive-integer product can occur only finitely often along one
forward trajectory, but this observation is not needed to assume periodicity.

For GCD-OFF all register triples are allowed targets, including noncoprime ones;
retaining MAIN's coprimality test would be wrong. For GEOMETRY-OFF the complete
register state stays on a finite product sector and is eventually periodic,
while the entire plane coordinate is fixed. Its source isotropy is therefore
a nonzero subgroup of Z at every source, but its clock image
is still zero. All three controls have complete own measure and groupoid
owners; no positive primitive time follows merely from a source cycle.

These results settle the controls' ENTIRE clock groups without an unjustified
global plane-cycle classification. Their zero-character kernels mean the full actual
source isotropy, not deletion of those arrows or replacement by identities.

## 7. Claims, gates and unresolved scope

| Item | Established / negative / open | Boundary |
| --- | --- | --- |
| T0 | ESTABLISHED full source, inverses, etale retained-lag owner and IMAGE | Broadened owner, not classical ASFS |
| T1 | ESTABLISHED exact evolving gcd interface and measure-derived clock | Strong arithmetic naturalness OPEN; square/map/measure designed |
| T2 positive | All global fixed states; actual primitive log n circles and full incoming law | Family not asserted to exhaust all primitive packets |
| T2 negative | Composite primitives; four distinct least-log2 packets in the bounded sector | Target prime/primitive ledger FAIL |
| T3 | NOT AUDITED | No transfer, zeta, trace, operator or quantum construction |
| Formal Route | UNASSIGNED; B NOT INVOKED | No inherited coordinate or readiness |

The entire same-object ledger remains intact. What remains unclassified includes
higher-period plane dynamics, the complete global primitive census and global coarse-
quotient topology. There is no claim that prime-length circles are absent:
they explicitly exist. Their coexistence with wrong primitives and excess packets
is exactly why existence alone is insufficient. No heuristic or scientific numeric
evidence is used here; all displayed conclusions follow from explicit algebra.

## 8. Portfolio decision and reproducibility

Portfolio: **STOP / FORK** for this frozen candidate. The decisive reason
is composite primitive identity, not a failure to own a clock or
to obtain a closed time orbit. Do not tune the quadratic map,
change the square transfer, discard roots or insert a packet quotient to
preserve this ID. A future architecture needs a genuinely different mechanism
distinguishing primitive arithmetic from repeated traversal before pursuing analytic operators.

Inputs are the original183-line card only. Methods are exact gcd/inverse
algebra, polynomial Jacobians and change of variables, common-future groupoid cancellation,
finite integer-product sectors, explicit fixed/two-step equations and full isotropy calculations.
The finite register bound in Section3 is a proved complete incoming bound,
not an empirical cutoff. No scientific computation, external theorem lookup, numerical
orbit search, fitted parameter, prime table or publication artifact was used.

See [claim ledger](claim-ledger.md), [evidence](evidence/README.md), [source record](evidence/scout-record.md)
and [internal review](evidence/independent-review.md). The two parallel Pre-P0 NONE
screens concern separately incomplete definitions, not proofs of this candidate's result.
ARS checks are inherited-model/shared-history NOT_CALIBRATED, not external peer review
or independent-error evidence. Earlier work and paused241/242 are preserved. The
programme goal remains active; no next full tuple is silently frozen.
