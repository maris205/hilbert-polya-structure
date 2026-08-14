# SD-C20 Exact Experiment Plan

## Frozen question

Can the same tensor-subset full shift support a relabeling-natural,
transition-dependent finite-group cocycle with genuine noncommutative Artin
blocks, and does that block distinguish prime atoms from matched nonprime
inventories?

No target-zero data are allowed.  The group, cocycle, determinant convention,
cutoffs, modular primes, and control seeds are frozen before execution.

## Claim-to-certificate matrix

| ID | claim | exact certificate | GO/STOP rule |
|---|---|---|---|
| E1 | incidence rules are indexed by `(u,v,w)` | all ordered subset pairs for `n=1..4` | `GO` iff orbit counts are `1,5,13,26` |
| E2 | the frozen `S3` rule has honest character blocks | exact `3d x 3d` determinants over `Z[x,y]` | `GO` iff trivial/sign equal `(1-x)(1-y)` and the standard formula matches |
| E3 | nonabelian leakage is present | determinant-log and direct trace-log through total degree six | `STOP_NONABELIAN_CLEAN_FACTOR` iff coefficients are `-3,-3,-6` |
| E4 | the four-edge word isolates a commutator | ordered group product and exact standard character | `GO` iff holonomy is nonidentity, traversal count is one, and gap is three |
| E5 | two-atom clean rules equal the natural gauge class in frozen groups | exhaustive `G^5` for `S3,D4,Q8` | report finite evidence only; never universalize |
| E6 | one-dimensional audits can miss holonomy | compare `Q8` 1D survivors with faithful-block survivors | `STOP_ONE_DIMENSIONAL_CHARACTER_AUDIT` iff `512>64` |
| E7 | the mechanism is arithmetically selective | six matched inventories, seeds `18001..18005` | `PROVES_TOO_MUCH` iff every control reproduces it |
| E8 | an honest Fredholm domain exists | exact absolute-series majorants | trivial threshold `1`, nontrivial symmetric threshold `2` |

## Exact exhaustive protocol

For every table `(a,c,h,u,v) in G^5`, all nontrivial one-dimensional blocks
are compared exactly as sparse polynomials.  Tables surviving that audit are
tested in a faithful block on complete rectangular grids over the primes
`1000003`, `1000033`, and `1000037`.  A `d`-dimensional block uses coordinate
degree bound `3d`.  The product of the three primes exceeds the frozen
absolute coefficient bound `2(3d)!2^(3d)`, so a survivor on all grids is an
integer-polynomial identity.  Every survivor must also satisfy

`h=a`, `v=u^-1 a^3`, and `c=u^-1 a^2 u`.

## Reproducibility

Run:

```bash
python experiments/run_sdc20_exact_suite.py --verify-byte-determinism
```

The orchestrator runs the scientific generator, analysis, fourteen tests,
integrity audit, and SHA freeze twice.  CSV uses LF line endings; JSON keys are
sorted; timestamps and elapsed-time fields are forbidden.

## Claim boundary

The exhaustive classification is limited to two atoms and the three named
groups.  Character determinants are not asserted to classify general finite
group extensions.  No continuation, functional equation, Weil form,
self-adjoint operator, target-zero calculation, RH claim, or Route-B claim is
part of this plan.
