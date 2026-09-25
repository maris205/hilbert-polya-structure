# Finite algebraic-sieve symmetries provide cycles only after the arithmetic selection is fixed

**Paper ID:** `067-algebraic-sieve-symmetry-screen`  
**Record ID:** `ASFS-SCOUT-20260914-45`  
**Date / status:** `2026-09-14; PRE-P0 STOP`  
**Route state:** `No ASFS Route-A coordinate; Route B NOT INVOKED`.

## Why this is a distinct screen

The algebraic-sieve framework defines selections on finite sets using finite group actions and studies permutations that preserve or commute with those selections. Its Goldbach example has dihedral selector/symmetry groups for a fixed even integer `N`; the selected set is described using primes, and in certain cases uses a prime `p=N-1`.

Unlike the monotone or nonmonotone sieve algorithms already screened, this source really does provide finite permutation cycles. It therefore clears the narrow question “can a sieve-related object have a periodic action?” The answer is yes, but the action is a symmetry *of the finished finite selection problem*.

## A0 and lineage boundary

For a fixed finite `N`, the universe, selector group, and selected prime configuration are already part of the setup. A group element maps that finite configuration to another state in the same predeclared problem; it does not read a next sieve prime from its current state, extend a survivor word, or determine the all-prime predicate. Varying `N` makes a family of distinct finite problems, not one autonomous action. Choosing an orbit or a modulus cannot repair the missing global owner.

Thus the source realizes at most

```text
finite arithmetic selection -> finite group symmetry,
```

not the required chain

```text
prime/composite sieve -> intrinsic symbolic admissibility -> justified sequential deformation -> Hénon/conservative lift -> symplectic realization.
```

Calling a group symmetry a “sieve iteration” would conflate a stabilizer/centralizer action with the construction that establishes selection. This violates both A0 ownership and the one-object invariant.

## Gate audit

| Gate | Finding | Status |
| --- | --- | --- |
| A0 | arithmetic prime configuration is preselected in a finite problem | scoped FAIL |
| A1 | finite group cycles exist, but they belong to a selected symmetry carrier | external local control only |
| A2 | no roofed suspension or same-object determinant | NOT EVALUATED |
| symplectic/Hénon lift | not defined | P0 not admitted |
| Route B | Route-A readiness absent | NOT INVOKED |

**Decision: `stop/fork`.** This control prevents a false route around the recurrence obstruction: finite periodic group orbits become relevant only after a future candidate proves that its very same group action generates, rather than preserves, its arithmetic selection. No such action is supplied here.

## Evidence index

- Francesco Maltese, [*S-invariant and S-multinvariant functions and some symmetry groups of algebraic sieves*](https://arxiv.org/abs/2411.17168)
- [017 finite-wheel Hénon control](../017-finite-wheel-henon-control/paper.md)
- [041 stationary prime-gap language control](../041-prime-gap-language-screen/paper.md)
