# Cross-hostile review A — P104

Date: 2026-08-29 UTC.  Reviewer role: independent of the P104 author.

Verdict: **internal GO / external HOLD**.  There is no mathematical
CRITICAL or MAJOR finding.  The finite-word, limit-law, endpoint, and
annealed-pressure claims survive independent reconstruction.  A specialist
direct-owner search remains a release-only MAJOR gate, already represented by
the manuscript's HOLD status.

## Scope and method

The review reread `main.tex`, the bibliography, all evidence documents, and
the verifier from the update convention upward.  It did not treat the stored
control output as a proof.  The following routes were reconstructed
separately:

1. literal left multiplication by `D` and `R=SD` versus the claimed
   orientation/occupation normal form;
2. singular values from a direct Gram matrix rather than from the asserted
   diagonal form alone;
3. the Markov additive functional and martingale decomposition of `Z_n`;
4. the signed-occupation transfer matrix, its characteristic polynomial, the
   absolute-value squeeze, and both deterministic endpoints; and
5. the P91/P93 collision boundary and the three cited owner records.

## Hostile findings

### CRITICAL

None.

### MAJOR

No mathematical or reproducibility defect.

One **release-only owner gate** remains: the source audit is bounded and has
not been replaced by an expert search for the exact atom pair
`D=diag(a,1), R=SD`.  Furstenberg--Kesten, generalized-Lyapunov transfer
methods, and the martingale CLT are correctly subtracted, but search absence
cannot establish priority.  No source change is appropriate because the
abstract, introduction, evidence ledger, and conclusion already state
external HOLD and avoid absolute novelty language.

### MINOR

None requiring repair.

## Formula-by-formula reconstruction

- For the left product `M_n=A_n...A_1`, the pre-update occupation convention
  gives
  `M_n=S^(J_n) diag(a^(U_n),a^(n-U_n))`.  The one-letter sentinel `M_1=R`
  fixes the otherwise easy-to-reverse convention.
- Since `S` is orthogonal and `0<a<1`, ordering the diagonal magnitudes gives
  the stated `sigma_max`, `sigma_min`, determinant magnitude, and condition
  number.  The exclusion of `a=0,1` is explicit.
- With `rho=1-2q`, summing
  `xi_t=Y_t-rho Y_(t-1)` yields the displayed bounded-endpoint martingale
  decomposition.  Its deterministic quadratic variation gives
  `(1-rho^2)/(1-rho)^2=(1-q)/q`.  The nonstationary initial state contributes
  only a bounded term.
- At `q=0`, `Z_n=n` and the top norm is one.  At `q=1`, `Z_n` is `0/1` by
  parity.  Neither endpoint is inferred from the interior aperiodic-chain
  argument.
- For pre-transition weights,
  `E exp(theta Z_n)=e_+^T(diag(e^theta,e^-theta)P)^n 1`.  The trace is
  `2(1-q)cosh(theta)` and the determinant is `1-2q`; the displayed positive
  root follows.  Evaluating the characteristic polynomial at one gives a
  strict negative value exactly when `0<q<1` and `s>0`.
- P91 uses a deterministic reverser shift and periodic/zeta invariants; P93
  uses a noninvertible stack with a boundary.  P104 is an invertible iid
  matrix cocycle with singular-value pressure.  The shared two-state additive
  mechanism is disclosed rather than claimed.

## Reproducibility and PDF gate

- Fresh exact control: **PASS**, 741,486 assertions.
- Stored stdout comparison: byte-for-byte **PASS**.
- Four stages: **PASS** (`pdflatex`, `bibtex`, `pdflatex`, `pdflatex`).
- PDF: 5 A4 pages, 307,296 bytes, PDF 1.5.
- Final log: zero undefined citations/references, package warnings,
  multiply-defined labels, or over/underfull boxes.
- Fonts: 23/23 embedded, subsetted, and Unicode-mapped.
- All five rendered pages visually inspected: **PASS**.

## Actual repairs

None.  The author-stage source and evidence statements were already accurate;
this review adds only the present independent audit ledger.

## Residual risk

The exact specialized cocycle could still have a direct owner missed by the
bounded query set.  This affects external circulation, not the validity of
the proved formulas.  External release, submission, contact, novelty, and
priority claims remain **HOLD**.
