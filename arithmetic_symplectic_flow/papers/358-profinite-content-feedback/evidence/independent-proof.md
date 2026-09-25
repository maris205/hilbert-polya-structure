# Independent bounded proof — profinite content feedback

Candidate: `ANG-20260921-PCF01`.
MAIN standing: owned Haar IMAGE and actual-lag extension; content-1/2 fixed
fibres empty; larger-content fixed points and longer returns **OPEN**.
Review standing: internal original-card derivation, `NOT_CALIBRATED`.

## 1. Inputs, access and method

I personally read candidate-card.md lines 1–123 through its authorized EOF,
including the owner-specific terminal clarification. Its measured SHA-256 is
`1024e37e35f67427af2f3568704b708d4633e78954ca5992aa7cc7be134bc2a5`.
This was the sole new scientific input. No author manuscript, outcome, peer,
scout, historical proof, network source, numerical experiment or auxiliary
agent was used. The ARS router, DA role and runtime policy were read this turn;
the previously read workflow/fallacy guidance is retained. No model change.
I derived MAIN and all three controls, sent the mathematical findings to root,
then wrote this report. Inherited shared history and the card's disclosed
diagnostic expectations prevent blindness or error-independence claims.
This is not external peer review, calibration, a novelty audit or a Route pass.
ARS scope discipline restricts the work to the frozen fixed-point diagnostic;
the author's later manuscript synthesis/review is not claimed completed here.

## 2. Full content and integer interface

Write K as the product of Z_p, as obtained by compatible prime-power residues
and the Chinese remainder theorem. Let v_p(0)=infinity and
e_p(x,y)=min(v_p(x),v_p(y)). Then P is precisely the set with every e_p=0.
It is the countable intersection of the clopen complements of (pK)^2,
hence closed. Each dP is compact. A pair has finite content exactly when all
e_p are finite and only finitely many are positive; its unique content is
the integer product of p^{e_p}. Thus the dP are disjoint, their union is Borel,
and delta, including its infinity value, is Borel. Infinite-content objects
are not replaced by a finite normalization or omitted from X.

Multiplication by a positive integer d is injective on K: reduction of dx=0
modulo dN gives x=0 modulo N for every N. Its image is dK, the kernel of
reduction modulo d, and its inverse there is a continuous division map.
Consequently division does not treat the zero-divisor ring K as a field.
For an embedded integer pair other than (0,0), the e_p are the usual gcd
valuations, including signed pairs and zero axes. Delta is their positive
integer gcd; (0,0) has infinite content. This proves the stated lineage interface.

## 3. All inverse branches and exact images

For MAIN put u=b-a^2-1. The complete target domain is exactly
E_d={ (a,b): a in dK and (u,a/d) in P }.
The additional source checks in the card follow from these two conditions:
(du,a)=d(u,a/d) has content d and T(du,a)=(a,b).
Conversely every source d(v,w) maps to (dw,v+d^2w^2+1), which lies in E_d.
Thus I_d(a,b)=(du,a) is a bijection E_d -> dP, and every incoming is listed.
The domain is compact and both branch maps are continuous on these subsets;
the full piecewise map is Borel, with no assertion of etaleness.

An explicit image test also describes all choices of d. For every p dividing u
(meaning u in pK), E_d requires v_p(a)=v_p(d)<infinity. For p not dividing u,
it requires merely 0<=v_p(d)<=v_p(a). Accordingly the forced product
d_0=product_{p|u} p^{v_p(a)} must be a finite positive integer: no infinite
exponent and only finitely many positive exponents are permitted. This is
necessary and sufficient for a target to have an incoming; all incoming d
are obtained by the remaining allowed finite-support choices at p not dividing u.
This is an exact countable enumeration, not a finite-inverse assertion.
MAIN is not onto: (0,1) has u=0 and no incoming. The terminal (0,0), however,
has precisely I_d(0,0)=(-d,0), one legal predecessor for every d>=1.

