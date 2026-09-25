# FSQ01 — card-only independent derivation

Candidate: `ANG-AUDIT-20260923-FSQ01`; Paper424; session2026-09-23.
Owner: the frozen whole finite-symmetry quotient and its three full controls.
Finite-action stabilizers are S_x; physical real return subgroups are H_x.

## 1. Input, separation and method

- candidate-card.md original116-line prefix SHA256 e6b73345d61bf23df58f218fe2e45183b82685b34a1d66aae0c2a8b6e4c4e7f3.
- evidence/scope-review.md SHA256 55343dec6e6ec0790a277ef9bf667b33aa4ffd6c916d0387650297b41018a272 — 96 frozen lines.
- Root read CP1 completely and explicitly released this card-only stage.
  I reread precisely card1–116 and remeasured its prefix hash; no later
  outcome, author paper/README/ledger, peer answer or sibling result was read.
- Retained ARS/router/workflow/DA/runtime instructions and local scope apply.
  Earlier shared history and disclosed design expectations are exposure,
  not a blind preregistration or evidence for the conclusions. This is
  NOT_CALIBRATED, not human/external peer or cross-model verification.
  Effective served model identity/settings are not independently attested.
- Methods: geometric density chain rule, every-Borel identities, finite
  coset permutations and exact integer-iterate equations. No external source,
  scientific numerical program, auxiliary agent, Git/PDF or external action.
  My only write is this raw file; the card and CP1 are not edited by me.

## 2. All-point covariance and the actual quotient IMAGE owner

For a C1 diffeomorphism A write J_A for its positive continuous density
Jacobian. Local change of variables and a countable chart partition give
mu(AE)=integral_E J_A dmu for every Borel E, including infinite measure.
The chain and inverse laws are

    J_AB(x)=J_A(Bx)J_B(x),     J_(A^-1)(Ax)=1/J_A(x).           (1)

For each a in K, measure preservation gives J_a=1 almost everywhere.
It gives J_a=1 EVERYWHERE: a nonzero continuous difference from1 at a point
would persist on an open set of positive smooth-density measure, contradicting
the Borel measure identity. Thus commutation Fa=aF and (1) imply

    J_F(ax)=J_F(x),     kappa(ax)=kappa(x),     q(ax)=q(x),     (2)

where q=J_(F^-1). These are equalities of the fixed geometric versions,
including periodic null points, not permissions to change an RN version.

The quotient sigma-algebra is the full finite-orbit Borel quotient: E is
Borel in Y precisely when pi^-1 E is Borel in M. Its measure is exactly
nu(E)=mu(pi^-1 E), with no division by |K| or orbit size. The smooth density
is sigma-finite: use a countable relatively compact chart cover. Saturating
finite-measure cover sets under the finite measure-preserving group gives
invariant Borel sets of finite measure covering M. Their quotient images
are Borel and have finite nu measure, so nu is also sigma-finite.

Commutation makes barF(pi x)=pi(Fx) well-defined, and the descended F^-1
is its actual Borel inverse. For every Borel E in Y, saturation gives

    pi^-1(barF E)=F(pi^-1 E),
    pi^-1(barF^-1 E)=F^-1(pi^-1 E).                            (3)

Define barJ(pi x)=J_F(x) and barq(pi x)=q(x) using (2). These are Borel,
positive, finite, prescribed at every quotient point. Applying (3) and the
definition of pushforward integration gives the two complete IMAGE laws

    nu(barF E)=integral_E barJ dnu,
    nu(barF^-1 E)=integral_E barq dnu.                         (4)

Also barq(y)=1/barJ(barF^-1 y), so barkappa(pi x)=kappa(x) is exactly
log barJ=-log(barq composed with barF). No Jacobian on a singular quotient
stratum was assumed. Equations (2)–(4) descend the geometric all-point
version; the measure identity alone is not claimed to determine null values.
The whole carrier, fixed strata and complete pushforward measure remain.

## 3. Complete actual groupoids, kernels and height phases

For all k in Z let D_k(x)=log J_(F^k)(x). For k>=0 this is the actual
sum of kappa along k steps; D_0=0, D_(-k)(F^k x)=-D_k(x). The chain law is
D_(k+l)(x)=D_k(x)+D_l(F^k x). Each D_k is K-invariant, and
barD_k(pi x)=D_k(x) is the corresponding quotient iterate clock.

