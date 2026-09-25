# Independent internal review — RAF01

**Candidate:** `ANG-20260919-RAF01`. **Date:** 2026-09-19.
**Reviewed status:** `OWNED AFFINE INDEX; NO PRIMITIVE RETURN PACKETS — STOP / FORK`.
**Verdict:** PASS for the bounded proof and stop record; no required change.
This does not constitute promising-main-candidate admission or a target pass.

## Inputs, procedure and independence

| Input | SHA256 |
| --- | --- |
| Frozen raw card, read before the manuscript | `c932e3e53c88bbf541c8f41e5734319b245bd6d0b2b2e27caf5d9f08d35b5602` |
| Manuscript reviewed | `235f8c4c297a471d60056a3e49e7321e99e29e8eacc12b366d6209d5921cd3e0` |

The reviewer independently derived the localization, full domains,
Borel clock, stabilizers and zero-orbit control from the card, and
sent those findings before reading the manuscript. Checkpoint 2 is a
subsequent comparison, not claimed blind at every stage. No clock or
return theorem from 270, 271 or another candidate was used as evidence.
A bounded auxiliary model audit received only the algebraic definitions
and requested controls, not files or manuscript; it confirmed the domain,
stabilizer and topology conclusions after the reviewer's own derivation.

ARS academic-research-suite's deep-research devil's-advocate procedure
organized the three checkpoints. No numerical run, additional orbit
census, literature campaign, new owner, operator, T3 construction or
formal Route evaluation was performed. Hash checks bind documents.
Shared model lineage/context remain limitations: this is internal model
review, not external peer review, human certification, formal proof
checking or a guarantee of independent errors.

## Checkpoint 1 — independent raw-card derivation: PASS

**Localization and all residue phases.** If mx=0 in X, reduction modulo
mN implies x=0 modulo N for every N. Thus multiplication by every
nonzero integer is injective. This makes X inject into S^(-1)X and
allows the injective integer embedding to extend to Q. If a reduced
rational u/v lies in X, then vx=u and reduction modulo v forces v|u,
so v=1. Consequently Q intersect X=Z inside B, including zero and
negative integers. No component choice or unit quotient is involved.

The image mX is exactly the kernel of reduction modulo m: the reverse
inclusion follows by approximating a compatible residue state using
integer multiples of m, then using compactness of the image. It is
clopen of index m and Haar mass 1/m. B is needed algebraically; no
adelic topology or unproved geometric identification of B is required.

**Exact domains for arbitrary common denominators.** Write q=a/c,
r=b/c with a,c>0 and signed integer b. Put h=gcd(a,c). The domain
is empty exactly when h does not divide b. Otherwise choose x_0 with
ax_0+b=0 mod c, and put y_0=(ax_0+b)/c. Direct substitution gives

    D_g=x_0+(c/h)X,
    theta_g(D_g)=y_0+(a/h)X,
    theta_g(x_0+(c/h)z)=y_0+(a/h)z.

These are the complete clopen domain and image. Their parametrizations
give a homeomorphism, including a/h=1 or c/h=1. All definitions refer
to the intrinsic element qx+r in B, so changing the presentation or
the chosen congruence representative cannot change them. The inverse
is (q^(-1),−r/q), with domain exactly the displayed image.

For first k and then g, the composable domain is D_k intersect D_(gk),
not necessarily all of D_(gk); the intermediate state must lie in X.
For q=1, the domain is nonempty precisely when r is an integer, and
then it is all X. A nonzero integer translation has no fixed point;
the identity fixes all states. Empty rational-translation domains are
not fictitiously retained as maps on X.

The complete finite-residue interface is also exact: theta_g(x) lies
in t+mX precisely when ax+b−ct lies in cmX. Multiplication by c gives
one direction and cancellation gives the other, which also enforces
the domain condition. This preserves finite residue questions, not
integer chronology, a sieve evolution or a prime-selective theorem.

**Borel image clock, independently proved.** For every positive n,
mu(nE)=mu(E)/n on all Borel E in X: integer multiplication is a
homeomorphism onto nX, and the identity on residue cylinders extends
by uniqueness of finite measures. Applying this and Haar translation
invariance to the two domain/image coset parametrizations gives

    mu(theta_g E)=(c/a)mu(E)=(1/q)mu(E),
    J_g=1/q,                      c(g,x)=log q.

This includes unreduced presentations and every Borel subset of a
nonempty branch. Translation affects domains and stabilizers even
though it cancels from this image ratio. Multiplication of Jacobians
and addition of clocks follow for every composable pair. Each clock
is constant on its label chart and hence continuous. A nonempty open
subset of a branch domain has positive Haar measure; two continuous
versions equal almost everywhere therefore agree everywhere. This
fixes the clock at null integer states without arbitrary reassignment.

