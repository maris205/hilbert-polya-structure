# Internal hostile review — P97

Audit date: 2026-08-29 UTC
Disposition: **internal GO after repair / external HOLD**

The initial package was written from the frozen P97 theorem contract.  It was
then attacked in two separate rounds.  Round 1 reconstructed the mathematics
from the definition of the map and independently traced every evidence claim
to the program.  After repair, Round 2 was a separate, strictly read-only
review by the integrating primary agent, who rederived the theorem and
endpoints before returning a severity-ranked report.  The rounds are
independent in reviewer and method; both remain internal adversarial review
rather than external peer review.

## Round 1 — proof reconstruction and endpoint attack

The reviewer recomputed the complete orbit structure from
`Phi(A)=A+A`.  No critical or major mathematical error was found.  Six
precision repairs were implemented:

1. The initial definition used “returns at a positive time” as the definition
   of recurrence.  The manuscript now states topological recurrence first and
   proves its equivalence, on the finite discrete phase space, to membership
   in a functional-graph cycle.
2. The Artin–Mazur product is now explicitly declared to be an identity of
   formal power series, avoiding an unintended analytic-convergence claim.
3. The theorem now writes the affine progression extremizers as
   `a+r{0,...,m-1}` with `r` nonzero, including the exact endpoint convention
   at `m=p`.
4. The order definition now records `h | p-1`, so every displayed cycle
   multiplicity and zeta exponent is manifestly integral.
5. The control language was narrowed from an unqualified claim of independent
   algorithms to two complementary, separately constructed routes.  They use
   a shared literal set-addition primitive but different iterate
   constructions.
6. The claims table said that the finite zeta identity had a direct control,
   but the original program explicitly checked fixed counts and Möbius cycles
   without reconstructing logarithmic zeta coefficients.  A new exact route
   now evaluates `n[z^n] log zeta` from the cycle factors through time `3h`
   for every registered prime.  This added 513 assertions and raised the
   stored ledger from 90,996 to **91,509 exact assertions**.

## Round 1 derivation ledger

- Induction gives `Phi^t(A)=2^t A`, where the right side is the
  `2^t`-fold sumset and not scalar multiplication of a set.
- Iterated Cauchy–Davenport gives
  `|qA| >= min(p,q(|A|-1)+1)`.  Thus every proper nonsingleton grows strictly
  under `Phi` until it reaches the full group.
- The recurrent core is consequently the full group and the singleton layer.
  The zero singleton is fixed; multiplication by `2` partitions the nonzero
  singletons into `(p-1)/h` cycles of length `h=ord_p(2)`.
- Therefore `F(n)=2+(p-1)1_(h|n)`.  The cycle product gives the displayed
  zeta function, and Möbius inversion leaves exactly two cycles of length one
  and `(p-1)/h` cycles of length `h`.
- If `K=ceil(log_2((p-1)/(m-1)))`, the growth envelope absorbs every
  `m`-set by time `K`.  An affine progression has size
  `2^t(m-1)+1` for `t<K` and covers all residues at `K`; hence the bound is
  exact on every layer, including `T_p(p)=0`.
- The first nonbaseline fixed count occurs at `h` and equals `p+1`, so the
  claimed recovery of `(p,h)` is exact.  The empty-set and `p=2` conventions
  were rederived separately and agree with the stated exclusions.

## Round 2 — independent read-only theorem and scope reattack

The separate reviewer reported **CRITICAL = 0** and **MAJOR = 0** after
recomputing the recurrent core, fixed counts, zeta factors, layer depths, all
endpoints, and the safe Vosper range.  Two minor points were returned and both
were resolved:

1. In the arithmetic-progression sharpness proof, the absorption endpoint now
   explicitly says that `2^K(m-1)+1>=p` consecutive integers contain every
   residue modulo `p`; additional modular wraparound is harmless.
2. The assertion total is now anchored to the stored executable output.  The
   manuscript and all ledgers consistently report **91,509**, superseding the
   pre-zeta-probe checkpoint of 90,996.

The remaining Round-2 scope and evidence checks passed:

- all six clauses of the frozen theorem contract have an explicit proof;
- the singleton, full-layer, empty-set, and `p=2` endpoints are stated rather
  than inferred from an invalid logarithm or order;
- the Vosper proposition uses only
  `|A+B|=|A|+|B|-1<=p-2`, and the manuscript explicitly refuses a global
  classification of all depth maximizers;
- Cauchy–Davenport, Vosper rigidity, general iterated-sumset structure, and
  the Artin–Mazur construction are positively attributed and excluded from
  the residual claim;
- all five bibliography entries are cited, every citation key resolves, and
  no uncited bibliography entry remains; and
- the bounded owner search is described only as negative evidence, never as
  a worldwide novelty or priority conclusion.

## Residual risks and verdict

- **Mathematics:** low after a uniform proof reconstruction, five complete
  functional-graph enumerations, all registered layer maxima, and direct
  fixed/zeta/Möbius controls.
- **Scope:** low after the safe-range Vosper restriction and explicit
  owner subtraction.
- **Literature/priority:** medium.  The exact combined finite-dynamics package
  may occur under different additive-combinatorics terminology; bounded
  search cannot settle priority.
- **Review independence:** two internal agents and two distinct protocols;
  this is not institutional or specialist peer review.
- **Verdict:** GO for internal Stage 2 use; HOLD for public release,
  submission, author contact, venue choice, or priority language.
