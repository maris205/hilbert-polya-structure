# Initial Proposal

## Starting point

The Batch05 search began after Paper16 had terminally closed the planar
nonzero-constant finite-rank problem:

- actual support at least two: explicit finite `T_2`, sharp infinite `T_1`;
- actual support one: absorbed explicit finite `T_4`, sharp infinite `T_3`.

The initial constraint was therefore strict: do not repackage Paper16, and do
not create a new project unless a theorem changed a material mathematical axis.
The exploratory lane was zero-write, with no CAS, code, data, compilation, or
project directory.

## Initial research question

Could torus survival for sparse generalized Hénon recurrences exhibit a new,
exact phase after one changes dimension, shift type, constant term, support
class, or arithmetic group scope?

The search stressed:

- `c=0` versus `c!=0`;
- polynomial versus Laurent/rational support;
- higher dimension and arbitrary type `nu`;
- mixed multiplicative cosets;
- exact exceptional coefficient loci; and
- qualitative versus effective window phase diagrams.

## Candidate pool and first dispositions

### Candidate A: all-dimensional terminal finiteness

For a type-`nu` shift-like map with `c!=0` and at least two nonconstant
monomials, try to prove that `T_k` is finite for every finite-rank group.

Initial attraction: moves from planar Hénon to arbitrary dimension.

Initial weakness: terminal finiteness alone looked like a thin Laurent
corollary and did not explain sharpness.

### Candidate B: full torus-coset decay profile

For survivor varieties `V_m`, seek

`max dim(torus coset in V_m)=k-m`, `0<=m<=k`,

with an explicit equality family and rank-one `T_{k-1}` sharpness.

Main risk: the middle indices might cycle by `nu`, introduce a gcd dependence,
or make the expected `2m` relations dependent.

### Candidate C: exact planar `c=0` phase

Classify all actual supports for

`x_{n+2}=P(x_{n+1})+a x_n`

when `P` has no constant. Seek exact exceptional coefficient loci, exact cosets,
and the first finite window.

Main risk: trivial-middle root-copy branches and the two endpoint/power
orientations might leave additional binomial or monomial survivors.

### Candidate D: Laurent-polynomial support

Allow negative exponents and ask for a torus-coset phase depending on the
diameter of the Laurent support.

Disposition: **STOP**. Clearing denominators changes endpoint multiplicities
and introduces coordinate-boundary effects; no complete theorem emerged.

### Candidate E: rational shift-like maps

Allow `P` rational and classify finite-rank survivor windows away from poles.

Disposition: **STOP**. Pole divisors and cancellations require a different
geometric framework and fall outside the standard polynomial automorphism.

### Candidate F: mixed multiplicative cosets

Replace `Gamma^k` by independently translated or coupled multiplicative cosets
in different coordinates.

Disposition: **STOP**. Laurent still gives finite unions, but no exact
compatibility classification or sharp threshold was proved.

### Candidate G: effective higher-dimensional phase diagram

Combine character geometry with quantitative unit equations to bound `#T_k`.

Disposition: **STOP**. This would require a new quantitative degeneracy
analysis; Laurent alone is qualitative, and a vague effectiveness claim is not
acceptable.

### Candidate H: classification of every equality coset

Describe all Part A cosets of dimension `k-m` and all coefficient conditions.

Disposition: **STOP**. The upper bound and one saturated sharp family close,
but a full maximal-coset classification is not proved and is unnecessary for
the central mechanism.

## Closure tests for Candidate B

Candidate B could advance only if all of the following closed by hand:

1. normalize `V_m` and scalar orientation exactly;
2. use a group-algebra singleton to force every active middle character
   trivial;
3. split `P(xi)` into zero and nonzero branches without losing the endpoint
   relation;
4. prove all `2m` relations independent for every `m<=k`;
5. show future coordinate characters are generated from initial characters;
6. replace the suspected rotation orbit by the correct translated residue set;
7. handle disconnected component groups;
8. construct a saturated, connected equality subtorus;
9. give a rank-one infinite `T_{k-1}` family; and
10. justify arbitrary finite rank, arbitrary torsion, and arbitrary
    characteristic-zero fields from Laurent's exact scope.

Every test closed. The key correction was that the forced residues are

`{n-nu mod k:0<=n<m}`,

not an orbit under repeated subtraction of `nu`; hence no gcd condition exists.

## Closure tests for Candidate C

Candidate C could advance only after:

1. separating trivial-middle nonroot killing from root-copy;
2. treating monomial support independently;
3. ruling out every support of size at least three by a singleton argument;
4. proving the binomial local partition list exhaustive;
5. writing both endpoint-to-power scalar orientations;
6. checking every two-label word;
7. deriving, rather than guessing, the unique `{1,d}` support and
   `a=-beta^2` locus;
8. proving the exact formula and uniqueness of `C_d`;
9. closing `C_d` at `V_3`; and
10. separating geometric coset existence from `Gamma`-compatible infinitude.

Every test closed. The monomial sharp tuple was also corrected from the early
misoriented `(t,t^e,2t^e)` to

`(x_0,x_1,x_2)=(t^e,t,2t^e)`.

## Merge test

Candidate B and Candidate C were not merged merely to increase length. They
share the same survivor varieties and character identities. Candidate B's
proof succeeds because the constant supplies a third fixed character alongside
at least two powers; Candidate C classifies exactly what can happen after that
fixed character is removed.

The resulting “constant anchors versus zero-anchor boundary” story supports
about 22 substantive pages with no appendix padding.

## Initial literature boundary

The primary-source search plan included:

- Laurent's exact finite-rank/division-group theorem;
- Bedford--Pambuccian and Bera for the standard shift-like map class;
- Bell--Ghioca for fixed-orbit subgroup intersections;
- Ji--Xie--Zhang for cyclotomic affine/Hénon rigidity;
- Mello--Yasufuku for higher-dimensional multiplicative dependence;
- Karimov et al. for torus-subvariety methods in linear multiple reachability;
  and
- current 2026 shift-like work.

The decision rule was bounded and conservative: a direct theorem-level
collision would stop the package; absence of a collision would support only a
provisional GO, never a priority claim.

## Initial decision

Advance the merged B+C package only after the exact proofs, Paper16 portfolio
deduction, Laurent scope audit, and 22-page unity test all pass. Stop every
incremental, effective-without-proof, Laurent/rational, or full-classification
variant.

**INITIAL GATE RESULT: ADVANCE MERGED PACKAGE TO FULL SOURCE DESIGN.**
