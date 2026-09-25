# GCN01 — frozen-card independent derivation

Candidate `ANG-AUDIT-20260922-GCN01`; Paper404; batch round5/5.
Status: card-only mathematical obligations closed within the stated conditional
scope. This is not a new candidate, coverage theorem or formal Route result.

## 0. Access, method and release

Root explicitly released mathematics after reading the complete CP1 report.
Sole scientific input: candidate-card.md, all 79 lines through its EOF.
candidate-card.md SHA256 16089321178ba1c175676952a83d73a0280b173c695289cd1a3932154dac8f35
Frozen scope-review.md: 72 lines; no content changed in this stage.
scope-review.md SHA256 b2e42a8c89d1beef5bf55ab6bbd1350a64559e47f5ac36b633d5f692f434564b
The card was reread and both receipts measured before derivation. The earlier
ARS instructions, current AGENTS.md and recorded plan slices remain applicable.
No manuscript, README, ledger, peer report, linked397, other new output or
external source was read. No numerical search, experiment or auxiliary agent
was used. Shell access served only reading, existence checks and receipts.
Method: exact change of variables, actual-triple algebra, elementary Gaussian
arithmetic and full-source control reconstruction. Shared history is retained;
this is neither blind nor external review. Runtime model identity/settings are
not independently attested. Internal NOT_CALIBRATED; no scoring or defect quota.

## 1. Actual domains, every-Borel IMAGE and the pointwise version

Write D_0=C and D_m for points with m legal steps. These sets are Borel by
induction. On D_m, put J_m(z)=product_{r=0}^{m-1}|f_{i_r}'(T^r z)|^2,
J_0=1 and S_m=log J_m. Every factor is finite and strictly positive.
The branch labels i_r are unique, including at all assigned cuts.
Outside D there is only the zero-step forward path, not an artificial next step.
The carrier is C, not its projective compactification; infinity is not added.

For one branch write Q_i=f_i(P_i), g_i:Q_i->P_i its actual inverse. For every
Borel E subset Q_i, the exact inverse-IMAGE statement is

    mu(g_i(E)) = integral_E |f_i'(g_i(w))|^(-2) dmu(w).                 (1)

Here Q_i is Borel and g_i Borel (also explicit in the frozen assumptions).
To justify (1) even for arbitrary Borel P_i, cover its points by countably many
open neighbourhoods on which f_i has a holomorphic inverse. Such neighbourhoods
exist because there is no pole or critical point there. Disjointify the cover
on P_i. The ordinary real change-of-variables formula applies to every Borel
subset of each resulting chart; injectivity on P_i makes the images disjoint.
Summing proves (1), including infinite measures. The real Jacobian is |f_i'|^2.
The same construction works for every finite itinerary and its actual image.

Equation (1) does not determine a unique pointwise density on null sets.
The frozen holomorphic-derivative prescription supplies that version at every
legal point, including cuts; (1) proves it is compatible with the actual measure.
No derivative of a merely Borel restriction is inferred from measure alone.
For a noninjective global T, images of different source branches may overlap:
one cannot replace (1) by a global arbitrary-set forward IMAGE equality.
All inverse histories are compositions of all legal g_i, with actual successive
target membership. This is exhaustive and does not impose arithmetic membership.

## 2. Full actual-triple groupoid, cocycle, kernels and measure

Let G={(z,m-n,w):z in D_m,w in D_n,T^m z=T^n w}, as a set of triples.
Units are (z,0,z) for every z in C, including terminals. Inverse interchanges
z,w and negates the lag. This is a Borel, countable-source-fibre groupoid:
there are countably many finite inverse itineraries and meeting depths.
No etale, smooth-quotient or Hausdorff-quotient assertion is needed.

