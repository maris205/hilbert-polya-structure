# E2 Round 2: independent local AS certificate review

2026-09-09 UTC. Internal nonauthor review by
/root/c429_e2_wild_witt_review, under the established current-session
review setting. Not external-model review, human peer review, or admission.

## Verdict

**PASS as a single-pair auxiliary certificate; zero open must-fixes.**
For the canonical small-cycle factor at exactly \(p=3,e=2\), over
\(K=\overline{\mathbb F}_3((s))\), the reviewed producer gives

\[
\operatorname{polar}(a_2)=s^{-6}+2s^{-4},\qquad
[a_2]=[2s^{-4}+s^{-2}]\ne0.
\]

One separately authorized, materially independent check verifies the
same reduced class by a different trace-one element at precision \(64\).
It does not rerun or import the producer. Thus the local factor is
irreducible and its splitting field is totally ramified cyclic of degree
\(9\). **Neither the all-odd-prime/all-level local lemma nor original
global PC424-D is closed.** No new paper admission follows.

The first producer's exit-2, precision-512 result remains correctly
inconclusive. It is not retroactively relabelled successful.

## 1. Reviewed inputs and mathematical normalization

I read both complete producer drivers, the first execution log, the
second log's event records and coefficient certificate, and the author's
final REPORT.md and PROOF_SUPPLEMENT.md. The independent program parses
the entire coefficient record; mathematical verification is not inferred
from its digest. First-pass proofs/reviews remain read-only accepted inputs.

The object is \(P_s(z)=(1+s)z+z^2\),
\(Q_2=(P_s^9-z)/(P_s^3-z)\), and the unique monic degree-nine factor
\(M_2\equiv z^9\bmod s\). The changes
\(c=(1-s^2)/4,\ x=z+(1+s)/2\) retain the original one-step quadratic
clock. The base is the same fixed \(K\) throughout the comparison.
No original-parameter uniformizer is silently substituted for \(s\).

The coefficient computation over \(\mathbb F_3\) identifies the
canonical factor over the algebraic closure by coprime Hensel uniqueness;
it is not a claim that arbitrary factors remain irreducible after a
constant extension.

## 2. Producer arithmetic and precision audit

