# Evidence and source lock — `ANG-20260914-SCS01`

Carrier sources: Connes and Consani, [*The Scaling Site*](https://arxiv.org/abs/1507.05818), and [*Knots, Primes and the adele class space*](https://arxiv.org/abs/2401.08401). They give the `N^times` site action and `C_p=R_+^times/p^Z` of length `log p`.

Symbolic source: Holt, [*Discrete dynamics of Eratosthenes sieve*](https://arxiv.org/abs/2608.26384), recorded locally in [019](../019-primorial-gap-recursion-control/paper.md). Its R1 step reads `p_(k+1)=g_1+1` from `G(P_k)`.

Bridge definition: the finite prime-exponent vector of `P_k` is its finite
supernatural/finite-adele coordinate `[P_k]`; R1–R3 maps to
`[P_k] -> [p_(k+1)P_k]`. This is a lineage coding only, not orbit generation.

Boundary refinement: `[P_k,1]=[1,P_k^(-1)]` in the quotient, placing coded
stages on the free scaling orbit. The free orbit is dense in every `C_p`.
Density does not prove a discrete primorial limit, landing, or factor map.

Canonical landing test: because `[P_k,1]=[1,P_k^(-1)]` in the quotient and
`P_k^(-1)->0`, the coded sequence tends to `[1,0]`. The arithmetic-site source
identifies the `A_f x {0}` contribution as fixed by the scaling action. Prime
orbits instead require a vanishing *finite* component at the selected prime.
Thus this canonical limit is not a nontrivial `C_p`.
