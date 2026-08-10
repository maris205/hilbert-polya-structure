# HCS-C28 experiment plan

## Decision target

Resolve the full-prime assembly gate left by HCS-C27 at theorem level.  Exact
arithmetic is used to certify source locks and decisive obstructions; no
larger prime or word scan is permitted.

## Frozen inputs

- HCS-C25 all-length decoder and free positive AGY first-return monoid;
- HCS-C26 common Bergman domain, bounded constant/evaluation maps, and
  locally uniform branch trace-norm summability;
- HCS-C27 finite-Weil operators and Thomas character formula;
- unreordered chronological Rauzy products, odd primes, and the complete
  \(p^2\)-dimensional finite Weil fibre;
- the frozen HCS-C24 eventually-positive control ledger, used only for an
  ambient full-Rauzy fixed-plane test.

Both implementations verify byte-level hashes of C24--C27 before emitting a
result.

## Claims and falsifiers

| Gate | Pass condition | Falsifier or boundary |
|---|---|---|
| Character limit | \(p^{-2}\Theta_p(h)\to\mathbf1_{h=I}\) for every fixed integral cocycle element | rank stability or the Thomas magnitude law fails |
| Sharp local size | \(\|\mathcal L_{s,p}\|_{S_q}\asymp p^{2/q}\), locally uniformly in \(s\) | the decoder/trace witness gives no nonzero lower bound |
| Direct-sum phase diagram | \(\oplus c_p\mathcal L_{s,p}\in S_q\iff\sum p^2|c_p|^q<\infty\) | either implication cannot be justified |
| Ordinary Fredholm gate | \(\mathfrak L_{s,z}\) is trace class exactly for \(\operatorname{Re}z>3\) | boundary \(\sum_p1/p\) is summable or the upper bound is not locally uniform |
| Chronology gate | word traces contain \(p^{-nz}\Theta_p(g_w)\), with \(g_w\) in source order | averaging, branch-character multiplication, or \(\Theta_p(g)^r\) enters |
| Normalized-trace gate | all positive moments tend to zero and the common small-disc determinant germ tends to \(1\) | a nonempty positive word equals the identity |
| Ambient fixed-plane gate | C24-P073 gives \(\Theta_p=p\) for every odd \(p\), hence \(\sum1/p\) | exact minors or Thomas quotient do not certify the formula |
| Arithmetic gate | regular orbit sums reduce to orbit-dependent quadratic prime Dirichlet series plus finite bad-prime corrections | a common character is silently imposed |
| HP gate | prime grading follows from the original roof | \(p^{-z}\) remains an external second clock and no self-adjoint generator exists |

## Reproducible exact computation

1. Lock the C24--C27 certificates by SHA-256.
2. Rebuild the C26 control word \(\gamma_*\); verify
   \(\det(I-g)=460097253=3^4\cdot7\cdot11\cdot71\cdot1039\) and squarefree
   kernel \(5680213\).
3. Certify reduced residue classes with quadratic character values \(-1\)
   and \(+1\).  Dirichlet's theorem then rules out convergence of the bare
   character product; this is a control, not an Euler-factor theorem.
4. Replay C24-P073.  Check the characteristic polynomial
   \((x-1)^2(x^2-18x+1)\), vanishing of all \(3\times3\) minors of \(g-I\),
   gcd one for its \(2\times2\) minors, and Thomas quotient determinant
   \(-4\).  Deduce \(\Theta_p(g)=p\) for every odd prime.
5. Recompute the entire 146-cycle C24 fixed-space census and require
   \(\{k=0:125,k=1:20,k=2:1\}\), with P073 uniquely at \(k=2\).
6. Encode the exact criterion \(q\operatorname{Re}z>3\) at interior,
   boundary, regularized-determinant, and noncompact controls.
7. Emit a payload-hashed certificate and replay all decisive fields with an
   implementation that imports no producer code.
8. Mutation-test source locks, payload hashes, theorem gates, chronology,
   P073 scope, and Route-B denial.  The release runner verifies an existing
   manifest; refreshing hashes is an explicit separate action.

## Analytic derivation

For a fixed branch \(\delta\), compress \(\mathcal L_{s,p}\) between the
constant embedding and an interior evaluation.  Pair the resulting fibre
operator with \(\rho_p(g_\delta)^{-1}\) under normalized trace.  C25 matrix
injectivity and the normalized character limit isolate the nonzero
coefficient of \(\delta\), giving the sharp Schatten lower bound.  C26
branch summability gives the matching upper bound.  No finite scan enters
this proof.

## Output contract

- `results/c28_certificate.json` and `c28_independent_check.json`;
- `results/RESULTS.md`, `VALIDATION_REPORT.md`, and `TEST_REPORT.md`;
- `DERIVATION_PACKAGE.md` and `THEOREM_PACKAGE.md`;
- a compiled paper and reproducibility manifest;
- `route_a_evaluation.yaml` with a conservative, source-locked verdict.

## Scope firewall

The half-plane \(\operatorname{Re}z>3\) is sharp for the ordinary direct-sum
Fredholm determinant.  It is not a continuation theorem toward \(z=0\), a
functional equation, an Euler product for one global automorphic object, or
a self-adjoint Hilbert--Pólya construction.  C24-P073 obstructs the full
Rauzy dimension-normalized marked assembly; it is not asserted to lie in
the selected C26 induced section.
