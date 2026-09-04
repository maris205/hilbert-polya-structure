# Theorem package

Let `m=2^n`, `alpha_n=2^(1/m)`, `zeta_m` be primitive, and

```text
R_n={zeta_m^j alpha_n : j in Z/m},
K_n=Q(R_n)=Q(alpha_n,zeta_m).
```

For odd `a`, put `chi_2(a)=(2/a)=(-1)^((a^2-1)/8)`.

## Main theorem

For every `n>=3`:

1. `Q(alpha_n) intersect Q(zeta_m)=Q(sqrt(2))`, and
   `[K_n:Q]=2^(2n-2)`.
2. Under the faithful action on indices `j in Z/m`,

   ```text
   Gal(K_n/Q) = H_n
     = {(a,b) in (Z/m)^times semidirect Z/m : (-1)^b=chi_2(a)},
   (a,b): j -> a*j+b.
   ```

   Thus `H_n` has order `2^(2n-2)` and index two in
   `AGL_1(Z/m)`.
3. Restriction from level `n+1` is coordinate reduction
   `(a,b) mod 2^(n+1) -> (a,b) mod 2^n`.  It is surjective and has kernel
   order four.  Consequently the infinite image is

   ```text
   H_infinity={(a,b) in Z_2^times semidirect Z_2:
               (-1)^(b mod 2)=chi_2(a)},
   ```

   a closed index-two subgroup of the 2-adic affine group.
4. In the permutation action on `R_n`, the number of elements with exactly
   `r` fixed roots is

   ```text
   r=2:       2^(2n-4),
   r=2^k:     2^(2n-2k-1) for 3<=k<n,
   r=2^n:     1,
   r=0:       2^(2n-2) minus the preceding sum.
   ```

   No element has exactly one or four fixed roots.
5. The odd primes for which `x^(2^n)=2` has a root modulo `p` have natural
   density

   ```text
   delta_n=7/24+1/(3*4^(n-1)).
   ```

   More strongly, each nonzero root multiplicity has the Chebotarev
   density obtained by dividing its count in item 4 by `|H_n|`.
   Therefore `delta_n` decreases to `7/24`.
6. Pullback along the Galois permutations gives a canonical unitary
   representation on `l^2(R_n)`.  This is a finite Koopman realization.
   No family-wide antiunitary taking every action to its inverse, nontrivial
   phase/weight preservation law, or global self-adjoint Hamiltonian owner is
   proved, so the strict grade is `A4_FORMAL_HINT`.

## Route-A rating boundary

The all-level statements above remain proved as written.  They do not,
however, provide an all-level primitive-cycle/repetition enumeration,
orientation and phase data, multiplicity weights, monodromy/stability, or
an intrinsic `p <-> gamma_p` and `log p` period law.  The mandatory A1
shuffled-period, random-weight, random-phase, same-density-length,
neighboring-parameter, and simpler-parent orbit tests are uncompleted.
Thus strict evaluator v0.2 assigns `A1_WEAK` and overall
`ROUTE_A_EXPLORATORY`.

At A0, neighboring basepoint 3 is an analytic control with trivial
radical--cyclotomic intersection and full affine image; the exhaustively
checked full-affine parent restores `2^(2n-5)` four-fixed-root elements; and
the odd-composite ledger retains five prime powers as `Frob_p^r` repetition
classes while rejecting only twenty mixed composites as single-prime owners.
These controls support specificity but do not upgrade A1.

## Proof dependency map

```text
sqrt(2)=zeta_8+zeta_8^(-1)
        |
sqrt(2) is not a square in Q(zeta_m)
        |
Capelli irreducibility of X^(m/2)-sqrt(2)
        |
intersection and [K_n:Q]
        |
shared-sqrt(2) parity relation + equal cardinality
        |
exact H_n image ----> coordinate restrictions ----> H_infinity
        |
linear congruence (a-1)j=-b
        |
fixed-root law ----> Chebotarev density
```

The full proof is in `proof/ANALYTIC_PROOF.md` and is reproduced in the
final paper.  No arrow in this chain uses the finite evidence table.

## Ownership boundary

HCS-C12A retains the universal zero-dimensional statement that a finite
Frobenius permutation has fixed-point traces and a reciprocal finite
determinant.  C374 owns the basepoint-two all-level radical--cyclotomic
entanglement, exact affine image and restrictions, fixed-root spectrum, and
Chebotarev root-density formula.