For either own bijection T, cancellation of invertible iterates in a meeting
T^m z=T^n w gives w=T^(m-n)z. Thus ALL arrows, with no path multiplicities,
are (z,k,T^k z), source T^k z and range z, and their clock is D^T_k(z).
Composition adds integer lags and the chain law adds clocks; inverse arrows
negate both. In particular forward motion z->Tz is the arrow (Tz,-1,z)
of clock -kappa_T(z). All negative iterates exist in these frozen owners.

The full kernels for either owner are exactly

    K_lag(T) = units,
    K_clock(T) = {(z,k,T^k z):D^T_k(z)=0},
    K_lag(T) intersect K_clock(T) = units.                    (5)

The clock kernel can contain nonunit arrows between aperiodic points; only
the equal-endpoint part is relevant to H. A point of least SOURCE period p
has full source isotropy pZ. If C=D^T_p(z), its clock on np is nC, hence

    H_z=CZ,     extension isotropy={np:nC=0}.                 (6)

For C!=0 the positive primitive is |C|, with all positive repetitions n|C|;
extension isotropy is zero. For C=0, H_z=0, source/extension isotropy pZ
is retained and there is no positive physical primitive. Aperiodic points
have trivial source and extension isotropy and H=0, regardless of arrow
clocks. Each full source orbit is T^Z z, including every inverse history.
If T^N z is periodic, applying T^-N to its return proves z was already
periodic. Thus no outside point enters a finite core in a finite time.

Every real height is retained. For a reference b in a source orbit and
z=T^n b, the arrow (b,n,z) is FROM z TO b and has clock D^T_n(b).
The entire extension-orbit phase is

    [h+D^T_n(b)] in R/H_b.                                   (7)

For an aperiodic orbit n is unique. For a period-p orbit changing n by mp
changes the value by mC, for every integer m. Conversely equality modulo H_b
supplies a reference isotropy arrow, so (7) is a complete invariant, not
just necessary. All values occur at (b,h). Height translation is addition
on R/H_b and its entire physical stabilizer is H_b. This is an orbitwise
SET description; no global Borel transversal or smooth orbit space is claimed.

The natural functor on actual arrows is

    Pi(x,k,F^k x)=(pi x,k,barF^k(pi x)).                      (8)

It is surjective and preserves clock and lag. Its fibres are exactly K-orbits
of arrows: choose a lift of the range, then its source is forced by F^k.
The object map on extensions is (x,h)->(pi x,h), with NO height rescaling;
K itself acts by (x,h)->(ax,h). This is compatible by (2). Preimages and
images of each of the kernels (5) agree under Pi. It does not follow that
isotropy at a CHOSEN lift surjects onto quotient isotropy. No extra finite
group arrow or stabilizer factor is inserted into the ordinary quotient G.

## 4. All periodic lifts, all group return elements, and exact multiplicity

Let y=pi x have least SOURCE period ell under barF. Fix

    S=S_x={a in K:ax=x},
    A_x={a in K:F^ell x=ax}.                                 (9)

A_x is nonempty by the quotient return. Choose any g in A_x, without
discarding the others. Commutation and invertibility give S_(F^n x)=S_x
for every integer n. Since S_(gx)=g S g^-1, it follows that g normalizes S.
Moreover

    A_x=gS=Sg,     gS in N_K(S)/S.                           (10)

Indeed ax=gx iff g^-1 a belongs to S. The relevant finite permutation order
is r=ord(gS), the least positive r with g^r in S, NOT necessarily ord(g).
Changing the chosen element of A_x leaves that coset, r and the subgroup
L=<S,g> unchanged. Here S is normal in L and |L|=r|S|.

Commutation yields F^(t ell)x=g^t x for all t in Z. Any upstairs return
must project to an ell-multiple downstairs, so

    upstairs least SOURCE period p=r ell.                   (11)

This also proves that a quotient-periodic point has only periodic lifts.
An upstairs periodic point plainly projects to a periodic point. Thus a
quotient orbit is aperiodic iff every one of its lifts is aperiodic.
There is no creation of periodicity from a nonperiodic lift in this finite class.

The FULL preimage of the ell-point quotient cycle is

    {a F^j x : a in K, 0<=j<ell}.                            (12)

