# HCS-C19 frozen experiment plan

## Question

Does the adopted period-seven formula define a genuine generic Hénon cycle,
does its parameter-varying coordinate curve have positive genus, and can
orientation be retained rather than averaged away?

## Frozen objects and clocks

- recurrence: \(x_{i+1}=a-x_i^2-x_{i-1}\);
- parameter relation: \(a=\sigma^2-2\sigma\);
- scalar control: normalization \(C\) of the adopted septic \(P(\sigma,x)\);
- chronological object: ordered-edge cover \(\widetilde C\) with
  \(\tau(x,y)=(a-x^2-y,x)\);
- Hénon time: \(s\in\mathbb Z/7\mathbb Z\);
- arithmetic clock: Frobenius extension degree \(r\), kept distinct from
  \(s\) and the fixed period label \(n=7\);
- forbidden data: Riemann zeros and target prime tables.

## Exact gates

1. Refute or validate the literal Eq. (16) with an exact source fibre.
2. Prove geometric integrality and factor \(\operatorname{Disc}_xP\).
3. Compute the generic neighbor gcd in \(\mathbb Q(\sigma)[x]/(P)\).
4. Prove distinct nonloop neighbors, symmetry, graph connectedness, and exact
   period seven.
5. Construct the degree-14 ordered-edge cover and verify \(\tau\) and reversal.
6. Resolve the scalar curve in characteristic zero and compute its genus by
   Riemann--Hurwitz and plane-septic defects.
7. Count affine points at \(p=5,11,13\) and apply the frozen branch ledger,
   keeping good-reduction status explicit.
8. Recover candidate reciprocal numerators and repeat all counts independently.
9. Apply Route A to \((\widetilde C,\tau)\), not to an averaged transition
   matrix or to the scalar quotient alone.

## Decision

- `GENERIC_HENON_PASS`: exact neighbor correspondence gives one seven-cycle.
- `ORIENTATION_PASS`: ordered edges carry \(\tau\) of exact order seven.
- `POSITIVE_GEOMETRY`: the scalar quotient has genus three.
- `GOOD_REDUCTION_OPEN`: finite-prime rows remain branch-corrected candidates.
- `ROUTE_A_EXPLORATORY`: A1 improves, but A2/A3 fail and A4 is only a formal
  hint; Route B remains closed.
