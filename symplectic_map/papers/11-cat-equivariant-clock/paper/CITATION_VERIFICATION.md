# Publication-Layer Citation Verification

## Scope, cutoff, and immutable-source boundary

Verification cutoff: **2026-08-15 UTC**.

This publication-layer record verifies the identities, venues, and exact
allowed uses of the references in `paper/references.bib`. It binds but does
not modify the frozen design-side citation record
`notes/CITATION_VERIFICATION.md` (SHA-256
`1bfc33598d9ff5e5a8636a9ba5f8365ef9c3176614ba90a2b64ae1eb6dc4154b`),
source lock v2 (SHA-256
`331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b`),
or any result artifact. The search is bounded and supplies neither an
absence result nor a historical-priority claim.

The publication layer also binds the independent postrun theorem-quantifier
audit (SHA-256
`f7b365c9e6c8933cf3cbcaf3c96692cbacdaabcc84400bdc629f1d482cb243e4`,
`PASS_WITH_SCOPE_CORRECTION`). Citation text must not be used to revive the
rejected per-row scalar nonattainment statement. The only authorized
statement is family-uniform nonattainment, with the exact $q=2$ exception
shown explicitly.

Primary/official publisher or arXiv records were preferred. Journal metadata
were cross-checked by DOI where available. Each entry below states the
allowed scientific use and a boundary that the manuscript must preserve.

## Bibliographic correction frozen at publication layer

The frozen design-side sidecar and the corresponding source-lock record list
Laura Walton's 2018 paper as *Journal of Number Theory* **189**, 202--223.
That is a historical bibliographic typo. The DOI-authoritative Elsevier
record for `10.1016/j.jnt.2018.03.023` is:

> Laura Walton, “Counting periodic points on quotient varieties over
> $\mathbb F_q$,” *Journal of Number Theory* **192** (2018), 386--405.

The publication bibliography uses **192**, 386--405. This correction changes
no title, author, DOI, theorem, source formula, registered result, novelty
score, or scope conclusion. The design-side file remains immutable so that
the terminal source/result hash chain is preserved. Manuscript metadata,
claim manifests, and final references must use only the corrected
publication record.

## Direct construction records

### `GuseinZadeLuengoMelle2008`

- S. M. Gusein-Zade, I. Luengo, and A. Melle-Hern\'andez, “An equivariant
  version of the monodromy zeta function.”
- In *Geometry, Topology, and Mathematical Physics*, AMS Translations,
  Series 2, volume 224, pp. 139--146, American Mathematical Society (2008).
- arXiv: `0803.3708`; verified record:
  <https://arxiv.org/abs/0803.3708>.
- Verified content: a rational power series with coefficients in the
  Grothendieck/Burnside ring of finite $G$-sets, using equivariant Lefschetz
  numbers and the Burnside $\lambda$/power structure.
- Allowed use: direct predecessor of the fixed-point/point-order rational
  Burnside series.
- Boundary: arbitrary marks or the additive orbifold map are not asserted to
  preserve Burnside multiplication or symmetric powers. Paper 11 does not
  originate this construction.

### `GuseinZade2013`

- S. M. Gusein-Zade, “On an equivariant analogue of the monodromy zeta
  function.”
- *Functional Analysis and Its Applications* **47**(1), 14--20 (2013).
- arXiv: `1207.2282`; verified record:
  <https://arxiv.org/abs/1207.2282>.
- Verified content: the invariant is a virtual finite or locally finite
  $G$-permutation, equivalently a $(\mathbb Z\times G)$-set, and its
  irreducible data are parametrized by a triple $(H,m,\alpha)$.
- Allowed use: the complete twisted Lefschetz table and regular-torsor triple
  $(1,1,a_q^{-1})$ under the frozen left-action convention.
- Boundary: exact twist recovery requires a fixed labelled effective action;
  it is not supplied by the untwisted point-order series.

### `GuseinZadeLuengoMelle2015`

- S. M. Gusein-Zade, I. Luengo, and A. Melle-Hern\'andez, “On an equivariant
  version of the zeta function of a transformation.”
- *Arnold Mathematical Journal* **1**(2), 127--140 (2015).
- DOI: `10.1007/s40598-015-0012-8`; arXiv: `1203.3344`.
- Verified records:
  <https://doi.org/10.1007/s40598-015-0012-8> and
  <https://arxiv.org/abs/1203.3344>.
