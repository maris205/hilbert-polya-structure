# C163 theorem-and-evidence plan

## Frozen object and conventions

- One-site gate: `A=F3^* diag(1,0,1)`.
- Register dynamics: the cyclic Walsh shift `B_k`.
- Clock: one `B_k` application is one tick; `C_k=B_k^k` is one full cycle.
- Phase: `rho/|rho|` for nonzero `rho` only.
- Measure: algebraic multiplicity divided by `2^k`.
- Joint variable: `Y_k=sqrt(k)((1/k)log|rho|+log(3)/4)`.

## Gates

1. Reconstruct the one-site polynomial and C158 modulus invariants exactly.
2. Derive `c=2cos(delta)`, prove that `3c^4-19c^2+27` is its primitive
   irreducible integer polynomial, and identify the monic rational minimal
   polynomial `c^4-(19/3)c^2+9`; its nonintegral coefficient excludes a
   root-of-unity phase ratio.
3. Prove the all-`k` binomial Fourier identity and Haar limit.
4. Prove the mixed characteristic/Fourier formula and the product
   Gaussian--Haar limit.
5. Prove the general binary torsion/non-torsion dichotomy; reconstruct the
   moved-hole order-four control.
6. Freeze exact ledgers, run independent and SymPy paths, byte replay, and
   repaired/stale-hash mutations.
7. Complete two manuscript-improvement rounds, deterministic PDF builds,
   font/layout inspection, Route-A evaluation, and manifest closure.

## Pivot rule

If Gate 2 cannot be made unconditional, abandon this candidate and switch to
a natural quantum walk with a provably non-torsion coin-phase ratio.  Gate 2
passes for the original gate; `pivot_required=false` is therefore recorded.

All stages forbid target zero/divisor tables, primes, arithmetic local data,
Euler factors, root numbers, automorphy, Hilbert--Polya claims, and Route B.
