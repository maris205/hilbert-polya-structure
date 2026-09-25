# RCZ01 — independent analytic derivations for the full controls

Audit ID: `ANG-AUDIT-20260921-RCZ01`.
Unchanged flow family / frozen controls: `ANG-20260921-RCF01`.
Status: `OWN CONTROL ANALYTICS COMPLETE; NO SCALAR FREDHOLM IDENTIFICATION`.
Date: 2026-09-21.

## 1. Exact input, ownership and access

The new scientific input is only the complete original 192 lines of the
[349 analytic card](../candidate-card.md), SHA-256
`7549da0db82ad6b260ce91dbebde484ce8d6045f92b7672f467900a5fdc9366e`.
Its three control tuples exactly repeat the tuples proved in the author's
[348 control derivations](../../348-reeb-contact-refinement/evidence/control-derivations.md).
That retained 483-line proof was hash-checked, not newly reread in this task:
`e7c1e52468338ce2ae7555652219c55eb8b874b3beb2de4e45ce6a39fa646fb3`.
It supplies complete own basins, full quotient topology, physical flows,
volumes and return groups, not a MAIN analytic theorem.

The relevant identity check is literal: FACTOR-OFF changes only singleton
refinement to singleton identity and keeps scaled geometry/Phi; DRIFT-ONLY
keeps C/S/G and uses Psi; UNIT-HOLONOMY replaces source geometry by identity
and keeps C/beta/Phi. The scalar prescriptions below are applied separately
to each full quotient with its descended contact volume, not atlas-counting
pushforward, a selected periodic subsystem, or a new Hilbert space.

No MAIN manuscript, new MAIN conclusion or 349 peer result was read. The
original card itself contains certified348 MAIN input lemmas; they were
read as part of the full card but are not analytic proof inputs below.
The retained348 proof includes its disclosed auxiliary check; no new
auxiliary agent was used in349. Thus this is shared-history, inherited-model,
nonblind internal AI derivation, `NOT_CALIBRATED`, not external peer review,
cross-model verification, independent-error assurance or formal checking.

The author reread the complete ARS 3.22.0 router and retained the already
fully read deep-research workflow, DA/logical-fallacy and runtime instructions
from348. Local AGENTS/plan authority is retained from that full read; plan's
unchanged SHA-256 was checked as
`9fa4aade2ca5e71077a70b3aa78b82378795d25fbb1007158f0d21297c1431a0`.
The current registry was not opened, to avoid unintended MAIN-result access.
The raw-contract, derivation and adverse checks remain bounded to this task.
No external source, numerical experiment, new flow/bundle/space, Git action,
PDF, upload or formal Route evaluation is used. Only this file is writable.

## 2. Retained complete control geometry and ordinary operators

Use u=log q, v=q*xi and the full real transverse pair (v,z). The original
348 proof establishes beta wedge d beta=du dv dz=dq dxi dz everywhere.

FACTOR-OFF has an isolated empty component R^3, a gcd=1 component R^3,
and, for every integer n>=2, a component

    Q^F_n=(R/(log n)Z) x R^2,
    Phi^t(theta,v,z)=(theta+t,exp(t)v,exp(-t)z).                 (A1)

Its line components have the same formula with real first coordinate.
Its ONLY primitive physical orbit in each Q^F_n is v=z=0, of length
L_n=log n. There are no physical closed orbits in either line component
or at any nonzero transverse point. Each incoming word's actual phase is
[u-A(w)]_(log n), where A(w) is the sum of log heads along its finite
history to its core. This has already been proved on the full quotient;
the present integral does not count those histories again.

DRIFT-ONLY has one terminal R^3 component and one atom-r component

    Q^D_r=(R/(log r)Z) x R^2,
    Psi^t(theta,v,z)=(theta+t,v,z).                              (A2)

EVERY transverse pair (v,z) labels a distinct primitive circle of length
log r. The terminal component has no return. UNIT-HOLONOMY has one R^3
per main word basin (terminal or atom), with Phi as in (A1) but real u;
it has NO physical closed orbit anywhere. Source lag isotropy Z in its
atom basins, and in FACTOR-OFF's gcd=1 basin, remains source data only.