- Verified content: distinct equivariant Lefschetz sequences counting fixed
  points and fixed $G$-orbits; rational versus integral exact-period
  constructions; additive orbifold reductions; and a period-one quotient
  when the transformation lies in the symmetry group.
- Allowed use: the point/orbit definition separation, exponentwise additive
  orbifold maps, and the static orbit-order specialization.
- Boundary: the two zetas are not one invariant, and Paper 11 creates neither
  definition.

### `EbelingGuseinZade2018`

- Wolfgang Ebeling and Sabir M. Gusein-Zade, “Enhanced equivariant Saito
  duality.”
- *Journal of Algebra and Its Applications* **17**(10), 1850181 (2018).
- DOI: `10.1142/S0219498818501815`; arXiv: `1506.05604`.
- Verified records:
  <https://doi.org/10.1142/S0219498818501815> and
  <https://arxiv.org/abs/1506.05604>.
- Verified content: the enhanced Burnside ring of finite $G$-sets carrying a
  $G$-equivariant transformation and isotropy characters, together with an
  enhanced orbifold fixed-sector reduction.
- Allowed use: the regular-torsor tuple $(1,1,a_q,1)$ and the distinction
  between carrier retention and the one-fixed-point enhanced orbifold image.
- Boundary: no new enhanced class, Saito duality, or orbifold zeta is claimed.

## Quotient and acting-group boundaries

### `Zegowitz2017`

- Stefanie Zegowitz, “Closed orbits in quotient systems.”
- *Ergodic Theory and Dynamical Systems* **37**(7), 2337--2352 (2017).
- DOI: `10.1017/etds.2016.3`; arXiv: `1502.02693`.
- Verified records:
  <https://doi.org/10.1017/etds.2016.3> and
  <https://arxiv.org/abs/1502.02693>.
- Allowed use: established survival, shortening, and gluing terminology and
  formulas for finite-group quotients.
- Boundary: Paper 11's shortening factor $1/r_q$ and gluing number $m_q$ are
  regular-action specializations, not a new quotient-orbit theorem.

### `Miles2017`

- Richard Miles, “A dynamical zeta function for group actions.”
- *Monatshefte f\"ur Mathematik* **182**(3), 683--708 (2017).
- DOI: `10.1007/s00605-016-0909-x`; arXiv: `1506.08555`.
- Verified records:
  <https://doi.org/10.1007/s00605-016-0909-x> and
  <https://arxiv.org/abs/1506.08555>.
- Allowed use: adjacent stabilizer-sensitive acting-group-zeta context.
- Boundary: the paper's setup tacitly assumes an infinite acting group; it is
  not an off-the-shelf finite-$G_q$ construction and is not implemented here.

### `Walton2018`

- Laura Walton, “Counting periodic points on quotient varieties over
  $\mathbb F_q$.”
- *Journal of Number Theory* **192**, 386--405 (2018).
- DOI: `10.1016/j.jnt.2018.03.023`; arXiv: `1705.09034` (preprint title:
  “Counting periodic points over finite fields”).
- Verified records:
  <https://doi.org/10.1016/j.jnt.2018.03.023> and
  <https://arxiv.org/abs/1705.09034>.
- Allowed use: the finite-field quotient/twist boundary and the relation
  between quotient periodic points and periodic points on twists.
- Boundary: the hypotheses concern quasiprojective varieties over finite
  fields, not arbitrary finite sets over composite residue rings. Paper 11
  neither extends nor implements Walton's theorem.

### `BaakeNeumaerkerRoberts2013`

- Michael Baake, Natascha Neum\"arker, and John A. G. Roberts, “Orbit
  structure and (reversing) symmetries of toral endomorphisms on rational
  lattices.”
- *Discrete and Continuous Dynamical Systems* **33**(2), 527--553 (2013).
- DOI: `10.3934/dcds.2013.33.527`; arXiv: `1205.1003`.
- Allowed use: inherited Paper-10 rational-lattice centralizer and orbit
  context only.
- Boundary: it is not evidence that the Paper-11 definition comparison is a
  new centralizer theorem.

## Current frontier boundary records

These records prevent the related-work section from presenting only older
Burnside literature. They are context, not originality evidence and not
implementation authority.

