# ECD01 — original-card independent derivation

Candidate: ANG-20260923-ECD01. Internal same-model **NOT_CALIBRATED** review.
Result: MAIN owns its prescribed Borel IMAGE clock, but every actual positive
primitive has time `p log 4=log(4^p)` for an integer `p>=1`. Thus the joint
nonempty/ordinary-prime-only target fails, whether or not MAIN cycles exist.
MAIN cycle existence and multiplicities are not asserted. **STOP / FORK**.

## 1. Input, stages and limits

Sole scientific input: `candidate-card.md`, clarified original lines 1–100,
personally reread through that EOF after the separate mathematical release;
100 lines, 5986 bytes, SHA-256
`af74a4508865d5a947ac2527abb97681615c580e878996c37d2428ae45558b74`.
Its initial 91-line prefix has SHA-256
`4164f4ff5863e0999125ce017d900f1ce8274d95d29301e7c6416427d9a4f4e9`.
CP1 identified the sector/clock notation collision and missing explicit sums;
the pre-proof append resolved them without changing any map. Its frozen
99-line scope report remains unchanged. ARS workflow/DA/runtime instructions
remain applied. No paper, outcome, README, ledger, sibling or peer proof was
read. No auxiliary, web, scientific code, numerical search or model change
was used. Design exposure disclosed in the card is not reviewer access to
those sources. Shared inherited history precludes blindness, external peer
review, calibration and error-independence claims.

## 2. Arithmetic and exact inverses on the entire source

Use `a(z)=A_nm=g+i r` on the assigned floor cell. Always `g>=1`, so
`|a(z)|>=1` and `a(z)!=0`. All coefficients are finite. On the integer
interface the quotient and gcd give exactly the card's displayed complex
ratio; a zero imaginary part is precisely zero Euclidean remainder.
The interface is not a replacement carrier or a permission restriction.

For MAIN every nonzero source maps to a nonzero target. Hence all such
forward histories are legal forever; zero is terminal and has no predecessor.
For nonzero `w`, the card's two square roots for every integer cell, retained
exactly when they lie in that cell and their assigned sector, give ALL
predecessors. Indeed a predecessor must solve `a z^2=w` for its own cell;
conversely every root passing those tests has exactly that readout and image.
Every nonzero source belongs to precisely one half-open cell and one sector.
Thus no source is lost on a cut, and labels do not multiply actual points.

This is also a finite exact membership test for each particular target:
`|z|^2=|w|/|a(z)|<=|w|`. If `R=sqrt(|w|)`, only integer labels
`-ceil(R)<=n,m<=floor(R)` can occur; each supplies at most two roots.
The bound is proved, not a numerical truncation. MAIN's image is precisely
the nonzero targets with a nonempty retained set; no surjectivity is assumed.

Control A has exactly the two square roots of each nonzero target and none
at zero, with no integer-cell labels. Its image is the punctured plane.
Control L is total. For each target its entire predecessor set is
`{w/A_nm: floor/readout checks for C_nm hold}`. Invertibility of each nonzero
coefficient proves necessity and sufficiency. Since `|z|<=|w|`, only finitely
many cells need testing for that target by the analogous bound with `R=|w|`.
At zero this set is exactly `{0}`, with assigned coefficient `A_00=1`.
L has no terminal state. Its exact image is given by that complete predicate;
total forward definition is not incorrectly promoted to surjectivity.

## 3. EVERY-Borel IMAGE and all-point versions

For MAIN, the analytic inverse germ at a retained root satisfies
`theta'(w)=1/(2 A_nm theta(w))`. Real area, rather than complex derivative
modulus, therefore gives
`J_nmj(w)=1/(4 |A_nm|^2 |theta(w)|^2)=1/(4 |A_nm| |w|)`.
It is strictly positive and finite at every assigned nonzero target.
Different actual inverse branches at a target may have different densities.
For A, `J_A(w)=1/(4|w|)`. For L, `J_L(w)=1/|A_nm|^2`, including zero.

The selected square-root functions are not assumed globally continuous
across their Arg cut. For each fixed coefficient, split the target into its
cut ray and the complementary slit plane. Off the ray each root is a smooth
injective analytic branch; restricting ordinary change of variables to the
actual Borel floor/sector domain proves the IMAGE identity for every Borel
subset there. The ray and its root image have area zero; their Borel subsets
therefore satisfy the same identity with the prescribed finite density.
This proves `mu(theta E)=integral_E J dmu` for EVERY actual Borel branch
subset, including cut/floor intersections. L follows directly from its
invertible linear germ. No null state or null inverse subset is discarded.
The germ prescription fixes the all-point version; IMAGE alone would not
make versions unique on null sets. Branchwise IMAGE is not global invariance.

