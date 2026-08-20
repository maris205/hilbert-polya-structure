# Adaptive batch HCS-C74 through HCS-C78

Status: **C74--C78 complete; round closure ready**.

This is a five-paper adaptive round continuing the frozen C69--C73 mark-core
lane.  Each successor is selected only after its predecessor supplies a new
exact theorem or a certified obstruction.  Every paper must pass source
binding, a fresh exact producer, an independent checker, a separate
computer-algebra or group cross-check, clean-process replay, hostile semantic
mutations, two isolated byte-identical LaTeX builds, visual inspection, and an
explicit prefreeze manifest before commit and push.

## C74 (complete)

C73 proved that the abstract sixteen-label generation hypergraph has
automorphism order `345600`, while explicitly refusing to identify those
combinatorial symmetries with automorphisms of the universal core.  C74 closes
that boundary for the actual C72 named coordinate realization

```text
Q = Z/9 + Z/3 + Z/2.
```

Writing automorphisms of the odd part as

```text
(x,y) |-> (a*x + 3*b*y mod 9, c*x + d*y mod 3),
```

the exact computation gives

```text
|Aut(Q)| = 108
|Aff(Q)| = 54 * 108 = 5832
named-multiset affine stabilizer = 1
underlying 10-point-set affine stabilizer = 1
```

The nonidentity affine overlap maximum is `14/16`, attained by exactly two
linear maps.  Thus the full C73 hypergraph symmetry is label combinatorics,
not an affine symmetry of the named core.  C74 must retain the distinction
between repeated labels, the ten distinct core points, and the sixteen
vertices of the generation hypergraph.

Project: `henon_mu3_yukawa_mark_named_core_affine_rigidity/`.

## C75--C78

### C75 (complete)

C74 separates the affine action on named points from the abstract C73
hypergraph.  C75 computes the exact symmetry of the lifted closure
incidence object: retain the ambient `Q` action, the cyclic-subgroup closure
fibres of the sixteen named labels, and the duplicate-label permutations.
The certified result is a weighted fibre stabilizer `K` of order `12`, a duplicate
fibre order `5!*2!*2!*2! = 960`, and a lifted order `11520`.  The subgroup-node
projection has a `C6` kernel, so the paper must distinguish the faithful
ambient lift from the nonfaithful action on the 20-subgroup lattice.

Project: `henon_mu3_yukawa_mark_closure_incidence_lift/`.

### C76 (complete)

C75 supplies the 11520-element ambient lift.  C76 extracts its faithful
1920-element label image and classifies all 65536 named supports under that
action, recording their cyclic-closure geometry.  The certified atlas gives 3024 support
orbits, an exact orbit-size spectrum, 98 inclusion-minimal supports across all
twenty closure subgroups (34 orbits, including the empty support for the
trivial subgroup), and 25 full-core minimal triples in 7 orbits.  The paper
must retain the distinction between the 11520-element lifted pair group and
the 1920-element effective label image.

Project: `henon_mu3_yukawa_mark_closure_orbit_atlas/`.

### C77 (complete)

C76 classifies supports by effective label orbits.  C77 changes the observable:
it performs Möbius inversion on the actual 20-subgroup lattice of `Q` to obtain
the exact generating-closure polynomial for every subgroup.  For a retained
support with independent deletion probability `q`, it uses
`P_{<=H}(q)=q^(16-n_H)` and
`P_{=H}(q)=sum_{K<=H} mu(K,H) q^(16-n_K)`, checks all 65536 supports directly,
and verifies that the top polynomial agrees with C73's reliability result.

Project: `henon_mu3_yukawa_mark_subgroup_mobius_reliability/`.

### C78 (complete)

C77 supplies exact subgroup-level reliability polynomials.  C78 measures the
complementary repair geometry: for a deletion set `D`, `rho(D)` is the minimum
number of deleted labels restored for `L\\D` to generate the full core.  The
release enumerates all 65536 supports and publishes the exact bivariate
support/repair generating function.  Its locked values are certified rather
than merely predicted:

```text
rho <= 3
P(x,1) = (1+x)^16
P(1,y) = 30400+32704y+2368y^2+64y^3
evidence SHA-256 = 728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae
PDF SHA-256 = 2d0e0e553f3a2a6335822916505e0bde14eb225b0172dfc3522a64cb96ed0571
manifest SHA-256 = 955b5ce23bf811d7377c0e41afd8d7dbc384a467790647e04cf0dadc98347c60
```

Project: `henon_mu3_yukawa_mark_repair_distance_geometry/`.

## Round closure

All five papers pass source binding, fresh exact production, independent
checking, algebraic/group cross-check, clean replay, hostile semantic
mutations, two isolated byte-identical LaTeX builds, visual inspection, and
prefreeze-manifest hashing.  The round scope firewall remains
`NO_BAD_EULER_OR_ROOT_NUMBER`; no arithmetic/local, Euler-factor, root-number,
automorphy, full Burnside-ring/table-of-marks, or Hilbert--Polya claim is made.