For composable presentations (z,m-n,w),(w,r-s,v), put L=max(n,r).
The common w-tail gives a presentation with meeting depths
m+L-n and s+L-r. These iterates are legal because the common tail exists.
Their difference is (m-n)+(r-s), proving closure with the required lag.
If two presentations of the same triple differ, both depths differ by the
same integer. Taking the longer pair adds the identical common forward tail
to both sums. Hence c(z,m-n,w)=S_m(z)-S_n(w) is presentation-independent.
The same common-tail identity proves additivity under composition.

The entire kernels, with no source or inverse branch removed, are exactly

    K=ker c={g as above:J_m(z)=J_n(w)},
    M=ker lag={(z,0,w):some legal n has T^n z=T^n w},
    K intersect M={(z,0,w):some legal n has T^n z=T^n w,
                                      J_n(z)=J_n(w)}.              (2)

These are iff membership descriptions, not just necessary tests. They include
all units; equality conditions are independent of the chosen presentation.
For an actual finite-itinerary transport w->z, its real Jacobian is
J_n(w)/J_m(z)=exp(-c). This follows by forward and inverse chart composition,
on the actual restricted domain, and gives every-Borel transport IMAGE.
The extension sends (w,h) to (z,h+c). If a measure on this extension is desired,
mu(dz)e^h dh is preserved on these transports: base factor exp(-c) cancels
the height-density factor exp(c). This adds no quotient regularity claim.

## 3. Entire isotropy, incoming components and every physical phase

An eventual cycle means finite legal entry into a cycle of least period q.
If T^m z=T^n z with m>n, the forward tail from T^n z is a legal periodic
cycle. Conversely, eventual entry into a least-q cycle produces every lag
in qZ and no other lag. Thus G_z^z=qZ in that case, and is {0} otherwise.
A terminal-reaching point cannot be eventually periodic, and retains its unit.
This exhausts all source points: terminal-reaching, eventually periodic,
or infinite forward path with no eventual cycle.

For the eventual cycle a_0,...,a_{q-1}, let C=sum_j kappa(a_j).
At every point of its entire incoming component, c on lag kq is kC; incoming
finite sums cancel in loops. Consequently

    H_z=C Z;   extension isotropy={kq:kC=0}.                       (3)

If C!=0, H_z=|C|Z and extension isotropy is trivial. If C=0, H_z={0}
but extension isotropy remains the whole qZ. All other components have both
source/extension isotropy trivial and H={0}. No dense extra return subgroup
arises from inverse branching: a loop's lag has already exhausted qZ.

For completeness, fix a reference b in one source component and an arrow
g_z=(z,k_z,b). Every (z,h) is equivalent to (b,h-c(g_z)). Choices of g_z
differ precisely by source isotropy at b. Therefore that entire component's
extended orbit SET is R/H_b, with phase [h-c(g_z)] and height translation.
This proves that its full physical stabilizer is H_b, not a selected sublattice.
There is one physical periodic packet per eventual-cycle component when C!=0;
all phases occur, with primitive |C| and positive repetitions n|C|, n>=1.
When H=0 it is a free translation copy of R, not a positive periodic packet.
This is componentwise set identification, not a global Borel section claim.

For a cycle reference a_0 let A_j=S_j(a_0), T^j a_0=a_j. If T^r z=a_j,
then g_z=(z,r-j,a_0) has c=S_r(z)-A_j. Hence the phase is

    [h-S_r(z)+A_j] in R/CZ.                                      (4)

Different entry times into this same cycle alter (4) only by a multiple of C.
Different cycle reference origins translate its coordinate consistently.
When C<0 the positive generator corresponds to the opposite lag orientation;
using |C| does not discard negative lag or reverse the frozen local clock.
Distinct cycles cannot merge through incoming histories under a function T.

## 4. Gaussian-rational cycles and exact norm restriction

If one legal cycle point belongs to Q(i), every point on that cycle does:
all branch functions have coefficients in Q(i) and have no pole there.
Their derivatives also have coefficients in Q(i). The exact complex return
multiplier, using the prescribed extensions along the itinerary, is

    Lambda=product_{j=0}^{q-1} f_{i_j}'(a_j) in Q(i)^*,
    C=log |Lambda|^2=log N(Lambda).                               (5)

