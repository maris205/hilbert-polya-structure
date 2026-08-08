# Source and novelty audit

**Audit date:** 2026-08-08
**Status:** Stage-1 source lock; theorem-level novelty remains provisional

## Paper-5 source lock

The foundational source is the repository copy
`docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf`.
The present project preserves its physical coordinate convention

\[
H_a(q,p)=(1-aq^2-p,q),
\qquad
q_{i+1}=1-a_iq_i^2-q_{i-1}.
\]

Paper 5 motivates a time-dependent area-preserving Hénon model and studies
fitted/static schedules near a different parameter range.  HCS-C22 does not
inherit those fitted schedules, does not treat their numerical agreement as
a theorem, and does not claim that the parameters \(59/10,61/10\) come from
Paper 5.

The additive convention used in parts of HCS-C19--C21,

\[
H_A(x,y)=(A-x^2-y,x),
\]

is conjugate to the Paper-5 convention at one fixed nonzero parameter after a
parameter-dependent scaling.  There is no single fixed scaling that
conjugates a switched two-parameter family.  Therefore C22 never mixes the
two conventions.

## Repository overlap audit

### Direct parent

HCS-C01 in
`next_paper_henon_candidate_search/CANDIDATE_REGISTRY.md` already defines the
two-letter chronological skew product at \(5.9\) and \(6.1\).  HCS-C22 is a
promotion of that registered idea to its first common-hyperbolicity,
chronology-classification, and operator theorem gates.  Novelty may not be
claimed for merely writing down the skew product.

### Nearby but distinct projects

- `next_paper_henon_ruelle_operator` concerns a fixed single \(H_6\)
  pressure/dimension program.  C22 varies the fibre map in chronological
  order and counts joint base--fibre cycles.
- HCS-C19--C21 study algebraic periodic covers in the additive map convention.
  They supply symmetry and clock warnings, not a common switched-family
  theorem.
- HCS-C02B/C02D supply complex-pinning infrastructure and a finite-memory
  trace obstruction.  Their failure forbids treating an arbitrary memory
  truncation as an exact operator for C22.
- Existing obstruction records HEN-O01, HEN-O03, HEN-O06, HEN-O15, HEN-O16,
  HEN-O25, HEN-O29, and HEN-O44 are mandatory controls: source drift,
  determinant misidentification, clock loss, branch incompleteness,
  conjugacy/parameter mixing, branch-to-aggregate overclaim, finite-memory
  substitution, and chronology erasure are all live risks.

No repository project was found that proves the complete C22 chain:
common switched-family survivor, joint chronology quotient, certified
non-dihedral intrinsic-weight witness, and common nuclear ordered operator.

## External prior art

### Nonautonomous Hénon dynamics

Balibrea-Iniesta, Lopesino, Wiggins, and Mancho, *Chaotic Dynamics in
Nonautonomous Maps: Application to the Nonautonomous Hénon Map*, develops
nonautonomous hyperbolicity tools and applies them directly to an
area-preserving nonautonomous Hénon family.  Its coordinate form and example
schedule differ from C22, but it closes any broad novelty claim that
nonautonomous Hénon maps can have chaotic invariant structure.

- arXiv: <https://arxiv.org/abs/1705.10216>
- DOI: <https://doi.org/10.1142/S0218127415501722>

### Periodic nonautonomous zeta functions

Alves and Málek study zeta functions for periodic nonautonomous systems in a
one-dimensional piecewise-monotone setting.  Thus periodic protocol zetas
and Floquet reductions are not novel categories.  C22 must earn novelty from
its explicit two-dimensional common survivor, exact chronology quotient,
intrinsic weights, or operator theorem.

- DOI: <https://doi.org/10.3934/dcds.2013.33.465>

### Random zeta and transfer cocycles

Buzzi shows that random zeta functions can behave very differently from
deterministic meromorphic zetas and that trace data need not recover random
transfer-operator Lyapunov exponents.  This is a primary reason not to market
C22 as a general quenched-random-zeta program.

- DOI: <https://doi.org/10.1017/S0143385702000524>

Bogenschütz and Gundlach develop Ruelle operators for random subshifts of
finite type.  Froyland, Lloyd, and Quas develop Oseledets theory for transfer
operator cocycles, and Dragičević and collaborators treat ordered random
hyperbolic cocycles.  These sources define the operator-theoretic prior-art
boundary: an operator cocycle by itself is not a new Hilbert--Pólya
mechanism.

- Bogenschütz--Gundlach DOI:
  <https://doi.org/10.1017/S0143385700008464>
- Froyland--Lloyd--Quas arXiv: <https://arxiv.org/abs/1001.5313>
- Dragičević et al. arXiv: <https://arxiv.org/abs/1812.07340>

### Determinant rigor

Infinite-dimensional determinant claims must meet trace-ideal hypotheses;
finite matrices do not supply those hypotheses.  Simon's trace-ideal
determinant framework is a baseline reference.

- DOI: <https://doi.org/10.1016/S0001-8708(77)80044-3>

## Provisional novelty claim

The only defensible Stage-1 novelty claim is a question:

> Can the explicit Paper-5-coordinate family at the rational window
> \([59/10,61/10]\) support a single certified local symbolic/holomorphic
> model in which the intrinsic instability determinant distinguishes
> protocols beyond dihedral and finite-memory controls?

The following are explicitly **not** novelty claims:

- discovery of a nonautonomous Hénon map;
- noncommutativity of two Hénon maps;
- existence of a periodic-word monodromy;
- a finite block determinant identity;
- a random/ordered transfer operator cocycle;
- numerical separation of two selected branches.

The novelty status changes to `PASS` only after T1--T3 produce a theorem
delta not already implied by the cited frameworks.
