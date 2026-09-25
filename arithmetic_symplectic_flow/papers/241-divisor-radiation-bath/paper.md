# Conservative divisor-channel fields and the full primitive clock

**Paper ID:** `241-divisor-radiation-bath`  
**Candidate ID:** `ANG-20260918-DRB01`  
**Date:** 2026-09-18.  
**Status:** `ADVANCE — PRIME-ONLY FULL-FIELD PACKETS; PHYSICAL LOGARITHMIC CLOCK; NATURALNESS OPEN`.  
**Gates:** `T0 ESTABLISHED; T1 ENGINEERING POSITIVE / NATURALNESS OPEN; T2 ESTABLISHED; T3 NOT SUPPLIED`.  
**Independent review:** Separate model-assisted technical readback completed; see [review record](evidence/review.md).  
**Portfolio:** ADVANCE as a conservative-mechanism control; source-naturalness OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

The frozen all-integer oscillator/field system admits a continuous, complete,
two-sided mild action on its entire real Hilbert phase space and preserves its
displayed nonnegative Hamiltonian. On its full energy-one carrier, an active
proper-divisor channel excludes every periodic state: a nonzero temporal
harmonic would require a field response with a nonintegrable pole inside the
continuous frequency axis. This argument uses bounded frequency projections
and therefore covers mild states outside the strong generator domain.
Inactive channels are retained and have no nonzero exact periodic state.
Consequently the full carrier has exactly one primitive oriented packet for
each prime, no composite packet, and no stationary state. Actual primitive
times satisfy \(T_p=2\sqrt2\log p+O(1)\) with a uniform error and unchanged
time units; every repeat has time \(rT_p\). The coupling is a different
conservative realization of the divisor-symbol exclusion rule, but incidence
and the integer label remain static. An arbitrary Boolean incidence control
can select arbitrary zero-channel labels. Naturalness is therefore OPEN.
No decay, scattering, transfer operator, trace, zeta, determinant, classical
finite-dimensional suspension, or formal Route result is supplied.

## 1. Candidate identity and scope

Every claim below concerns the unchanged version-one
[candidate card](candidate-card.md). The admission under
[SCJ01](../240-source-clock-joint-frontier/candidate-card.md) is a bounded
conservative-mechanism control, not a new arithmetic source-law solution.

| Item | Same-object owner | Status |
| --- | --- | --- |
| Carrier | Entire \(M=\coprod_{n\ge2}\{H_n=1\}\) in the frozen Hilbert spaces | Full, no state restriction |
| Action | Exact scalar equations and field Duhamel formula in the card | Complete mild action, Proposition 1 |
| Hamiltonian structure | Frozen real weak symplectic form and strong generator domain | Strong Hamiltonian identity; no claim of an everywhere defined Hilbert-valued vector field |
| Arithmetic | Every proper trial-divisor channel, with static incidence \(\varepsilon_{n,d}\) | Frozen divisor symbols act on actual field coordinates |
| Clock | Actual time in the full equations | Derived on surviving packets |
| Packets | All nonconstant full-state periodic orbits modulo time translation only | Full classification, Propositions 2–3 |
| Classical base / roof / mapping torus | None | NOT APPLICABLE |
| Operator / trace / zeta / determinant | None | NOT SUPPLIED |
| Later contact / quantum owner | None | NOT SUPPLIED |

The lineage is proper-divisor symbolic exclusion, followed by all-channel
conservative oscillator/field coupling. The integer is not an evolving scan
register. The source is not claimed to generate a sequential sieve, nor to be
conjugate to a historical Logistic or Hénon map. The rational well is shared
as a formula with [171](../171-separatrix-witness-hamiltonian-clock/candidate-card.md),
but its four-dimensional flow and its return map are different owners.
The clock is rederived here after the complete field classification.

## 2. Exact definitions and claim boundary

For fixed \(n\ge2\), set

\[
\mathfrak h=L^2((0,\infty),(1+\omega)d\omega;\mathbb C),\qquad
X_n=\mathbb R^2\times\mathfrak h^{n-1},\qquad
D(M_\omega)=\{z\in\mathfrak h:\omega z\in\mathfrak h\}.
\tag{1}
\]

All spaces are regarded as real phase spaces when forming Hamiltonian
derivatives. Write \(\varepsilon_d=\varepsilon_{n,d}\), where
\(\varepsilon_1=0\) and \(\varepsilon_d=\mathbf1_{\{d\mid n\}}\)
for \(2\le d<n\), and define

