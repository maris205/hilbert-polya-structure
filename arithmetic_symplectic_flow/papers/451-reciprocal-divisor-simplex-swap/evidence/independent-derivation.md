# 451 — frozen card-only independent derivation

Candidate **ANG-20260924-RDSS01**; date 2026-09-24; internal **NOT_CALIBRATED**.

## 1. Input, authorization and limits

After root's full CP1 reading and distinct RAW RELEASE, I personally reread only the original `candidate-card.md`, lines 1–93 through EOF: 93 lines / 5658 bytes, SHA-256 `065e2b6753f85f74904348af8edfd75bfdae6ad7860463d0bb59739dd4bf3f4d`.
The completed CP1 report is 72 lines / 8172 bytes, SHA-256 `00040bb1936c8dec9f505c906c71e8c2638decc5798f17463493680a9258d5a4`; its instruction-read and historical-status exposure disclosure remains applicable.
No author manuscript, package README/ledger/outcome, peer answer, old proof or sibling science was accessed. No auxiliary, network, scientific code/numerics, Git or PDF was used. All calculations below are exact elementary derivations from this card.
The inherited model/shared history is not blind, cross-model or error-independent verification. This raw report will be immutable after full self-read and hash receipt; manuscript access requires a separate unlock.

## 2. Full carriers, permissions and integer interface

Put σ(x,y)=x+y on X={x>0,y>0,σ<1}, with the frozen restricted Lebesgue measure μ. Write n=floor(1/x), d=floor(1/y), so both labels are positive integers everywhere on X.
For q≥0 define F_q(x,y)=(y,x)/(1+qx), and λ=1+qx. Then λ≥1, both outputs are positive, and σ(F_qz)=σ(z)/λ<1. Thus the frozen geometric guards add no restriction when the specified q is nonnegative.
Consequently D_M=A={d|n}, with q=n/d≥1; D_G=X, with q=floor(n/d)≥0; and D_Q=A, with T_Q(x,y)=(y,x). MAIN and Q have terminals X\A; G has none. No terminal acquires an outgoing identity step.
For the integer interface, 1<D<N and N≥3 imply 1/N+1/D≤1/3+1/2<1. The reciprocal readings are exactly N,D. MAIN admission is exactly D|N; G is geometrically legal with its own floor quotient, and Q has its own divisibility permission. This argument does not restrict the full carrier to reciprocal integer points.
The cell I_nd uses (1/(n+1),1/n] in each coordinate. These cells form a disjoint Borel partition of X, including all assigned upper endpoints. Empty cells cause no exception or additional object.

## 3. Complete actual inverse domains and images

For target a=(u,v)∈X and fixed q≥0, set δ_q=1−qv and θ_q(a)=(v,u)/δ_q. Direct substitution gives both F_qθ_q(a)=a and θ_qF_q(z)=z whenever the respective positive denominators occur.
For MAIN retain exactly the labels d|n, q=n/d, for which δ_q>0 and θ_q(a)∈I_nd. For G retain every n,d with q=floor(n/d) and the same reconstruction tests. Their source guards and forward equalities then hold; conversely any predecessor supplies exactly this label and reconstruction.
For Q the inverse is the swap θ(a)=(v,u), retained exactly when its own reconstructed labels satisfy d|n. No denominator or MAIN quotient is used for Q.
These are Borel partial inverse maps. Target outgoing legality is never imposed, so a target may be terminal and still have these predecessors. The strict simplex boundary remains outside X; no internal reciprocal cut is discarded.

An equivalent finite, target-dependent enumeration makes image completeness especially explicit. Define

\[
 R(a)=\frac{1-u-v}{v}>0,\quad
 N_q=\left\lfloor\frac{1-qv}{v}\right\rfloor,\quad
 D_q=\left\lfloor\frac{1-qv}{u}\right\rfloor.
\]

The reconstructed point belongs to X exactly when q<R(a): its coordinate sum is (u+v)/(1−qv)<1, which also ensures δ_q>0. On this range N_q,D_q≥1.
MAIN's complete predecessor set consists of θ_q(a) for integers 1≤q<R(a) satisfying N_q=qD_q. G's consists of θ_q(a) for integers 0≤q<R(a) satisfying floor(N_q/D_q)=q. A target is in the corresponding full image if and only if this finite set is nonempty.
The first reconstructed coordinate v/(1−qv) is strictly increasing in q. Distinct retained q therefore give distinct predecessors, and unique floor labels remove label duplication. MAIN has at most ceil(R)−1 predecessors, G at most ceil(R); these are bounds, not claims that every possible q is admitted.
For Q, Pre_Q(a)={ (v,u) } if floor(1/u) divides floor(1/v), and is empty otherwise. This also gives its complete image and global partial injectivity.
For example (2/5,2/5) has no MAIN or G predecessor: any predecessor must be diagonal, hence has q=1, whose reconstruction is (2/3,2/3)∉X. Thus totality of G is not surjectivity. No surjectivity is assumed in the history construction.

## 4. Every-Borel IMAGE and all-point clock versions

For F_q and θ_q, the fixed-label real derivative matrices are