On every full control, physical flow preserves the descended volume nu.
Consequently the specified U_t f=f composed with flow^(-t) extends
uniquely from C_c^infinity to a unitary operator on the SAME L2(Q,nu),
with inverse U_(-t). For compactly supported smooth f, small-time pullbacks
have support in a common compact set and converge uniformly to f; dominated
convergence, density and unitarity also give strong continuity if needed.

NONE of these U_t, at ANY real t, is an ordinary trace-class operator.
For a direct proof, take a normalized orthonormal sequence of smooth bumps
with disjoint supports in any one R^3 chart. Its unitary images remain an
orthonormal sequence, with no norm-convergent subsequence. Thus U_t is not
compact, whereas every trace-class operator is compact. This is an ordinary
classical pullback test, not a generator-spectrum or quantization claim.

The scalar Schwartz kernel with respect to nu is exactly the frozen
delta at flow^(-t)(x). It has no amplitude twist. The following positive-time
diagonal calculation is separate from ordinary operator trace class.

## 3. FACTOR-OFF ordinary orbit zeta: every integer primitive remains

Its complete primitive set gives, initially for Re s>1,

    G_F(s)=log Z_F(s)=sum_(n>=2) sum_(k>=1) n^(-k*s)/k,
    Z_F(s)=product_(n>=2) (1-n^(-s))^(-1),
    D_orb,F(s)=exp(-G_F(s)).                                    (A3)

Here n is an intrinsic gcd-core label after the full orbit classification,
not a representative chosen from a larger primitive family. Composites are
not deleted. If sigma=Re s>1, then

    sum_(n,k) |n^(-k*s)|/k
      <= (1-2^(-sigma))^(-1) sum_(n>=2) n^(-sigma) < infinity.   (A4)

This bound, uniform on closed half-planes sigma>=1+epsilon, proves absolute
and local uniform convergence, legitimate rearrangement and a nonzero
holomorphic Z_F. The derivative series is bounded in the same way by a
constant times sum_(n>=2)(log n)n^(-sigma). Hence

    -Z_F'(s)/Z_F(s)=D_orb,F'(s)/D_orb,F(s)
      =sum_(n>=2,k>=1) (log n)n^(-k*s)
      =integral exp(-s*t) Theta_orb,F(dt), Re s>1.               (A5)

The absolute domain in (A3) is EXACTLY Re s>1: its k=1 subseries diverges
absolutely when sigma<=1. The integral in (A5) has the same exact absolute
abscissa, since that subseries is sum (log n)n^(-sigma). Both Z_F and
D_orb,F tend to 1 as Re s tends to positive infinity, uniformly in Im s.

### 3.1 Colliding lengths add; they never identify orbits

The uncombined length distribution is

    Theta_orb,F=sum_(n>=2,k>=1) (log n) delta_(k log n).          (A6)

For any compact positive-time interval [a,b], n^k<=exp(b) leaves only
finitely many n and k; thus (A6) is locally finite. To express collisions,
let N>=2 and write its unique atom factorization with exponents e_1,...,e_d.
Set h(N)=gcd(e_1,...,e_d). Then

    a(N)=sum_(k|h(N)) 1/k,
    b(N)=(log N)*a(N),
    Theta_orb,F=sum_(N>=2) b(N) delta_(log N),
    G_F(s)=sum_(N>=2) a(N)N^(-s), Re s>1.                      (A7)

Indeed n^k=N iff k divides every exponent, and log n=(log N)/k.
Each contribution retains its actual primitive n and repetition k. For
example at log 4, the primitive n=4 and second traversal of primitive n=2
give total weight log 4+log 2; they are two different orbit/repetition data.
Equation (A7) is derived from the full ledger, not inserted arithmetic weights.

### 3.2 OPTIONAL NONCORE: a self-contained, bounded continuation

This completed supplement is not part of the controls' completion gate and
does not support any extra MAIN or Route claim. No further extension is planned.

