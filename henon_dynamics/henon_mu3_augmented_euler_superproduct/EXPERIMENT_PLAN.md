# Experiment Plan

## Objective

Certify the intrinsic \(\mu_3\) symmetry, the exact integral augmentation
local factors, the absence of local sector cancellation at frozen control
primes, and the analytic-half-plane theorem for the Hénon Euler
superproduct.

## Claims Under Test

| ID | Claim | Evidence target |
|---|---|---|
| C1 | \(U_pR_p=R_p^{-1}U_p\) and \([U_p^2,R_p]=0\) | exact finite-field replay |
| C2 | sector dimensions are \((p+2,p-1,p-1)/3\) | exact orbit census |
| C3 | \(T_{p,1}\) and \(T_{p,2}\) have equal characteristic polynomials | exact polynomial identity |
| C4 | augmentation moments equal \(\operatorname{Tr}((R+R^2)T^n)\) | exact projector algebra |
| C5 | frozen controls have \(\gcd(\chi_{p,0},\chi_{p,1})=1\) | exact modular gcd |
| C6 | reduced local degrees grow linearly on the frozen ledger | exact consequence of C2, C3, C5 |
| C7 | the canonical Euler log converges locally uniformly for \(\Re s>1\) | theorem replay from Deligne bound |
| C8 | the raw product fails conjugation symmetry already at \(p=7\) | exact residue histogram and cyclotomic argument |

## Frozen Inputs

- Hénon parameter: homogeneous map \(H_0(q,p)=(-6q^2-p,q)\).
- Kernel: \(S_0(q,Q)=qQ+2q^3\).
- Complete split-prime ledger through 73:
  \(7,13,19,31,37,43,61,67,73\).
- Auxiliary prime rule: the smallest prime \(\ell\equiv1\pmod{3p}\).
- Order-three element: primitive-root power \(g_p^{(p-1)/3}\).
- Augmentation weights: \((2,-1,-1)\).
- Canonical Euler variable: \(z_p=p^{-s}\); the critical-line display
  \(p^{1/2-s}\) is recorded separately.
- Forbidden data: Riemann-zero tables, fitted phases, prime-dependent weights,
  post hoc polynomial cancellation.

## Exact Computational Method

For every frozen prime \(p\):

1. choose the frozen auxiliary prime \(\ell\);
2. construct exact roots of unity of orders \(p\) and three in
   \(\mathbb F_\ell\);
3. construct the unnormalized kernel matrix
   \(A_p(Q,q)=e_p(qQ+2q^3)\);
4. form \(T_p=p^{-1}A_p^2\), avoiding square-root choices;
5. construct the three character-sector bases from the \(\zeta_p\)-orbits;
6. restrict \(T_p\) exactly to every sector;
7. compute characteristic polynomials and gcds with FLINT;
8. replay the defining matrix identities independently in the checker.

## Controls

- swap \(\zeta_p\) with \(\zeta_p^{-1}\): sectors one and two must swap;
- change the cubic coefficient from two: source lock must reject the artifact;
- replace two-step time by one-step time: sector-preservation gate must fail;
- replace integer augmentation by complex color weights: determinant gate must
  reject it;
- mutate one characteristic-polynomial coefficient: checker must fail;
- duplicate an auxiliary prime or use a composite modulus: checker must fail;
- insert a fake common factor: degree and gcd gates must fail;
- change a JSON integer to a Boolean or float: type-strict checker must fail.

## Stop/Go Criteria

`GO_POSITIVE_EULER_GERM` if C1--C7 pass.

`STOP_RAW_ROUTE_A_PROMOTION` if C8 passes.

`STOP_SYMMETRY_REDUCTION` if the two nontrivial sectors are not exactly paired
or the augmentation trace is not chronological.

The finite Tate-plus-\(j=0\)-CM replacement is excluded by the source-locked
C41--C42 rigidity result.  The only permitted replacement candidate is a
pure self-dual compatible system, built from the conjugate-paired Hénon
Fourier--Deligne moments at both split and inert places, over one fixed
coefficient field and with rank and conductor bounded independently of the
prime.  Its first gate is a uniform bound on the algebraic degrees of the
paired first moments; only then is a uniform Hankel-rank theorem for all
moments admissible.  The inert clock is \(\log N\mathfrak p\), not an averaged
rational-prime clock.  Post hoc conjugate multiplication is a control, not a
Route-A promotion.

## Reproducibility

The producer and checker must be separate programs.  The checker rebuilds
all matrices from frozen scalar inputs and does not trust producer verdicts.
All released artifacts are hashed, and the default runner is read-only.
