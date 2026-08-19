# HCS-C69 defect-extension splitting

Status: **PREFREEZE_COMPLETE_NOT_RELEASED**.

C69 proves that the actual C68 subgroup

```text
D = <[u1],[u2],[u3]> ~= Z/8 + Z/2 + Z/2
```

is a direct summand of `C = Z^16 / M Z^16`.  The explicit retraction is

```text
rho([x]) = (x10 mod 8, x3 mod 2, x1+x15 mod 2).
```

Its kernel is represented by the index-32 lattice defined by the three zero
congruences above.  In an explicit basis `B`, the complement presentation
`B^{-1}M` has Smith invariants

```text
[1,1,1,1,2,2,2,2,2,2,2,2,4,4,12,144].
```

Thus the complement is isomorphic to the C68 quotient.  Moreover, the set of
retractions, equivalently the set of complements to this fixed `D`, is a
torsor under `Hom(C/D,D)` and has exactly `2^41 = 2199023255552` elements.
The displayed complement is explicit, not canonical.

Entry points:

- `code/c69_defect_splitting.py`: source-bound exact producer;
- `code/c69_defect_splitting_checker.py`: independent exact checker;
- `code/c69_snf_crosscheck.py`: SymPy Smith-form cross-check;
- `code/c69_defect_splitting_replay_checker.py`: clean-process replay;
- `code/c69_mutation_test.py`: hostile semantic mutations;
- `results/c69_defect_splitting_evidence.json`: canonical evidence;
- `paper/main.pdf`: compiled manuscript.

The scope firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.  No full Burnside-ring,
arithmetic/local, Euler-factor, root-number, automorphy, or Hilbert--Polya
claim is made.
