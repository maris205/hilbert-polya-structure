# Arithmetic continuation: frozen contracts

Date: 2026-09-07 UTC. Owner: arithmetic lane. This is the same C419–C423
batch, with two previously admitted contracts left untouched. At most two
new precise candidates may be screened here. This file is written before
any new finite arithmetic diagnostic or long proof. No paper number,
admission, manuscript, formal evaluation, GPU run or external model call
is authorized by this lane's scouting contract.

## ED1 — Full-image duplication Lattès prime distribution

**Family.** All elliptic curves `E/Q` with full 2-adic Galois image
`rho_E,2(G_Q) = GL_2(Z_2)`. This condition, not an arbitrary list of curves
or known proper images, defines the family. Fix E before taking a prime
limit. In a short Weierstrass model `y^2 = x^3 + Ax + B`, the map is

`L_E(x) = (x^4 - 2 A x^2 - 8 B x + A^2)/(4(x^3 + Ax + B))`.

Only good odd primes are counted. The domain is the entire projective
line `P^1(F_p)`, including infinity and poles. The clock is one ordinary
iterate of this degree-four quotient of `[2]`; all periodic points are
ordinary distinct points, never local scheme length or weighted traces.

**Observable.** `r_E(p) = #Per(L_E,P^1(F_p))/(p+1)` and the empirical
probability measure of these values over good odd primes at most X.

**One paper-level question.** Determine an explicit universal weak limit
for the entire family, with a complete, proved joint valuation law

`(v_2 det(I-g), v_2 det(I+g)),  g Haar-uniform in GL_2(Z_2)`,

including every atom, dependency between the valuations, exceptional
zero-determinant sets, tail control, and the pushforward under
`(a,b) -> (2^(-a)+2^(-b))/2`. A mere invocation of Haar pushforward,
an isolated mean, finite congruence tables, or Bell's existing formula
is not a completed substantive contract. A full proof can still fail
the independent-content gate if the residual is only a short corollary.

**Imported ownership.** Bell et al. own the exact finite-field Lattès
periodic-proportion formula and its Hasse error. Finite-layer Chebotarev
owns equidistribution in Galois images. Local C382 owns the Gaussian CM
Frobenius mechanism; the previous `arithmetic/CM_DENSITY_PROOF.md` owns
the CM prime weak-law and tail argument. None is relabelled as new.
Recent work on elliptic finite-group distributions, joint quadratic
twists, Lattès densities and 2-adic Galois images must also be subtracted.

**Cheap decisive checks, frozen before execution.** First derive the
joint law by residue classes modulo 2 and any necessary stationary
recursion. Then at most enumerate `GL_2(Z/2^k Z)` for `k <= 4`, with
valuation >= k explicitly censored; compare exact rational masses only.
A contradiction of an alleged residue law kills that formula. A short
routine residue calculation after the imported inputs kills ED1 as a
paper candidate even if its theorem is true. No asymptotic proof is
inferred from these finite checks.

**Success / replacement.** Success requires a genuinely substantial
joint classification not already owned and a complete proof with the
prime-limit passage. If primary collision or mathematical simplicity
leaves only a short classical corollary, reject ED1 and freeze exactly
one materially different arithmetic subtype below before investigating
or computing that subtype. The second candidate is not yet selected.

**Target boundary.** This source-side distribution supplies no target
Euler factors, root number, automorphy, zero correspondence or
Hilbert–Pólya realization. `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.

## ED1 early residual decision

The hand derivation found that the full-image joint generating function
reduces to the three conjugacy types in `GL_2(F_2)`, then the sixteen
classes in `Mat_2(F_2)` for the identity branch. The only infinite input
left there is the standard one-variable random determinant distribution.
ED1 is therefore rejected as a substantial independent paper, subject to
checking the displayed screening calculation, not because its conjectured
weak law is false. No arbitrary proper-image table will be substituted.

## ED2 — Uniform prime decay for the Basilica polynomial

Frozen after the ED1 residual decision and before external ED2 searches,
new ED2 calculations, or a proof attempt. This is the second and final
candidate of this lane; it is not another elliptic or Galois-image table.

**Family / domain / clock.** The fixed polynomial `b(x)=x^2-1` over Q,
and equivalently its Q-rational projective conjugates after excluding
their finitely many model primes. The native domain is the entire
`P^1(F_p)` at every odd prime p, infinity included. One iterate is one
time unit; counts are ordinary distinct periodic points. The critical
orbit `0 -> -1 -> 0` is retained, not perturbed into a generic disjoint
critical-orbit family.

**One complete paper-level question.** Prove or refute the existence of
an absolute, effectively obtainable C and p0 such that, for every prime
`p >= p0`,

`#Per(b,P^1(F_p))/(p+1) <= C / log(log(p))`.

The logarithms are natural and p0 must make the denominator positive.
This is an all-prime quantitative statement, not merely liminf zero,
prime-average zero, a density-one subset, or a fixed inverse-tree level.
The proposed mechanism is uniform contraction of fixed-point proportions
in all arithmetic Frobenius cosets of the Basilica iterated-monodromy
tower, combined with explicit genus/degree control at growing level.
Inverse-tree fixed points must be connected to native forward periodic
points by an actual image-set inequality; they are not the same counts.

**Subtracted classical inputs.** Deduct existing arithmetic/geometric
iterated-monodromy groups, known fixed-point-proportion limits and
finite-field Chebotarev/image-set estimates. In particular, inspect the
exact postcritical hypotheses and the quantifier order in the closest
Jones / Bridy–Jones–Kelsey–Lodge / Pink / Juul literature before using
any theorem. An immediate specialization of an existing uniform theorem
is a rejection, not an admission.

**Cheap decisive falsifier.** First inspect the arithmetic-coset
classification and its exceptional branches. A proved positive limiting
periodic density along any infinite prime sequence refutes this contract.
An exact known theorem with the stated bound owns it and rejects the new
candidate. A finite prime sample cannot refute or prove an asymptotic
bound with unspecified C and p0, so no forward prime census is planned.
A short inverse-tree check is permitted only after a precise claimed
coset recurrence has been frozen, and never certifies a growing-level
Chebotarev estimate.

**Success / stop.** A complete proof must establish the uniform coset
bound and the growing-level error with constants. If the available
argument controls only one fixed level at a time or only a density-one
set of primes, retain that gap and reject admission. Do not weaken the
theorem silently, add a third candidate, write a manuscript, or assign
an evaluation. This remains source arithmetic only, with every target
claim and Route-B claim absent.

## Final lane disposition

ED1: no admission because the explicit full joint law has only a short
residue-calculation residual after imported ownership is deducted. The
single frozen diagnostic passed; it does not certify novelty.

ED2: no admission because the all-arithmetic-coset quantitative bound
and growing-level prime error are unclosed. No counterexample to the
frozen theorem is claimed, and no weaker theorem is substituted.

The two-candidate allowance is exhausted. See
[SCOUT_REPORT.md](SCOUT_REPORT.md) and [SOURCE_AUDIT.md](SOURCE_AUDIT.md).