No external analytic continuation theorem is needed here. Define
A(w)=sum_(n>=2)n^(-w) initially for Re w>1. Counting n<=x and integrating
term by term gives

    A(w)=1/(w-1)-w*integral_1^infinity {x}x^(-w-1) dx.           (A8)

Since 0<={x}<1, the integral and all its local parameter derivatives
converge uniformly on compact subsets of Re w>0. Thus (A8) gives a
meromorphic continuation there, with its only pole at w=1, residue 1.
This argument verifies the needed continuation directly; no standard
named-function theorem or zero data is imported.

Absolute rearrangement in (A3) gives

    G_F(s)=sum_(k>=1) A(k*s)/k, Re s>1.                         (A9)

Use (A8) for the finitely many low k terms to continue (A9) to

    Omega_F={Re s>0} minus {1/j:j=1,2,...}.

On a compact set Re s>=delta>0, all sufficiently large k have k*delta>1,
and their original series satisfies

    |A(k*s)|<=2^(-k*delta)*(1+2/(k*delta-1)).                    (A10)

The resulting uniform exponential tail proves normal convergence of (A9)
on Omega_F. It defines a single-valued meromorphic logarithm on Re s>0
and hence holomorphic nonzero continuations Z_F=exp(G_F), D_orb,F=exp(-G_F)
on Omega_F. Near s=1/j,

    G_F(s)=1/(j^2*(s-1/j))+a function holomorphic near 1/j.      (A11)

Only the k=j term has this pole; the remaining normally convergent terms
are analytic there. Both exponentials have ESSENTIAL singularities at
every 1/j, not poles or removable singularities. This is a justified
continuation of this integer-primitive control, not an assertion of a
global meromorphic zeta or an ordinary Fredholm determinant. No continuation
through Re s=0, its accumulating exceptional point, is claimed.

## 4. FACTOR-OFF joint scalar diagonal and flat-determinant FUNCTION

On a cylinder of length L=log n, use local circle difference coordinates.
For U_t, flow^(-t)(theta,v,z)=(theta-t,exp(-t)v,exp(t)z). Its joint
time/space diagonal is governed near a return T=kL>0 by the three equations

    t-T=0, (exp(-t)-1)*v=0, (exp(t)-1)*z=0.                     (A12)

The derivative in variables (t,v,z) at (T,0,0) is invertible, with absolute
determinant

    W(T)=|(1-exp(-T))*(1-exp(T))|
        =exp(T)+exp(-T)-2>0.                                   (A13)

This proves the JOINT diagonal restriction exists by an ordinary local
change of variables for delta distributions. It is not obtained by assuming
an orbit formula for the trace. The induced local distribution is

    delta_(T)(t)*delta_0(v)*delta_0(z)/W(T).

Integrating the remaining actual circle coordinate with volume dtheta
contributes its full length L, exactly once. Away from this zero set the
restriction is zero. On the two line components the equation u-t=u has no
solution for t>0, so their restriction is also zero everywhere. Thus

    Theta_0,F=sum_(n>=2,k>=1) (log n)/W(k log n) delta_(k log n)
             =sum_(N>=2) b(N)/(N+N^(-1)-2) delta_(log N).        (A14)

The same finite n,k bound as for (A6) proves positive-time local finiteness
after pushforward over the FULL noncompact quotient. The transverse delta
already localizes to (0,0); no integration of an infinite transverse volume
or atlas sheet count has been substituted. This includes all colliding
lengths, all incoming phases and both free line components.

Only now define the frozen flat-determinant function. Since

    1/W(k log n)=n^(-k)/(1-n^(-k))^2,

its logarithm is

    F_0(s)=-log D_0,F(s)
       =sum_(n>=2,k>=1) n^(-k*(s+1))/(k*(1-n^(-k))^2).         (A15)

Its EXACT initial absolute domain is Re s>0. For sigma>0, use
(1-n^(-k))^(-2)<=4 to dominate by 4*G_F(sigma+1). For sigma<=0,
the k=1 absolute subseries dominates sum_(n>=2)n^(-(sigma+1)), which
diverges. Normal convergence and the corresponding derivative bounds
prove that D_0,F is holomorphic and nonzero on Re s>0, tends to 1 as
Re s tends to infinity, and satisfies

    D_0,F'(s)/D_0,F(s)=integral exp(-s*t) Theta_0,F(dt),
    Re s>0.                                                    (A16)

