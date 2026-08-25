# C166 exact-validation plan

1. Generate the canonical evidence over `1<=r<=6`, `2<=d<=16`, and every
   iterate through `2M`; these 25,200 coefficient-clock cases are sentinels.
2. Directly iterate every state whenever `q^d<=4096` and verify the exact
   first return `M` without using the coefficient formula.
3. Construct the substitution matrix by truncated polynomial multiplication;
   check its square and its conjugation of multiplication by `1+t`.
4. Reconstruct the same matrix independently from
   `S_(i,j)=(-1)^i binom(i-1,j-1)` and rerun all clock checks by Pascal-row
   recurrence.
5. Run a separate SymPy path, canonical byte replay, repaired-hash semantic
   mutations, and a stale-hash control.
6. Build three content-distinct paper stages and verify the final PDF twice at
   fixed epoch `1787616000`, including fonts, logs, pages, and visual layout.

Finite ranges are regression sentinels only.  The theorem range is every
`r>=1,d>=2,n>=1` and is established in `THEOREM_PACKAGE.md`.
