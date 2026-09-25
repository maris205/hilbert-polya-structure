# Frozen full face-cotangent conservative lift

**Paper ID:** 196-face-cotangent-conservative-lift  
**Candidate ID:** ASC-20260916-FCL01  
**Version:** 1, frozen on research date 2026-09-16 before proof.  
**Initial status:** FROZEN — FULL COPRODUCT GEOMETRY, PROJECTION AND PACKET AUDIT OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

This is the separately defined geometry lane of the
[198 scope](../198-cone-extension-frontier/candidate-card.md), extending
the full first-return data of
[193 / AQC-20260916-IRC01](../193-indecomposable-radial-quotient/candidate-card.md).
It does not modify 193, attach another owner's operator to it, or assert
that its original topology already has a symplectic realization. The
bounded question is whether the following entire conservative coproduct
has a complete suspension and preserves the full projected packet/clock
ledger. All construction, continuity and periodic-point assertions below
are obligations, not results of this freeze.

## Source, lineage and allowed input

Use the real monoid algebra on all integers n>=1, with e_m e_n=e_(mn),
the ideal I spanned by e_n for n>=2, and the declared quotient Q=I/I^2
from 193. Let A denote its surviving basis atoms, with their inherited
integer multiplier a from D(e_n)=n e_n. Their identification with primes
is the proved factor-admissibility result in 193, not a prime list in
this definition. Use its whole finite-support unit positive section

    S = { u=sum_a u_a q_a : u_a>=0, finite support, sum_a u_a=1 },
    c(u) = sum_a u_a/a,
    F(u) = D^(-1)u/c(u),
    tau(u) = -log c(u).

S retains 193's topology from all weighted norms
||v||_k=sum_a a^k |v_a|, k>=0. Its return and roof are the actual
section data of the radial quotient flow, not newly selected parameters.

Lineage: prime/composite factor admissibility -> indecomposable symbolic
observable -> the full positive radial source and actual return -> a
declared facewise cotangent conservative lift. This realizes a precise
source-preserving dimensional/geometric extension in the direction of
the [prior-work guide](../../docs/prior_work/README.md), not a claim of
Logistic/Henon conjugacy, automatic physical naturalness or computational
trial division. No prime table, per-prime parameter fit, zero data,
von Mangoldt weight, trace formula or manually assigned prime period is
permitted. The indecomposable quotient, positivity, integer-size scale
and universal radial speed retain their disclosed design status.

## Entire new carrier and exact map

For every nonempty finite set J of atoms, freeze

    Delta_J^o = { (u_a)_(a in J) : u_a>0, sum_(a in J) u_a=1 },
    M_J = T*Delta_J^o times R^2,
    M = coproduct_(J finite, nonempty) M_J.

The coproduct has the disjoint topological coproduct topology and the
ordinary smooth structure on each component. It is explicitly NOT the
original subspace topology of S across face boundaries. Components have
dimension 2|J|, which is not fixed globally. All covectors and every
real Q,P coordinate are retained, including all mixed-support states.
The label ASC means arithmetic symplectic coproduct; it does not claim
a fixed-dimensional classical ASFS manifold or supplied lamination.

On T*Delta_J^o let theta_J be the tautological one-form and use

    omega_J = -d theta_J + dQ wedge dP.

Put f_J=F restricted to Delta_J^o. Its full cotangent lift is

    C_(f_J)(u,xi) = (f_J(u), xi composed with (D f_J(u))^(-1)),
    B(Q,P) = (2Q,P/2),
    G|_(M_J) = C_(f_J) times B.

The inverse, global domain, regularity and preservation of omega_J must
be proved, not inferred merely from the words “cotangent lift.” The
same B is used for every J; it is not chosen for individual atoms.
The singleton cotangent factor has dimension zero, but the entire R^2
factor remains part of its base. No center, zero section or bounded
momentum subset may be substituted for M.

The forgetful map is h(u,xi,Q,P)=u in the original S. Prove its global
continuity, surjectivity and exact intertwining with F. A continuous
projection is not a topological identification; any stronger property
requires proof rather than inheritance from 193.

## Unchanged projected roof and full suspension

Freeze rho=tau composed with h. Use the full endpoint construction

    Y = { (z,t) : z in M, 0<=t<=rho(z) }
        / ((z,rho(z)) equivalent to (Gz,0)).