\[
 DF_q=\begin{pmatrix}-qy/\lambda^2&1/\lambda\\1/\lambda^2&0\end{pmatrix},
 \qquad D\theta_q=\begin{pmatrix}0&1/\delta_q^2\\1/\delta_q&qu/\delta_q^2\end{pmatrix}.
\]

Their signed determinants are −λ^(−3) and −δ_q^(−3). Hence the inverse IMAGE density is J_q=δ_q^(−3)>0, finite at every actual target. At a source image, δ_q(F_qz)=1/λ, so J_q(F_qz)=λ³.
The maps F_q and θ_q are mutually inverse smooth maps on the corresponding open positive-denominator regions. Ordinary two-dimensional change of variables, restricted to any actual Borel branch domain E, gives μ(θ_q E)=∫_E δ_q^(−3)dμ. Source and image lie in X, so this is the original restricted μ, not a replacement measure.
This argument applies to every Borel E, including intersections with null reciprocal cuts. The fixed rational germ prescribes J at those points even though the measure law alone determines only an almost-everywhere version. No derivative of the floor function is taken.
For q=0 this is the ordinary swap with J=1. Q independently has the same swap derivative, signed determinant −1, J_Q=1 and the every-Borel law on its own restricted domains.
Therefore the actual one-step clocks are

\[
 \kappa_M(z)=-3\log(1+q_Mx)<0,\quad
 \kappa_G(z)=-3\log(1+q_Gx)\le0,\quad \kappa_Q(z)=0.
\]

G's equality set is exactly q_G=0, equivalently n<d. No κ is assigned to an outgoing MAIN/Q terminal step. Signed and zero clocks have not been replaced by positive roofs.

## 5. Full history owner, exact potential and branch-pair laws

All finite legal iterates are Borel. Refining by every finite label word gives countably many injective Borel history branches, with their complete inverse compositions; no common-history depth is truncated.
Thus G_T={(z,r−s,w):T^rz=T^sw legally} is a Borel groupoid with countable source/range fibres, retained lag, units (z,0,z), source w and range z. Inversion reverses the triple and lag.
For composable meetings T^rz=T^sw and T^uw=T^va, if u≥s the first equality legally extends by u−s, giving T^(r+u−s)z=T^va. If s≥u the second extends by s−u, giving T^rz=T^(v+s−u)a. The needed segment exists along the already-legal history of w. Both products have the summed lag; neither pads a terminal beyond its history. Associativity follows from addition and endpoint composition.
For every owner define the globally finite Borel function B(z)=3log σ(z). MAIN/G's exact σ identity and Q's preserved σ give, at every legal source including all cuts,

\[
 \kappa_T(z)=B(Tz)-B(z),\qquad
 S_r(z)=B(T^rz)-B(z).
\]

There is no log-zero boundary: σ>0 on the entire frozen X. If T^rz=T^sw, then

\[
 c(z,r-s,w)=S_r(z)-S_s(w)=B(w)-B(z).
\]

This proves full-point witness independence and additivity, even when witnesses meet on null cuts or at a terminal. In particular c(Tz,−1,z)=−κ(z). The clock is not generally zero merely because it is a coboundary.
On a refined branch pair mapping w to z through the common future, the forward/inverse chain rule gives IMAGE density exp(S_s(w)−S_r(z))=exp(−c)=(σ(z)/σ(w))³, valid for every Borel subset of its actual domain. The potential also shows that different witnesses for the same arrow give the same prescribed all-point density.

## 6. Planned global discriminator: MAIN and G

For MAIN, every legal step has q≥1 and x>0, so σ(T_Mz)<σ(z). A legal positive-period return is impossible. This excludes all eventual cycles as well, since such a history would contain an actual cycle.
For G, σ never increases. If q_G(z)>0, its first step strictly decreases σ, and the second cannot undo that decrease.
If q_G(z)=0, then n<d and the actual first step is the swap. The next reciprocal readings are exactly n'=d,d'=n, including all floor endpoints, so q_G(T_Gz)=floor(d/n)≥1. The second step strictly decreases σ.
G is total, hence σ(T_G²z)<σ(z) for every z∈X. A purported cycle would also return after an even number of steps, contradicting this strict two-step decrease. G has no eventual cycles.
These are global proofs, not finite period tests. They neither assert convergence of all infinite histories nor classify which MAIN histories terminate. G histories are infinite by totality; MAIN's legal finite/infinite alternatives remain governed by its actual admission.
For both M and G, every source isotropy group is {0}. Consequently every extension isotropy and entire return group H is {0}. This is stronger than merely finding no positive cycle in a window.

## 7. Q: entire legal two-step set, cores and terminal basins

One legal Q step requires d|n. The swap rereads labels d,n, so two legal steps require both d|n and n|d, equivalently n=d. This proves the entire two-step-legal set E={z∈X:n=d}; T_Q² is identity precisely there among legally two-step sources.
The fixed set is exactly {(t,t):0<t<1/2}. The entire least-two set is E\{x=y}. There are no other cycles: Q is a partial swap, and every legal source outside E reaches a terminal after one step.
More explicitly, all Q source orbits, including their incoming, fall into four disjoint types:

