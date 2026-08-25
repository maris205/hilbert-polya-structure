# C153 results

- Exact rank ledger: 624 rows (`k<=24`, `0<=n<=2k`).
- Exact macroscopic ledger: 192 rows (eight rational alpha values, `k<=24`).
- Fixed-period cluster ledgers: 20, with every divisor class represented by an
  explicit infinite gcd subsequence and equal complex values merged.
- All-parameter rank:
  `rank(B_k^n)=2^min(n,k)3^(k-min(n,k))`.
- Signed macroscopic log survival:
  `min(alpha,1)log(2/3)`; positive escape exponent:
  `min(alpha,1)log(3/2)`.
- Fixed-period normalized traces: `3^(-k)Tr(B_k^n)->0`.
- Raw-trace obstruction at period two: the odd and even subsequences have
  distinct exact constant values.
- Route-A tuple:
  `(A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)`.

The finite ledgers validate implementations; the theorem package supplies the
all-parameter proofs.
