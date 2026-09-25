# Coordinate clock conjugacy and the full cotangent determinant owner

**Paper ID:** 389-coordinate-clock-ownership.  
**Candidate:** ANG-AUDIT-20260922-CCG01; batch GEOMETRIC-RETURN-20260922-H, round 5/5.  
**Date:** 2026-09-22.  
Outcome: `CONDITIONAL CONJUGACY ESTABLISHED; COTANGENT CLOCK SUBSTITUTION STOP`
**Route:** conditional audit only; classical candidate fields NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED; T3 NOT AUDITED.

## Abstract

For a deterministic owner with a single-valued ambient branch Jacobian, coordinate and density changes add a coboundary to the point clock. The induced height map has a minus sign and conjugates the entire retained-lag extension without rescaling time. Closed-loop sums and physical stabilizers are unchanged, although the zero-clock kernel on unextended arrows need not be. A self-contained hard continued-fraction source supplies the probe, its intrinsic one-dimensional derivative and the complete 23 return class. Both coordinate controls preserve its least time. The analytic local cotangent lifts instead preserve full Liouville area: their full determinant clock is zero. Over the entire probe class only zero covectors are eventually periodic; every nonzero fibre is retained. This distinguishes clock owners, not a no-go theorem for conservative geometry.

## 1. Frozen input and conditional boundary

The [candidate card](candidate-card.md) comprises 54 original lines plus the pre-mathematics single-valued-Jacobian clarification through line 63. This entire prefix has SHA-256 19bee24c132e6e7c10c51825b0b934546bac5d811b25e23d2d4c37f6e1929633. It is the sole scientific input; no 385 result, other manuscript, raw proof or peer report is used. Root released mathematics after CP1.

Let X be the complete declared carrier inside a C1 manifold M, and F a deterministic, possibly partial map. Every actual inverse step has a specified local C1 diffeomorphism extension and a finite nonzero Jacobian relative to a fixed positive continuous volume density m. Only iterates that are defined are used. If overlapping extensions do not give one assigned Jacobian at each x, and no unique extension owner was frozen, the clock is NOT DEFINED and the conditional theorem does not start. No germ label is silently added to repair that defect.

Define the assigned point clock kappa(x)=-log J_m I_x(Fx) whenever Fx exists. An ambient derivative on a nonmanifold X is declared data unless shown intrinsic. It is not a probability or an ambient-Lebesgue IMAGE identity on X. The general theorem is pointwise and set-theoretic; unprovided measure or regularity properties of the carrier are not inferred.

| Owner | Data and scope |
| --- | --- |
| General clock | Fixed density, actual inverse-step Jacobian and deterministic point dynamics |
| Coordinate controls | Same entire carrier and branch data transported by phi; target density stated explicitly |
| Source arrows | Actual triples (z,k-l,w) with F^k z=F^l w; equal triples identified, lag retained |
| Extension | All X times R and every declared clock arrow; height translation on the orbit SET |
| Probe | Complete hard continued-fraction coding and standard dx branch clock |
| Cotangent control | Entire local cotangent maps, all real fibre coordinates and Liouville area |
| Missing geometry | No global symplectic map, T*X manifold, Hamiltonian flow or analytic owner asserted |

## 2. Coordinate and density coboundaries, with the height-map sign