This chain multiplier is valid on the local composition of extensions; it
does not claim the full Borel piecewise iterate is differentiable across cuts.
For C!=0, R=exp(|C|)>1 equals N(Lambda) if C>0, and N(Lambda^(-1)) if C<0.
Thus R is a positive rational Gaussian norm for either sign.

Here is an elementary exact characterization, not a borrowed norm theorem:

    R in Q_{>0} is N(u), u in Q(i)^*, iff v_p(R) is even
    for every ordinary prime p congruent 3 modulo 4.               (6)

Necessity: write u=(a+ib)/d with integers a,b,d, d!=0, not both a,b zero.
For p=3 mod4, -1 is not a square modulo p. Indeed multiplication by any
nonzero residue permutes the nonzero residues and gives x^(p-1)=1; a square
root of -1 would instead give (-1)^((p-1)/2)=-1. After dividing a,b by the
common p-power p^r, at least one is nonzero modulo p and their squared sum
cannot vanish there. Therefore v_p(a^2+b^2)=2min(v_p(a),v_p(b)), with the
usual infinite valuation for a zero entry, and v_p(N(u)) is even.

Sufficiency can also be established elementarily. N(1+i)=2. For an odd prime
p=1 mod4, pairing each invertible residue with its inverse proves Wilson's
identity (p-1)!=-1 modulo p. With n=(p-1)/2 even, pairing k with p-k then
gives (n!)^2=-1 modulo p. Choose r=n! modulo p.
Gaussian integers have Euclidean division for the norm: round the real and
imaginary parts of a quotient to integers; the remainder norm is at most
one half the divisor norm. Thus their Euclidean algorithm gives Bezout gcds.
Let delta=gcd(p,r+i). It is not a unit: modulo p, r+i annihilates the nonzero
element r-i, so cannot be a unit as Bezout would require. Nor is delta
associated to p, since p does not divide the imaginary coefficient 1 of r+i.
Since delta divides p, N(delta) divides p^2; excluding 1 and p^2 leaves
N(delta)=p. Finally factor a positive rational into finitely many prime powers.
For p=3 mod4 with even exponent e, use the rational Gaussian scalar p^(e/2).
For p=2 and p=1 mod4 use the constructed norm-p element to the integer power e;
negative exponents are legitimate in Q(i)^*. Multiplying proves (6).

In particular, R=p for p=3 mod4 is impossible in (5), since v_p(p)=1.
This excludes least positive physical time log p for the entire incoming
packet of any Gaussian-rational cycle, for both signs of C. It does not
exclude a cycle whose nonzero clock gives R=p^2 or another permitted norm.
At C=0 there is no positive primitive; source isotropy is still qZ by (3).

Condition (6) is sufficient for being an algebraic norm, NOT for realization
as a multiplier of a specified owner, for multiplicity, or for prime coverage.
Inert primes are infinite: from a hypothetical finite list with product P,
4P-1 has a prime factor 3 mod4 not dividing P. Thus an additional hypothesis
that all positive packets have Gaussian-rational cores would obstruct eventual
all-prime coverage. That hypothesis is NOT imposed on the full frozen class.
The present result cannot globally exclude its non-Gaussian periodic cores.
Likewise forward preservation of Q(i) does not imply backward preservation:
nonlinear inverse roots of a Gaussian-rational value can lie outside Q(i).

## 5. N and S — two separate full-plane owners

For N take a=1+i, Q=2; for S take a=2+i, Q=5. Each has its own full domain
C, map T_a(z)=az, Lebesgue measure, inverse w/a and clock log Q everywhere.
For every Borel E, mu(E/a)=Q^(-1)mu(E); all inverse iterates w/a^m are retained.
There are no terminals, cuts or missing target values for these owners.

