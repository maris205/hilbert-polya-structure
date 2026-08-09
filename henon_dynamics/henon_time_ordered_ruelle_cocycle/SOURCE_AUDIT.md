# Source and novelty audit

**Audit date:** 2026-08-09
**Status:** scoped T1--T3 theorem delta audited; T4--T5 operator novelty open

## Paper-5 source lock

The foundational source is the repository copy
[`5-An Area-Preserving Henon-Map Model.pdf`](../docs/prior_work/papers/5-An%20Area-Preserving%20Henon-Map%20Model.pdf).
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
[`CANDIDATE_REGISTRY.md`](../next_paper_henon_candidate_search/CANDIDATE_REGISTRY.md)
already defines the
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

No audited repository project or cited external source was found to prove
the achieved T1--T3 conjunction for this explicit rational two-letter
Paper-5-coordinate family: a common switched-family local survivor, a joint
rather than separately canonicalized primitive-orbit ledger, complete
state-sector instability separation for the matched protocol pairs, and the
complementary all-complex signed-residue collapse.  The nuclear
ordered-operator extension remains open and is not part of the present
novelty claim.

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

## Post-T1--T3 scoped novelty verdict

Within the audited repository and cited primary literature, the defensible
project-specific theorem delta is the conjunction of:

1. an explicit common local four-state survivor, uniform over all binary
   schedules in the frozen rational two-letter window;
2. an exact joint parameter--state primitive-orbit and reversal ledger;
3. exact-rational complete-state separations of \(Q_w(1)\) for the minimal
   tested non-dihedral same-bigram and same-trigram protocol classes; and
4. the complementary unit-numerator all-complex signed-residue collapse
   under the stated scheme convention.

The novelty status is `SCOPED_PASS` for this achieved T1--T3 conjunction and
remains `OPEN` for T4--T5.  This is a scoped "not found in the audited
sources" statement, not a universal priority claim.

The project does not claim novelty for introducing a nonautonomous Hénon
map, noncommutativity, periodic monodromy, a block determinant, a random or
ordered transfer cocycle, or a selected-branch numerical separation.  It
also does not yet claim a convergent instability determinant, a nuclear
Ruelle operator, an infinite-memory potential, an arithmetic correspondence,
or a Hilbert--Pólya realization.
