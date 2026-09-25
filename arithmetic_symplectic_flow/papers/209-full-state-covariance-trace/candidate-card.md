# Full-state covariance regularization of the actual quotient flow

**Paper ID:** 209-full-state-covariance-trace  
**Candidate ID:** AQC-20260916-QCV01  
**Version:** 1, frozen 2026-09-16 before the new proof.  
**Initial status:** FROZEN — FULL-STATE COVARIANCE AND ACTUAL-FLOW TRACE OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## One retained owner and the exact new question

Retain the complete geometry of [194](../194-rapid-decay-cone-completion/paper.md)
and the fixed scalar Hilbert representation of
[204](../204-quotient-orbit-feature-hilbert/paper.md), including every support,
the original topology, the actual time and the exact Hilbert norm. The
arithmetic source is the all-positive-integer monoid algebra e_m e_n=e_mn,
its nonunit ideal I and Q=I/I^2; the nonzero atom classes q_a are derived,
not supplied as a prime table. In particular

    E={v: sum_a a^k abs(v_a)<infinity for every integer k>=0},
    P_hat={v in E:v_a>=0 for all a} minus {0},
    Dv=(a v_a), X_hat=P_hat/<D>, phi_t[v]=[exp(t)v].

The existing section is m(u)=1, c(u)=sum_a u_a/a,
F(u)=D^(-1)u/c(u), tau=-log c. Singleton circles have actual least
period log a and all positive repetitions; mixed states are not periodic.
Classical finite-dimensional symplectic, contact, Hamiltonian and quantum
fields are NOT APPLICABLE / NOT SUPPLIED. This card supplies no new roof.

204 fixes theta by m(D^(-theta(v))v)=1, w=D^(-theta)v,
g_0=1, g_*=exp(2 pi i theta), g_a=w_a, beta_0=beta_*=1/4,
beta_a=2^(-a), rho(t)=exp(-abs(t))/2. Its exact coefficient kernel
is quotiented to obtain H of actual bounded continuous functions. Write
k_x=kappa(.,x) for its evaluation vector, inner product linear first:

    kappa(x,y)=sum_j beta_j integral g_j(phi_r x) conj(g_j(phi_r y)) rho(r)dr,
    R_t f=f o phi_t, ||R_t||<=exp(abs(t)/2), B_0=sum_j beta_j<=1.

H, its kernel and norm do not depend on a spectral parameter. The new
question is whether an explicitly fixed full-support sampling covariance
on this same H is injective trace class and produces an actual-flow trace,
and, if so, what that trace does and does not encode about closed orbits.

## Frozen sampling rule, not an invariant measure

List every nonzero finite-support vector with positive rational nonzero
coordinates. Represent it uniquely by a tuple
(a_1,p_1,q_1,...,a_d,p_d,q_d), where a_1<...<a_d are derived atoms,
v_(a_i)=p_i/q_i, p_i,q_i are positive coprime integers. Order tuples first
by integer height a_d+sum_i(p_i+q_i), then lexicographically, with a
proper prefix first. Every height level is finite. Let v_n be that list,
n>=1, x_n=[v_n], and

    mu=sum_(n>=1) 2^(-n) delta_(x_n).

Deck-equivalent repeated x_n remain in the list; they are not silently
deduplicated. This is a declared representation design, not a natural
arithmetic invariant probability. Density must be proved in the original
all-norm quotient topology. A dense sampling list is not a deletion of
unsampled infinite-support states from X_hat or from H.

On the unchanged H propose the genuine rank-one series

    C f=sum_(n>=1) 2^(-n) <f,k_(x_n)> k_(x_n),
    A_t=R_t C,  T(t)=Tr(A_t), t in R.

Prove the exact convergence class, positivity, injectivity, density of
range, and whether range(C) still separates every state. The trace must
be derived on H; it cannot be borrowed from 201's weighted-return space.
Check the kernel order/conjugation in its formula and continuity in t.
No commutation of C with R_t, preservation of constants by C, or algebra
closure is assumed. Do not claim unsmoothed R_t is trace class.

## Decisive arithmetic and adverse controls

Evaluate the kernel on an actual singleton circle and compare it with
the genuine least period and repetition convention. Check whether the
trace contains mixed-state terms and whether it localizes on closed
orbits. A continuous regularized correlation is not automatically the
atomic positive-time periodic-orbit distribution. No prime-power weight
is added to C to force agreement.

As controls only, compare full-support probabilities
(1-epsilon)mu+epsilon delta_([q_2]) and
(1-epsilon)mu+epsilon delta_([q_3]), 0<epsilon<1, without changing the
frozen candidate mu. Test whether their zero-time traces distinguish
representation choice from source-clock necessity. Give a generic
bounded continuous RKHS control for PROVES_TOO_MUCH. The lineage is
proper-factor symbolic admissibility -> indecomposable all-integer
source -> completed positive geometry -> actual-flow observables;
no claimed Logistic/Henon conjugacy or natural-source theorem is added.

Stop this contract at its exact covariance/trace result and the scoped
arithmetic mismatch. If density, faithfulness or trace convergence fails,
record that failure without changing the measure, norm or flow. An
intrinsic localized/distributional trace, invariant regularizer, limit
removing C, Euler determinant or continuation requires a new card.
Naturalness remains OPEN; formal Route coordinates remain UNASSIGNED.

## Ownership and process

Root owns only this new package plus eventual navigation integration.
One different actual invocation reviews the final four core files; it
is nonblind model review, not human peer review. The research controller
owns separate time-smoothing screens and the Round22 portfolio. Numbers
209--212 and the proposed IDs were absent in read-only checks before
this freeze; reservations do not require creating extra papers.

ARS is used only for bounded claim/evidence/reasoning and adverse
controls under the approved research question, not a full paper pipeline
or scoring/interview workflow. Writes use apply_patch and stay Markdown.
Old packages, guidance, mirrors, other streams and Git/config state stay
read-only. Root performs the integrated verification after writers stop.

## Appended outcome under unchanged version-1 inputs

**Status:** ADVANCE — INJECTIVE FULL-STATE TRACE-CLASS REGULARIZATION; SCOPED STOP AS AN UNREGULARIZED CLOSED-ORBIT TRACE; NATURALNESS OPEN.

The rational quotient list is dense in the original topology. Its exact
covariance is positive, injective and trace class with dense range that
still separates every state. Actual R_t C has the kernel-correlation
trace in the paper, continuous and uniformly bounded in real time.
The true prime-circle frequency survives, but mixed states contribute
and full-support sampling controls change the trace without changing
any periodic orbit. This continuous trace is not the atomic positive-
time closed-orbit distribution. No measure, norm, state, clock or source
was changed; no unregularized trace, 201 determinant, natural-source
result or formal Route coordinate was obtained. Stop this contract at
the proved regularizer and scoped mismatch; further localization needs
a new card.