Consequently the legal step clocks are
`kappa=log 4+2 log|a(z)|+2 log|z|` for MAIN,
`kappa_A=log 4+2 log|z|` for A, and `kappa_L=2 log|a(z)|` for L.
MAIN/A terminal next-step clocks remain undefined. Signed and zero legal
clocks are permitted; none has been replaced by a positive roof.

## 4. Exact radial identity and the FULL actual cocycle

Put `lambda=log 4` and `B(z)=2 log|z|` for `z!=0`; set `B(0)=0` only
as a Borel bookkeeping value, not as `log 0` or a terminal step clock.
For MAIN, `|Tz|=|a(z)| |z|^2` gives the exact identity
`kappa(z)=lambda+B(Tz)-B(z)`. The same identity holds for A.
For L, on nonzero sources `kappa_L=B(T_L z)-B(z)`; it also holds at zero
because `T_L0=0`, `A_00=1` and `kappa_L(0)=0`.
Hence legal finite sums for MAIN/A are
`S_r(z)=r lambda+B(T^r z)-B(z)`, while for L they omit `r lambda`.

All maps and legal domains are Borel. The actual retained-lag groupoid is
the countable union of equal-iterate Borel sets inside `X x Z x X`.
For an arrow `(z,k,w)`, cancellation of the common final state gives

- MAIN/A: `c(z,k,w)=k lambda+B(w)-B(z)`.
- L: `c_L(z,k,w)=B(w)-B(z)`.

At MAIN/A's origin only the identity arrow exists, so the formula still
holds there; it does not assign nonexistent iterates. At L's origin all
integer isotropy arrows are present with clock zero. These formulas prove
descent and additivity on actual triples, not a free history presentation.
The forward arrow has `k=-1` and clock `-kappa`. Composed branch germs have
IMAGE density `exp(-c)`. Their every-Borel laws follow by iterated change
of variables on countably many finite branch-pair domains; equal-witness
clocks agree by the formula. No illegal continuation through zero is used.
The extension on the full `X x R` and its commuting height translations
are therefore defined on the orbit SET, without a nice-quotient assumption.

For MAIN/A the complete kernels, always restricted to actual `G`, are
`K_lag={k=0}`, `K_clock={k lambda=B(z)-B(w)}`, and
`K_joint={k=0, B(z)=B(w)}`. On nonzero endpoints the clock condition is
equivalently `|z|/|w|=2^k`. These are arrow kernels, not just isotropy.
For L they are respectively `{k=0}`, `{B(z)=B(w)}`, and their intersection.
L's cocycle is a global coboundary, not necessarily identically zero.

## 5. Entire isotropy, incoming and phase descriptions

For every deterministic owner here a nonzero isotropy lag exists precisely
when its point is eventually periodic. If the least eventual source period
is `p`, the entire source isotropy is `p Z`; otherwise it is `{0}`.
This follows from equality of two legal iterates and the least period of
their eventual cycle. Branching predecessors supply no extra isotropy lags.
For MAIN/A, all eventually periodic points therefore have
`c(kp)=kp lambda`, `H=p lambda Z`, trivial extension isotropy and positive
primitive `p lambda`, with repetitions `j p lambda`. Other sources have
`H={0}` and trivial extension isotropy. In particular the terminal origin
has no positive return and only its identity arrow. For L all `H={0}` and
extension isotropy equals source isotropy, including the fixed origin.

Let `P` be the exact predecessor operation in §2; recursively set
`P^0(E)=E`, `P^(r+1)(E)=union_{v in P^r(E)} P(v)`.
This gives every finite incoming depth, with no label or branch cutoff.
The orbit of `z` is exactly `union_(a,b>=0, T^b z legal) P^a({T^b z})`.
Arrows into a range `z` are exactly `(z,a-b,w)` with `w in P^b({T^a z})`.
A cycle's full basin is the union of all inverse depths of all its points;
distinct eventual cycles cannot merge. These are exact constructions, not
an asserted enumeration or finiteness of those full basins.

