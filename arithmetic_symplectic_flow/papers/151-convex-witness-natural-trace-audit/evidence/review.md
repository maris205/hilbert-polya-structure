# Bounded independent-task model review — ASFS-20260915-CWT01

**Date:** 2026-09-15.  
**Reviewed:** the full [paper](../paper.md), [frozen card](../candidate-card.md),
[claim ledger](../claim-ledger.md), [summary](../README.md), and
[evidence index](README.md).

**Result:** The three stated analytic obstructions pass this bounded
mathematical review. No mathematical correction was required. The complete
periodic-count argument and its separation from operator traces were also
checked.

This is a separate task-context review by a model in the same agent family.
The reviewer received the proposed arguments and formulas before checking
the complete manuscript, so this was not a blind review. Evidence is
limited to manual mathematical rechecking. It is not human peer review,
cross-model validation, formal proof-assistant certification, or a formal
Route evaluation. No numerical cross-check or external literature
verification was performed.

## 1. Full-area operator

The displayed global inverse and symplectic pullback show that the full
map is invertible and preserves componentwise area. Consequently
composition with F is an isometry of the full L2 space and composition
with its inverse is the inverse operator: U_0 is unitary, not merely an
isometry into a proper subspace.

The full space is infinite-dimensional already on one component plane.
Normalized indicators of pairwise disjoint unit squares form an
orthonormal sequence. For any fixed finite complex s, images under U_s
have pairwise distance sqrt(2) exp(-Re(s)), a strictly positive number.
This proves noncompactness and therefore excludes trace-class membership.
The same proof applies to each positive power.

The manuscript correctly stops the proposed ordinary trace-class
Fredholm determinant. Small nonzero operator norm for large Re(s) does
not make an infinite-dimensional scalar multiple of a unitary operator
compact. No conclusion about every different transfer space, smoothing
operator, or regularized determinant is justified or claimed.

## 2. Local index of every repetition

For each fixed returning period m=r K_p, the only fixed point on a prime
phase plane is (1,1). The auxiliary family H_eta adds a strictly positive
constant to the same square force. Summing the recurrence over a
hypothetical m-cycle gives

\[
0=\sum_{t=0}^{m-1}(x_{t+1}-1)^2+m\eta,
\]

which excludes every cycle when eta>0.

The required degree-homotopy condition is explicitly present: the
original return has no fixed point on the compact boundary of a small
ball, and uniform continuity there supplies a sufficiently small
parameter interval avoiding all boundary zeros. Thus the original
local degree equals the zero degree of a fixed-point-free endpoint.
The interval may depend on m; no all-period uniform estimate is needed.

Every phase point and every repetition therefore has index zero, not
the counting weight +1. The auxiliary perturbation is a proof homotopy
specified in the analytic contract, not an unnoticed replacement map.
No global noncompact Lefschetz formula is used.

## 3. Gaussian graph/diagonal test

At integer label 2 the witness vanishes and the exact difference map is

\[
F(q,p)-(q,p)=(u,u+v^2),\qquad
u=p-q,\quad v=p-1.
\]

The absolute coordinate Jacobian is one. The substitution
u=epsilon a, v=sqrt(epsilon)b contributes epsilon to the power 3/2
against the Gaussian normalization epsilon to the power -2. Hence
epsilon to the power 1/2 times the local integral has precisely the
integrand in equation (14) of the paper.

The transformed cutoff tends pointwise to one and is bounded uniformly
by its fixed supremum. The majorant is integrable because

\[
\frac{a^2+(a+b^2)^2}{2}
=(a+b^2/2)^2+b^4/4,
\]

and integration first in a leaves sqrt(pi) exp(-b^4/4). Dominated
convergence therefore proves the stated positive finite limiting
constant C and the exact asymptotic C epsilon to the power -1/2.

This checks one explicitly normalized positive Gaussian family with a
fixed cutoff. It is not a universal obstruction to every finite-part
prescription, distributional extension, or alternative regularization.
The nonzero scalar e^(-s) from the weighted Koopman kernel cannot remove
the divergence of this particular test.

## 4. Counting, ownership and disposition

The full cycle-sum proof still gives exactly one primitive K_p packet
per prime, including the distinct fixed packets for labels 2 and 3.
For a fixed positive m, the condition K_p dividing m limits p to a
finite set, so the stated N_m is finite. Its regrouping at m=r K_p
produces the coefficient 1/r and the ordinary product on Re(s)>log 2.
That counting identity does not become an area Hilbert trace, a
local-index sum, or a finite Gaussian diagonal integral.

The new analytic-owner ID and the unchanged geometric formula and unit
roof are consistently disclosed. The paper retains the positive
geometric and scalar results while stopping only the three frozen
analytic proposals. Its broader analytic possibilities remain OPEN,
formal Route coordinates remain UNASSIGNED, and Route B is NOT INVOKED.
