# Literature, terminology, and claim-boundary addendum

Status: `POST_CANONICAL_CLAIM_RENDERING_AWAITING_INDEPENDENT_RESEAL`
Candidate: `SD-C42`
Source lock: `2269e06576dd20c513c5ca9482cb49d36678e07358aaf80f2f08b33806b87041`
Mayer boundary: `a9dcbc922f8c47b0b845e7c6e76422aad3a0e744940a6529c2172176f5725bc5`
Selection audit: `0739263b6da1795bfa693ba2600e92a87fd973d9af08398d505a8fa4afa3190c`

This file supersedes all literature wording bound to the provisional source
`2041dec0...`.  It is a post-run dependent rendering and awaits a new
independent literature/novelty seal.  It does not convert the retrospective
M1--M20 correction or the post-run M21--M25 proof/rendering edits into a
prospective novelty claim.

## Preferred object name

Use **two-digit/even-iterate Gauss--Mayer return**.  Do not shorten it to
“even Gauss map,” which risks confusion with the distinct even-continued-
fraction algorithm.  The digit space is `X=N^N` with one-digit shift `sigma`;
the pair space is `X2=(N^2)^N` with one-pair shift `rho`; the exact relation is
`rho iota=iota sigma^2` through the grouping bijection `iota`.

The historical SD-C04 parent owns the Gauss branches, `L_s`, digit-primitive
grammar, and analytic determinant `det(I-L_s^2)`.  P40 newly re-indexes the
even iterate on pair space and proves the `RhoPrimitivePair` ledger.  No pair
A1 credit is inherited.

## Priority and claimed delta

Paper 1 already records that trace, discriminant, norm, or parity collisions
do not create a canonical rational-prime ledger.  The historical SD-C04 Route
card records 7,018 non-reversal trace-collision groups and asks for the next
trace/composite-discriminant audit.  Accordingly, P40 does not claim:

- discovery of the qualitative projection mismatch;
- discovery or priority of trace collisions;
- minimality or novelty of the trace-4, trace-6, or trace-10 witnesses;
- a new Gauss/Mayer transfer mechanism;
- a new arbitrary-`u` two-variable Selberg identity; or
- universal nonexistence of selector twists.

The three exact collision classes are contract falsifiers only.  The
trace-10 witness is retained because it is non-reversal and cross-pair-length,
not because it is first or minimal.  The only claimed delta is scoped
theorem-grade synthesis and closure of the pre-existing audit request:
exactly three projections, universal algebraic firewalls, explicit typed
witnesses, exact return/branch ownership, strict controls, and a
contract-relative selector conclusion.  The correction cycle itself earns no
novelty credit.  The independent literature verdict should remain
`PROCEED_WITH_CAUTION_AS_SCOPED_CLOSURE_ONLY`; the prior 4/10 assessment is a
historical expectation, not a valid seal for the replacement bytes.

## Discriminant terminology

Throughout,

\[
\Delta(w):=\Delta_{\mathbb Z[M]}(w)=\operatorname{tr}(M(w))^2-4
\]

means the trace/order or characteristic-polynomial discriminant of
`Z[M]`.  It is not automatically the fundamental field discriminant and not
the discriminant of a larger multiplier ring.  Maucourant's terminology
distinguishes these objects and should be followed consistently.

## Mayer source and domain boundary

On Mayer's specified holomorphic Banach-space realization, Proposition 3
states

\[
Z(s)=\det(I-L_s)\det(I+L_s)=\det(I-L_s^2)
\]

holomorphically on `Re(s)>1/2`.  The initial Euler-product/absolute-
convergence region is `Re(s)>1`; Corollary 3 provides meromorphic continuation
to the complex plane.  These three domains must be stated separately.

