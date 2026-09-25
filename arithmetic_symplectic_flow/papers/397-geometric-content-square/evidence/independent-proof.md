# 397 independent raw proof — full-plane geometric-content square

Candidate `ANG-20260922-GCS01`; card-only exact derivation after root's explicit release.
Sole scientific input: `candidate-card.md`, complete clarified lines 1–89, SHA256 `0ec028ebd6682ce9cd6272263fd8e5a5a8a7908fa398b4cb83ce248412bb4727`.
Original 75-line prefix SHA256 `18e2e3fe06094686a57cecf45c23ce46d5a2a401e32bf71c2cade9b3ae114a34` remains unchanged.
Frozen CP1: `scope-review.md`, 60 lines, SHA256 `f7c4bd305748399e1f7e1af2d4262143101e7583d0a529042e2a0b141084fadc`.
Actual access: the card reread in full through line 89 and its EOF; no manuscript, author support files, peer proof, or other new scientific output was read.
Retained ARS and stream instructions govern method only. Shared history/model: internal **NOT_CALIBRATED**, not blind or external peer review.
No numerical experiment, network access, auxiliary delegation, new carrier, measure adjustment, or higher-period census is used.

## 1. Domains and every incoming branch

Write `C_ab=[a,a+1)×[b,b+1)`, `d_ab=gcd(|a|,|b|)`, and `D=⋃_{d_ab≥2} C_ab`.
The content and every declared map are Borel. Moreover,

`z∈D  ⇒  |z|>1`.                                                   (1)

Indeed one integer coordinate has absolute value at least 2. A coordinate with floor at most −2 is strictly less than −1; one with floor at least 2 is at least 2.
Thus no legal MAIN, C, or M source is zero. G explicitly excludes zero. Every map sends a nonzero legal source to a nonzero point, so zero is an isolated terminal in all four owners.
All other declared complement points remain terminal states, with their actual incoming branches; terminal identity arrows are not forward steps.

The sets `H_+`, `H_-` partition the punctured plane and contain exactly one member of each pair `{z,−z}`.
Define the Borel square root `r_+(w)` in `H_+` for every `w≠0`, and `r_-(w)=−r_+(w)`.
For example, using argument in `(−π,π]` gives the stated positive-imaginary assignment on the negative real axis.
For a square-map cell with its own constant `q>0`, set

`θ_ab,ε(w)=sqrt(q) r_ε(w)`,
`A_ab,ε={w≠0 : θ_ab,ε(w)∈C_ab∩H_ε}`.                            (2)

MAIN uses exactly the cells `d_ab≥2`, with `q=d_ab`.
G uses all integer cells, with `q=max(1,d_ab)` and the punctured source already enforced by (2).
C uses exactly the cells `d_ab≥2`, with `q=1`.
These are separate actual inverse atlases: in each case `Fθ(w)=w` and `θF(z)=z` on that cell and half-plane.
Their domains are Borel by the explicit root formula. Each forward restriction is injective because equal nonzero squares differ only by sign.
Every incoming source belongs to its unique half-open cell and unique half-plane, and therefore occurs exactly once in the corresponding atlas.
No assertion identifies the inverse domains belonging to different owners.

For M and each integer `d≥2`, the complete inverse is

`θ_d(w)=d w`,  `A_d={w : d(d w)=d}`.                              (3)

Here the outer `d(·)` denotes the frozen floor/gcd function. Equivalently split `A_d` into the Borel sets `d w∈C_ab`, `d_ab=d`.
These cell pieces are disjoint, and the grouped map in (3) is already injective. For `w≠0`, different integers d produce distinct sources; `w=0` belongs to no `A_d`.
Conversely every M predecessor of w has precisely this form with its actual content d, so (3) is exhaustive.
Equations (2)–(3), at every target including terminals, are the full one-step incoming ledger, with no digit cutoff.
Every finite incoming history is a composition of these inverses with each successive domain test imposed. The empty history retains the target itself.

## 2. All-point IMAGE, including assigned cuts

