# Initial Proposal

## Source-stage starting point

The starting question was whether the support-one local Hénon analysis could
lead to a genuinely new arithmetic-dynamics theorem, rather than a cosmetic
restatement of its finite-window argument.  The map class under consideration
was

`H(x,y)=(P(x)+ay,x)`

over characteristic zero, with torus points drawn from a finite-rank subgroup
of the ground-field multiplicative group.

No project directory, manuscript, code, data, or experiment was authorized at
the initial-idea stage.

## Candidate pool

### Candidate A: complete support-one degeneracy stratification

Absorb the earlier support-one result and classify every infinite or
positive-dimensional branch for windows `T_1`, `T_2`, and `T_3`, followed by
uniform finiteness at `T_4`.  The anticipated free words were `BA`, `CB`, and
`CBA`, with exact coefficient compatibility conditions.

Potential value: a complete finite/infinite dichotomy and a sharp four-window
theorem.  Main weakness: substantial overlap with the local predecessor, so it
could be standalone only through full absorption and no parallel submission.

### Candidate B: a genuinely sparse two-transition theorem

Take

`P(X)=c+sum_{j=1}^s b_j X^(e_j)`

with actual support `s>=2` and all displayed coefficients nonzero.  Ask whether
every first-local degenerate branch is forced to pass through a multi-term
sparse polynomial image, either immediately or at the second recurrence.  If
so, prove a coefficient-uniform explicit bound on `T_2` for arbitrary
characteristic-zero fields and arbitrary finite-rank groups.

Potential value: a support-size phase transition independent of the detailed
support-one automaton.  Main risk: a zero subsum could leave a monomial curve or
free vertical chain not closed by the second step.

### Candidate C: sharp-window examples without a new finiteness theorem

Construct infinite shorter-window families for several supports and classify
parameter compatibilities.  This was retained only as a fallback because
counterexamples alone would not carry enough standalone value.

## Required closure tests

Candidate B could advance only if all of the following were proved without
computation:

1. The sparse-image equation uses a rank-`2r` tuple group and has a fully
   explicit degenerate-subsum contribution.
2. The first local Hénon equation uses rank `3r`, without adjoining coefficients
   to the variable group.
3. A fixed `Z/U/M_j` convention gives an exhaustive four-type degeneracy split.
4. Both graph endpoints, `J=[s]` and `|J|=1`, retain a polynomial with at least
   two terms.
5. Both root types have finite `v` budgets and their vertical fibers close at
   the second recurrence even if its constant term cancels.
6. Simultaneous zero subsums are covered without assuming the strata are
   disjoint.
7. Infinite torsion is compatible with every fiber estimate.
8. Explicit examples show that `T_1` may be infinite for every prescribed
   support, and that `c=0` or `a=0` really breaks the proposed theorem.

## Initial literature boundary

The search plan required primary-source comparison with:

- Amoroso--Viada and Evertse--Schlickewei--Schmidt for quantitative unit
  equations;
- Krieger--Levin--Scherr--Tucker--Yasufuku--Zieve for one-variable `S`-unit
  image and orbit uniformity;
- Bell--Ghioca for fixed-orbit subgroup intersections;
- Ji--Xie--Zhang for cyclotomic Hénon rigidity;
- Mello--Yasufuku for higher-dimensional semigroup integrality and
  multiplicative dependence;
- current arithmetic constructions of rational Hénon periodic points.

The Krieger et al. comparison had to be checked at theorem level: published
Theorem 1.7 concerns monic `S`-integral polynomial images, whereas Theorem 1.8
is the local exceptional-coefficient valuation statement and Corollary 1.9 is
its number-field orbit consequence.  None is a two-dimensional all-initial-
state finite-rank theorem.

## Initial decision rule

Advance Candidate B only if the four-type proof closes rigorously and a bounded
current search finds no direct collision.  Use Candidate A only as an absorbed
comparison theorem.  Stop rather than claim a vague theorem for arbitrary
sparse maps if a monomial-curve or free-chain gap remains.