For free marker `u`, P40 owns the Fredholm family
`D_42(s,u)=det(I-u^2L_s^2)` in the nuclear setting.  Its logarithmic trace and
primitive-pair product are used only coefficientwise/formally in `u^2`, or
analytically for sufficiently small `|u|`.  No single-valued log is continued
through determinant zeros.  At `u=1`, the Selberg identity and continuation
come solely from Mayer's sourced theorem.  The identity is functional; it
does not give an objectwise pair/geodesic bijection.

## Primitivity firewall

`RhoPrimitivePair`, `SigmaPrimitiveDigit`, and
`GeodesicPrimitiveClass` are separate types.  A period-`n` digit orbit splits
under `sigma^2` into `gcd(n,2)` cycles, so odd periods stay one and even
periods split two.  The pair census follows

\[
N_{D^2}(k)=2N_D(2k)+\mathbf1_{k\text{ odd}}N_D(k).
\]

The global raw-index reversal used to express `L_s^{2k}` in stored branch
order is compatible with cyclic pair classes and repetition.  This
bookkeeping fact does not identify reversals in the object quotient and does
not bridge to geodesic primitivity.

## Ownership and target convention

The ownership theorem says only that no rational-prime scalar projector is
declared in the frozen untwisted `K_s` schema.  It does not rule out all
twisted, representation-valued, or future transfer families.  The exact
comparison object is `D_42^-1`, because `-log D_42` has positive Fredholm
trace coefficients.  The source coefficient

\[
\frac{u^{2kr}d_w^{rs}}{r(1-d_w^r)}
\]

must be compared with the target coefficient
`u^(2kr)p^(-rs)/r`.  The source stability denominator/Selberg tower, digit
marker, multiplicity, sign, orientation, and phase may not be discarded.

## Selection and P39 firewall

The six-card machine-literal filter keeps `SD-C01`, `SD-C02`, and `SD-C04`;
`SD-C04` uniquely wins A3 then A4.  It is incorrect to say only C01/C04
survive.  The local card hashes and evidence anchors are frozen in
`SELECTION_AUDIT.md`.

P39 is provenance only.  Its terminal-clean artifact commit is
`0f194edbfd05af853153043a568ffafd6c2f8afb`; its metadata commit/HEAD is
`18530b90317f6efc43ec2e4601ed8cef57daaddc`.  The immutable root research
Route file hashes to
`7bdb90811575a96518c2f67510ef9deb4335e2051c965643f7e3572e806ff6cd`;
the sealed canonical metadata Route card hashes to
`3a5da787a2d20439f345610b7523a565bf1eb55a618b977933ef1046eab0dbb8`;
the final P39 manifest file hashes to
`9fe17f0e746fa57a3dbbec7c96d4578b480b6cebcd04c7cb1be03209692516bd`.
These roles must not be conflated, and P39 neither ranks nor authorizes
SD-C42.

## Chronology and novelty concession

Provisional v1 and multiple in-flight corrective smoke outputs were known
before the final corrected input set existed.  Only the exact fifteen files,
seeds, grids, and fixtures in `CONTROL_LOCK.md` were frozen before the
canonical replacement rerun.  Proof, Route, literature, report, and manifest
files are post-run renderings.  M21--M25 repaired proof and schema wording
after that run without altering the locked inputs or canonical outputs.
Neither phase receives prospective, witness-priority, or novelty credit.

The final independent literature audit must bind the active source, Mayer
boundary, selection audit, this addendum, final proof/ownership/primitivity
files, canonical result hashes, P39 terminal provenance, and the acyclic
`CLAIM_BOUNDARY_SEAL.sha256` manifest that excludes the literature audit
itself.  A later research lock may bind both the claim seal and the completed
audit without creating a hash cycle.  Any audit bound only to `2041dec0...`
is obsolete.

## Bibliographic metadata guard

The Belolipetsky--Cosac--Doria--Teixeira Paula citation must be recorded as
*Communications in Mathematical Physics* **407**, article 76 (2026), DOI
`10.1007/s00220-026-05581-w`, published 9 March 2026.  Do not render it as
issue `407(4)`.  Include one Maucourant record only; do not duplicate it under
two discriminant descriptions.
