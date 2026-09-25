# Source-transit card — ASFS-20260915-SGC01

**Version:** 1, 2026-09-15; frozen before the construction audit.  
**Initial status:** P0 HYPOTHESIS — FULL FLOW, PACKETS AND CLOCK OWNERSHIP OPEN.

This contract tests a uniform geometric timing assumption for an actual
finite divisor scan. It does not claim the arithmetic source uniquely forces
that assumption. The full state space, including all nonperiodic states, is
fixed before the audit.

For every integer n>=2 set L_n=n-1, let d=1,...,L_n be cyclic, and define
w(n,d)=1 if 2<=d<n and d divides n, and w(n,d)=0 otherwise. Set

\[
M=\coprod_{n\ge2,\,1\le d<n}\mathbb R^2_{n,d},\qquad
\omega=dq\wedge dp,
\]
\[
f_{n,d}(q)=q+\tfrac12\tanh q+L_n w(n,d),\qquad
F(n,d,q,p)=\left(n,d^+,f_{n,d}(q),p/f'_{n,d}(q)\right).
\]

Freeze the same universal transit law on each scan interval: dr/dt=r,
starting at r=d and ending at r=d+1. Its proposed roof is

\[
\tau(n,d,q,p)=\int_d^{d+1}\frac{dr}{r}
=\log\frac{d+1}{d}.
\]

The full flow carrier is the endpoint-glued suspension of exactly this F
and tau. Equivalently, use slabs (z,r) with d<=r<=d+1 and vector field
r partial_r: an internal endpoint is glued to (Fz,d+1), whereas the final
endpoint (z,n) is glued to (Fz,1). The final seam is a reset, not a
positive-time path from n back to 1. r is not asserted to be a global
real-valued observable on the quotient. Local collars must identify
r_new=r_old/n at the final seam so the vector field agrees there.

| P0 field | Frozen scope |
| --- | --- |
| Source lineage | Prime/composite divisor exclusion -> complete local finite scan with a neutral d=1 initialization interval -> bounded witness drift -> canonical cotangent lift |
| Allowed data | All integer n and d, ordinary divisibility, tanh and fixed coefficient 1/2, integer gain n-1; no prime list, factorization oracle, prime-specific coefficient or zero data |
| Changed owner | A new serial-scan map, phase set and geometric transit roof; 147/153 are comparisons, not suppliers of clock or trace credit |
| Geometric assumption | The same dr/dt=r on every real transit interval, plus the specified scan-reset gluing; this is a design assumption, not a derived symmetry of integer arithmetic |
| Non-Zeno test | Prove forward and backward accumulated roofs diverge on every full trajectory; a global infimum of zero does not by itself decide completeness |
| Coding | Actual integer, scan-phase and witness observations; no complete Markov coding or chronological cross-n sieve orbit claimed |
| Packets | Every intrinsic periodic point of the full F, all momenta and all integer fibres retained; modulo cyclic shift, no selected centres |
| Stability / repetition | Derive from full DF and actual accumulated transit times; do not transfer the dyadic K_n convention |
| Analytic proposal | Ordinary unweighted orbit Z only after complete primitive classification, normalized by Z(s)->1 as real s->+infinity; operator, function space, trace and Fredholm owner OPEN |
| Measure | Componentwise symplectic area; no finite normalization of canonical area is supplied, and no trace normalization is supplied |
| Controls | Remove witnesses; replace scan endpoint schedule/velocity; retain all momentum states; inspect the reset-edge clock cohomology; distinguish fixed-n completeness from global roof infimum |
| PROVES_TOO_MUCH | Generic nonnegative integer constraints can replace w; alternative positive velocities preserve the event skeleton but change time. Source-determined or privileged clock naturalness remains a separate obligation |
| Stop/fork | Stop at a failed global inverse, full packet, positivity, completeness or clock-ownership check. A changed velocity, gain, endpoint, carrier or operator requires a fresh card |
| Later owner / Route | Hamiltonian/contact/quantum DEFERRED; formal Route coordinates UNASSIGNED; Route B NOT INVOKED |

Two pre-P0 screens are retained as controls, not candidate credits: a true
log-scale coboundary cancels on a closed scan including its reset, whereas
positive dilation transit with a quotient seam is a distinct geometric
assumption. The audit must not confuse those objects. A cohomological
concentration of time on the reset edge does not by itself prove that this
explicit full construction is invalid, nor does a consistent construction
prove arithmetic naturalness.

## Audit result — version-1 tuple unchanged

**Status:** ENGINEERED PRIME-LOG FLOW UNDER PRESPECIFIED DILATION/RESET TIMING — ESTABLISHED; SOURCE-CLOCK NATURALNESS OPEN; STOP PROMOTION.

Under the prespecified dilation/reset timing, the [paper](paper.md)
proves the global symplectic inverse, the complete full-state suspension,
one hyperbolic primitive packet per prime, no composite periodic states,
and primitive times log p with all repetition conventions retained.
The owned ordinary product is the prime Euler product on Re s>1.

The roof identity tau=h(Fz)-h(z)+1_(d=n-1) log n, with h=log d,
remains an explicit adverse finding: the timing can be concentrated at
the reset edge. No proof derives the selected velocity, initialization
or seam from arithmetic alone. Source-clock naturalness is OPEN.

Portfolio: retain this engineered-clock control; stop promotion / fork
for the missing source-clock mechanism. Operator, trace and Fredholm
construction are NOT SUPPLIED. Formal coordinates remain UNASSIGNED;
Route B NOT INVOKED.
