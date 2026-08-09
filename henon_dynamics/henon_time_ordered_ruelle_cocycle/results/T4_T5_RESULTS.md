# HCS-C22 T4 and orbitwise scalar-T5 results

**Verification status:** exact producer PASS; nonimporting checker PASS;
15/15 regression and mutation tests PASS

## Gate summary

| Gate | Result | Exact evidence |
|---|---|---|
| T4 repetition law | PASS | \(M_{\gamma^r}=M_\gamma^r\), \(\ell_{\gamma^r}=r\ell_\gamma\) |
| T4 Euler/log trace | PASS | exact primitive-to-marked fixed-point identity |
| T4 nonzero convergence domain | PASS | multiplier and symbolic-growth majorant |
| T5 common base pinning domain | PASS | six rational endpoint/parameter cases |
| T5 projective/log domain | PASS | two rational parameter cases, unique unstable lift |
| T5 orbitwise scalar denominator cancellation | **NO-GO** | primitive/double fixed-denominator contradiction |
| Graded exterior complex | OPEN | next dynamical form; no operator asserted |

## T4 constants and domain

The certified all-period multiplier bases are

\[
E^2=\frac{129299641}{14112000},
\qquad
U^2=\frac{11420060341}{189778176}.
\]

Thus

\[
E^n\le|\Lambda_{u,n}|\le U^n.
\]

With \(\varphi=(1+\sqrt5)/2\) and

\[
\chi(t)=E^{-t}\quad(t\ge0),
\qquad
\chi(t)=U^{-t}\quad(t<0),
\]

the instability Euler product and its log series converge normally and are
zero-free on

\[
2\varphi|z|\chi(\Re s)<1.
\]

The guaranteed radii are \(0.3090169943\ldots\) at \(s=0\) and
\(0.9353771139\ldots\) at \(s=1\).  At \(z=1\), the coarse theorem requires
\(\Re s>1.0603180797\ldots\); it does not reach the pressure boundary.

## Common complex geometry

For both \(a=59/10\) and \(a=61/10\), the inherited \(X,Y\) disks support
all chronological signed-square-root branches.  The exact common quantities
are

\[
\text{radicand modulus}\ge\frac{55}{488},
\quad
\text{squared-image gap}\ge\frac7{4392},
\quad
\text{coordinate clearance}\ge\frac7{5490}.
\]

Each endpoint derivative has squared upper bound \(40/649\); the squared
two-neighbor sup Lipschitz bound is \(160/649<1\).

The common normalized slope disk \(|m|\le1/2\) is mapped into

\[
|m|\le\frac{125440}{466211}<0.2691,
\]

with projective derivative at most

\[
\frac{11289600}{129299641}<0.0874.
\]

The oriented expansion factor stays in the right half-plane with clearance
\(11371/3360\), so one principal logarithm defines the holomorphic one-step
weight.  There is exactly one lifted periodic slope in the domain.

## Orbitwise scalar no-go

For an area-preserving saddle with \(t=\operatorname{tr}M\),

\[
\det(I-M)=2-t,
\qquad
\det(I-M^2)=4-t^2.
\]

A scalar cocycle that cancels each primitive flat-trace denominator term by
term would need its square to cancel the double-return denominator.  This
would require

\[
|4-t^2|=|2-t|^2,
\]

which is false for every \(|t|>2\).  Hence orbitwise scalar denominator
cancellation is closed without a spectrum computation.

This remains false on the certified projective lift.  Its return eigenvalues
are \(\lambda,\lambda^{-1},\lambda^{-2}\); writing
\(|\lambda|=x>1\), the positive- and negative-multiplier incompatibility gaps
reduce to

\[
2(2x^2-x+1)>0,
\qquad
2(2x^2+x+1)>0,
\]

respectively.

The result does not exclude compensation among different same-period orbits
in an unmarked aggregate scalar trace.  It also does not exclude a symbolic
trace with no geometric denominator, a graded exterior complex, a non-scalar
bundle operator, or an unrelated nonlocal construction.

## Artifacts

- `c22_t4_certificate.json`: exact T4/domain/obstruction producer artifact.
- `c22_t4_independent_check.json`: hash-bound nonimporting reconstruction.
- `../T4_T5_DERIVATION.md`: theorem proofs and scope.
- `../GRADED_PIVOT_ROADMAP.md`: the only authorized next operator form.

No finite operator spectrum, target zero, prime table, or fitted normalization
appears in this release.
