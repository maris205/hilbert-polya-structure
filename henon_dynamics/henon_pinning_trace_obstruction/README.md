# Exact pinning kernels for the area-preserving Hénon map: two obstructions

Date: 2026-08-06  
Candidate: `henon_h6_scalar_signed_pinning_v1`  
Decision: **`C02D_NO_GO; RESEARCH_NOTE_COMPLETE; RETURN_BREADTH_FIRST`**

## Outcome

This project closes the pre-registered C02D route for

\[
H_6(q,p)=(1-6q^2-p,q)
\]

without computing a finite-section spectrum. Two independent kill
conditions occur before such a computation is mathematically authorized.

1. After the coordinate swap, the standard BPS/Rugh pinning construction is
   already an exact one-Hénon-step Cauchy-kernel operator. The C02C
   length-\(N\) endpoint functions are the iterated pinning data in the word
   summands of \(\mathcal L^N\), on their common domain. They are not a
   same-clock finite-memory approximation \(\mathcal L^{[N]}\) of the kind
   frozen in the C02D protocol.
2. With the BPS contour and residual conventions, deleting the orientation
   sign from the elementary kernel gives

   \[
   \operatorname{tr}K_{\rm raw}^n
   =-\sum_{x\in\operatorname{Fix}F^n}
     \frac1{\det(I-DF^n(x))}.
   \]

   The missing constant factor \(-1\), orbit by orbit and for every
   repetition, cannot be supplied by an ordinary multiplicative scalar edge
   cocycle. This is an orbitwise obstruction; it does not exclude an
   accidental equality between aggregate trace sums caused by cancellations
   among distinct orbits. An odd supertrace or reciprocal Fredholm determinant encodes it,
   but these are classical graded mechanisms and the reciprocal is generally
   meromorphic, not a new entire Fredholm determinant.

The conclusion is deliberately scoped. It does **not** prove that every
possible history-space lift or every alternative holomorphic representation
is impossible. It proves that the standard exact pinning kernel does not
support the approximation semantics pre-registered for C02D, and that the
specified orbitwise scalar sign repair fails.

## Positive result retained

The audit also supplies a new explicit domain lemma needed to place this
Hénon survivor inside the pure-hyperbolic BPS framework. Put

\[
X_\sigma=\overline D\!\left(\sigma\frac{23}{48},\frac7{48}\right),
\qquad
Y_\sigma=\overline D\!\left(\sigma\frac{121}{256},\frac{41}{256}\right).
\]

Then \(X_\sigma\Subset Y_\sigma\) with margin \(1/128\), and every
allowed edge has the signed square-root pinning map

\[
P_\sigma(w,z)=\sigma\sqrt{(1-w-z)/6},
\qquad
P_\sigma(Y_t\times X_r)\Subset X_\sigma,
\]

with a certified Euclidean clearance at least \(1/360\) and
\(|\partial_wP|,|\partial_zP|\le2/\sqrt{66}\). These \(Y\)-disks are a
new domain repair in this project; they are not retroactively attributed to
C02C. The result is useful analytic infrastructure, not a Hilbert--Pólya
construction.

## Reproduce

Only the Python standard library is required.

```bash
python3 henon_pinning_trace_obstruction/code/certify_pinning_obstruction.py
python3 henon_pinning_trace_obstruction/code/check_pinning_obstruction.py \
  henon_pinning_trace_obstruction/results/certificate.json
```

Both programs must report `all_checks_pass: true`. The checker reconstructs
the rational geometry and obstruction independently; it does not import the
producer.

## Project map

- `DERIVATION_PACKAGE.md`: frozen object, derivation, scope, and checks.
- `SOURCE_AUDIT.md`: primary-source ledger and novelty boundary.
- `paper/outline.md`: negative-result paper route and theorem order.
- `code/PROTOCOL.md`: pre-computation protocol and tamper policy.
- `code/`: canonical producer and independent checker.
- `results/`: exact rational certificate, checker record, and interpretation.
- `evaluations/route_a/`: schema-complete Route-A rejection record.
- `REPOSITORY_UPDATE.md`: handoff and next breadth-first action.

No prime table, Riemann-zero table, target spectrum, fitted clock, averaged
transition matrix, or Route-B evaluation is used.
