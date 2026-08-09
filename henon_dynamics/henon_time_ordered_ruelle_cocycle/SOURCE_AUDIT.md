# Source and novelty audit

**Audit date:** 2026-08-09
**Status:** T1--T4 and orbitwise scalar-T5 theorem delta audited; graded operator
novelty open

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
novelty claim.  The fixed-\(H_6\) pinning project already proves the exact
one-step BPS kernel semantics and a different constant-sign repetition
obstruction.  C22's new scalar obstruction concerns nonmultiplicativity of
the full fixed-point denominator; it is not a rediscovery of that sign
result.

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
and period-composition reductions are not novel categories.  C22 must earn novelty from
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
determinant framework is a baseline for Hilbert-space operator ideals.  It is
not by itself sufficient for the mixed holomorphic Banach spaces proposed
here; those require the relevant Grothendieck nuclear order, approximation
property, canonical trace, and determinant theorem to be stated separately.

- DOI: <https://doi.org/10.1016/S0001-8708(77)80044-3>
- Grothendieck, *La théorie de Fredholm*:
  <https://doi.org/10.24033/bsmf.1476>

### Analytic pinning, generalized determinants, and exterior cancellation

Rugh's analytic-hyperbolic work supplies the classical pinning-coordinate
and nuclear-operator framework for flat/generalized dynamical determinants.
His later Axiom-A paper supplies generalized Fredholm determinants.  Therefore
neither analytic pinning nor an abstract flat/generalized determinant is a
new C22 mechanism.  These results do not by themselves realize the frozen
pure weight \(|\Lambda_u|^{-s}\).

- Rugh, *The correlation spectrum for hyperbolic analytic maps*:
  <https://doi.org/10.1088/0951-7715/5/6/003>
- Rugh, *Generalized Fredholm determinants and Selberg zeta functions for
  Axiom A dynamical systems*:
  <https://doi.org/10.1017/S0143385700009111>

Baladi, Pujals, and Sambarino specialize Rugh-type methods to analytic
surface diffeomorphisms with dominated splitting and obtain entire or
slit-plane determinant statements under their hypotheses.  This creates a
strict novelty ceiling: merely inserting a Hénon horseshoe into a general
analytic-hyperbolic theorem is not a new operator construction.

- Primary preprint: <https://arxiv.org/abs/math/0307045>
- Journal DOI: <https://doi.org/10.1017/S1474748005000046>

Ruelle's differentiable Fredholm theory allows vector bundles and exterior
powers.  The identity

\[
\det(I-M)=\sum_k(-1)^k\operatorname{tr}(\wedge^kM)
\]

is the standard signed/oriented Lefschetz cancellation under the relevant
branch, differentiability, and bundle hypotheses.  It does not alone prove
analytic nuclearity or entireness for C22.
Consequently the C22 graded pivot may claim only its explicit common
two-letter domains, chronology-preserving specialization, and effective
constants--not exterior cancellation itself.

- Ruelle, *An extension of the theory of Fredholm determinants*:
  <https://www.numdam.org/item/PMIHES_1990__72__175_0/>

Baladi and Tsujii relate dynamical determinants to spectra on anisotropic
distribution spaces in a proved disc.  Their quasi-compact framework must
not be restated as a holomorphic nuclear-space theorem.

- Primary preprint: <https://arxiv.org/abs/math/0606434>

Faure and Tsujii use a Grassmann-bundle extension to handle an unstable
bundle and apply an Atiyah--Bott trace formula in a symplectic Anosov
semiclassical setting.  This confirms that the projective/Grassmann lift is
standard technology, but it does not automatically verify C22's local
analytic branch domains or nuclear pinning kernels.

- Primary preprint: <https://arxiv.org/abs/1206.0282>

## T4--T5 theorem and novelty boundary

T4 is now proved, but its abstract mechanism is standard thermodynamic
formalism: a positive Hölder periodic weight with exponential orbit growth
has an Euler product in its pressure half-domain.  The project-specific
content is the exact switched-Hénon input and explicit constants

\[
E^2=129299641/14112000,
\qquad
U^2=11420060341/189778176,
\]