\[
c=c_n=1+n^{-2},\quad W(q)=\frac{4q^2}{(1+q^2)^2},\quad
f(\omega)=e^{-\omega},\quad g(\omega)=\omega f(\omega),\quad
y_d=z_d+\varepsilon_d qf.
\tag{2}
\]

The frozen Hamiltonian and equations are

\[
H_n=\frac{p^2}{2}+cW(q)+\sum_d\|\sqrt\omega\,y_d\|_{L^2}^2,
\tag{3}
\]
\[
\dot q=p,\qquad
\dot p=-cW'(q)-2\sum_d\varepsilon_d
\operatorname{Re}\int_0^\infty g\bar y_d\,d\omega,
\qquad i\dot z_d=\omega z_d+\varepsilon_d qg.
\tag{4}
\]

The field equation means, for every initial field in \(\mathfrak h\),

\[
z_d(t)=U_tz_d(0)-i\varepsilon_d\int_0^tU_{t-s}q(s)g\,ds,
\qquad U_tz(\omega)=e^{-i\omega t}z(\omega).
\tag{5}
\]

The integral is a Bochner integral in \(\mathfrak h\), with its oriented
meaning for negative \(t\). Neither an outgoing condition nor a field-phase
quotient is part of (1)–(5). Generalized monochromatic distributions are not
Hilbert states. No coupling coefficient, counterterm, energy, or time unit
will be changed in the proof.

The strongest result is an exact full-state periodic ledger for this
engineered conservative carrier. It is not a scattering theorem, a
source-naturalness theorem, a stability theorem, or a trace construction.
The word "radiation" names the continuum-field architecture; no decay of
oscillator energy or existence of asymptotic scattering states is asserted.

## 3. Complete mild owner and conserved energy

### Proposition 1. Global action on every full Hilbert component

Equations (4)–(5) define a unique continuous two-sided group action on every
\(X_n\). The Hamiltonian (3) is preserved for all mild states. Its full
level \(H_n=1\) is invariant and is a regular Hilbert hypersurface. The
given weak symplectic form represents the Hamiltonian equation on the strong
domain; no strong-domain restriction is imposed on the mild carrier.

**Proof.** Use the product Hilbert norm on \(X_n\). The operators
\(U_t\) are isometries of \(\mathfrak h\), are strongly continuous by
dominated convergence, and have generator \(-iM_\omega\) with the stated
domain. Both \(f\) and \(g\) belong to \(D(M_\omega)\).
The real functional in the scalar force is bounded because

\[
\left|\int g\bar z\,d\omega\right|
\le \left(\int\frac{|g|^2}{1+\omega}\,d\omega\right)^{1/2}
\|z\|_{\mathfrak h}.
\tag{6}
\]