Different j give disjoint fibres, and within one fibre a is labelled by
a left coset aS. F increments j; on wrapping j=ell-1 to0 it sends
aS to agS. Right multiplication by g is well-defined since g normalizes S.
Every orbit of that permutation has length r, because ag^tS=aS exactly
when g^t belongs to S. Consequently ALL upstairs cycles have length r ell,
and their exact number over this ONE quotient cycle is

    N=[K:S]/r=[K:L].                                        (13)

They are the cycles {aF^n x:n in Z}, indexed by left cosets aL.
L is exactly the K-setwise stabilizer of the chosen upstairs cycle: ax
belongs to that cycle iff ax=F^(t ell)x for some t, hence a in L.
This proves exhaustion and distinctness, not just a lower bound. For another
lift aF^j x, the finite stabilizer and monodromy data conjugate by a; r,
p and N remain the same. Ineffective group elements are already in every
S_x. Neither freeness, effectiveness nor a universal |K| shortening is used.

Let D be the signed clock sum on the quotient ell-cycle. By the owned
pointwise descent, D=D_ell(x). Each successive block of ell upstairs steps
has the same sum, since it starts at g^t x and the clock is K-invariant.
Every one of the N upstairs cycles therefore has signed sum C=rD, and

    source isotropy upstairs = r ell Z, downstairs = ell Z,
    H_up=(rD)Z,             H_down=DZ.                       (14)

These are the ENTIRE groups. Pi includes the upstairs source isotropy as
the indicated subgroup of downstairs isotropy, preserving the actual clock
on each existing lag. A downstairs lag-ell return lifts to an arrow from
gx to x; it is not an upstairs isotropy arrow unless g belongs to S.

If D!=0, there are N upstairs positive packets of primitive r|D| over the
single downstairs packet of primitive |D|. Extension isotropy is zero on
both owners. H_up is an index-r subgroup of H_down. All repetitions remain;
there is no deletion of a negative signed sum or merging by equal periods
alone. If D=0, both physical groups vanish and all N upstairs zero-clock
cycles and the downstairs zero-clock cycle remain, with ineffective source
isotropy r ell Z and ell Z respectively, and real phase lines on both sides.

Using references ax upstairs and y downstairs, the induced phase map is

    R/(rD Z) -> R/(D Z),     [u] -> [u].                     (15)

For D!=0 this has degree r on each of N circles. For D=0 each is an identity
map of real lines; these are not positive-period circles. The group element
g preserving the chosen upstairs source cycle acts on its phase by u->u+D,
as (gx,h)=(F^ell x,h) has phase h+D relative to x. Thus cycle shortening
comes from the actual group action and return structure, not division of
the local clock. The local clock is unchanged by the descent (4).

## 5. Nonperiodic quotient orbits and their complete preimages

Let y=pi x be aperiodic and S=S_x. Its full orbit is {barF^n y:n in Z},
with all these states distinct. Its full preimage is

    {aF^n x:a in K,n in Z}.                                 (16)

The quotient index n is unique. Within a fixed n the lifts are precisely
the cosets aS because S_(F^n x)=S. Two upstairs orbits indexed by aS,bS
could meet only if aF^n x=bF^m x. Projection forces n=m, then aS=bS.
Thus (16) splits into exactly [K:S] disjoint COMPLETE aperiodic upstairs
orbits, each {aF^n x:n in Z}; K permutes them transitively. None is omitted
by choosing a sheet or a sign, and none has nonzero source isotropy or H.

For z=aF^n x, use ax as its upstairs reference and y downstairs. Formula
(7) gives u=h+D_n(x) on both sides, since D_n(ax)=D_n(x). Each of the
[K:S] free real phase lines therefore maps identically to the one downstairs
line. All heights, kernels (5), inverse histories and aperiodic clock arrows
are retained. The finite S_x is not additional dynamical isotropy in either G.

## 6. Control A — actual duplicate copies

Put L0=log2. On M=R times {0,1}, the own inverse of F(x,j)=(2x,j) is
(x,j)->(x/2,j). Its all-point inverse density is1/2 and forward density2
for Lebesgue/counting measure, hence kappa=L0 at every point. K swaps
sheets, preserves that measure and commutes with F. Its stabilizer S_x is
trivial at EVERY state, including both origins. The full pushforward is
nu=2 Lebesgue on Y=R. Its own inverse y->y/2 has IMAGE density1/2 relative
to nu, including the descended value at0; barkappa=L0, with no extra factor.

