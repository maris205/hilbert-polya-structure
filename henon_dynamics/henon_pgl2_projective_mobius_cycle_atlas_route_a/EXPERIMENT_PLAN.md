# Exact regression plan

1. Construct `F_q` from an explicit irreducible polynomial for 18 values `q=2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32`.
2. Enumerate exactly one canonical matrix representative for every class in `PGL_2(F_q)`; the expected count is `q(q^2-1)`.
3. Form the induced permutation of all `q+1` projective points and obtain its cycles without using the trace/determinant classifier.
4. Independently classify from permutation geometry (number of fixed points and cycle lcm), then compare the full type/order histogram with the arbitrary-`q` formulas.
5. Hash every matrix/type/order/cycle record in canonical order so omissions and reorderings are detectable.
6. Cross-check Cayley--Hamilton, reversors, fixed ledgers, zeta/Koopman cycle determinants, and group census symbolically.
7. Require byte replay and rejection of 40 repaired-hash semantic mutations.

Finite evidence is explicitly not the proof. It stress-tests prime, extension, odd, even, and both involution faces against a separate implementation.