**Whole groupoid and time.** The discrete countable label set with
compact-open domain charts gives a locally compact Hausdorff,
second-countable étale groupoid. The exact partial-action laws prove
continuity of multiplication and inversion. G×R has the corresponding
extension charts, and all real translations are jointly continuous
groupoid automorphisms, with inverse time and no added positive roof.

**Every fixed state and actual time group.** The fixed equation is
(q−1)x=−r in B. If q!=1, its unique solution is rational, so it lies
in X exactly when it is an integer. In the common-denominator notation,
a!=c gives the integer solution −b/(a−c) precisely when (a−c)|b.
If a=c, only b=0 fixes a point. Conversely each integer N is fixed by
every (q,(1−q)N), q>0 rational, and those are its entire stabilizer.

| State | Base isotropy | Extension fixed-object isotropy | Actual time-return group |
| --- | --- | --- | --- |
| N in Z | {(q,(1−q)N):q in Q_(>0)} | identity only | log Q_(>0), dense, no least positive element |
| x outside Z | identity only | identity only | {0} |

At integers, log((k+1)/k)>0 tends to zero, explicitly excluding a least
positive return. Extension isotropy additionally requires log q=0,
which forces q=1 and r=0. Thus dense time stabilizers do not imply
nontrivial fixed-object extension isotropy. No state has H=T Z with
T>0, so no primitive cyclic-return packet exists anywhere. Selecting
one prime dilation would replace the full stabilizer, not read it.

**The precommitted zero-orbit control.** Every arrow from (0,u) lands
at (r,u+log q), and admissibility requires r in Q intersect X=Z.
Conversely every integer r and positive rational q is admissible there.
Thus its orbit is exactly Z times (u+log Q_(>0)). Embedded integers
are dense in X and log Q_(>0) is dense in R, while the orbit is
countable and proper. It is therefore nonclosed. Its quotient singleton
has nonclosed inverse image, proving that the coarse quotient is not
T1 and hence not Hausdorff. This does not contradict the Hausdorff
object and arrow spaces and is not an additional general orbit census.

## Checkpoint 2 — manuscript comparison: PASS

Lemma 1 and Propositions 2–5 match the earlier derivation. The manuscript
retains unreduced denominators, empty domains, q=1, negative integers,
the full intermediate-state composition condition and all arrow labels.
The Borel image sign and continuous null-point version are correct.
No multiplication-only result is imported to justify the new action.

The full integer stabilizer is used rather than a prime-generated
subgroup. Its dense clock image and trivial extension isotropy are
correctly separated. The zero-orbit density/properness argument supplies
the claimed non-T1 obstruction without claiming more coarse geometry.
All integer points are correctly retained despite their countable
Haar-null set; no almost-everywhere deletion changes the result.

The lineage is explicitly limited to the compatible finite-residue
interface and its affine update. Naturalness remains OPEN. The paper
does not turn this interface into a chronological prime sieve, a
Logistic/Hénon realization or a known analytic operator. Its proofs
are elementary and self-contained; no external theorem was needed.

## Checkpoint 3 — final adverse checks and decision: PASS

| Strongest objection | Resolution |
| --- | --- |
| A rational fixed value might be a noninteger profinite state | The proved intersection Q intersect X=Z excludes it. |
| An unreduced denominator might change admissibility or clock | The gcd congruence and intrinsic B action fix the domain; c/a=1/q fixes the image ratio. |
| A rational translation might act everywhere | Only integer translations alone have nonempty domains. |
| A log p fixed arrow might define a primitive packet | All positive rational dilations fix that integer after their matching translation; arbitrarily small positive clocks remain. |
| Null integer clocks might be independently chosen | Full support fixes the continuous chartwise image Jacobian there. |
| Trivial extension isotropy might remove all time returns | Integer isomorphism-class time stabilizers are dense despite trivial fixed-object isotropy. |
| Hausdorff groupoid charts might ensure Hausdorff coarse flow | The exact dense proper zero orbit disproves even T1. |

Required changes: **none**. **Stop target promotion / fork** on absence
of primitive cyclic-return packets. Retain the scoped source, domain and
index-clock results without changing the full owner. T3 is NOT SUPPLIED /
NOT PURSUED; classical fields are NOT APPLICABLE, formal coordinates
UNASSIGNED and Route B NOT INVOKED. This is a bounded negative audit,
not a no-go theorem for every rational-affine arithmetic construction.