1. A fixed diagonal singleton has source isotropy Z. Its only predecessor is itself.
2. An off-diagonal equal-label pair {z,swap z} has source isotropy 2Z at either point. Its only predecessors are the other pair members, so it has no external ancestors.
3. A proper-divisibility source n=qd, q≥2, maps to its terminal swap. This two-point terminal basin has exactly that one nonunit forward arrow and its inverse; the original source has no predecessor. Both source isotropy groups are trivial.
4. When neither label divides the other, the point is terminal and has no predecessor; its source orbit is an identity-only singleton.

This is exhaustive: a terminal with n|d proper is the target in type 3; all remaining terminals are type 4. The equal-label case n=d=1 is empty in X, without creating an exceptional orbit.
On every Q arrow c=0. Its extension isotropy is therefore exactly its source isotropy, not automatically trivial. All H are {0}; fixed or two-cycle source isotropy does not create a positive physical return.
On an equal-label pair an arrow (z,k,w) exists exactly when z=swap^k(w); fixed singletons admit all k. Type-3 arrows have only the actual lags 0 and ±1, and type-4 only lag 0. This specifies the full retained lag rather than replacing Q by a globally periodic permutation.

## 8. Every incoming depth, full kernels and all real phases

For any owner let Pre_T be the complete finite predecessor operation in §3, Pre_T^0{a}={a}, and Pre_T^(j+1){a}=⋃_{b∈Pre_T^j{a}}Pre_T(b). Every generation is finite; all generations are retained.
Let L_T(z)={r≥0:T^rz is legal}. The full incoming arrows with range z are exactly

\[
 \{(z,r-s,w):r\in L_T(z),\ s\ge0,\ w\in\operatorname{Pre}_T^s\{T^rz\}\},
\]

with equal triples deduplicated. The union of these endpoints is the exact complete source orbit O_T(z). This formula gives membership for every depth, without an unproved uniform depth cutoff or a restriction to a core's original cell. For M/G the lag between any two connected points is unique because isotropy is trivial.
For a MAIN terminal τ its full basin is ⋃_{j≥0}Pre_M^j{τ}, with unique arrival depth d(z). It is its whole source orbit: a common future with τ must be τ itself. Its arrow from w to z has lag d(z)−d(w) and clock B(w)−B(z). Distinct terminal basins are disjoint. Q's terminal basins are exactly the finite cases already listed; G has none.
The full kernels, for all three actual owners, have the following exact all-arrow descriptions:

\[
 K_{\rm lag}=\{(z,0,w):\exists j\ge0,\ T^jz=T^jw\text{ legally}\},
 \qquad K_c=\{(z,k,w)\in G_T:\sigma(z)=\sigma(w)\},
 \qquad K_{\rm joint}=K_{\rm lag}\cap K_c.
\]

Together with the finite explicit Pre test and unrestricted history formula, these are complete predicates, not statements only about isotropy. Q's partial injectivity makes K_lag and K_joint its unit set, whereas K_c is all of G_Q. G's legal q=0 swap arrows exhibit nonunit clock-kernel arrows whenever n<d.
For M/G the restrictions of all three kernels to each isotropy group are trivial. For Q the clock-kernel restriction is the entire source isotropy, including Z or 2Z; the lag and joint restrictions are trivial. This separates full arrow kernels from isotropy kernels.
On the full extension, the canonical phase is h+B(z). Indeed (w,h) maps to (z,h+B(w)−B(z)), preserving this value. Every extension orbit over a source orbit O is exactly

\[
 \{(z,a-B(z)):z\in O\},\qquad a\in\mathbb R.
\]

This gives all real phases with no selector and no topological quotient assumption. Height translation sends a to a+t; thus its return group is exactly {0} on every extension-orbit class. For Q, B is constant on each source orbit and the same description is equivalently the unrestricted height h.
All three positive primitive packet ledgers are empty, so there is no positive primitive length or positive repetition law to attach. The Q source cycles and their nontrivial zero-clock extension isotropy remain explicitly present; they are not erased to reach that conclusion.

## 9. Bounded decision and preserved unknowns

MAIN owns its prescribed every-point Jacobian clock and full retained-lag Borel history structure, but its entire positive return ledger is empty. The precommitted nonempty-ledger requirement therefore fails: **STOP / FORK**. This is an actual MAIN conclusion; neither control supplies its proof or a replacement clock.
G and Q independently have the full classifications above and their own empty positive ledgers. Nonzero MAIN/G transport clocks remain; H=0 is not c=0. All source, terminal, null-cut and zero-clock distinctions are retained.
The permitted global discriminator and direct telescoping identity suffice. No longer period search, measure change, denominator tuning, added roof or endpoint repair was used. Strong naturalness, novelty/nonconjugacy and PROVES_TOO_MUCH are not proved. T3 is NOT AUDITED, classical fields N/A, formal coordinates UNASSIGNED, and Route B NOT INVOKED.
Only `evidence/independent-derivation.md` is written in this stage. After complete self-read and the frozen hash receipt, I HOLD for root's full raw reading and a distinct PAPER UNLOCK; no later manuscript claim will be backfilled into this raw.