The right side has the same exact absolute domain; its k=1 terms contain
the additional positive factor log n. The original /t integral defining
D_0 is exactly (A15), since (log n)/(k log n)=1/k; there is no new clock.

For Re s>0, expanding x/(1-x)^2=sum_(j>=1)j*x^j and using absolute
convergence yields the useful OWN identity

    F_0(s)=sum_(j>=1) j*G_F(s+j),
    D_0,F(s)=product_(j>=1) D_orb,F(s+j)^j
            =product_(n>=2,j>=1)(1-n^(-(s+j)))^j.               (A17)

All products in (A17) are normally convergent functions, not operator
determinants. The following continuation is OPTIONAL NONCORE, already
derived with Section 3.2 and unnecessary for the control verdict. To
continue farther, retain the continued j=1 factor from
Section 3.2. For j>=2 and Re s>-1, one still has Re(s+j)>1; those factors
have a normally convergent logarithm by the exponential large-j bound.
Consequently D_0,F has a justified holomorphic nonzero continuation to

    Omega_0={Re s>-1} minus {1/k-1:k=1,2,...}.                  (A18)

At s=1/k-1 it has an essential singularity: its logarithm has principal
part -1/(k^2*(s-(1/k-1))), from the j=1 term alone. The other factors
are holomorphic and nonzero there. No stronger continuation is claimed.

The scalar and ordinary objects do NOT agree. At the first return log 2,
W(log 2)=1/2, so Theta_0,F has coefficient 2 log 2 whereas Theta_orb,F
has log 2. Equivalently along real sigma tending to infinity,

    2^sigma*G_F(sigma)->1, 2^sigma*F_0(sigma)->2.                (A19)

For example, bound all n>=3 terms by the integral comparison used in
(A10), and all k>=2 terms by a geometric tail; after multiplication by
2^sigma both tails vanish. Thus D_0,F and D_orb,F cannot be the same
normalized holomorphic function. The mismatch is the actual transverse
Jacobian, not an omitted coincident-length contribution. It is not repaired.

## 5. DRIFT-ONLY: both ordinary counting and scalar diagonal fail

Every atom r has the full primitive family gamma_(r,v,z), (v,z) in R^2,
all of length log r. The ordinary frozen log-zeta includes, already at k=1,

    sum_((v,z) in R^2) r^(-s).                                  (A20)

For every finite complex s the summand is a fixed NONZERO number. The net
of finite subfamily sums is not Cauchy: arbitrarily many new transverse
pairs add an arbitrarily large multiple of that same number. Thus there
is no absolute or unordered ordinary series at ANY s, and no initial
holomorphic Z_orb,D_orb to continue under the frozen prescription.
No enumeration, representative per atom or transverse probability measure
has been authorized. This conclusion does not define a zeta equal to zero,
infinity or a regularized function.

The positive length-counting sum also fails to be a distribution: any
nonnegative test function h with h(log r)>0 receives infinitely many equal
positive contributions (log r)h(log r). Even an arbitrarily large finite
subfamily proves unboundedness; it is used to disprove local finiteness,
not to select the orbit set. The terminal component contributes nothing
but cannot cure this failure. Collisions across other lengths cannot cancel
an infinite positive mass already present at one primitive length.

The OWN scalar kernel is not the hyperbolic kernel in Section 4. Locally
on the r-cylinder it is

    delta_circle(theta_y-theta_x+t)
       *delta(v_y-v_x)*delta(z_y-z_x).                          (A21)

At a positive return t=k log r, its diagonal equations have only the time
constraint; the two transverse difference equations vanish identically.
Their joint derivative has rank 1 rather than 3. Concretely, approximate
the two-dimensional transverse delta by epsilon^(-2)*rho(./epsilon),
where rho is smooth, nonnegative, mass 1 and rho(0)>0. This family converges
to the original OFF-diagonal kernel distribution. On the diagonal, however,
pairing near t=k log r with a nonnegative compactly supported spatial test
chi and h(k log r)>0 gives

    epsilon^(-2)*rho(0)*h(k log r)*integral chi dnu,

