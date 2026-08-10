# HCS-C26 methodology blueprint

## Design

This is a theorem-first obstruction study with an exact computational
certificate.  The new theorem is an application of two already released
facts, not a new proof of either one:

1. HCS-C24: an absolutely summable family of distinct metaplectic atoms has
   essential norm bounded below by the `ell^2` norm of its coefficients.
2. HCS-C25: fixed-start Rauzy return words have distinct full matrices; in
   the full-rank four-letter `H(2)` model their projected symplectic matrices
   remain distinct, and the AGY weights are absolutely summable throughout
   `Re(s)>-sigma_0`.

The C26 contribution is to expose the whole transfer operator through a
bounded constant/evaluation slice.  That replaces the branch-supported bump
used in C25 and therefore applies to standard holomorphic spaces where a
nonzero compactly supported function cannot exist.

## Main proof chain

Let `F=L^2(R^2)`.  For a vector-valued function space `X`, define

\[
J:\mathscr F\to X,\qquad (Jv)(x)=v,
\qquad
E_{x_0}:X\to\mathscr F,\qquad E_{x_0}F=F(x_0).
\]

The experiment checks the following gates in order.

1. `J` and `E_x0` are bounded for the proposed realization.
2. The literal pointwise branch series is bounded on `X`.
3. Absolute scalar summability at `x0` follows from
   `sum_gamma ||w_s,gamma||_infinity < infinity`.
4. Pointwise evaluation gives the exact identity

   \[
   E_{x_0}\mathcal L_sJ
   =\sum_{\gamma\in\Gamma}w_{s,\gamma}(x_0)U_\gamma.
   \]

5. HCS-C25 matrix injectivity removes projected-atom aggregation; every
   coefficient is nonzero.
6. HCS-C24 gives

   \[
   \left\|E_{x_0}\mathcal L_sJ\right\|_{\rm ess}
   \ge
   \left(\sum_\gamma|w_{s,\gamma}(x_0)|^2\right)^{1/2}.
   \]

7. The two-sided ideal property of compact operators yields

   \[
   \|\mathcal L_s\|_{\rm ess}
   \ge
   \frac{\left(\sum_\gamma|w_{s,\gamma}(x_0)|^2\right)^{1/2}}
        {\|E_{x_0}\|\,\|J\|}>0.
   \]

The certified HCS-C25 branch `gamma_*` gives the explicit weaker bound

\[
\|\mathcal L_s\|_{\rm ess}
\ge
\frac{S_*(x_0)^{-(\operatorname{Re}s+4)}}
     {\|E_{x_0}\|\,\|J\|}.
\]

## Computational experiment

The producer independently rebuilds the four-letter Rauzy graph, the
length-128 source branch, its chronological matrix, projective point, roof,
and Jacobian.  It emits exact integers and fractions plus the explicit
one-atom lower bounds at selected real parts of `s`.

The checker does not import producer code.  It recomputes every released
quantity, verifies the slice identity symbolically at the coefficient level,
checks the HCS-C24/HCS-C25 dependency conditions, and runs registered
mutations for chronology, transpose, normalization, exponent, and sign
errors.  A finite first-return ledger is retained only as an implementation
sentinel; it is not evidence for the all-length decoder theorem.

## Scalar holomorphic sub-study

The stronger scalar statement is audited separately.  It requires:

- a bounded complex neighborhood `Omega` of the real section;
- one `Omega'` compactly contained in `Omega` with
  `h_gamma(Omega) subset Omega'` for every branch;
- denominators uniformly separated from zero and a single holomorphic
  logarithm convention;
- `sum_gamma sup_Omega |w_s,gamma| < infinity`;
- a cited nuclearity theorem whose hypotheses match this countable system;
- a justified interchange for traces of powers.

Failure of any item leaves scalar nuclearity **open**.  It does not weaken
the vector-valued no-go theorem.

## Validity threats and controls

| Threat | Control |
|---|---|
| Repackaging C24 as a new theorem | Cite C24 as the atomic input and identify only the C26 slice application as new. |
| Assuming holomorphic branch localizers | Use constants and one point evaluation; no branch isolation occurs. |
| Cancelling distinct chronological branches | Invoke the C25 all-length decoder and full-rank symplectic conjugation. |
| Treating a distribution character as a trace | Ordinary trace claims stop at noncompactness; Weil character formulas remain outside the determinant claim. |
| Inferring a complex domain from real contraction | Run a separate proof audit; downgrade the scalar half if any uniformity gate remains open. |
| Confusing finite tests with an infinite theorem | Label finite enumeration as a mutation sentinel only. |
| Losing genuine non-autonomous chronology | Multiply later edges on the left and retain pathwise metaplectic lifts. |

## Reproducibility contract

- exact arithmetic for all integer and rational witnesses;
- deterministic scripts with no random seed;
- independent producer and checker implementations;
- mutation tests for every convention that can reverse the conclusion;
- SHA-256 manifest for released source and result artifacts;
- a one-command runner and a compilation report for the paper.