For MAIN/A fix a base in a source orbit and, for each point `z`, choose
an actual arrow from the base with lag `ell_z`. In a periodic basin the
lags are well-defined modulo `p`. The complete height phase is
`h+B(z)-ell_z lambda mod p lambda`; the base's constant is immaterial.
This lag correction is essential: radial height alone need not be invariant
modulo the least physical period. In a non-eventual nonzero orbit the lag
is unique and the same expression is an unreduced real phase. On the terminal
origin's singleton source orbit the phase is `h`. For L, `h+B(z)` is invariant on
the extension globally, giving the real phase over each separate source
orbit; at zero it is again `h`. No equal-time merger of packets is imposed.

## 6. The decisive MAIN global gate, without an existence claim

On ANY legal least-`p` MAIN cycle, put `rho_i=|z_i|` and `a_i=a(z_i)`.
Multiplying `rho_(i+1)=|a_i| rho_i^2` gives
`prod_i |a_i| rho_i=1`. The product of the real-area forward Jacobians is
therefore `prod_i 4 |a_i|^2 rho_i^2=4^p`, also directly obtained from §4.
All assigned boundaries obey the same germ/radial identity. This computation
does not require a special arithmetic itinerary or an interior cycle.
The entire stabilizer calculation in §5, not one chosen loop, then gives
least positive time `log(4^p)`. Since `4^p` is composite for every `p>=1`,
no positive primitive in this owner can have ordinary-prime logarithmic time.

If MAIN has any cycles, its nonempty positive ledger violates prime-only.
If it has no cycles, its positive ledger is empty and violates nonemptiness.
Thus the stated JOINT target fails globally without settling which existence
case occurs. Existence, counts, higher-period realizations and multiplicities
remain unclassified; none is inferred from this conditional proof.
There was no fixed-window or period search. Dividing the area clock by two,
selecting a different loop as primitive, or changing the owner would not be
an interpretation of the frozen target. The authorized decision is STOP/FORK.

## 7. Own control consequences and scope

For A the exact iterate identity `T_A^r z=z^(2^r)` gives an optional complete
membership description without enumerating periods: a nonzero source is
eventually periodic exactly when it is a root of unity. Writing its order
as `2^s M`, with `M` odd, its eventual least period is the multiplicative
order of `2` modulo `M`, with value `1` when `M=1`. This follows directly
from `z^(2^a(2^p-1))=1`; the power of two is removed by initial squaring.
The entire groups and phases are those of §5. Every inverse depth of a
nonzero target is its full set of `2^r` distinct roots, and their union over
the cycle gives its full basin. At least the fixed core `1` is present, with
primitive `log 4`; its basin consists of roots of unity of power-of-two order.
Other roots/cycles are characterized by the equation, not a census or a
claim that every positive integer period has been separately realized.
The zero terminal has a singleton source orbit with trivial source isotropy.

For L, on a nonzero cycle the radial product gives `prod_i |a_i|=1`.
Every factor is at least one, so each is one. As `g>=1` is real and integral,
`|g+i r|=1` forces `g=1,r=0`, hence every such step is the identity.
Therefore L has only fixed cycles. Its exact full fixed set is
`{floor(y)=-1 or floor(y)=1} union ([0,1)+i[0,1))`.
Indeed for `m!=0`, `r=0` implies `|m|` divides `n` and then `g=|m|`;
unit modulus occurs exactly at `m=±1`. For `m=0`, `r=n`, giving only `n=0`.
This also includes the origin and all assigned strip endpoints correctly.
Its full eventual-fixed set is `union_(r>=0) P_L^r(Fix(T_L))`; every point
there has source/extension isotropy `Z`, and outside it source isotropy is
trivial. All `H` vanish. The origin has only itself as predecessor, while
other fixed basins retain every branch in the exact recursion; they are not
asserted singleton or uniformly finite. All phases/kernels are as in §§4–5.

The strongest positive result is a complete same-owner Borel clock law and
exact structural period restriction, not a positive prime fit. The A control
exhibits the same degree/area obstruction with arithmetic removed; L isolates
the zero-return effect when degree is removed. Neither conclusion is borrowed
as MAIN's proof. Strong naturalness and the design concern remain explicit.
No general impossibility theorem for complex or arithmetic dynamics is proved.
T3 remains unaudited, formal Route unassigned and Route B not invoked.
Freeze this original derivation before separate PAPER UNLOCK and CP2/CP3.