not a new general convergence theorem.

The two-letter common base-pinning domain and common projective logarithm
domain are explicit certificate deltas relative to the fixed-\(H_6\)
repository work.  They give:

- minimum base-pinning coordinate clearance \(7/5490\);
- common slope disk \(|m|\le1/2\) mapped into
  \(|m|\le125440/466211\);
- projective contraction at most \(11289600/129299641\);
- common right-half-plane logarithm clearance \(11371/3360\);
- one lifted unstable periodic point per base orbit.

The orbitwise scalar denominator-cancellation gate is rigorously closed because

\[
|\det(I-M^2)|\ne|\det(I-M)|^2
\]

for every area-preserving hyperbolic \(2\times2\) return.  This is a scoped
no-go for multiplicative scalar pinning weights required to match each
periodic-point summand (or independent formal orbit marker).  It does not
exclude compensation among distinct same-period orbits in an unmarked
aggregate trace, a graded exterior complex, a non-scalar bundle operator, or
an unrelated nonlocal representation.

Within the frozen C22 lineage and audited sources, the only open operator
novelty question is therefore whether these explicit two-letter domains
support one chronology-preserving, quantitatively nuclear graded family with
the exact supertrace.  General pinning, Grassmann lifting, exterior
cancellation, and alternating Fredholm products remain prior art.

## Do-not-repeat ledger after T4--T5

The repository and primary-source audit forbids the following as future
progress claims:

1. refining unrestricted or restricted Ulam grids;
2. replacing ordered letter products by an averaged matrix or kernel;
3. calling a C02C \(N\)-window a same-clock operator approximation;
4. separately rotating parameter and state words;
5. calling an Euler-log recursion an operator trace theorem;
6. inferring nuclearity from Hölder quasi-compactness or compactness;
7. using \(|\det(I-M)|^r\) in place of
   \(|\det(I-M^r)|\);
8. using \(|\lambda|^{-s}\) in a complex kernel without a certified sector
   and logarithm branch;
9. allowing both stable and unstable projective fixed points in the lifted
   trace;
10. calling an alternating quotient of entire determinants one entire
    scalar determinant without a cancellation theorem;
11. treating finite-section root stability as continuation or as
    Hilbert--Pólya evidence.

## Post-T4/orbitwise-scalar-T5 scoped novelty verdict

Within the audited repository and cited primary literature, the defensible
project-specific theorem delta is the conjunction of:

1. an explicit common local four-state survivor, uniform over all binary
   schedules in the frozen rational two-letter window;
2. an exact joint parameter--state primitive-orbit and reversal ledger;
3. exact-rational complete-state separations of \(Q_w(1)\) for the minimal
   tested non-dihedral same-bigram and same-trigram protocol classes; and
4. the complementary unit-numerator all-complex signed-residue collapse
   under the stated scheme convention;
5. explicit all-period instability multiplier and Euler-product convergence
   bounds for the switched survivor;
6. common two-letter base-pinning and projective-logarithm domains with
   exact rational clearances; and
7. the primitive/double-repetition obstruction to orbitwise scalar
   denominator cancellation for the pure instability weight.

The novelty status remains `SCOPED_PASS` for the explicit C22 conjunction:
T1--T3, the effective two-letter T4 constants, the common base/projective
complex certificates, and the scalar-denominator obstruction.  The abstract
T4, pinning, projective, exterior, and generalized-determinant mechanisms are
all prior art.  Novelty remains `OPEN` only for a quantitatively certified
chronology-preserving graded nuclear realization.  This is a scoped "not
found in the audited sources" statement, not a universal priority claim.

The project does not claim novelty for introducing a nonautonomous Hénon
map, noncommutativity, periodic monodromy, a block determinant, a random or
ordered transfer cocycle, or a selected-branch numerical separation.  It
now claims a convergent instability determinant in the proved local domain
and a two-sided Hölder roof, but still does not claim a nuclear Ruelle
complex, continuation past the pressure boundary, a proved finite-memory
classification, an arithmetic correspondence, or a Hilbert--Pólya
realization.
