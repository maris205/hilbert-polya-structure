# Cross-hostile review B — P104

Date: 29 August 2026.  Reviewer role: second independent reviewer, separate
from the author and review A.  External circulation remains **HOLD**.

## Verdict

**Internal PASS.**  Unresolved CRITICAL: 0.  Unresolved MAJOR: 0.
Unresolved MINOR: 0.  No source repair was required by this pass.  All
finite-word identities, endpoint branches, limit normalizations, and the
annealed-pressure formula survived a derivation from the two generators.

## Independent formula attack

1. **Composition orientation and normal form.**  With the stated left
   product `M_n=A_n...A_1`, direct multiplication from both orientation
   states gives
   `M_n=S^(J_n) diag(a^(U_n),a^(n-U_n))`, where `U_n` counts the state
   before the next letter acts.  The one-letter word `R=SD` fixes the
   convention.  Taking the Gram matrix independently reproduces the two
   singular values, `|det M_n|=a^n`, and `kappa_2=a^(-|Z_n|)`.
2. **Quenched endpoints and interior CLT.**  For `0<q<1`,
   `Y_t=(-1)^(J_t)` has correlation parameter `rho=1-2q`.  The martingale
   differences `xi_t=Y_t-rho Y_(t-1)` have deterministic conditional
   variance `1-rho^2`, while
   `(1-rho)Z_n=sum xi_t+Y_0-rho Y_(n-1)`.  Hence the variance is
   `(1+rho)/(1-rho)=(1-q)/q`, with no missing factor of two.  Continuous
   mapping gives exactly the three folded-normal displays.  The reducible
   `q=0` and periodic `q=1` chains are correctly handled outside this CLT.
3. **Annealed exponent.**  Because occupation is pre-transition,
   `E exp(theta Z_n)=e_+^T[diag(e^theta,e^-theta)P]^n 1`.
   Its trace is `2(1-q)cosh(theta)` and determinant `1-2q`; the displayed
   Perron root follows.  Combining
   `||M_n||_2^s=a^(sn/2)exp(theta|Z_n|)` with the two-sided exponential
   squeeze proves the claimed exponent.  Evaluating the characteristic
   polynomial at one gives `2(1-q)(1-cosh(theta))<0`, proving the strict
   interior gap.  At `q=0,1` the root and exponent reduce to the separately
   stated endpoint values.
4. **Finite-time recurrence.**  Cayley--Hamilton applied to the same
   two-state transfer matrix yields the displayed second-order recurrence;
   it is not used circularly to establish the Perron limit.

## Proof, owner, and collision scope

The martingale CLT, Furstenberg--Kesten framework, and tilted-transfer
method are explicitly assigned to their established owners.  A bounded
targeted search did not reveal a direct source for this exact two-atom
monomial cocycle and the conjunction of its folded fluctuations and strict
annealed gap.  Search absence is not a priority certificate, so specialist
direct-owner review remains a release gate.

The strongest internal overlaps are already disclosed: P91 also contains a
two-state reversal mechanism but studies deterministic shift periods and
zeta data; P93 uses a reflected noninvertible push--pop stack.  P104 instead
has an invertible random matrix product, constant determinant magnitude, and
singular-value/moment observables.  P101 also has stochastic synchronization,
but its capped scalar state and absorption law do not reproduce the matrix
cocycle, transfer spectrum, or folded CLT.  These are motif collisions, not
theorem duplication.

## Control independence

The verifier's primary lane multiplies literal rational `2 x 2` matrices and
compares the result with the normal form.  Separate dynamic-programming,
signed-transform, moment, endpoint, and recurrence lanes do not infer their
expected data from that literal multiplication.  A fresh frozen-tree run
reported **741,486 assertions** and reproduced the stored stdout byte for
byte.  The finite controls verify the algebra and finite distributions; they
do not purport to prove the asymptotic martingale CLT.

## LaTeX/PDF replay

The exact sequence `pdflatex -> bibtex -> pdflatex -> pdflatex` exited zero.
Final `main.log`/`main.blg` scans found no substantive warning, undefined
citation/reference, multiply-defined label, overfull/underfull box, or
error.  The PDF has 5 A4 pages and 307,296 bytes.  All 23 font entries are
embedded, subsetted, and Unicode-mapped; layout text extraction recovered
17,326 bytes.  All five rendered pages were visually inspected with no
clipping, collision, malformed display, or orphaned heading.

## Residual risk

- **Direct-owner risk: medium.**  The model is an elementary specialization
  of Markov-additive random matrix theory and could have appeared under
  different notation.
- **Asymptotic-control risk: low.**  The limit theorem rests on the written
  martingale argument, appropriately not on finite enumeration.
- **Release status: HOLD.**  No absolute novelty or priority inference is
  authorized.