The complete groupoid for either owner is

    G_a={(z,k,a^k z):z in C,k in Z},   c=k log Q.

Thus K=M=K intersect M=all units. Since |a|>1, a^q z=z, q>=1,
forces z=0. The only periodic point is the fixed point 0; no other point is
strictly preperiodic, because the map is a bijection and T_a^m z=0 forces z=0.
At 0 the whole source isotropy is Z, H=(log Q)Z, and extension isotropy is 0.
It gives exactly one positive periodic packet, all height phases modulo log Q,
with primitive log Q and repetitions n log Q. Its full incoming basin is {0}.
Every nonzero point has entire source/extension isotropy and H equal to 0.
Its full source component is a^Z b for any reference b!=0. Writing z=a^n b,
the real phase h+n log Q identifies its extended quotient with the free R
translation action. All such nonzero components remain in the owner.
These separately realize the admitted primes 2 and 5 as external controls;
they do not supply endogenous prime generation or all-prime coverage.

## 6. I — actual inverse branches, terminal and all kernels

Write P(z)=z^2+3/4 only as a polynomial extension. The actual partial map is
T=P on C\{0}; the state 0 is retained but has no forward step. Its branch
domains H_+ and H_- from the card partition every nonzero source exactly once.
Each maps bijectively onto Y=C\{3/4}: the two nonzero roots of w-3/4 are
opposites and exactly one lies in each assigned half-plane, including its cut.
Denote these actual Borel inverse branches r_+(w),r_-(w). Neither is defined
at 3/4. There is no legal inverse there; the sole polynomial preimage 0 is
excluded as a SOURCE, not deleted as a state. The target 0 does have its two
legal incoming points +i sqrt(3)/2 and -i sqrt(3)/2.

At every nonzero source, kappa(z)=log(4|z|^2). For every Borel E subset Y,

    mu(r_+(E))=mu(r_-(E))=integral_E 1/(4|w-3/4|) dmu(w).           (7)

This follows from the same actual local inverse Jacobian, including the cut
version. The full preimage of a Borel E has measure the integral of
1/(2|w-3/4|) over E intersect Y, since the two source branches are disjoint.
It is not a forward global IMAGE law. All finite compositions of both r signs
are included exactly when each successive target belongs to Y.

For any legal m define B_m(z)=2^m product_{j=0}^{m-1}T^j z, B_0=1;
J_m=|B_m|^2=4^m product_j|T^j z|^2. The FULL groupoid contains all legal
(z,m-n,w) with P^m(z)=P^n(w). Its cocycle is log(J_m(z)/J_n(w)).
Hence its complete K, M and intersection are (2) with precisely these J_m
and legal domains. These finite-product equalities are exact iff criteria
over all complex sources and inverse histories, not a selected-root ledger.
The distinction is real: (z,0,-z) belongs to K intersect M for every z!=0;
(1/2,1,1) belongs to K but not M, since kappa(1/2)=0.
Conversely, (1/2,0,i sqrt(7)/2) belongs to M via two steps to 7/4,
but not K: the two J_2 values are 4 and 28, giving c=-log 7.
The local clock is negative for 0<|z|<1/2, zero at radius 1/2, positive
outside. It is not a positive classical roof.

## 7. I — complete fixed packets and general eventual-cycle ledger

The COMPLETE fixed set solves z^2-z+3/4=0 and consists of

    alpha_+=(1+i sqrt(2))/2,  alpha_-=(1-i sqrt(2))/2.

Both are legal and non-Gaussian-rational. Their multipliers 2alpha_+ and
2alpha_- have squared modulus 3, so each cycle clock is exactly log 3.
For each sign its full finite-entry basin is

    E_alpha=union_{n>=0}{z:P^n(z)=alpha}.                          (8)