The whole actual groupoids and clocks are

    G_up={((x,j),k,(2^k x,j)): k in Z},    c_up=kL0,
    G_down={(y,k,2^k y):k in Z},           c_down=kL0.          (17)

Lag, clock and joint kernels on BOTH owners consist of units, since L0!=0.
For any nonzero integer n, 2^n x=x forces x=0; this same test applies to B,C.
Upstairs only (0,0),(0,1) are periodic, each fixed, each source isotropy Z,
H=L0 Z and extension isotropy0. They are TWO distinct positive packets of
primitive log2 with repetitions n log2. Downstairs only0 is periodic, fixed,
with source Z, H=L0 Z, extension isotropy0 and ONE primitive log2 packet.
Here ell=1, S={e}, A_x={e}, r=1, N=2. No source-period shortening occurred.

For every nonzero x each sheet has its full aperiodic orbit {(2^n x,j):n in Z};
downstairs the corresponding full orbit is {2^n x:n in Z}. Source/extension
isotropy and H are zero. The entire preimage of each such quotient orbit
consists of exactly the two sheet orbits. Unique inverse histories remain;
no nonzero point enters an origin in finite time. For any starting object,
the complete extended orbit is {(F^n z,h-nL0):n in Z}, upstairs or downstairs.

Normalize a nonzero coordinate by n=floor(log_2|x|), u=2^(-n)x, with
1<=|u|<2. References (u,j) upstairs and u downstairs give real phase h+nL0.
At origins phase is h modulo L0. Both upstairs origin circles map identically
onto the downstairs circle through the ACTUAL sheet symmetry. All signs,
heights and aperiodic packets remain. Upstairs fails uniqueness at prime2;
downstairs meets the finite necessary benchmark but lacks all-prime coverage
and supplies no endogenous arithmetic. It is an EXTERNAL CONTROL only.

## 7. Control B — source-phase cycling, not a divided local clock

Now F(x,j)=(2x,j+1 mod2), with own inverse (x/2,j-1). Its real inverse
derivative1/2 and the sheet permutation give every-Borel IMAGE density1/2
for the full upstairs measure; kappa=L0. K is again the free sheet swap and
commutes with F. The full quotient is R with nu=2 Lebesgue, own inverse y/2,
all-point density1/2 and barkappa=L0. Both clocks were computed from their
own measures, not obtained by dividing one old cycle sum.

    G_up={((x,j),k,(2^k x,j+k mod2)):k in Z},   c_up=kL0,
    G_down={(y,k,2^k y):k in Z},               c_down=kL0.      (18)

All three kernels are units on both owners. A periodic upstairs point must
have x=0 and an even return lag. The two origin states form ONE least-SOURCE-
period-2 cycle, source isotropy2Z, H=2L0 Z and extension isotropy0. Its
physical primitive is2L0=log4, with every repetition n log4. The quotient
origin is fixed, source isotropy Z, H=L0 Z and extension isotropy0; its
primitive is log2, with every repetition n log2. The full preimage is that
single two-state core: ell=1, S={e}, A_x={sheet swap}, r=2 and N=1.

For x!=0 the full upstairs source orbit is {(2^n x,j+n mod2):n in Z}; it is
aperiodic with source/extension isotropy0 and H=0. To see ALL lifts of a
quotient nonzero orbit, write x=2^n u with 1<=|u|<2, and put epsilon=j-n
modulo2. References (u,epsilon), epsilon=0,1, label two distinct complete
upstairs orbits over the same quotient orbit, exchanged by K. Phase is h+nL0
on each real line and on the quotient real line. No fixed sheet is selected.
Full extended orbits are {(F^n z,h-nL0):n in Z} on either owner.

At the origin use upstairs reference (0,0): a state (0,j,h) has phase
h+jL0 modulo2L0. Downstairs its phase is h modulo L0. Thus the circle map
is exactly R/(2L0 Z)->R/(L0 Z), of degree2; the sheet swap acts by adding
L0 upstairs. This is an actual symmetry identification, with all heights
retained. All incoming to the finite cores already belongs to those cores.
Upstairs fails prime support at log4; downstairs meets the finite necessary
benchmark at prime2 only. Neither owner is an admitted arithmetic candidate.

