# SD-C12 Source Lock

- **Primary family:** countable Symbolic Dynamics only.
- **Atoms:** tensor-indecomposable full shifts `F_p`, ordered by topological
  entropy `log p`.
- **Grammar:** the atom-reduced loop grammar; each atom loop is primitive and
  its powers are repetitions.
- **Grading/modeling rule:** adjacent entropy ranks form blocks
  `(p_(2n-1) | p_(2n))`, with odd rank even/super-plus and even rank
  odd/super-minus. This is canonical only relative to the ordered list's
  starting point and chosen orientation.
- **Roof:** the intrinsic entropy roof `tau(F_p)=log p`.
- **Function spaces:** `H_+=ell^2(N)` and `H_-=ell^2(N)` with the canonical
  rank-pairing unitary.
- **Transfers:** `D_s^+=diag(p_(2n-1)^(-s))` and
  `D_s^-=diag(p_(2n)^(-s))`.
- **Primary operator:** the relative quotient
  `(I-zD_s^+)(I-zU^*D_s^-U)^(-1)`.
- **Determinant:** ordinary Fredholm determinant of that `I+S_1` quotient;
  primary normalization `z=1`. On `Re(s)<=1` it is not a quotient of two
  standalone Fredholm determinants.
- **Reflection completion:** `H(s,z)=R(s,z)R(1-s,z)`.
- **Allowed data:** tensor structure, entropy order, exact symbolic traces,
  and target-free matched-inventory controls.
- **Forbidden data:** Riemann-zero tables, fitted phases/scales, inserted
  von Mangoldt weights, post-hoc prime signs, and another primary system
  family.

Claim boundary: exact relative trace-class and determinant theorems, exact
reflection, critical-line motion, a zero-free strip, and a finite-block
cancellation rigidity theorem. No positive Euler ledger, target divisor,
analytic completion, or Hilbert--Polya operator is claimed.

Evaluation boundary: the exact relative object is auxiliary. Its signed ledger
fails the Route-A target primitive-orbit orientation; the reflected product is
formed tautologically by multiplying the copy at `1-s`, not derived as an
arithmetic functional equation. Overall status:
`ROUTE_A_REJECTED / STOP_SCOPED / PROVES_TOO_MUCH`.