For MAIN, G, or C on a cell with its own q, `F(z)=z²/q` has nonzero complex derivative `2z/q` at every legal point.
At a source z and its target w, its locally analytic inverse therefore has the exactly specified real Jacobian

`J_θ(w)=q²/(4|z|²)=q/(4|w|)>0`.                                  (4)

This is finite at every actual w. It is the derivative of the analytic extension through the assigned source point, even if that point is on an integer or half-plane cut.
It need not be a derivative of the entire discontinuous, piecewise-defined global map across that cut.
For C, (4) reads `1/(4|w|)` on its own inverse domain. For M the global linear extension gives

`J_θd(w)=d²>0`.                                                  (5)

To prove every-Borel IMAGE, cover each nonzero source branch by countably many open neighborhoods on which its polynomial extension is a diffeomorphism.
Partition the actual Borel branch into disjoint Borel pieces subordinate to that cover, apply ordinary change of variables on each piece, and sum.
The branch inverse is Borel by (2) or (3), so this gives, for EVERY Borel subset E of its actual inverse domain,

`μ(θ(E)) = ∫_E J_θ(w) dμ(w)`.                                    (6)

The formula allows infinite values on both sides. The local extension at each cut gives exactly (4) or (5); no density value has been repaired there.
Lebesgue measure remains the frozen nonatomic, sigma-finite measure on the entire plane. Null fixed points and null inverse histories remain states.

## 3. Actual arrows and closed clock formulas

Let `F` denote one specified owner, and require every iterate below to be legal for that owner.
The source groupoid is exactly

`G_F={(z,k,w): ∃m,n≥0, k=m−n, F^m z=F^n w}`.                    (7)

Equal triples are one arrow. Units are `(z,0,z)`, inverse reverses endpoints and k, and composition adds k when endpoints match.
For composition, align the two legal histories of the shared point at the longer of their lengths; the matching history on the other endpoint extends by the same legal segment.
This proves closure even with forward terminals. The set (7) is Borel, as a countable union of Borel finite-iterate equality sets.
Countably many inverse branches imply countable source fibers. No topology or smooth quotient is needed for the declared orbit SET.

Put `v(z)=2log|z|` for `z≠0`, and `L=log4`. Zero has only its identity and is treated separately throughout.
For EACH of MAIN, G, and C, its own (4) gives

`κ_F(z)=log(4|z|²/q²)=L+v(Fz)−v(z)`,
`S_m(z)=mL+v(F^m z)−v(z)`,
`c_F(z,k,w)=kL+v(w)−v(z)`.                                      (8)

For M, its own (5) instead gives

`κ_M(z)=−2log d(z)=v(Fz)−v(z)`,
`S_m(z)=v(F^m z)−v(z)`,  `c_M(z,k,w)=v(w)−v(z)`.                  (9)

Thus all c values are independent of the presentation `(m,n)` of an actual triple and add under composition.
Equivalently, replacing `(m,n)` by a longer presentation with the same lag appends the same legal tail to both sums, which cancels.
Set c=0 on the isolated zero unit. No step at zero, or at any other terminal, has been manufactured.
The extension is the declared arrow `(w,h)→(z,h+c_F(z,k,w))` on the whole `Y×R`.
Forward arrival `F^m z=w` is the arrow `(w,−m,z)` and shifts height by `−S_m(z)`; the inverse-history direction shifts by `+S_m(z)`.
Neither (8) nor (9) asserts positivity of individual steps or an invariant measure on this extension.

## 4. Full kernels, isotropy, physical stabilizers, and phases

All the following kernel statements are restricted to ACTUAL arrows (7), not arbitrary endpoint pairs satisfying a radial equation.
For MAIN and G, excluding the isolated zero unit which is always included,

`ker c = {(z,k,w)∈G_F : |z|=2^k|w|}`,
`ker lag = {(z,0,w): ∃m≥0, F^m z=F^m w}`,
`ker c∩ker lag = {(z,0,w)∈G_F : |z|=|w|}`.                     (10)