There are no illegal paths hidden in (8). A path passing through 0 would
thereafter, under the polynomial extension, stay real, and could not reach
nonreal alpha. Every derivative on a path in (8) is therefore nonzero.
P^n(z)=alpha has exactly 2^n distinct roots, by the derivative product and
degree (or inductively the two nonzero inverse roots). The root sets are
nested since alpha is fixed. Exact first-entry layers have sizes 1 for n=0
and 2^(n-1) for n>=1. Thus (8) is the exhaustive countably infinite basin,
not just its core, one selected inverse branch or a basin of asymptotic attraction.
It contains no Gaussian-rational state: forward preservation would contradict
alpha not belonging to Q(i). The two full basins are disjoint source components.

At every point of either basin, full source isotropy is Z, extension isotropy
is 0 and H=(log 3)Z. Formula (4), here [h-S_r(z)] modulo log 3, supplies
every phase. There are exactly two DISTINCT fixed-basin packets with primitive
log 3, both with repetitions n log 3. This asserts a count of these fixed-basin
packets only, not the total count of all higher-cycle packets in this owner.
It refutes both a global inert-prime exclusion outside the Gaussian hypothesis
and unique multiplicity for the full owner: two log 3 packets already exist.

For an exact all-period parametrization put
Omega_q={z:P^q(z)=z and P^d(z)!=z for every proper positive divisor d of q}.
Every polynomial periodic point is legal: otherwise its cycle would include
0, whereas P^n(0)>0 for n>=1. Thus the Omega_q, modulo cyclic rotation,
are exactly all actual primitive cycles, with no root or itinerary selected.
For every such least-q cycle O, with no higher-period census attempted,

    Lambda_O=2^q product_{a in O}a,
    C_O=log(4^q product_{a in O}|a|^2).

Its entire basin is union_{n>=0}{z:P^n(z)=a_0} for any chosen cycle point a_0.
No real point is periodic: P(x)-x=(x-1/2)^2+1/2>0 on R. Thus all cycle points
are nonreal; the preceding no-critical-prehistory argument applies to this
whole basin as well. It contains all incoming phases, cannot merge with a
different cycle, and obeys exactly (3)–(4): source isotropy qZ; H=C_O Z;
extension isotropy qZ if C_O=0 and 0 otherwise. For C_O!=0 its primitive is
|C_O|, with all positive repetitions; for C_O=0 it is not a periodic packet.
If such a core lies in Q(i), the norm restriction applies, otherwise it does not.

The terminal component is precisely union_{n>=0}{z:P^n(z)=0}. For n>=1,
P^n(0)>0; therefore those backward levels are disjoint and no path to 0
passes through 0 prematurely. Every level has 2^n legal distinct roots.
All its source/extension isotropy and H are 0, including at terminal 0;
its real phase is h-S_n(z) at exact terminal-entry depth n.
Every remaining point has an infinite non-eventually-periodic path, hence
source/extension isotropy and H equal to 0. Its complete component and all
real phases are the actual-triple construction in sections 2–3. This exhausts
the carrier without deleting aperiodic states, cuts, terminals or incoming.

## 8. Closure and stop

The frozen conditional restriction is proved; N/S and I have separately owned
IMAGE laws, clocks, full kernels and entire return groups. In particular I's
non-Gaussian log 3 packets cannot be transferred into the Gaussian hypothesis.
No main full prime-symbolic candidate or naturalness theorem has been supplied.
No controls' coefficients or packets are promoted to endogenous arithmetic.
Other fields, nonholomorphic owners, non-Gaussian cores and other clocks remain
outside the restriction. Classical NOT APPLICABLE; T3 NOT AUDITED;
formal UNASSIGNED; B NOT INVOKED. No numerical, operator or novelty claim.
No blocker in the frozen mathematical contract was found. Portfolio: retain
this conditional filter and fork only on future separate authority; no sixth
round is authorized. Freeze this raw record and preserve CP1 bytes. Stop for
root's full read and separately explicit PAPER UNLOCK before any author read.

EOF — card-only independent raw; internal NOT_CALIBRATED.
