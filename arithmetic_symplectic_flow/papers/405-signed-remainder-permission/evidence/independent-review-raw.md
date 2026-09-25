# Original-card independent mathematics — SRP01

Candidate `ANG-20260923-SRP01`; package405.
Stage: explicitly released card-only raw, before PAPER UNLOCK.
Internal inherited-model/shared-history AI derivation: `NOT_CALIBRATED`.
No blindness, external peer review, cross-model or independent-error claim.

## 1. Inputs and actual access

- Original `candidate-card.md`1–96:5237 bytes, SHA256
  `d69d39a4115002b725175ca673e42e617a687abbe2eb53f2a6808b80ec1d0540`.
- Clarified full `candidate-card.md`1–101, read again through EOF after release:
  5517 bytes, SHA256 `02c8aa8e26bb30dc3ab9e85509db99062e615b578a40a2f30807aea303061b79`.
- Frozen `scope-review.md`:101 lines, SHA256
  `7c24348301e2a83bed9ac8eeb27274624f533c0aa39ae4b42fe48783439d20c8`.

CP1 identified the lineage integer-type omission; the pre-proof append resolved it.
Root reported reading the complete scope report and then explicitly released raw
mathematics. Only this clarified card supplied new scientific input. No manuscript,
README, ledger, author/peer result or other new scientific file was read.
The ARS router/workflow/DA/runtime and relevant logical-fallacy guidance were read
at CP1 and retained. Earlier shared context and disclosed scout expectations are
not erased. No auxiliary, web, scientific code/numerics, model change or Git action
was used. This proof does not transfer any earlier candidate's result.

## 2. Exact full inverses and images of all four owners

Let target=(u,v). MAIN and D share the target band

    E={u!=0, 0<=v-1/u<1}.

Set n=floor u. At a point of E, MAIN has exactly the predecessors
(u(v+q)-1,u) for all signed nonzero divisors q of n. D has the same formula
for EVERY q in Z, including0. In each case the reconstructed ratio is
q+(v-1/u); its floor is exactly q, and direct substitution gives the target.
Conversely the actual source equation gives that formula and band, so no inverse
is missing. Distinct q give distinct sources because u!=0. The n label is unique.

MAIN's entire image is E, since q=1 always divides n. Each target in E has
2*tau(|n|) predecessors when n!=0, and countably infinitely many when n=0.
Here tau is the number of positive divisors, used only to describe a finite count;
no divisor table or cutoff is input. D has countably infinitely many predecessors
at every point of E. Outside E neither owner has a predecessor.

R instead has entire image E_R={u!=0,0<=v<1}, with exact predecessors
(u(v+q),u) for all signed nonzero q dividing floor u. The same source-floor and
forward checks hold with residual v. Its counts are the same divisor counts as
MAIN on E_R, including the infinite case floor u=0.

Q has at most one predecessor, namely (uv-1,u). It exists precisely when

    u!=0, q=floor(v-1/u)!=0, n=floor u, q divides n.

This is its entire image and not MAIN's target band. Reconstructing x/y gives
v-1/u, and its own forward equation returns (u,v). Q is a partial bijection;
cell names do not supply additional inverse arrows.

These are Borel domains and Borel branches, with all signed floor cuts assigned
by the displayed half-open inequalities. No map replaces a signed variable by
its absolute value. The absolute value used later belongs only to the determinant.
The x+1=0 line remains subject to ordinary source permission, not an extra deletion.

No target with first coordinate0 has any predecessor in any owner. Terminals are
y=0 for D, and y=0 or q=0 or q not dividing n for MAIN/R/Q. These are states,
not absorbing loops. The image criteria apply even when a target is terminal.
For example the horizontal target(u,0) has MAIN/D incoming exactly for u<-1;
the sources are (uq-1,u) with the respective allowed q. R permits every u!=0,
with sources(uq,u) and its own divisor test. Q permits the unique source(-1,u)
exactly when its displayed target permission passes. All further incoming is
the complete inverse recursion below; no terminal forward step is added.

## 3. Every-Borel IMAGE and the prescribed full-point version

For MAIN/D the inverse derivative matrix is

    [ v+q   u ]
    [   1   0 ],

with determinant -u. R has the same derivative matrix; Q replaces v+q by v.
Consequently each OWN inverse density is J(u,v)=|u|, positive and finite at every
actual target, including integer cuts, residual endpoints and terminal targets.
The analytic extension is specified even on null boundaries; a.e. uniqueness of
a Radon–Nikodym derivative alone would not establish those values.