For C these same formulas hold, and simplify to `ker c=ker lag`.
To see this, a nonidentity actual relation involves points of modulus greater than 1 by (1) and `F_C^m z=z^(2^m)`.
Writing `α=log|z|>0` and `k=m−n` gives `log|w|=2^k α`, hence

`c_C=kL+2(2^k−1)α`,                                             (11)

which is nonzero with the sign of k when `k≠0`. For `k=0` equal iterates give equal moduli and c=0. Units satisfy the same kernel conclusion.
This describes the entire global C kernel, not just its isotropy.

For any deterministic partial F, a nonzero isotropy lag at z is equivalent to eventual arrival at a legal cycle.
Indeed `F^m z=F^n z`, `m>n`, produces such a cycle; conversely a cycle supplies all multiples of its least period.
If the eventual cycle has least source period `p≥1`, then `G_z^z≅pZ` with every retained lag, not just one displayed period.
If no such cycle exists, source isotropy consists only of the unit.
Consequently for MAIN and G the full physical stabilizer is exactly

`H_z = pL Z` if z eventually reaches a least-p cycle, and `H_z={0}` otherwise. (12)

Their extension isotropy is trivial at EVERY height and state, since `c(z,k,z)=kL` and nonzero isotropy has nonzero k.
In particular the least positive physical return is `pL`; all positive repetitions are `j pL`, `j=1,2,…`.
C has no legal cycle: by (1) modulus strictly increases at each legal square step. Thus C has trivial source and extension isotropy and `H_z={0}` everywhere.
This does not remove its nontrivial coalescing, zero-lag arrows from the global kernel.

M has no cycle and in fact every legal step lands directly in a content-one terminal.
Write `z=(a+u)+i(b+v)` with `0≤u,v<1` and `d=gcd(|a|,|b|)≥2`; division by d gives floors `a/d,b/d`, whose gcd is exactly 1, including negative and zero coordinates.
Thus `τ(z)=1` on D and `τ(z)=0` off D is its full stopping depth; write `t(z)=F_M^τ(z) z` for its actual terminal.
Its whole groupoid and kernels have the exact further description

`G_M={(z,τ(z)−τ(w),w): t(z)=t(w)}`,
`ker lag_M={(z,0,w): t(z)=t(w), τ(z)=τ(w)}`,
`ker c_M = units`,  `ker c_M∩ker lag_M = units`.                 (13)

For the last equality, common finite iterates imply nonzero z and w are positive scalar multiples of the same point.
By (9), a zero clock means equal moduli, hence z=w; absence of cycles then forces k=0. Zero is its isolated unit.
All M source and extension isotropy is trivial, and `H_z={0}` at every state.

Here is the phase description for EVERY source orbit, without discarding any inverse history.
For a reference state o in that orbit, the full set of phases of `[z,h]` at o is

`{h+c(g): g is an actual arrow z→o}`,                            (14)

a single coset of `H_o` in R. The difference of any two such arrow clocks is exactly an isotropy clock; conversely composing isotropy realizes every element of that coset.
Thus each source orbit carries the entire translation orbit `R/H_o`, not a chosen height or orbit representative used to change multiplicity.
If `H_o=0` the translation action is free; if `H_o=pL Z` it is a circle of least period pL. These set-level statements require no smooth quotient claim.
For M the canonical reference is its actual terminal t, and the phase is `h+v(z)−v(t)` for nonzero states; the zero orbit has phase h.
For C, (14) retains all terminating and all infinite nonperiodic histories even though neither has positive physical returns.

## 5. Complete fixed sets and full fixed-basin packets

For MAIN, the fixed equation at a legal z is `z²=d(z)z`. Since zero is not legal, it forces `z=d(z)`.
This is a positive integer at least 2. Conversely every real integer `n≥2` has content n and satisfies `T(n)=n`.
Therefore

`Fix(T)={2,3,4,…}`.                                             (15)

