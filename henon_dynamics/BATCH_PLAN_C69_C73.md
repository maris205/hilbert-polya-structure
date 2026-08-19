# Adaptive batch HCS-C69 through HCS-C73

Status: **C69 prefreeze complete; C70--C73 contingent**.

This is a five-paper adaptive round. Each successor is selected only after the
predecessor has an exact theorem or a certified obstruction. Every paper must
pass a fresh exact pilot, source binding, an independent checker, a clean
process replay, a separate computer-algebra cross-check, hostile semantic
mutations, two clean LaTeX builds, and an explicit prefreeze manifest before
commit and push.

## C69 (completed prefreeze)

Let

```text
C = Z^16 / M Z^16,
D = <[u1],[u2],[u3]> ~= Z/8 + Z/2 + Z/2
```

be the actual C68 embedding. C69 determines whether this particular subgroup,
not merely an abstract subgroup with the same invariants, splits from `C`.
The fresh pilot gives the retraction

```text
rho([x]) = (x10 mod 8, x3 mod 2, x1+x15 mod 2).
```

Its kernel is represented by an index-32 congruence lattice with an explicit
basis `B`; the presentation `B^{-1}M` has Smith invariants

```text
[1,1,1,1,2,2,2,2,2,2,2,2,4,4,12,144].
```

Project: `henon_mu3_yukawa_mark_defect_splitting/`.

All retractions of the fixed inclusion form a torsor under `Hom(C/D,D)`.  The
three target-coordinate exponents are `(17,12,12)`, so there are exactly
`2^41` retractions and, equivalently, `2^41` complements.  The producer,
independent checker, SymPy cross-check, clean replay, 23/23 hostile mutations,
and byte-reproducible two-build paper gate all pass.

## C70--C73

`UNSELECTED_CONTINGENT`: each later slot remains open until the preceding
paper's released theorem or certified obstruction supplies a distinct exact
question. No slot will be filled by merely renaming a matrix invariant already
proved in C64--C69.

The scope firewall for the round is `NO_BAD_EULER_OR_ROOT_NUMBER`.