Let phi be a C1 diffeomorphism between the relevant ambient domains, and let m' be a fixed positive continuous target density. Write
\[
B(x)=\log J_{m,m'}\phi(x),\quad F'=\phi F\phi^{-1},\quad
I'=\phi I\phi^{-1}.
\]
Here J_(m,m')phi is defined by phi^*m'=J_(m,m')phi times m; in charts it is the target density at phi(x), times |det Dphi(x)|, divided by the source density at x. All quantities are finite and positive at the actual points; no global bound is assumed.

**Theorem 1 (point-clock transformation).**
\[
J_{m'}I'(\phi Fx)=
e^{B(x)-B(Fx)}J_mI(Fx),\qquad
\kappa'(\phi x)=\kappa(x)+B(Fx)-B(x).
\tag{1}
\]

**Proof.** Apply the chain rule to phi composed with I composed with phi^(-1), including the source and target density ratios. The factors of phi are its Jacobians at the predecessor and tail, respectively; taking the negative logarithm gives the sign in (1). Because endpoints and the assigned old Jacobian are fixed, overlapping permitted extensions still agree after transport. QED.

If m'=phi_*m, then J_(m,m')phi=1 and B=0: every step is exactly the same metric clock in new coordinates. Choosing standard target-coordinate volume is a different declared metric choice and generally gives nonzero B. Independently, changing density on the same domain to m_tilde=e^R m gives kappa_tilde=kappa+R composed with F-R. This is (1) with phi the identity; it is not a time-unit rescaling.

For A_n=sum_(i<n)kappa(F^i x), A_0=0, the full lag owner is
\[
G=\{(z,k-l,w):F^kz=F^lw,\ k,l\geq0\},\qquad
c(z,k-l,w)=A_k(z)-A_l(w).
\]
Padding both witnesses adds identical common-tail sums, proving that c is well-defined. For composition, align the middle exponents to their maximum and cancel the middle A-sum. Determinism ensures that any needed padding exists even for a partial map: the identical common-tail point has the same available forward iterates. Thus c is additive; units have value zero and inverses negate it.

**Theorem 2 (entire extension conjugacy).** Under the source-arrow bijection
(z,n,w)->(phi z,n,phi w),
\[
c'(\phi z,n,\phi w)=c(z,n,w)+B(w)-B(z).
\tag{2}
\]
The height map is
\[
\Phi(x,h)=(\phi x,h-B(x)).
\tag{3}
\]
It maps every old arrow (w,h)->(z,h+c) to the corresponding new arrow and commutes with height translation by the SAME real time.

**Proof.** Summing (1) gives A'_k(phi z)=A_k(z)+B(F^kz)-B(z). The two equal common-tail terms cancel, proving (2). The new target height from source height h-B(w) is h-B(w)+c+B(w)-B(z)=h+c-B(z), exactly (3) at the old target. The inverse height map adds B at phi^(-1)x'. Each value is finite; unbounded B near a missing endpoint does not obstruct this bijection. QED.

The full lag kernel is unchanged under this bijection. In contrast, the preimage of ker c' is precisely {g=(z,n,w):c(g)=B(z)-B(w)}, not automatically ker c. Its intersection with the lag kernel adds n=0. Thus an isomorphism of extensions does not assert equality of the zero-clock subgroupoids on unextended arrows.

## 3. Closed loops, complete isotropy and signed clocks

An actual point has nontrivial source isotropy exactly when it is eventually periodic. If its least eventual period is d, every isotropy lag is a multiple of d and every multiple occurs by shifting past the preperiod. Write L for the sum of kappa over that least cycle; then c(x,kd,x)=kL. If no eventual cycle exists, source isotropy is trivial. These statements include transient incoming states and partial maps whose forward histories terminate.

Keeping all real heights, the extension isotropy is source isotropy intersected with ker c: it is trivial when L is nonzero, and all dZ when L=0. On the orbit SET the physical stabilizer is
\[
H_x=c(G_x^x)=
\begin{cases}L\mathbb Z,&x\text{ is eventually periodic},\\
\{0\},&x\text{ is not eventually periodic}.
\end{cases}
\tag{4}
\]
Equality of [x,h+s] and [x,h] requires an arrow with both endpoints x, proving (4). For an entire source orbit, connecting arrows identify height offsets modulo exactly H_x; all incoming points and all height phases therefore give R/H_x, as a set with translation action.

For signed clocks, a nonzero L gives least positive physical time |L|; oriented source repetitions have sums kL. If L=0, H={0}: physical height translation has no positive period, despite nontrivial extension isotropy. It does not become an R stabilizer. No positivity, uniform lower bound or classical suspension is inferred from the conditional construction.

Equation (2) has no boundary term on isotropy. Hence source isotropy, its clock values, extension isotropy, the entire H and all primitive/repetition times are preserved by (3). All legal incoming histories are transported, not just a cycle chart. Closed loops cannot acquire a different time solely through the coordinate/density operation specified in Theorem 1.

## 4. The hard Gauss probe, with intrinsic coding and derivatives

Take every sequence a=(a_i) with a_i>=2 and a_(i+1) dividing a_i+1. Its point is x=[0;a_0,a_1,...] in U=(0,1/2). For a>=2 put I_a(y)=1/(a+y). On [0,1/2] these maps have Lipschitz constant at most 1/4. Successive finite compositions give nested intervals with diameters at most (1/2)4^(-n), and hence a unique limit for every infinite word. Each tail is strictly positive, so x=1/(a_0+y) lies strictly between 1/(a_0+1/2) and 1/a_0.

The digit is therefore recovered as floor(1/x)=a_0 and the next tail is Fx=1/x-a_0. An infinite path cannot represent a rational: the Euclidean reciprocal-remainder procedure on a positive rational terminates, whereas every declared tail stays positive. Digit recovery proves injectivity and that shifting is exactly F. Common-prefix contraction proves continuity of the coding; successive digit recovery away from the interval endpoints proves continuity of its inverse. This independently identifies the whole carrier X with the stated symbolic source.

The actual inverse domain E_a comprises all tails whose first digit b divides a+1. There are finitely many such b>=2, so it is a union of full relative cylinders. Every preimage is exactly one of these insertions. Every tail beginning b has a legal predecessor 2b-1, so F is onto. Legal finite incoming words obey all their transitions and the final transition to the tail's first digit. Periodic words obey the same rule cyclically; no separate parity constraint is imported. Constants are not admissible, since a cannot divide a+1 when a>=2.

The environment extensions are the declared analytic diffeomorphisms
\[
I_a:U\to V_a=\left(\frac1{a+1/2},\frac1a\right),\qquad
f_a:V_a\to U,\quad f_a(x)=1/x-a.
\]
Their derivatives are also intrinsic to their actual one-dimensional source restrictions. To see this, every state has a branching successor choice immediately or one step later: if a+1 is composite it has at least two divisors >=2; if a+1 is prime p>=3, the next state p has the distinct successors 2 and p+1. Thus every cylinder, including every fixed first-digit inverse domain, has distinct histories converging to any specified history. Coding carries these to distinct convergent real points. Difference quotients along them force every C1 extension agreeing with I_a to have the same derivative at that point.

Consequently the standard-dx metric clock is intrinsically
\[
I_a'(y)=-\frac1{(a+y)^2},\quad f_a'(x)=-x^{-2},\quad
J_{dx}I_a(Fx)=x^2,\quad \kappa(x)=-2\log x>2\log2.
\tag{5}
\]
This is a metric Jacobian calculation, not a probability/IMAGE law on X. The general theorem permits signed steps; the probe's positivity in (5) is a separately proved property.

## 5. The entire 23 class, source periods and H

Both transitions are legal: 3 divides 2+1 and 2 divides 3+1. Put s=sqrt(15). Solving q_0=1/(2+q_1), q_1=1/(3+q_0) gives
\[
q_0=\frac{s-3}{2},\quad q_1=\frac{s-3}{3},\quad
q_0q_1=4-s,\quad
\Lambda=(4-s)^{-2}=31+8s>1.
\tag{6}
\]
Since 3<s<4, both points lie in U and are distinct; the source period is exactly 2. The intrinsic inverse Jacobian around either phase is (q_0q_1)^2=Lambda^(-1), while the full forward return derivative is Lambda. Thus
\[
L=\kappa(q_0)+\kappa(q_1)=\log\Lambda=2\log(4+\sqrt{15}).
\tag{7}
\]

Let O be every legal finite prefix followed by either q_0 or q_1 in coding. This is exactly the full source orbit: a common-tail equality gives such a prefix, and every such prefix gives an actual arrow. At EVERY point of O source isotropy is 2Z, c on it is kL, extension isotropy is trivial, and H=LZ. The entire class and all real heights give one R/LZ physical orbit; the two source phases are not separate packets. The r-fold traversal has time rL and source lag 2r. No numerical estimate or external source result enters these conclusions.

More generally every legal primitive cyclic word has its intrinsic coded least period and cycle sum from (5); all its incoming states have the same H by Section 3. No classification by an unrelated finite shift, full-phase-space census or prime dictionary is assumed.

## 6. Q1 and Q2: complete coordinate owners

**Q1.** Freeze phi_1(x)=x/(1+x), target U_1=(0,1/3) and standard dz. The entire conjugate carrier, branch domains and dynamics are phi_1 images, not selected subdomains. Here B_1(x)=-2log(1+x). With y=Fx and z=phi_1(y),
\[
I_a^{Q1}(z)=\frac{1-z}{a+1-az},\quad
J I_a^{Q1}(z)=\frac1{(a+1-az)^2},\quad
\kappa_{Q1}(\phi_1x)=2\log\frac{a+1+y}{1+y}.
\]
The last expression is positive on the probe. The full height map is h+2log(1+x), as required by (3). All closed sums, source/extension isotropy, incoming offsets, H and primitive repetitions are those of the original owner. For 23, H=LZ with exactly (7), not a new time.

**Q2.** Freeze phi_2(x)=x^2, target U_2=(0,1/4) and standard dz. Its derivative 2x is nonzero at every point but has no uniform lower bound near the missing endpoint 0. Here B_2(x)=log(2x), and
\[
I_a^{Q2}(z)=(a+\sqrt z)^{-2},\quad
J I_a^{Q2}(z)=\frac1{\sqrt z(a+\sqrt z)^3},\quad
\kappa_{Q2}(x^2)=\log\frac{y}{x^3}.
\]
The height map is h-log(2x), defined on every retained point despite its unbounded shift. On THIS hard source the next digit b satisfies b<=a+1, so y>1/(a+3/2), x<1/a and y/x^3>a^3/(a+3/2)>=16/7>1. Thus Q2's probe steps are also positive; this uses its admission rule and is not a conclusion for arbitrary conjugacies. All full-history conclusions of Sections 2--3 apply, giving exactly the same 23 H and repetitions.

For both controls, ker c on unextended arrows is governed by (2), not silently identified with the old ker c. The complete extensions and physical time actions are conjugate without scaling time. Their positive probe steps do not turn the fractal source or its noninvertible return map into a classical symplectic suspension.

## 7. C: complete local cotangent maps and the regularity boundary

For a local diffeomorphism f:V->W use every (q,p) in T*V, with
\[
\widehat f(q,p)=\bigl(f(q),p/f'(q)\bigr).
\tag{8}
\]
For a merely C1 f this is a homeomorphism, but it need not be C1; a pointwise differential determinant is not thereby supplied. At that regularity, full area-measure transport is still proved by Fubini: in the integral of a nonnegative Borel g(f(q),p/f'(q)), first substitute p=f'(q)P and then Q=f(q). The factors |f'(q)| cancel, giving the full Liouville-area integral on T*W. This transport statement is distinct from an everywhere differential determinant.

The actual f_a in this probe are analytic. Their lifts are therefore smooth, and
\[
D\widehat f=
\begin{pmatrix}f'&0\\-pf''/(f')^2&1/f'\end{pmatrix},
\quad\det D\widehat f=1,\quad
\widehat f^{\,*}(P\,dQ)=p\,dq.
\tag{9}
\]
Thus the complete local maps preserve the canonical symplectic form and Liouville area on ALL real fibres. Their full forward and inverse area Jacobians are one, and their full determinant point clock is exactly zero. For a generic conditional base branch, (9) requires additional regularity such as C2; none is silently added to the general C1 theorem.

This zero full-determinant clock is not (5). Its derivative includes the reciprocal fibre factor as well as the base factor. The zero section, projected derivative and full area determinant are different declared observables; naming them the same clock would replace the owner.

## 8. Every fibre return over the probe, actual lag and germ powers

For the two phases the analytic local base returns are
R_0(q)=(7q-3)/(1-2q) and R_1(q)=(7q-2)/(1-3q). Their derivatives at the corresponding q_j are Lambda. Cotangent composition obeys the ordinary derivative chain rule in (8), hence
\[
\widehat F(q_0,p)=(q_1,-q_0^2p),\qquad
\widehat F^{\,2}(q_j,p)=(q_j,p/\Lambda).
\tag{10}
\]
This holds for EVERY real p over both phases. The only fibre point fixed by any positive repeated return is p=0, because Lambda>1. It has actual least point period 2; each nonzero p has no point period. None is removed.

For every incoming z=I_u(q_j) with legal word u of length r, let A_r(z)=(F^r)'(z), a finite nonzero derivative. Then
\[
\widehat F^{\,r}(z,p)=(q_j,p/A_r(z)).
\tag{11}
\]
This includes every real incoming covector. Such a lifted point is eventually periodic exactly when p=0. Nonzero covectors remain nonzero and their later return values are distinct powers of Lambda^(-1). All source orbits over O are retained: at the reference phase q_0 their fibre classes are precisely p modulo p~Lambda^n p. There is one zero class and the full continuum of nonzero classes, with the other source phase and every incoming covector connected by (10)--(11).

For point-lag statements define only the actual lifted HISTORY restriction Y=X times R inside T*U, with deterministic map (Fq,p/f'_a(q)). This is not declared a symplectic manifold or a global symplectomorphism. Its inverse history branches are the restrictions of the complete local cotangent maps. Over O, its actual point-lag isotropy is 2Z at zero covectors and trivial at nonzero covectors. These follow from the full point returns, not merely from the projected base.

The full-area clock has c_C=0 on every defined lifted-history arrow. Its clock kernel is the whole actual groupoid; its lag kernel is equality after the same number of lifted steps, and the intersection equals that lag kernel. With ALL real extension heights retained, extension isotropy equals source isotropy: 2Z at the incoming zero covectors over O and trivial at nonzero covectors. Physical H_C={0} for every such point. Each complete source orbit gives an R of height phases with no positive physical period, not the base R/LZ.

The k-th local return germ has original forward lag 2k, not k. At (q_j,0) its derivative is diag(Lambda^k,Lambda^(-k)), so nonzero powers are not identity germs, although the point returns. At nonzero p the powers move the fibre and are not isotropy arrows at all. A germ-power owner and an actual point-lag owner must therefore be distinguished; point return never licenses collapsing the retained lag or asserting identity of the full local germ.

All fibre classifications in this section concern the full fibres over the probe class O and its actual incoming histories. No full-phase-space periodic classification outside that scope, global manifold gluing or T*X symplectic construction is asserted.

## 9. Audit decisions and non-inference boundary

| Owner / test | Established result | Boundary |
| --- | --- | --- |
| Conditional class | Equations (1)--(4), complete coordinate/density/height conjugacy | Single assigned finite Jacobian required; signed clocks allowed |
| Q1 | Full conjugate standard-coordinate metric owner; same L and H | Coordinate expression is not a new closed-loop mechanism |
| Q2 | Same conclusion with unbounded endpoint potential; actual hard-source positivity proved | No assumed endpoint lower bound, no global suspension claim |
| C | Analytic full cotangent determinant one, full-area clock zero; all probe fibres retained | This owner is not the one-dimensional metric clock |
| Regularity | C1 measure transport separated from pointwise differentiability | No automatic smooth cotangent lift of arbitrary C1 data |
| Route / analytic | Conditional T0--T2 audit only | Classical NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED; T3 NOT AUDITED |

**Decision:** retain the conditional conjugacy theorem and STOP the substitution of the full cotangent determinant for the one-dimensional clock. A coordinate/density change satisfying the theorem does not alter a closed-loop time. A changed metric/action/unstable-direction observable can be studied only with its own exact owner and obligations; it is not ruled out here. No statement that all conservative or higher-dimensional realizations fail follows.

The next screening use is concrete: first verify a single-valued Jacobian owner, then the closed-loop coboundary and the height-map sign; for a lift, compare the full-dimensional observable and every retained fibre return before transferring any packet claim. Strong naturalness remains OPEN. This is a class audit, not a new main candidate.

## Reproducibility and final-round handoff

The full 63-line card was read through its clarification before proof. The author retained earlier shared research context but read no 385 new result, main, raw or peer material. An isolated author-side helper checked the same-card cotangent return and regularity issue; it is not the separate review. All formulas are exact, with no scientific numerical run, external source lookup, target fitting, PDF, upload or Git write.

Model-assisted internal work is shared-history NOT_CALIBRATED. ARS's bounded evidence/claim discipline is retained; criteria_binding_unavailable, with no venue-readiness assertion. Data availability: the card and proofs contain all inputs and methods. Ethics: no human/animal subjects or personal data. Contributions: AI-assisted formal analysis and writing, without assigning human authorship. Funding/conflicts: no declarations supplied; absence is not presumed.

This is round 5/5. After root integration and CP2/CP3, hand off and await the user; no sixth round is authorized.