For G the same algebra gives `z=e(z)`, with the puncture excluding zero. Precisely all real integers `n≥1` qualify:

`Fix(T_G)={1,2,3,…}`.                                           (16)

For C the only algebraic solutions of `z²=z` are 0 and 1, and both are outside D; hence `Fix(T_C)=∅`.
For M, `z/d(z)=z` with `d(z)≥2` forces z=0, which is outside D; hence `Fix(T_M)=∅`.
All these statements concern actual legal steps. Retained terminals do not enlarge any fixed set.

For MAIN or G and each of its fixed integers n, its entire source orbit is the full incoming basin

`B_n={z: ∃m≥0 legal, F^m z=n}`.                                 (17)

Indeed an actual arrow to n has a common iterate with n, and every iterate of n is n; this proves both inclusions without selecting a history.
Equations (2) and successive exact domain tests enumerate all of (17), including every cut and null point.
More explicitly, for any legal square history put `q_j=q(F^j z)` and

`Q_m(z)=∏_{j=0}^{m−1} q_j^(2^(m−1−j))`,
`F^m z=z^(2^m)/Q_m(z)`.                                        (18)

Thus (17) imposes `z^(2^m)=n Q_m(z)` with ALL intermediate source/content checks; choosing arbitrary q values without those checks is not allowed.
The same formula handles every incoming target, not merely fixed integers. For C it specializes to q=1 on its own legal histories.
For M every legal finite incoming history satisfies `F_M^m z=z/∏_{j<m}d(F_M^j z)`, again with all intermediate checks from (3).

Distinct fixed integers n and n' have disjoint basins and distinct source orbits: a common forward iterate would equal both fixed points.
At every point of `B_n`, source isotropy is the full Z, extension isotropy is trivial, and `H_z=LZ` by (12).
Its whole phase circle has the explicit incoming-independent coordinate

`h+2log(|z|/n)  mod L`,                                        (19)

because an arrival after m steps shifts by `−mL+v(z)−v(n)`; the integer multiple of L disappears in the phase quotient, not from the source lag ledger.
There is exactly one primitive physical translation packet per full basin `B_n`, containing all phases, of least time `L=log4`.
Every such packet has its own repetitions `j log4`, and no equal-time identification merges distinct n.
These are ALL the least-source-period-one packets, since (15)–(16) are complete fixed sets and (12) assigns a larger least time to every higher least source period.
The basins are countable (countable inverse alphabet and finite words), hence Lebesgue-null; the all-point clock version retains them in full.
MAIN has countably infinitely many such packets indexed by `n≥2`; G has countably infinitely many indexed by `n≥1`.
C and M have no positive primitive packets anywhere, by their complete no-cycle arguments above, not merely by their empty fixed sets.

## 6. Gate decision and limits

MAIN's necessary target fails already on every packet in (15): `log4` is not `log p` for an ordinary integer prime p.
It also has countably infinite same-length packet multiplicity; merging them is forbidden, though the composite-time violation alone is decisive.
The full return formula (12) is consistent with this finding and does not classify the existence or locations of higher-period cycles.
Ownership and every-Borel IMAGE are established for the frozen full-plane owner; no positive-roof suspension or smooth physical flow is constructed or asserted.
The three controls are complete OWN-owner derivations: G retains its extra fixed packet at 1; C has strict radial expansion; M has finite-time termination and an exact potential clock.
None of those changed maps or outcomes repairs MAIN. No state, terminal, incoming path, phase, or null fixed point has been removed.
The gcd cell observable preserves the stated symbolic lineage and drives the next geometric permission, but is not a primality test or proof of strong naturalness.
Portfolio: **STOP / FORK — owned clock, but composite fixed-packet primitive time and excess same-length packets.**
No higher-period census, tuning, prime-coverage proof, trace/zeta, classical claim, or formal Route evaluation is supplied; T3 NOT AUDITED, formal UNASSIGNED, B NOT INVOKED.

EOF — card-only raw proof complete; await root's full read and separate PAPER UNLOCK.