The proposed flow psi^r is actual translation in the t coordinate,
with all crossings performed using G and rho. Its existence, joint
continuity, smooth componentwise owner and completeness must be checked
on the entire carrier, including negative time and unbounded covectors.
No unit roof, radial-speed change or rescaling is allowed. Establish a
continuous, surjective, time-preserving map to 193's full flow, using
h and the same elapsed time. It must not be called a symplectic
conjugacy of the old owner.

The base has its componentwise Liouville measure and the coproduct sum
normalization, with no probability or finite-total-volume assertion.
No invariant suspension measure or analytic operator is required by
this contract. The odd-dimensional suspended components are not called
symplectic or Hamiltonian. Hamiltonian, contact, Hilbert and quantum
owners are NOT SUPPLIED; trace/zeta/determinant are NOT INVOKED.

## Full packets, monodromy and first discriminators

Packets mean all nonconstant primitive oriented closed trajectories of
Y modulo actual time translation, retaining intrinsic multiplicity.
For every positive integer r test G^r z=z on every component and every
covector. Then derive the least return, actual sum of rho along it,
all repetitions, and the transverse first-return derivative at every
closed orbit. No closed curve in a projection alone counts as a lifted
orbit, and no fixed center is credited until all other states have been
excluded by the same complete return equation.

The first discriminators are: continuity under the declared coproduct
topology; all mixed supports rather than axes; singleton transverse
states; full cotangent iterates; non-Zeno behavior in both directions;
and whether the projected roof really gives the same elapsed time.
Stop at a decisive failure of those exact requirements. Do not change
topology, add/delete momenta, alter B or repair the roof under this ID.

Controls to report are the old face-boundary topology, omission versus
identity of the uniform plane, every mixed support, changed roof,
absence of the indecomposable quotient, and distinct generic generator
multipliers. Changed-object controls never replace this frozen owner.
The generic-alphabet control must keep PROVES_TOO_MUCH and source-clock
naturalness visible; a successful geometric extension alone is not
a natural-A0 or formal Route pass.

## Freeze provenance and bounded handoff

The author read the stream guidance and plan, current entry and registry
guidance, the complete six Markdown files of 193, 198's scope card,
the paper template, roadmap boundary, and prior-work guide. A targeted
pre-freeze check found this directory absent and the proposed ID only
in 198's reservation, with no already frozen same-ID card. This is a
local collision check, not a global novelty claim.

Only this new package is writable by its author, excluding its review
file. Use Markdown and apply_patch. One actual different-invocation
mathematical review is coordinated by the controller, with shared
context and nonblind feedback disclosed. No further review tree,
script, Git mutation, old-package edit, navigation edit, external-model
upload, PDF or publication operation belongs to this bounded contract.
ARS is limited to claim/evidence/reasoning and counterargument discipline.
Unknown or future analytic/geometric obligations remain OPEN or NOT
SUPPLIED; no formal Route coordinate is evaluated and B is not invoked.

## Appended audit outcome, unchanged version 1

**Status:** ADVANCE — COMPLETE SYMPLECTIC COPRODUCT WITH FULL LOG-PRIME PACKETS; NEW TOPOLOGY; NATURALNESS OPEN.

The [paper](paper.md) proves the entire cotangent lift in global
log-ratio coordinates, the full Hausdorff endpoint suspension and
completeness, and the exact continuous surjective time-preserving
projection to 193. The map h is explicitly not a quotient map: its
singleton component is open but the corresponding old vertex is not.
The induced full-flow projection is likewise not a quotient map or
conjugacy. Components retain their different dimensions 2|J|.

All mixed-support states and all noncentral singleton transverse states
are aperiodic. The whole periodic set contains exactly one base fixed
point per derived atom, hence one primitive suspended circle per prime,
with actual time log p, repetitions r log p and monodromy
diag(2^r,2^(-r)). No momentum, center or mixed state was deleted;
the frozen card and roof are unchanged. This is a scoped conservative
extension, not an assertion of original-topology symplectification,
natural A0, fixed-dimensional ASFS, Hamiltonian/contact realization or
analytic ownership. Formal Route remains UNASSIGNED; B is NOT INVOKED.
