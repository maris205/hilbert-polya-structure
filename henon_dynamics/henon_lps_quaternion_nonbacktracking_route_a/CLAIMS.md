# Claims

1. The six norm-five quaternions give a symmetric set of six distinct
   projective matrices for every eligible `q`; changing the square root of
   `-1` conjugates the set.
2. The LPS theorem identifies the connected graph as the Cayley graph of
   `PSL2(F_q)` when `(5/q)=1` and of `PGL2(F_q)` when `(5/q)=-1`.  The exact
   vertex counts are `q(q^2-1)/2` and `q(q^2-1)` respectively.
3. The `PGL2` chamber is bipartite with the determinant-square class as its
   two-coloring.  The connected `PSL2` chamber is nonbipartite.
4. For adjacency `A_q` and oriented-edge Hashimoto operator `H_q`,
   `det(I-uH_q)=(1-u^2)^(2|V_q|)det(I-uA_q+5u^2I)`.
   Its traces count closed cyclically nonbacktracking oriented walks, and
   Möbius inversion gives every primitive oriented cycle count.
5. The LPS Ramanujan bound implies that all Hashimoto eigenvalues other than
   the trivial `±1,±5` possibilities lie on `|mu|=sqrt(5)`.  The `-5`
   eigenvalue occurs exactly in the bipartite chamber.
6. Quadratic reciprocity and the prime number theorem for arithmetic
   progressions give conditional natural density `1/2` for each chamber
   among eligible primes.

Claims 2 and the adjacency Ramanujan bound use the cited LPS theorem; claim
4 uses the cited general Bass--Hashimoto identity.  The package proves the
remaining deductions and exact specialization.  None is a target arithmetic
local factor or target zero statement.

Under the strict Route-A evaluator v0.2, claim 4 remains an exact
source-graph theorem but earns only `A1_WEAK`: `q` and its primality are not
carried by individual primitive orbits, no `p <-> gamma_p` or prime-power
repetition law is proved, no intrinsic `log p` or von Mangoldt orbit weight
appears, and the mandatory shuffled-period, random-weight, random-phase, and
same-density-length controls have not been run at the orbit-correspondence
layer.  The exact wrong-residue-prime, matched-composite, and chamber-label
shuffle tests are A0 controls, not substitutes for these A1 tests.  Hence the
overall status is `ROUTE_A_EXPLORATORY`.