For C replace u by b-a^2 in the branch/domain and valuation formulas. For B replace (u,a) by
(a,b): its exact domain is b in dK and (a,b/d) in P, with inverse (da,b).
The same valuation rule, now using the first component as u and second as a,
is the complete image test for B. Both B and C are nononto: (0,0) has no
incoming. B at (1,0), and C at (0,1), each have the predecessors (d,0), d>=1.
For B/C the content of every image divides the finite source content d:
locally primitivity makes the new common valuation at most v_p(d), and
makes it zero when p does not divide d. Hence every infinite-content terminal
of B/C has no incoming. This fact is not transferred to MAIN or total A.

## 4. Every-Borel Haar IMAGE and its pointwise prescription

The global map (a,b)->(b-a^2-1,a) preserves product Haar by a coordinate swap
and translation in one coordinate, using Fubini for arbitrary Borel sets.
The analogous shear for C also preserves Haar. Multiplication by d on the
first coordinate takes normalized Haar to the normalized restriction on
dK, whose Haar mass is 1/d. This follows from its d cosets and uniqueness
of translation-invariant probability on that compact subgroup.
Therefore, for EVERY Borel E subset E_d,
mu(I_d E)=mu(E)/d, for MAIN, B and C, using their own target domains.
The same argument is an integral identity for nonnegative Borel functions;
it is not just a comparison of two whole-domain masses or one finite quotient.
All maps used are injective Borel maps with the stated Borel inverses.

The prescribed all-point version is j_d=1/d, so kappa=log d everywhere on dP.
It includes zero coordinates and null fixed fibres. Haar measure alone cannot
force uniqueness of pointwise values on null sets; this version is the card's
consistent branch prescription, not an a.e.-uniqueness theorem. No terminal
has an invented kappa, successor or absorbing loop.

## 5. Actual groupoid, sign, full kernel and physical phases

Legal iterates have Borel domains. Their equality relations give the inherited
Borel set G subset X x Z x X. Composition aligns the common middle history;
the longer existing history supplies precisely the needed legal continuation.
If two witnesses represent the same triple, both iterate counts differ by
the same integer; the extra common-tail sums cancel. Thus
c(z,m-n,w)=log(D_m(z)/D_n(w)), D_m=product_{i<m} delta(T^i z), D_0=1,
is well-defined and additive on actual triples, not free word witnesses.
For inverse itinerary charts I_alpha,I_beta on a common Borel target set E,
mu(I_alpha E)=D_alpha^{-1}mu(E)=exp(-c) mu(I_beta E).
This verifies the sign of the branch-pair IMAGE for every Borel E, including
zero-mass E. Countably many finite content itineraries cover all arrows.
The FULL arrow kernel is exactly D_m(z)=D_n(w), not merely identity arrows.

The extension (w,h)->(z,h+c) is a Borel groupoid on all X x R. Height
translation commutes with every arrow. The coarse object is only the orbit
set with its quotient sigma-algebra; no standard-Borel/Hausdorff structure
or smooth quotient is claimed. Each fixed-time induced map is measurable.
Source isotropy is 0 unless the forward history eventually enters a cycle.
For an actual least-length ell cycle it is ell Z. If its content product is
D, its entire time group is log(D) Z; when D=1 this means {0}, not a positive
primitive. Isotropy-kernel and extension isotropy are ell Z if D=1 and 0
if D>1. The source's ineffective lags have not been removed.
These conditional formulas classify groups once the actual cycle is known;
they neither assert an unproved cycle nor classify MAIN's remaining histories.

For any source orbit choose a representative f and, for each z, an actual
triple (z,k,f). Put a_z=c(z,k,f). The complete extension classes
over this orbit have phase h-a_z modulo H_f: changing the arrow changes a_z
by exactly an isotropy character. Distinct source orbits never merge.
For a fixed f of content d, its ENTIRE incoming basin is union_{r>=0} T^{-r}{f},
computed with all the above inverse domains. With first-hit sum A_z, the phase
is h-A_z mod log(d) if d>1, and exactly h-A_z if d=1. Distinct fixed points
cannot share a forward tail. Terminal basins use the same first-hit sum but
have isotropy 0, H=0 and an unreduced real phase; no terminal loop is inserted.