## 8. Control C — whole nonfree reflection quotient, including0

Upstairs F(x)=2x has own inverse x/2, density1/2 at EVERY point, so kappa=L0.
Reflection a(x)=-x commutes and preserves Lebesgue measure. S_0=K=C2,
whereas S_x={e} for every x!=0. With pi(x)=|x|, the full quotient is
[0,infinity). For every Borel E there, pi^-1 E consists of its positive
and negative copies, with a possible common singleton0 of measure0.
Consequently nu(E)=2 Leb(E), including sets containing0. This is not a
free-action assumption and does not delete the null fixed stratum.

The own quotient inverse is y/2 on the WHOLE half-line. Its IMAGE identity
is nu(E/2)=(1/2)nu(E) for every Borel E. Its all-point prescribed density1/2
at0 comes from the already proved geometric descent, not from an arbitrary
RN assignment or a presumed differential Jacobian on a quotient singularity.
Thus barkappa=L0 everywhere and

    G_up={(x,k,2^k x):x in R,k in Z},       c_up=kL0,
    G_down={(y,k,2^k y):y>=0,k in Z},       c_down=kL0.         (19)

Again all lag/clock/joint kernels are units. Only0 is periodic on either
owner; it is fixed, has source isotropy Z, H=L0 Z, extension isotropy0,
physical primitive log2 and all repetitions. Here ell=1, S=K and A_x=K.
Either g=e or g=reflection represents the return, but gS is the identity
coset, so r=1 and N=1. The order2 of a possible representative g is NOT
the shortening factor. The finite stabilizer supplies no extra C2 isotropy
in the ordinary downstairs G and does not halve the physical primitive.

Each positive quotient aperiodic orbit {2^n y:n in Z} has exactly TWO full
upstairs preimages: its positive and negative dyadic orbits. Reflection
exchanges them; neither is periodic. All their source/extension isotropy
and H vanish. Normalize y=2^n u with 1<=u<2; choose references +u,-u
upstairs and u downstairs. The full real phase is h+nL0 in all cases.
At0 phase is h modulo L0 and the circle map is the identity. Every extended
orbit is {(T^n z,h-nL0):n in Z} for its own T. Unique inverse histories,
both signs upstairs, all half-line points downstairs and all heights remain;
no nonzero point enters0 in finite time. Both positive ledgers have one
prime2 packet, but no all-prime coverage or endogenous arithmetic mechanism.

## 9. Exact bounded implications and freeze hold

The class law distinguishes N merged source packets from r shortened source
cycles and from finite S_x; no one of these is universally |K|. Nonzero
cycle clocks survive as nonzero clocks, and zero clocks remain zero, because
C=rD. Positive nonemptiness is therefore preserved by these finite quotients.
Only K-related upstairs cycles project to the same quotient cycle; equality
of clock values alone supplies no such identification. A shows genuine
duplicate merging, B genuine shortening, C the nonfree fixed-point boundary.

If an upstairs positive primitive is log p for an ordinary prime and r>1,
its quotient primitive is (log p)/r, not log of any integer prime: otherwise
p=q^r. Conversely a composite prime power can shorten to a prime, as B
exhibits. These are conditional consequences, not universal quotient rescue
or no-go claims. The controls can meet the finite necessary target downstairs
without supplying a prime-symbolic source, all-prime coverage or naturalness.

Every inverse IMAGE version, full actual arrow set and kernel, finite return
coset, source/extension isotropy, entire H, nonperiodic preimage, incoming
history and real phase is accounted for. No point, null stratum, equal-period
packet or zero-clock cycle was discarded. The ordinary quotient was never
replaced by an orbifold/action-groupoid enhancement or by representative data.

Portfolio: CONDITIONAL FILTER; any arithmetic application needs its own
parent and the exact N,r,S_x ledger. Arithmetic T1 NOT PASSED; T2 conditional;
classical NOT APPLICABLE; T3 NOT AUDITED; formal Route UNASSIGNED; B NOT INVOKED.
No operator, RH, literature priority or external verification claim is made.
Freeze after complete readback, then HOLD for root's full read and separate
PAPER UNLOCK. Preserve CP1 and the scientific prefix. No425 is authorized.

EOF — card-only derivation; shared-history internal NOT_CALIBRATED.
