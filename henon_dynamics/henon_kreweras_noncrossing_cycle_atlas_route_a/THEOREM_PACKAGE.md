# HCS-C209 theorem package: the ordinary Kreweras cycle atlas

## Frozen object and conventions

For every integer n >= 1, put the labels 0,1,...,n-1 on a convex n-gon.
`NC(n)` is the set of set partitions whose block hulls are pairwise disjoint.
For a partition π, let `p_π` cycle the entries of each block in increasing
circular order.  Put `c=(0 1 ... n-1)` and define

```text
K(π) = cycles(p_π^{-1} c).
```

This is the orientation used by every script.  Replacing c by c^{-1} changes
only the sign of the displayed rotation.  The clock is one application of K;
the measure is counting measure on NC(n).

Two orders are recorded:

```text
L_n = 1 (n=1), 2 (n=2), 2n (n>=3)       actual permutation order;
G_n = 1 (n=1), 2n (n>=2)                abstract CSP group order.
```

At n=2 the abstract C4 action has a kernel of order two.  Keeping L_n and G_n
separate prevents a common root-of-unity bookkeeping error.

## Main theorem (source-derived, with finite consequences proved here)

For every n >= 1:

1. **Cardinality and rank.**

   ```text
   |NC(n)| = Cat_n = binom(2n,n)/(n+1),
   rank(π) = n - number_of_blocks(π),
   #{π : number_of_blocks(π)=b} = binom(n,b) binom(n,b-1)/n.
   ```

2. **Complement and dihedral identities.**  K is a bijection, reverses
   refinement, and

   ```text
   number_of_blocks(K(π)) = n+1-number_of_blocks(π),
   K^2 = ρ_{-1},       ρ_{-1}(i)=i-1 mod n.
   ```

   Hence K commutes with every rotation.  For every polygon reflection
   `R_j(i)=j-i mod n`,

   ```text
   R_j^2=1,        R_j K R_j = K^{-1}.
   ```

3. **Exact clock order.**  The order of K is 1 at n=1, 2 at n=2, and 2n for
   every n >= 3.  The singleton and two-point actions are explicit boundary
   cases, not generic 2n cycles.

4. **All-iterate fixed counts.**  For n >= 2 reduce d modulo L_n.  If d=2r is
   even, then

   ```text
   F_n(2r) = Cat_n                         if r ≡ 0 (mod n),
             binom(2g,g), g=gcd(n,r)       if 0 < r < n.
   ```

   For odd d, `F_n(d)=binom(n,(n-1)/2)` exactly when n is odd and
   `d ≡ n (mod 2n)`; every other odd row is zero.  At n=1, F_1(d)=1.

5. **Cyclic sieving formulation.**  Let

   ```text
   Cat_n(q) = [2n]_q! / ([n]_q! [n+1]_q!) in Z[q].
   ```

   The type-A order-2n Kreweras-complement CSP gives

   ```text
   F_n(d) = Cat_n(exp(2π i d/G_n)).
   ```

   For n=2 this evaluates at fourth roots for the abstract C4, even though
   the image permutation has order two.  The even rows are the ordinary
   rotation CSP of Reiner--Stanton--White; the odd rows are the type-A m=1
   complement CSP verified by White and recorded in Bessis--Reiner.  C209 does
   not claim ownership of either source theorem.

6. **Periods, cycles, zeta, and determinant.**  For every ell dividing L_n,

   ```text
   P_{n,ell} = sum_{d|ell} μ(ell/d) F_n(d),
   C_{n,ell} = P_{n,ell}/ell.
   ```

   P is the population of points of least period ell and C is the cycle count.
   They are nonnegative integers and sum to Cat_n.  The finite Artin--Mazur
   zeta and reciprocal Koopman determinant are

   ```text
   ζ_{K,n}(z) = product_{ell|L_n} (1-z^ell)^(-C_{n,ell}),
   det(I-z U_n) = product_{ell|L_n} (1-z^ell)^(C_{n,ell}) = ζ_{K,n}(z)^(-1).
   ```

7. **Finite Koopman spectrum and reversor.**  For `U_n f=f∘K` on
   `ell²(NC(n))`,

   ```text
   mult(exp(2π i k/L_n))
       = sum_{ell|L_n, L_n divides k*ell} C_{n,ell},
   Tr(U_n^d) = F_n(d).
   ```

   The permutation matrix is unitary.  Complex conjugation composed with R_j
   is an antiunitary reversor.

## Proof and evidence boundary

The complement identities follow from the noncrossing geodesic factorization
`p_π p_{K(π)}=c`; applying it twice gives the stated rotation and block
duality.  For n >= 3, polygon rotation is faithful on NC(n), so K² has order
n.  If n is odd, K^n is an odd power and reverses rank, sending the discrete
partition (rank zero) to the indiscrete partition (rank n-1).  If n is even,
K^n=(K²)^(n/2)=rho_{-n/2}, which is nontrivial by the same faithfulness.
Hence K^n is nonidentity in either parity, while K^(2n)=1, so the order is
2n.  For n=1 and n=2 the sets are a singleton and a two-point transposition.

The all-n fixed formula is source-derived from the type-A CSP.  At even powers,
the root specialization is the ordinary rotation count `binom(2g,g)`.  At odd
powers, rank reversal forces `(n+1)/2` blocks; cyclotomic cancellation leaves
only the central half-turn for odd n, with value `binom(n,(n-1)/2)`.  Möbius
inversion, zeta, determinant, spectrum, and antiunitary identities are finite
permutation arguments proved directly.

The executable enumerator is a regression test only: it builds all partitions
through n=8 (2,055 partitions in total).  SymPy independently checks all
q-polynomial root values through n=12, while the closed formula ledger runs
through n=24.  Finite enumeration does not prove the all-n CSP.

## Scope and route verdict

The source is a finite combinatorial clock.  n, Catalan/Narayana counts, and
polygon roots have no intrinsic rational-prime carrier.  No target prime/zero
table, local arithmetic datum, Euler factor, root number, target divisor,
functional equation, automorphy assertion, or Hilbert--Polya operator is used.
The conservative tuple is

```text
(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)
overall = ROUTE_A_REJECTED; route_b_invocation_allowed = false.
```

`A4_NATURAL_QUANTIZATION` means only the source-native finite Koopman
permutation unitary with the same clock/counting normalization and its
reflection antiunitary reversor.  It is generally non-self-adjoint, has no
arithmetic phase or weight, and is not a Hilbert--Polya operator.

## Relation to HCS-C187

C187 owns promotion of rectangular standard Young tableaux, its q-hook
polynomial, and evacuation.  C209 owns ordinary set partitions, geometric
Kreweras complement, K² polygon rotation, and the order-2n complement clock.
They have different state sets, actions, source owners, and theorem statements;
C209 is not a parameter continuation or subdivision of C187.

## References (attribution only)

* G. Kreweras, *Sur les partitions non croisées d'un cycle*, Discrete
  Mathematics 1 (1972), 333--350, DOI `10.1016/0012-365X(72)90041-6`.
* V. Reiner, D. Stanton, and D. White, *The cyclic sieving phenomenon*,
  Journal of Combinatorial Theory, Series A 108 (2004), 17--50, DOI
  `10.1016/j.jcta.2004.04.009`.
* D. Bessis and V. Reiner, *Cyclic sieving of noncrossing partitions for
  complex reflection groups*, Annals of Combinatorics 15(2) (2011), 197--222,
  DOI `10.1007/s00026-011-0090-9`, arXiv `math/0701792`.