Fix any actual branch. For each u!=0 its first output coordinate is an affine
function of v of slope u, and its second output coordinate is u. One-dimensional
change of variables, coordinate interchange and Tonelli prove
mu(theta(E'))=integral_(E') |u| dmu for EVERY Borel subset E' of its full domain,
allowing infinite integrals and both signs of u. Thus this is not a cylinder-only
or whole-mass comparison. Countable branches do not turn this branchwise law
into global measure invariance of a many-to-one map.

At any legal source z=(x,y), all four owners therefore have their OWN derived
kappa(z)=-log|y|. This expression is evaluated only at y!=0. A zero next second
coordinate is allowed; one does not evaluate another step there. In particular
there is no log0, and terminal objects still have the empty sum S_0=0.

## 4. Actual histories, kernels, entire groups and phase conventions

For each owner, put T^i z=(x_i,y_i) along a valid finite history and define

    P_m(z)=product_(0<=i<m) |y_i|,   P_0=1,   S_m(z)=-log P_m(z).

The actual arrow (z,m-n,w), T^m z=T^n w, has
c=log(P_n(w)/P_m(z)). Its actual branch-pair IMAGE from w to z has density
P_m(z)/P_n(w). Repeated changes of variables prove this on every Borel history
domain; finite inverse branches are injective and all intermediate permissions
are retained. This matches c's negative-log IMAGE orientation.

Equal triples have witnesses differing by a common legal padding; their extra
factors agree and cancel. Composing two arrows aligns the middle valid histories
and cancels there. This never requires a forward step beyond a terminal, or
agreement of derivatives of different extensions on arbitrary null intersections.
It proves well-definedness/additivity for the actual integer-lag G, not a free-word
groupoid. G and c are Borel by the countable finite-history domains and equalities.

The full lag kernel is the set of actual(z,0,w) with equal-depth coalescence.
The full clock kernel is precisely the actual triples with P_m(z)=P_n(w).
The intersection imposes both tests. These tests cover ALL points and histories,
not merely the fixed/short-return window or the isotropy kernels.

An explicit full incoming enumeration for reference r is

    O_r={ I_p(T^n r): n any valid forward length, p any finite legal inverse word }.

All intermediate target tests in section2 are mandatory. The arrow from r to
z=I_p(T^n r) is(z,|p|-n,r); reverse arrows have opposite lag and clock.
This is countable, exhaustive, and untruncated, including zero histories.

For a deterministic partial map, source isotropy is dZ exactly at a source
eventually entering a least-d cycle, and is0 otherwise. An equality of distinct
valid iterates gives a cycle; on that eventual cycle precisely multiples of d
are possible. For that cycle put P_C=product_(i=0)^(d-1)|y_i|. Transients cancel:

    c(kd)=-k log P_C;   H=(-log P_C)Z.

If P_C!=1, H has positive primitive |log P_C| and extension isotropy0.
If P_C=1, H=0 and the ENTIRE source isotropy dZ survives in the extension.
Noneventually-periodic and terminal sources have both isotropy groups0 and H=0.
The lag kernel within source isotropy is always0; it is not the full arrow kernel.
This conditional ledger is exact without purporting to classify all higher cycles.

All X times R is retained. Height translation commutes with extension arrows,
so gives a complete real-time action on orbit SETS, without a topological upgrade.
For T^r z=T^n a, the phase relative to a is h+S_n(a)-S_r(z) modulo H_a.
Above one complete source orbit this gives every phase R/H_a. Its physical time
stabilizer is H_a; the sign on lag+d does not determine the positive generator.
Distinct actual cycles cannot merge under a common-future arrow, even at equal times.

## 5. ALL fixed states and their complete basins

A fixed state is(t,t) with t!=0, hence its actual quotient is1. The permission
1|floor t always holds. MAIN and D have next second coordinate1/t, so ALL their
fixed states are p_+=(1,1) and p_-=(-1,-1). R has next second coordinate0 and
has NO fixed state. Q instead requires t=1+1/t, giving exactly

    p_phi=(phi,phi), phi=(1+sqrt5)/2;
    p_psi=(psi,psi), psi=(1-sqrt5)/2=-1/phi.

Both Q roots pass their actual floors and permission. No terminal identity is
counted as a fixed step, and no sign or zero case has been dropped.

MAIN: p_+ has exactly the predecessors p_+ and(-1,1); p_- has exactly p_- and
(1,-1), because floor(target first)=+1 or-1 allows only q=+1,-1.
The two noncore predecessors have no predecessors: their residuals in E are2
and-2, respectively. Thus the COMPLETE basins/source orbits are

    B_+={(1,1),(-1,1)},   B_-={(-1,-1),(1,-1)}.

At every point of these basins, source isotropy is Z, H=0 and extension isotropy
is Z. All steps inside them have |y|=1, so c vanishes on their entire arrow
restrictions, and the complete phase is h in R. In particular zero clock does
not discard either the source isotropy or nonidentity arrows between the two states.
They are distinct zero-time core orbits, not positive primitive packets.

D has larger, explicitly exhaustive basins:

    B_+^D={(a,1):a in Z}
           union {(a*k-1,a): integers a>=2,k in Z};
    B_-^D={(a,-1):a in Z}.

Proof: inverse generations from either integer core remain integral. The direct
predecessors are exactly(a,1) or(a,-1), respectively. An integer target(a,1)
has incoming iff a>=1. At a=1 this gives the same first generation; at a>=2
the inverse formula gives(a*k-1,a). Such targets have integer second coordinate
at least2, so cannot satisfy E for ANY nonzero integer first coordinate; there
is no third new generation. Among targets(a,-1), only a=-1 satisfies E, giving
the existing first generation again. First-coordinate0 targets have no incoming.
Thus these formulae are whole basins, not just subsets. Every basin point has
source/extension isotropy Z and H=0. The relative phase is h on the first
generation, and h+log a on(a*k-1,a), since its first clock is-log a and the
next clock is0. These two basins cannot merge under the actual forward map.

Q is injective on its active domain; substituting either fixed root into its
single inverse returns that same root. Hence both COMPLETE fixed basins are
singletons. At p_phi the lag1 clock is-log phi; at p_psi it is+log phi.
Both have source isotropy Z, extension isotropy0, ENTIRE H=log phi Z, one
positive primitive packet each and every phase in R/(log phi Z). Their source
orbits do not merge. Since 1<phi<2, log phi is not the logarithm of any ordinary
integer prime. These are two genuine CONTROL packets, not a MAIN counterexample.
R has no fixed core requiring a basin ledger; all other R histories remain covered
by its own inverse recursion and conditional groups in section4.

## 6. Complete prescribed MAIN quotient-word window

Any legal two-step return must have T(x,y)=(y,x), with x and y both nonzero.
For prescribed quotients q_0=-1 and q_1=-2, clearing these nonzero denominators
in the two step equations yields

    x*y=x+1+y,     x*y=y+1+2*x.

Subtracting forces x=0 and then y=-1. This is NOT a legal solution: x=0
prevents the second step. At the proposed first state(0,-1), n=-1 but the
actual quotient is0, not-1, so MAIN forbids even the first step. Divisibility
of the prescribed label does not rescue its incorrect floor value.
The rotated word(-2,-1) similarly forces y=0,x=-1 and is already terminal
at the first step. These exhaust the real solutions of the multiplied equations;
neither survives the original divisions and source tests. No Jacobian or cycle
clock is assigned to these illegal words, and no log0 is evaluated.
Both actual points remain terminal source objects under their ordinary definitions.

Thus there is NO legal MAIN return in either prescribed word, and no phase
rotation to count twice. This is not a statement about other quotient words
or all two-step cycles, let alone higher periods.

## 7. Lineage, target and stop boundary

With the clarified integers N,d and real eta,rho in[0,1), the interface gives
floor y=N and floor(x/y)=d. MAIN permission is exactly d|N on that full family,
and its update is(y,rho+1/y). Thus divisibility governs existence of the same
step, with both next integers read from the new geometry; no extra integer root
or prime list is installed. This proves the stated interface, not naturalness.

All four inverse/IMAGE/actual-history owners pass these exact checks. MAIN's
entire fixed-state part has H=0, and its prescribed negative two-step words
have no legal return. Accordingly this bounded window contains no positive
MAIN primitive. It proves neither global nonemptiness nor global absence,
coverage, prime-only correctness or a target counterexample elsewhere.
Q's wrong-time fixed packets cannot convict MAIN; D/R likewise own their changes.

Scoped result: OWNED signed-permission clock; tested MAIN positive window empty;
global MAIN target remains bounded OPEN / FORK under the card's stop rule.
No search through other words or a higher-period census is undertaken.
Strong naturalness and arbitrary-encoding/PROVES_TOO_MUCH risks remain OPEN.
Classical NOT APPLICABLE; T3 NOT AUDITED; formal Route UNASSIGNED; B NOT INVOKED.
No unresolved owner/definition blocker was found after the pre-proof clarification.
The strongest positive alternative remains a legal prime packet outside this window;
this audit neither establishes nor rules it out. CP2/CP3 await separate PAPER UNLOCK.

EOF — independent raw proof, frozen only after complete readback.