The rational function \(W''\) is bounded on \(\mathbb R\): its
denominator has no real zero and it tends to zero at infinity. Hence the
nonlinear remainder \(B\), obtained by removing the free field generator
from (4), is globally Lipschitz on \(X_n\). Its terms are \(p\), the
globally Lipschitz scalar \(-cW'(q)\), finitely many bounded linear
field functionals and linear counterterms, and the vectors
\(-i\varepsilon_d qg\). The Lipschitz constant may depend on \(n\).
Moreover \(B(0)=0\).

For completeness, let \(S_t\) be the identity on \((q,p)\) and
\(U_t\) on every channel. The equation

\[
x(t)=S_tx_0+\int_0^tS_{t-s}B(x(s))\,ds
\tag{7}
\]

is a contraction on continuous paths over a sufficiently short interval,
using \(L_n|t|<1\). Iteration gives a unique local solution, while
Gronwall gives

\[
\|x(t)\|\le e^{L_n|t|}\|x_0\|,\qquad
\|x(t;x_0)-x(t;\widetilde x_0)\|
\le e^{L_n|t|}\|x_0-\widetilde x_0\|.
\tag{8}
\]

The same construction in negative time gives existence on every finite
interval. Uniqueness and autonomy give the group law and inverse at
\(-t\). Estimate (8), together with strong continuity of \(S_t\),
gives a jointly continuous action. The scalar variables are continuously
differentiable and \(q\) is twice continuously differentiable.

If all initial fields lie in \(D(M_\omega)\), write
\(w_d(t)=U_{-t}z_d(t)\). The forcing
\(-i\varepsilon_d q(t)U_{-t}g\) is continuous in the graph norm of
\(D(M_\omega)\). Thus (5) preserves this domain and gives
\(z_d\in C(D(M_\omega))\cap C^1(\mathfrak h)\).
Here \(y_d\) also lies in the domain and

\[
\dot y_d=-i\omega y_d+\varepsilon_d pf.
\tag{9}
\]

The energy is a continuously differentiable real function on the whole
\(X_n\), since \(z\mapsto\sqrt\omega z\) is bounded from
\(\mathfrak h\) into ordinary \(L^2\). On a strong solution,

\[
\frac d{dt}\|\sqrt\omega y_d\|_2^2
=2\varepsilon_d p\operatorname{Re}\int g\bar y_d\,d\omega.
\tag{10}
\]

The free term has zero real part: it is \(-i\int\omega^2|y_d|^2\),
an absolutely defined imaginary number on the strong domain. Summing (10)
cancels the coupling terms in \(p\dot p+cW'(q)\dot q\), proving
energy conservation there.

To pass to arbitrary mild data, replace each initial field by
\(\mathbf1_{[1/R,R]}z_d(0)\), leaving its scalar initial coordinates
unchanged. These initial data are strong-domain data and converge in
\(X_n\). They evolve under the **full unchanged equations**, not a
truncated generator or a truncated set of channels. Estimate (8) gives
uniform convergence of the corresponding solutions on compact time
intervals. Continuity of \(H_n\) then gives conservation for the original
mild solution. The approximating energies need not equal one; this density
argument is performed in the ambient \(X_n\), before restricting to its
invariant energy-one level.

For the Hamiltonian identity, the field form
\(2\operatorname{Im}\int\bar u v\) is continuous and nondegenerate
on the real \(\mathfrak h\), but weak relative to its weighted norm.
On the strong domain, substitution of
\(\dot z_d=-i\omega y_d\) gives
\(\iota_{X_H}\Omega=dH_n\), including the scalar terms in (4).
The energy derivative need not possess a representing Hamiltonian vector
in \(\mathfrak h\) outside that domain. An everywhere smooth
Hilbert-valued vector field, or a global mild symplectomorphism theorem,
is not claimed.

Finally, \(dH_n=0\) forces \(p=0\) and \(y_d=0\) in every
channel: vary each field by itself in the positive quadratic form, or
test against arbitrary compactly supported frequency variations.
The remaining scalar derivative is \(cW'(q)\), whose zero set is
\(q=0,1,-1\), because

\[
W'(q)=\frac{8q(1-q^2)}{(1+q^2)^3}.
\tag{11}
\]

These critical configurations have energy \(0\) or \(c_n>1\).
Therefore one is a regular value. This proves the hypersurface assertion
and completes the proof. ∎

With the disjoint-union topology, these component actions form a continuous
action on \(X\) and on all of \(M\); no uniform-in-\(n\) norm bound is
needed. The transformation groupoid \(M\rtimes\mathbb R\) therefore
belongs to this same action. This statement supplies no groupoid trace.

## 4. Full periodic-field obstruction, including mild states

### Lemma 2. A free Hilbert field has no nonzero positive-time return

If \(U_Tv=v\) for \(T>0\) and \(v\in\mathfrak h\), then \(v=0\).

**Proof.** The equality implies
\((e^{-i\omega T}-1)v(\omega)=0\) almost everywhere. The zeros of
the multiplier on \((0,\infty)\) form a countable set. Lebesgue measure,
including the weight \(1+\omega\), gives that set measure zero. ∎

### Proposition 2. An active divisor channel excludes every return on energy one

If some \(\varepsilon_d=1\), there is no positive-time periodic state
on \(H_n=1\), stationary or nonconstant.

**Proof.** Suppose the full mild state has period \(T>0\), and set
\(\nu=2\pi/T\). Define temporal Fourier coefficients by

\[
q_k=\frac1T\int_0^Tq(t)e^{ik\nu t}\,dt,\qquad
Z_{d,k}=\frac1T\int_0^Tz_d(t)e^{ik\nu t}\,dt\in\mathfrak h.
\tag{12}
\]

These are Bochner coefficients for the fields. Their existence uses
continuity of the full mild orbit, not membership in the strong domain.
Let \(P_R\) be multiplication by \(\mathbf1_{[1/R,R]}\). Projecting
(5) gives a continuously differentiable equation with bounded frequency
generator on \(P_R\mathfrak h\). Integration by parts in this bounded
equation, using the equality of its endpoints, yields

\[
(M_\omega-k\nu)P_RZ_{d,k}
=-\varepsilon_d q_kP_Rg.
\tag{13}
\]

Taking integer \(R\) tending to infinity covers \((0,\infty)\), so
for almost every \(\omega\),

\[
(\omega-k\nu)Z_{d,k}(\omega)
=-\varepsilon_d q_kg(\omega).
\tag{14}
\]

For an active channel and any \(k\ge1\), if \(q_k\ne0\), this
requires
\(Z_{d,k}=-q_kg/(\omega-k\nu)\) off the resonant point. Since
\(g\) is continuous and strictly positive at \(k\nu>0\), its
squared weighted norm diverges on every sufficiently small interval
around that point. An assignment at the single point cannot repair this
divergence. This contradicts \(Z_{d,k}\in\mathfrak h\).
Thus \(q_k=0\) for all \(k\ge1\). Since \(q\) is real,
\(q_{-k}=\overline{q_k}\), and uniqueness of the Fourier coefficients
of a continuous periodic function gives \(q(t)=q_0\) for all \(t\).
For example, its Fejér means all equal \(q_0\) and converge uniformly
to \(q\).

Now \(p=\dot q=0\). For every channel, active or inactive,
\(y_d=z_d+\varepsilon_d q_0f\) solves the free mild equation;
this follows directly from (5) and \(g=M_\omega f\).
Periodicity and Lemma 2 force \(y_d=0\). The scalar force therefore
reduces to \(-cW'(q_0)\), which must vanish. The only possibilities
are \(q_0=0,1,-1\), with the full fields

\[
z_d=-\varepsilon_d q_0f,
\qquad H_n=cW(q_0)\in\{0,c_n\}.
\tag{15}
\]

None lies on \(H_n=1\). This also rules out all constant-\(q\)
periodic states and all stationary states in the asserted scope. ∎

The proof does not assume a one-sided radiation condition or loss of total
energy. A nonlinear periodic source is excluded by its exact harmonics in
the complete conservative field, not by an assertion that trajectories
must decay. A composite has at least one proper divisor and hence an active
channel; labels \(4\) and \(6\) are included without separate tuning.

## 5. Complete prime ledger and actual repetitions

### Proposition 3. Exactly one primitive packet on each prime component

On the full energy-one carrier there is exactly one nonconstant primitive
oriented orbit per prime \(n\), no composite orbit, and no stationary
state. Its field coordinates all vanish, its scalar coordinates traverse
the central energy oval, and its least physical period is

\[
T_n=4\int_0^{A_n}\frac{dq}{\sqrt{2(1-c_nW(q))}},\qquad
A_n=\sqrt{c_n}-\sqrt{c_n-1}.
\tag{16}
\]

Every positive return time on that orbit is a positive integer multiple
of \(T_n\); the \(r\)-fold repetition has time \(rT_n\).

**Proof.** For a prime \(n\), all incidences vanish. Every field is
free. Full-state periodicity and Lemma 2 force each of the retained
\(n-1\) fields to vanish, including the single inactive field at \(n=2\).
This is a derived condition, not the initial carrier. The scalar energy
is then exactly

\[
\frac{p^2}{2}+c_nW(q)=1.
\tag{17}
\]

The potential is even, increases from zero to \(c_n\) on \([0,1]\),
and decreases to zero on \([1,\infty)\). Its energy-one turning
points on the positive axis are
\(A_n\in(0,1)\) and
\(B_n=\sqrt{c_n}+\sqrt{c_n-1}=A_n^{-1}>1\).
The allowed scalar energy set consists of the central oval
\(|q|\le A_n\) and two outer components \(|q|\ge B_n\).
The turning points are simple by (11).

The central oval is regular, connected and compact, and its nonzero
Hamiltonian velocity traverses it as one orbit. Four successive quarter
traversals give (16); the turning-point square-root singularities are
integrable. A smaller positive return would have to complete less than
one traversal of this regular oriented oval and cannot return to the same
\((q,p)\). The crossing with negative momentum is part of the same
orbit, not a second orientation choice. The outer components each have
only one turning point and continue to spatial infinity; their motions
cannot form a closed trajectory. The complete ambient existence proof
already covers their full evolution.

There is no scalar equilibrium on (17). For completeness, a stationary
state in any component must satisfy the same configurations (15), whether
or not an active channel exists; none has energy one. Proposition 2
excludes every composite. All field states and every scalar branch have
therefore been accounted for. Time translation is the only quotient.
Traversing the resulting oval \(r\) times gives exactly \(rT_n\),
and every return requires such an integer number of traversals. ∎

In particular, a prime-power label \(n=p^a\), \(a\ge2\), is a
composite component with no packet. An \(a\)-fold traversal of the
prime component is a repetition of its one packet; it is not an orbit on
the separate label \(p^a\). This distinction prevents a multiplicity
change by relabelling. No transverse monodromy or Floquet-hyperbolicity
claim is made for the infinite-dimensional field.

## 6. The physical logarithmic clock

### Proposition 4. Uniform prime-period asymptotic in the original time units

The periods in (16), for every actual prime packet, satisfy

\[
T_n=2\sqrt2\log n+O(1),
\tag{18}
\]

with an error bounded uniformly over integers \(n\ge2\) in the
corresponding scalar integral. For composite labels this comparison
integral is not the period of an orbit of the full candidate.

**Proof.** Set \(c=1+n^{-2}\) and
\(\delta=\sqrt{(c-1)/c}=1/\sqrt{n^2+1}\). On the first quarter
of the inner oval let

\[
y=\frac{1-q^2}{1+q^2},\qquad
q=\sqrt{\frac{1-y}{1+y}},\qquad
a(y)=\frac1{(1+y)^{3/2}(1-y)^{1/2}}.
\tag{19}
\]

Then \(-dq/dy=a(y)\), the endpoints are \(y=1,\delta\), and
\(1-cW(q)=c(y^2-\delta^2)\). Thus the same physical time integral is

\[
T_n=\frac4{\sqrt{2c}}I(\delta),\qquad
I(\delta)=\int_\delta^1\frac{a(y)}{\sqrt{y^2-\delta^2}}\,dy.
\tag{20}
\]

Since \(0<\delta\le1/\sqrt5<1/2\), split the integral at \(1/2\).
On \([0,1/2]\), \(a(0)=1\) and \(a'\) is bounded, so for one
constant \(L\),

\[
\left|\int_\delta^{1/2}
\frac{a(y)-1}{\sqrt{y^2-\delta^2}}\,dy\right|
\le L\int_\delta^{1/2}\frac{y}{\sqrt{y^2-\delta^2}}\,dy
\le L/2.
\tag{21}
\]

On \([1/2,1]\),
\(\sqrt{y^2-\delta^2}\ge y/\sqrt5\ge1/(2\sqrt5)\), and
\(a\) is integrable at its only endpoint singularity \(y=1\).
That part of \(I\) is uniformly bounded. Consequently

\[
I(\delta)=\operatorname{arcosh}(1/(2\delta))+O(1)
=\log(1/\delta)+O(1)=\log n+O(1).
\tag{22}
\]

The second equality follows directly from
\(\operatorname{arcosh}x=\log(x+\sqrt{x^2-1})\) on the present
range \(x\ge\sqrt5/2\); its difference from \(\log(2x)\) is
uniformly bounded. Finally
\(4/\sqrt{2c}=2\sqrt2+O(n^{-2})\), and
\(n^{-2}\log n\) is bounded. Equations (20)–(22) prove (18). ∎

No logarithmic roof was supplied and no time rescaling was used. The
coefficient \(2\sqrt2\) remains part of the result. The argument proves
logarithmic-size physical time, not the exact identity \(T_p=\log p\).
The barrier excess \(n^{-2}\) and energy one remain declared all-integer
design choices; deriving their period does not make those choices canonical.

## 7. Controls, adverse findings and limitations

| Control | Exact consequence or boundary |
| --- | --- |
| Prime label 2, with its retained inactive field | Lemma 2 forces that field to zero on any return; the central oval remains one packet |
| Prime-power 4 and mixed composite 6 | Each has an active channel; Proposition 2 rules out all positive-time returns on energy one |
| Every inactive channel | Retained throughout; a periodic free field must vanish, rather than being projected away |
| Constant oscillator / possible stationary states | All fields shift to \(-\varepsilon_d qf\), then \(q=0,\pm1\); energies are 0 or \(c_n>1\), outside this carrier |
| All incidences set to zero as a separate comparator | The proof of Proposition 3 gives one packet for every integer, including composites |
| Replace each complete incidence row, including its neutral channel, by arbitrary Boolean channel data as a separate comparator | Exactly the all-zero rows admit one packet; every row with an active channel has none by the unchanged resonance argument |
| Constant barrier \(c>1\) as a separate comparator | Every admitted label has the same scalar energy-one period; no growth in \(n\) follows |
| Remove barrier excess, setting \(c=1\), as a separate comparator | The central energy-one level is separatrix rather than a nonconstant periodic oval; stationary states at \(q=\pm1\) now have energy one |
| Change fixed energy as a separate comparator | For \(0<E<1\), the prime inner periods approach a finite limit as \(c_n\to1\); for \(E>1\), sufficiently large labels have \(c_n<E\) and no bounded scalar oval |
| Full conservative owner | Total Hamiltonian is preserved for every mild state; no dissipative reduction or outgoing restriction was used |

The arbitrary-incidence control is a `PROVES_TOO_MUCH` warning: the same
field selection mechanism can realize an arbitrary chosen zero-row set.
In the actual frozen candidate that set is fixed by ordinary divisibility,
but the dynamics does not explain why this source graph, energy or rational
barrier should be privileged. Source-naturalness remains OPEN. The change
from static witness-modified force to reciprocal continuum coupling is a
specific conservative-mechanism result, not a solution of SCJ01's stronger
source-law question.

The energy-change row follows from the same scalar branch classification:
below the limiting barrier the simple inner turning points remain separated
from \(\pm1\), giving continuous finite period; above the barrier there
is no bounded component. These comparison choices are not changes to DRB01.

The construction does not prove that a typical composite trajectory
radiates to infinity, converges to an equilibrium, or has a scattering
state. Absence of exact periodic states is a weaker statement. Approximate
recurrence is also unclassified. The result does not construct a
finite-dimensional return map, invariant Liouville probability, stability
ledger, trace or analytic continuation. The weak-form/strong-domain
Hamiltonian identity is not promoted to an everywhere smooth vector field
or an unproved mild symplectic-flow theorem.

## 8. Gate assessment and decision

| Owner-level gate | Result for ANG-20260918-DRB01 | Boundary |
| --- | --- | --- |
| T0 | ESTABLISHED: full continuous global mild action, conserved full energy carrier, exact strong Hamiltonian identity and transformation groupoid | Energy hypersurface in a weak symplectic Hilbert ambient space; classical ASFS fields NOT APPLICABLE |
| T1 engineering source/clock | ESTABLISHED in the frozen design: divisor incidence selects returning prime components and actual times obey (18) | Static incidence and engineered barrier/energy; source-naturalness OPEN; no exact log-prime identity |
| T2 | ESTABLISHED: exactly one primitive oriented packet per prime, no composite or stationary state at energy one, every repeat has time \(rT_p\) | No stability or scattering statement |
| T3 | NOT SUPPLIED | No operator, trace, zeta, determinant or continuation result |
| Formal Route coordinates | UNASSIGNED | No classical A0–A2 or formal Route evaluation |
| Route B | NOT INVOKED | No quantum owner |

**Decision: advance** the completed conservative-mechanism control and end
this bounded audit. Its decisive positive gate is full-state field resonance:
unwanted returns are excluded while the prime oscillator packets survive
with their own physical times. The same-object ledger remains intact.
The search for a source-changing, naturally forced arithmetic law must
**fork** from the disclosed static-incidence design; neither this control
nor earlier negative records contribute transferable Route credit.

## Evidence, reproducibility and disclosure

- [Frozen card and unchanged-object result](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence record and review state](evidence/README.md)
- [Package overview](README.md)

All mathematical inputs are (1)–(5) and the all-integer divisibility rule.
The derivations above are exact; there was no numerical orbit cutoff,
simulation, fitting, spectral computation or prime-table input. Frequency
projections occur only as proof devices: in initial-data density and in
the bounded derivation of the temporal harmonic identity. The final claims
retain the full continuous frequency axis.

This Markdown research record was developed with AI assistance. Author
derivation and author-assisting checks are not independent peer review.
Separate model-assisted mathematical review is recorded in the
[evidence review](evidence/review.md); it is not external peer review or
a correctness certificate. No publication, human
participant study, personal-data processing, or external submission is
part of this package. Data availability: all definitions and proofs are in
this package; there are no empirical data. Human authorship/contribution,
funding and conflict-of-interest declarations are not supplied; no human
attribution or declaration is inferred. No venue criteria or submission
readiness is claimed.