The coefficient lists are low-degree-first in \(z\), each entry being
a polynomial in \(s\) modulo \(s^N\). I checked the implemented
convolution, monic division, multiplication matrices and Horner
substitution against these conventions. FLINT's truncation, low-product,
shift and inverse-series operations have the required meaning.
[Official python-flint documentation](https://python-flint.readthedocs.io/en/latest/nmod_poly.html)

The producer constructs precisely nine native iterates, saves the third,
and checks zero remainder and quotient degree \(504\). Its initial
factorization checks \(Q_2(z,0)=z^9V(z)\), \(V(0)\ne0\).

At a Hensel step with error \(F=Q_2-MN_0\in s^hR[z]\), the code solves
\(N_0A=F\bmod M\) using unit pivots, sets \(B=(F-AN_0)/M\), and checks
the new product modulo \(s^{2h}\). Both corrections have order at least
\(h\), so the omitted product \(AB\) vanishes at the next precision.
Their degrees preserve monicity. This proves identification with the
canonical Hensel factor, not just an arbitrary approximate root polynomial.

The matrix columns represent multiplication by \(M_2'(\alpha)\).
Bareiss elimination operates on exact polynomial representatives,
checks every division remainder, and tracks row-swap signs. Integral
determinants and adjugates vary by \(O(s^N)\) when matrix entries do.
Thus the visible valuation \(\delta=144<N\) is exact. Cramer column
replacement solves for the vector of \(\alpha^8/M_2'(\alpha)\), with
the right signs. No inverse of a nonunit in a truncated ring is taken:
the power \(s^\delta\) is separated first.

The decisive error calculation is:

\[
T=N-\delta,\quad W=s^\delta w\pmod{s^T},\quad
Y=s^\delta y\pmod{s^T},\quad
a=s^{-3\delta}(Y^3-s^{2\delta}Y)\pmod{s^{N-4\delta}}.
\]

All substitutions and products before the last division are integral.
Errors in the monic modulus also have order at least \(N\), hence do
not compromise precision \(T\). At \(N=1024\), \(T=880\) and the
final error exponent is \(448\). The pole bound is \(3\delta=432\).
The loop checks every coefficient with index \(0,\ldots,431\) in the
scaled scalar numerator, not just its first observed nonzero term.
The exact AS element is scalar by the accepted torsor identity; the
code additionally checks all eight nonconstant coordinates.

The trace-one identity remains valid for a disconnected cyclic-nine
torsor. Lagrange interpolation gives trace one; the weighted sum gives
\(\sigma y-y=1\); no irreducibility is assumed in extracting the class.
The logged native-return, trace and difference checks are consistent
with that proof.

At \(N=128\) the determinant is not visible. At \(N=512\), its
valuation is visible but \(512\le4(144)+8=584\). The driver correctly
returns 2 without evaluating the AS class. The separate N1024 driver
imports unchanged code and changes only the authorized precision path.

The value \(\delta\) is the polynomial/order discriminant valuation.
It is not automatically the different exponent of the normalized
field extension; no such identification is used here.

## 3. Materially independent check

The coordinator approved one new check at \(N=64\), one pair, no retry,
with 30 CPU seconds / 60 wall seconds / 512 MiB limits. The code is
[check_alternate_trace.py](check_alternate_trace.py), and the complete
output is [independent_execution.log](independent_execution.log).

It reads only the emitted factor coefficients. It does not import the
producer or use Hensel lifting, its full degree-504 construction,
\(M'\), Cramer determinants, or Bareiss.

Let \(R=P_s^3\), \(u_0=\alpha,\ u_1=R(\alpha),\ u_2=R^2(\alpha)\).
Using a hand-derived degree-eight expression for \(R\), the checker
computes polynomial divided differences
\(D_1=D_R(u_1,u_0)\), \(D_2=D_R(u_2,u_1)\).
The exact identity

\[
Q_2=1+D_1+D_1D_2
\]

follows by telescoping \(R^3(z)-z\) and cancelling the polynomial
factor \(R(z)-z\). It is valid even where that factor is not a unit.
The independently calculated remainder modulo the supplied \(M_2\)
is zero modulo \(s^{64}\). Together with monicity, reduction \(z^9\),
and the accepted coprime special-fibre factorization, this independently
identifies the input as the canonical factor to that precision.

Next it directly iterates \(\alpha\) nine times. The orbit trace is
scalar and equals minus the \(z^8\) coefficient:

\[
\tau=\operatorname{Tr}_{\rm native}(\alpha),\qquad
v_s(\tau)=10,\qquad [s^{10}]\tau=2.
\]

Use \(w_{\rm alt}=\alpha/\tau\) and
\(y_{\rm alt}=-\sum_{i=0}^8\bar i\,\sigma^i(\alpha)/\tau\).
The unit \(\tau/s^{10}\) is known modulo \(s^{54}\), so
\(s^{10}y_{\rm alt}\) is integral and known to that precision.
Cubing and subtracting the shifted linear term gives
\(a_{\rm alt}\) modulo \(s^{54-30}=s^{24}\), with pole bound \(30\).
All nonconstant coordinates and all thirty possible negative scalar
coefficients are checked.

The independent result is

\[
\operatorname{polar}(a_{\rm alt})=2s^{-4}+s^{-2},
\]

already AS-reduced. Two trace-one choices differ by an invariant
translation in their extracted \(y\)'s, so their AS classes agree.
This independently corroborates the class and inertia conclusion;
the producer's particular unreduced pole and \(\delta=144\) are
supported by its separately audited algorithm/log, not recomputed
by this alternate method.

Actual command from this review directory:

    bash -o pipefail -c 'timeout --kill-after=5s 60s prlimit --cpu=30 --as=536870912 -- python3 -u check_alternate_trace.py 2>&1 | tee independent_execution.log'

Actual exit: **0**, one execution, one precision. Start/end:
2026-09-09 14:06:48.334065 / 14:06:48.356419 UTC.
Reported final CPU time 0.086354 seconds, internal wall time
0.023885 seconds, peak RSS 29,244 KiB. No retry occurred.

## 4. AS conclusion, nonnesting and remaining limits

Subtracting \(\wp(s^{-2})=s^{-6}-s^{-2}\) from the producer's raw
polar part gives \(2s^{-4}+s^{-2}\). Its highest pole \(4\) is prime
to 3, hence it is not an AS coboundary. The regular part is
AS-surjective over \(\overline{\mathbb F}_3[[s]]\), including the
constant term; this last assertion would need qualification over
\(\mathbb F_3[[s]]\), but that is not the field of the theorem.

Every proper subgroup of \(C_9\) maps trivially to \(C_9/3C_9\).
The nonzero first AS quotient therefore forces \(H_2=C_9\).

The first quotient of this field has break 4, while the accepted
prime-level degree-three field over the same \(K\) has break 2.
They cannot be the same \(K\)-extension; multiplying an AS class
by a nonzero \(\mathbb F_3\) scalar does not change its reduced
highest pole. Since a cyclic-nine field has a unique degree-three
subfield, the prime-level field is not contained in it.
This is a comparison over the fixed identified base, not after an
arbitrary reparametrization or further ramified base change.

Classical Hensel, additive Hilbert-90/AS, ramification and
Lindahl–Rivera-Letelier small-cycle inputs remain subtracted as in
the first-pass E2 review. The new evidence is one local pair and its
specific cross-level nonidentification. It is not a uniform tower
law, full higher-break computation, global cycle transitivity,
component classification, ordinary point-count theorem or Route-A
target arithmetic upgrade.

## 5. Findings and final artifact identities

1. Mathematical/proof/code must-fixes: **none** after the independent check.
2. Scope: retain the explicit single-pair and fixed-base qualifiers.
3. The first inconclusive run and unchanged original code/log must remain
   preserved. Their historical status is part of the final report.

SHA256 identities of reviewed inputs and independent evidence:

| File | SHA256 |
| --- | --- |
| author diagnostic_p3_e2.py | 24cb9f6a2a44b91c72add50780f485cffd1e5d10b2911874314246b1a9ebbde9 |
| author diagnostic_p3_e2_n1024.py | d5a8eeeec4519a8149a7bcc2eef9545d0b1b199a7c37ea3c7e31d18b062ef58b |
| author execution.log | 828ff8b0d38be73d3725b13e5b34574feb0cc7ad1598f02b9ecc0d097b0b76c0 |
| author execution_n1024.log | 06d0ae1f02c93c0d3452e741f1f783b57464d4794a15a3912ae7f1fa03501412 |
| author REPORT.md | ad376779231c2c8d9b89fbce0e4cb80d8e4638469647596c401aedfa2fd02651 |
| author PROOF_SUPPLEMENT.md | c1ca361db3271fe0dba76e069fcc374255f5a3c2a15386cd433a6be0b9995969 |
| check_alternate_trace.py | 4d66d071f3e4d23a921f858fac87c94d981ff1e21e55b3aa97d6218a2c962359 |
| independent_execution.log | e21ff0b067a5e276627932e2a0a55f51ec00d8b8e3d7e433a147265e0dd01d31 |

Only this review directory was written. One new independent mathematical
execution; no producer rerun, source edit, old-file modification, Git,
evaluation, PDF, external upload, or additional child agent.

**ZERO_OPEN_MUST_FIXES; PAIR_AUXILIARY_VERIFIED; ORIGINAL_PC424_D_UNCLOSED.**
**NO_BAD_EULER_OR_ROOT_NUMBER.**