which tends to positive infinity when integral chi>0. This is a local
obstruction even before integrating an infinite transverse plane. It
shows why the unregularized diagonal pullback in the frozen prescription
is not defined; the delta equations cannot be replaced by an isolated
orbit weight. The approximate identity is only a proof of failure, not
a new regularization prescription or a redefined operator.

Therefore Theta_0,D is UNDEFINED under the specified joint scalar diagonal
prescription, and D_0,D is NOT DEFINED: its prerequisite Theta_0 has failed.
There is no legitimate scalar determinant function here to compare with
an ordinary orbit zeta. U_t itself remains a well-defined volume-preserving
unitary classical operator, but that does not create either failed trace.
The non-Reeb property of Psi for beta was already proved in348 and is not
used to manufacture this analytic obstruction.

## 6. UNIT-HOLONOMY: empty physical closed ledger, not empty source data

Each full quotient component is R^3. The physical inverse action has first
coordinate u-t, so at any t>0 the equation u-t=u has no solution. Its
joint kernel support is disjoint from the positive-time diagonal, locally
and globally; the diagonal restriction therefore exists and is identically
zero. This remains true on the entire countable component union before
pushforward, so there is no ambiguous infinite multiplicity times zero.

All physical primitive sets are empty, giving the ordinary and scalar
objects exactly as prescribed:

    Z_orb,U(s)=D_orb,U(s)=1, Theta_orb,U=0,
    Theta_0,U=0, D_0,U(s)=1, for EVERY complex s.                 (A22)

The empty sums and zero Laplace integral converge absolutely everywhere,
and the functions are entire with the frozen normalization. The source
lag isotropy Z on atom basins is retained but contributes no physical
orbit and no term to the kernel on the frozen coarse quotient. No point,
word, unit or transverse state is deleted to obtain (A22).

This is equality of trivial analytic functions, NOT an ordinary Fredholm
determinant identification: its actual U_t is still noncompact and not
trace class, by Section 2. Positive-time flat trace zero is compatible with
a nonzero unitary operator. Nothing here evaluates the excluded t=0
diagonal or supplies a zero-time renormalization.

## 7. Adverse checks, limits and handoff

All three results use their OWN full physical orbit sets and scalar kernels.
FACTOR-OFF retains composite primitive cores and sums colliding lengths;
DRIFT-ONLY retains its entire continuous family instead of choosing one
orbit per atom; UNIT-HOLONOMY distinguishes ineffective source recurrence
from absent physical returns. A trace-class conclusion cannot be inferred
from existence of a flat trace or equality of two scalar functions.

The proof of the scalar coefficient is a joint positive-time kernel
restriction, not a definition by an orbit formula. Noncompact integration,
the countable component union, exact absolute domains, differentiation,
repetitions and phases have been checked at their own scope. All continuation
claims are proved by (A8)--(A10) and the indicated normally convergent
products; no external continuation or unproved spectral correspondence is
used. No finite primitive list or scientific numerical calculation is an
input, and no state selection, new amplitude, bundle, roof or Hilbert space
has been added.

This is control evidence for the bounded RCZ01 analytic audit, not an
independent conclusion about MAIN's new analytic results. Strong arithmetic
naturalness remains OPEN. No assertion here is a formal Route coordinate,
classical A0/A1/A2 credit, quantization, generator spectrum, Riemann-zero
claim or global impossibility theorem for other unfrozen transfer choices.
Formal coordinates remain UNASSIGNED; Route B is NOT INVOKED.

## 8. Verification receipt

The original349 input was displayed only through line192 and hashed with
head -n192; no appended result was read. The348 proof and plan were checked
only by sha256sum in this task and matched the retained exact inputs above.
Scientific reasoning was entirely symbolic and analytic. The only file
created or edited was this one, via apply_patch. Final validation checks
its relative links, audit/flow identities, format/EOF and frozen input hash;
the final digest is reported in the handoff rather than inside itself.

EOF — independent full-control analytic derivations; no MAIN verdict issued.