## 6. MAIN's complete content-1 and content-2 fixed fibres

A fixed source has x=y=t=dv where v is a unit of K. This is equivalent to
delta(t,t)=d, not a restriction to integer seeds. The complete equation is
d^2 v^2+(1-d)v+1=0.
For d=1 it implies v^2+1=0, impossible modulo 3. For d=2 it implies
(8v-1)^2=-15, impossible modulo 7 since 6 is not a square modulo 7.
Both entire profinite fibres are empty. Terminal diagonal points are not
fixed source points. No claim about d>=3 or longer MAIN cycles follows.

## 7. A and C: own rules, empty fixed sets

A is the total homeomorphism (x,y)->(y,x+y^2+1), with full inverse
(a,b)->(b-a^2-1,a). The Fubini shear proof gives its own all-Borel IMAGE 1.
Its actual retained-lag groupoid has c=0, full arrow kernel G, H={0} for
every state and extension isotropy equal to source isotropy. Its entire
incoming source orbit is the two-sided iterate orbit; height is unchanged.
MAIN-terminal states continue under A. A fixed point requires x=y=t and
t^2+1=0, impossible modulo 3. Other source periods are not enumerated.

C has its own domains and density 1/d from sections 3–4. Its fixed equation
for t=dv is v(d^2v+1-d)=0. Here v is a UNIT, so cancellation is justified.
For d>=2 reduction modulo any p|d gives 0=-1; d=1 instead requires v=0.
Thus C has no fixed sources of any finite content. The formal zero solution
before normalization is a terminal, not a counterexample or a source loop.
Its full group/phase rules are section 5 with its own legal C histories.

## 8. B: complete fixed sources, incoming basins and multiplicity

The fixed equation is (d-1)x=0. Integer multiplication on K is injective,
so the fixed set is precisely P, at d=1, together with
f=(0,dv), d>=2, v in K^times. Each latter f has only itself as an immediate
predecessor: every inverse has first coordinate zero, hence is f, whose
content forces the same d. Its entire basin is the singleton {f}.
Its source isotropy is Z, entire H=log(d) Z, extension isotropy 0, and
phase h modulo log(d). The primitive is log(d), all repetitions k log(d).
Different v or d give different fixed cores and cannot merge by any tail.
In particular d=2 has continuum many distinct log(2) packets. Their sources
are Haar-null since {x=0} is null; the prescribed all-point clock retains them.

For completeness every content-one fixed f=(a,b) in P has the exact basin
{(Da,b): D>=1 an integer, every prime dividing D also divides b}.
Necessity follows by multiplying the actual divisions: every removed factor
divides the unchanged b. Sufficiency follows primewise: where p|D, a is a
unit and each step removes min(v_p(D),v_p(b)) from the finite exponent.
There are finitely many such primes, so finitely many steps reach f.
If a=0, b is a unit and the formula is a singleton. Otherwise D is unique
by integer injectivity, and the first-hit clock sum is log D. These states
have source isotropy Z, H=0 and extension isotropy Z, with phase h-log D.
This is a fixed-basin theorem, not a requested longer-cycle census.

## 9. Adverse check and bounded decision

The positive case is genuine: full arithmetic division, nonlinear feedback,
same Haar IMAGE and an all-point actual-lag extension have been established.
The adverse checks retain nonintegers, zero divisors, null clocks, nononto
targets, terminal incoming, ineffective isotropy and entire fixed basins.
Nevertheless MAIN's two empty fixed fibres give only a bounded negative
diagnostic, not failure of its whole packet target. B's continuum of packets
is a control result, not a transferable MAIN obstruction. A/C lack fixed
sources but this alone excludes no longer source cycles. MAIN promotion
remains OPEN at this gate; stop the prescribed search here without tuning.
Strong naturalness is OPEN; T3 is not audited, classical A0/A1/A2 are not
applicable, formal Route coordinates unassigned and Route B not invoked.

EOF — bounded independent proof; no author manuscript read.
