# Claim Matrix

## Purpose

This matrix is the claim-control ledger for the Stage-1 paper. It separates exact
geometry, established literature boundaries, planned numerical tests, and deferred
arithmetic hypotheses. No row marked `OPEN`, `MODELING_CHOICE`, `HEURISTIC`, or
`NOT_TESTABLE` may be written as a result.

Evidence labels follow the Route-A evaluator:

```text
PROVED
CONDITIONAL_THEOREM
NUMERICALLY_CERTIFIED
NUMERICAL_OBSERVATION
HEURISTIC
MODELING_CHOICE
OPEN
REFUTED
NOT_TESTABLE
STOP_SCOPED
```

## Claim ledger

| ID | Route layer | Claim | Current status | Required evidence / dependency | Allowed manuscript wording now | Stop or downgrade condition |
|---|---|---|---|---|---|---|
| G1 | Geometry | \(H_{a,\rho}(x,y)=(1-a x^2-\rho y,x)\) obeys \(DH^T\Omega DH=\rho\Omega\). | **PROVED** | Direct Jacobian multiplication. | "The family is conformally symplectic for \(\rho>0\), symplectic at \(\rho=1\), and singular at \(\rho=0\)." | None within the stated coordinates. |
| G2 | A1 | For a period-\(n\) orbit, \(\det M_\gamma=\rho^n\). | **PROVED** | Product of one-step determinants. | Exact identity. | Numerical violations imply an implementation error. |
| G3 | Geometry | At \(\rho=1\), \(S_a(q,Q)=qQ-q+(a/3)q^3\) generates the map and its periodic action is intrinsic. | **PROVED** | Differentiate \(S_a\) and recover \((Q,P)\). | Exact coordinate statement. | Do not extend the canonical-action claim to \(\rho<1\). |
| O1 | Boundary | A critical one-dimensional map cannot be a \(C^1\) smooth-submersion factor of a local diffeomorphism over its critical point. | **PROVED** | Chain rule plus rank comparison. | "An elementary regular-lift obstruction." | Must not be called a new deep theorem or a general ban on topological/inverse-limit lifts. |
| O2 | Boundary | The quadratic parent at \(\rho=0\) is a singular endpoint, not a regular symplectic continuation point. | **PROVED** | \(\det DH=\rho\) and O1. | Exact for this family and regularity class. | Do not infer that every branch or topological continuation is impossible. |
| O3 | Boundary | Hénon memory avoids O1 by abandoning the exact projection semiconjugacy to \(f_a\). | **PROVED** | First coordinate depends on \(y\); direct substitution. | "The arithmetic shadow, if any, must be re-tested." | Do not use "lift" without qualifying the lost factor relation. |
| O6 | Arithmetic control | At \(\rho=1\), a desired positive fixed-point multiplier \(\lambda\) can be produced by parameter tuning whenever \(t=\lambda+\lambda^{-1}>4\): choose \(a=t^2/4-t>0\). In particular \(\lambda=5\) gives \(a=1.56\). | **PROVED** | Combine the fixed-point equation \(ax^2+2x-1=0\), trace \(t=-2ax\), and \(\det DH=1\). | "An exact fixed-point prime hit under a nearby tuned parameter is a negative control, not arithmetic evidence." | Never use the \(a=1.56\), \(\lambda=5\) identity to select the primary parameter. |
| L1 | Novelty | Canonical/noisy two-dimensional Logistic extensions and their \(f'=0\) singularities are prior art. | **PROVED** as literature fact | Fogedby--Jensen (2005); Demaeyer--Gaspard (2009). | Cite as the closest direct prior. | If a more direct treatment of the exact frozen path is found, narrow novelty further. |
| L2 | Novelty | Generic Hénon orbit ledgers and dynamical zeta/Fredholm constructions have low standalone novelty. | **PROVED** as literature fact | Sattari--Mitchell, Gallas, Rugh, Sterling--Meiss, and related work. | Treat them as methods/controls. | No paper claim based only on reproducing a ledger or zeta. |
| P0 | A0 | The inherited Logistic construction provides a genuine rational-prime arithmetic seed. | **NOT_TESTABLE / unsupported** | A source-locked reproduction against mod-3/mod-6 and matched controls would be required. | "An attributed seed whose reproducible support is presently limited to a mod-2 shadow." | Any claim of established prime coding is forbidden. |
| P1 | A0 | The frozen parent displays a mod-2/even-return-gap symbolic shadow under the declared partition. | **NUMERICAL_OBSERVATION** | Development, validation, and sealed test each gave \(P(0)=1\) with full exposure. The effect is only a parity fixture and is not specific to rational primes. | "The declared parent parity fixture was reproduced." | Do not upgrade this to a rational-prime mechanism. |
| E1 | A0 | The mod-2 shadow survives for regular \(\rho>0\) and at \(\rho=1\). | **STOP_SCOPED / carrier unavailable** | In the sealed test, \(\rho=1\) exposure was 0.011724, survival was zero, 9,988 gaps were below threshold, and conditional \(P=-0.70665\), CI \([-0.71625,-0.69679]\). Neighbor specificity also failed. | "Small-\(\rho\) parity was visible but nonspecific; the frozen endpoint carrier was unavailable." | Never describe this as a theorem excluding every bounded invariant carrier. |
| E2 | A1 | A named periodic orbit at \(\rho=0\) remains "the same orbit" at \(\rho=1\). | **STOP_SCOPED / unresolved** | The singular endpoint and incomplete \(u_c\) ledger prevent a global branch-identity claim; A0 stopped the downstream orbit program. | "No orbit-identity survival claim is made." | A future branch study is a separate candidate and cannot repair E1 post hoc. |
| C1 | A1 control | At \((a,\rho)=(6,1)\), the implementation recovers the expected primitive binary-necklace orbit count through period 10. | **NUMERICALLY_CERTIFIED** | Counts \(2,1,2,3,6,9,18,30,56,99\) match exactly; maximum float cyclic residual \(1.42\times10^{-13}\); high-precision audit infrastructure and invariant tests pass. | "The orbit finder passes its declared high-\(a\) positive control." | Certification is regime- and cutoff-specific; it does not certify \(u_c\). |
| C2 | A1 | The primary \(u_c\) low-period ledger is complete. | **NOT_TESTABLE at present** | A covering/certification argument or independent saturating methods with quantified missed-orbit bound. | "Exploratory ledger with explicit completeness uncertainty." | No zeta/determinant claim may use an incomplete ledger as complete. |
| C3 | A1 | The implemented Jacobian, cyclic Jacobian, conformal-symplectic identity, monodromy determinant, generating function, action convention, cycle audit, symbolic protocol, clustered analysis, and attractor classifier pass their test suite. | **NUMERICALLY_CERTIFIED** | Current `PYTHONPATH=. pytest -q` run: 30 tests passed; includes finite differences, determinant identities, 80-digit refinement, split locking, censoring, endpoint gates, paired bootstrap/Holm utilities, and Jury-threshold fixtures. | "The implementation is numerically validated against the declared exact identities and fixtures." | This is software validation, not a theorem about all floating-point inputs or a completeness certificate at \(u_c\). |
| A1 | A0 | Primitive unstable multipliers at frozen \(u_c\) are intrinsically enriched at rational primes. | **STOP_SCOPED / never tested** | The prerequisite weak-shadow carrier and ledger-completeness gates failed before any prime labels were opened. | "No multiplier-prime experiment was run." | This branch cannot be reopened for the same candidate by post-hoc matching. |
| Z1 | A2 | \(Z_u(s)=\prod_\gamma(1-|\Lambda_{u,\gamma}|^{-s})^{-1}\) has the stated formal logarithmic derivative where absolutely convergent. | **CONDITIONAL_THEOREM** | Frozen primitive hyperbolic ledger and justified absolute convergence. | Formal conditional identity only. | No analytic continuation, divisor, or target match is implied. |
| Z2 | A2 | \(Z_u\) is a rational-prime Euler product or a Riemann dynamical determinant. | **STOP_SCOPED** | A0 and A1 must first pass with completeness and controls. | No claim. | Any A0 failure permanently stops the Riemann-targeted construction for this candidate. |
| S1 | Semiclassics | The usual symplectic stability denominator equals exactly \(|\Lambda|^{-r/2}\). | **REFUTED** | \(|\det(M^r-I)|^{-1/2}=|\Lambda|^{-r/2}/|1-\Lambda^{-r}|\). | Explicitly distinguish the two weights. | Never merge the provisional Euler product with a Gutzwiller factor. |
| Q1 | A4 | The candidate has a natural quantization relevant to Riemann zeros. | **STOP_SCOPED** | Requires A0--A3, an intrinsic Hilbert space, fixed boundary conditions, and classical/quantum trace consistency. | Mention only as outside Stage 1. | Generic quantizability or GUE statistics cannot reopen this claim. |

## Main paper claim hierarchy

The paper may eventually make claims in the following order only:

1. **Exact geometry:** G1--G3.
2. **Correctly scoped boundary:** O1--O3, with direct-prior citations.
3. **Validated method:** C1 and C3.
4. **Controlled transport result:** P1 and E1, positive or negative.
5. **Exploratory branch information:** E2 and C2, with uncertainty visible.

Claims A1, Z2, and Q1 are not part of the current paper unless a new preregistered
stage is explicitly opened after an A0 pass.

## Forbidden inference shortcuts

- Symplecticity \(\not\Rightarrow\) arithmetic relevance.
- Reciprocal multipliers \(\not\Rightarrow\) prime multipliers.
- A primitive-orbit theorem \(\not\Rightarrow\) rational primes.
- One multiplier near 5 \(\not\Rightarrow\) a prime correspondence.
- A complete high-\(a\) ledger \(\not\Rightarrow\) completeness at \(u_c\).
- A small conditional violation rate among rare survivors \(\not\Rightarrow\)
  transport.
- A visually Riemann-like spectrum \(\not\Rightarrow\) a Hilbert--Pólya candidate.

## Update protocol

Every result update must record:

1. claim ID;
2. exact artifact path and hash;
3. source-lock version;
4. development, validation, or confirmatory split;
5. evidence-label transition;
6. failed controls and uncertainty;
7. whether a stop rule fired.

No numerical run may promote a claim directly from `OPEN` to `PROVED`.