### `HochsSaratchandran2023`

- Peter Hochs and Hemanth Saratchandran, “A Ruelle dynamical zeta function
  for equivariant flows,” arXiv `2303.00312` (2023).
- Verified record: <https://arxiv.org/abs/2303.00312>.
- Boundary: proper smooth group actions, equivariant flows, and an analytic
  Ruelle/Fried setting rather than a finite internal permutation.

### `Rahmati2024`

- Mohammad Reza Rahmati, “Mirror Symmetry, Zeta Functions and Mackey
  Functors,” *Contemporary Mathematics* **5**(2), 1820--1842 (2024).
- DOI: `10.37256/cm.5220244455`.
- Official record:
  <https://ojs.wiserpub.com/index.php/CM/article/view/4455>.
- Boundary: orbifold cohomological zeta/L-series and Mackey-functor context,
  not the finite centralizer-torsor constructions audited here.

### `AyalaMazelGeeRozenblyum2025`

- David Ayala, Aaron Mazel-Gee, and Nick Rozenblyum, “Symmetries of the cyclic
  nerve,” *Advances in Mathematics* **466**, 110170 (2025).
- DOI: `10.1016/j.aim.2025.110170`; arXiv: `2405.03897`.
- Verified records:
  <https://doi.org/10.1016/j.aim.2025.110170> and
  <https://arxiv.org/abs/2405.03897>.
- Boundary: cyclic/paracyclic/epicyclic and Hochschild-homology context, not a
  finite Burnside zeta or a modulus clock.

### `HochsSaratchandran2025`

- Peter Hochs and Hemanth Saratchandran, “An equivariant Guillemin trace
  formula,” arXiv `2502.08367` (2025).
- Verified record: <https://arxiv.org/abs/2502.08367>.
- Boundary: proper cocompact analytic trace-formula context; no Paper-11
  trace, transfer, or Fredholm claim.

### `HochsPirie2025`

- Peter Hochs and Christopher Pirie, “The Equivariant Fried Conjecture for
  Suspension Flow of an Equivariant Isometry,” arXiv `2507.06792` (2025).
- Verified record: <https://arxiv.org/abs/2507.06792>.
- Boundary: equivariant Ruelle zeta and analytic torsion; no finite-torsor
  Burnside formula.

### `GuseinZade2026`

- Sabir M. Gusein-Zade, “Monodromy Zeta Functions in Singularity Theory.”
- In *Handbook of Geometry and Topology of Singularities VIII*, pp. 289--316,
  Springer, Cham (2026).
- DOI: `10.1007/978-3-031-99571-2_7`.
- Allowed use: current survey evidence that the monodromy-zeta landscape is
  mature.
- Boundary: not originality evidence and not authority for the Paper-10
  arithmetic theorem.

## Citation-use and quantifier locks

1. Every occurrence of “equivariant zeta” must name the precise 2008, 2013,
   2015, or 2018 construction.
2. The 2008 point-order, 2015 orbit-order, and 2013 labelled
   $(\mathbb Z\times G)$ constructions remain mathematically distinct.
3. Exact labelled twist recovery belongs to the stronger carrier and is
   exact only after effectivity; in general it recovers $a$ modulo the action
   kernel.
4. Orbifold and inertia multiplicities are static stabilizer data, not
   return times.
5. The point-cardinality reduction has source support and unit exponent when
   $m_q=1$. In the locked ledger, $q=2$ is the unique such row/type pair.
6. K011 certifies only that no scalar-reduction type has both properties
   uniformly across all nine locked rows. It does not certify per-row
   nonattainment.
7. The $q=2$ factor $(1-t^3)^{-1}$ is not a modulus identifier because
   $r_2=r_4=3$; no intrinsic prime selector or common clock follows.
8. Miles, Walton, and current analytic sources mark adjacent boundaries only.
9. No source supports a new zeta, a universal no-go theorem, a canonical
   cross-$q$ coefficient ring, a numerical analytic continuation, or Route B.

## Bibliography closure

`paper/references.bib` contains exactly the fourteen keys reviewed above.
No entry is generated from an unverified memory-only record. The publication
layer intentionally corrects only the Walton volume/page typo; all other
bibliographic identities agree with the frozen source sidecar and the cited
primary records.
