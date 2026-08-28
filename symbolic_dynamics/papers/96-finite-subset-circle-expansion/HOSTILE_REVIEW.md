# Internal hostile review — P96

Audit date: 2026-08-28 UTC  
Disposition: **internal GO after repair / external HOLD**

The initial package was written by the topological candidate scout. Round 1
was an independent integrating derivation by the primary agent. Round 2 was a
separate, strictly read-only review by the algebraic scout, followed by an
integrating repair pass. This is internal adversarial review, not external
peer review.

## Round 1 — independent mathematical reconstruction

The first pass reconstructed the system from the base map rather than trusting
the displayed formulas.

- `m_Q^ell(x)=x` has exactly `Q^ell-1` points, so Möbius inversion gives the
  base least-period orbit inventory.
- A finite fixed subset is a union of full base cycles. Binary selection of
  each cycle gives `prod_l(1+u^l)^O_l(Q)` and the quotient of ordinary Euler
  products
  `(1-Q*u^2)/((1-Q*u)(1+u))`.
- Coefficient extraction gives
  `E_j(Q)=(Q-1)(Q^j-(-1)^j)/(Q+1)`; summation was checked separately in both
  parity branches.
- Substitution `Q=d^n` gives the alternating Artin--Mazur factors with the
  recorded signs. Möbius inversion gives nonnegative integral temporal orbit
  counts and the stated `k>=2` asymptotic.
- The quotient `(S^1)^k -> exp_k(S^1)` has at most `k^k` points in a fiber;
  Bowen's factor inequality therefore gives entropy `k log d`.
- The nearest outer pole and zero recover `d` and `k`, with no cancellation.

The exact program passed **4,562 assertions** and tested **189,245 literal
rational-circle subsets**. The only mathematical-text correction in Round 1
was replacing `|A_k(d^e)|` by `A_k(d^e)`, because `A_k` is a number rather
than a set.

## Round 2 — owner, endpoint, and evidence attack

The algebraic reviewer independently recomputed every displayed theorem,
reran the original control, performed an isolated four-stage build, and
visually inspected all pages. The core theorem chain survived. The following
substantive repairs were then implemented:

1. **The rigidity endpoint was unnecessarily omitted.** The statement now
   includes `k=1`; its zeta is `(1-z)/(1-dz)`, so the zero at `1` and pole at
   `d^{-1}` recover `d` and then `k=1`. The prime-orbit asymptotic correctly
   remains restricted to `k>=2`.
2. **General mechanisms were overcounted as residual contribution.** The
   finite-permutation orbit-union observation is now positively tied to the
   induced finite-subset literature. The uniformly finite-to-one entropy
   equality is explicitly labeled a standard Bowen-factor consequence. The
   residual result is limited to the circle-multiplication rational collapse,
   parity formulas, unsigned zeta, temporal census, and rigidity.
3. **The owner boundary was expanded.** The manuscript now cites
   Higuera--Illanes for induced finite-subset dynamics, Kwietniak--Oprocha for
   hyperspace entropy context, and Rallis for symmetric-product periodic
   points. Tan is cited by the 2024 journal version, and the formal publication
   year of Akin--Auslander--Nagar is corrected to 2017.
4. **The evidence ledger had outrun the script.** A new formal-zeta probe now
   checks factor signs, every logarithmic coefficient through iterate 15, and
   outer pole/zero recovery for `2<=d<=7`, `1<=k<=9`. The temporal probe now
   includes `k=1`. The registered total increased from 4,562 to **7,000 exact
   assertions** while retaining all 189,245 literal subsets.
5. **Production replay.** After the expanded references caused a small page-1
   vertical overflow, one introductory sentence was tightened. The final
   build has no citation, reference, overfull, underfull, or rerun warning.

## Round 2 derivation ledger

- The quotient direction in the binary Euler transform is correct because
  `1+u^l=(1-u^(2l))/(1-u^l)`.
- The even total is `Q(Q^k-1)/(Q+1)`; the odd total is
  `(Q^(k+1)-1)/(Q+1)`. The `k=1,2,3,4` zeta table matches these polynomials.
- Every least-temporal-period orbit has exactly its period many points, so
  Möbius divisibility is structural rather than an unchecked congruence.
- Proper divisors are at most `m/2`; for `k>=2`, this error is absorbed by
  `d^((k-1)m)`, exactly as stated.
- The multiplicity-preserving symmetric power has fixed count
  `Q^(k-1)(Q-1)` and zeta `(1-d^(k-1)z)/(1-d^k z)`, so it agrees only at
  `k<=2` and does not explain the lower alternating finite-subset factors.

## Bounded literature and scope audit

Tuffley's finite-subset topology and induced degree, qualitative hyperspace
dynamics, general entropy transfer, rotational subsets, and symmetric-product
fixed-index/periodic theory are all positively cited and excluded from the
residual claim. A bounded search did not identify the exact parity-split
unsigned ledger or its rational zeta rigidity for this family. Search absence
is not a novelty or priority proof.

## Residual risks and verdict

- **Mathematics:** low after two derivations, literal subset enumeration, and
  formal zeta/temporal controls.
- **Scope:** low after explicit subtraction of general hyperspace mechanisms.
- **Literature/priority:** medium because differently named finite-set
  dynamical enumerations may remain.
- **Verdict:** GO for internal Stage 2 use; HOLD for public release,
  submission, contact, or priority language.
