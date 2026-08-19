# HCS-C74 named-core affine rigidity

C74 resolves the symmetry boundary left explicit in C73. In the frozen
presentation `Q = Z/9 + Z/3 + Z/2`, the named 16-occurrence coordinate
multiset and its 10-point underlying set have trivial affine stabilizer, even
though the abstract C73 generation hypergraph has automorphism order
`345600`.

Headline values:

```text
|Aut(Q)| = 108
|Aff(Q)| = 5832
named multiset stabilizer = 1
named underlying-set stabilizer = 1
largest nonidentity occurrence overlap = 14/16 (two maps)
```

The occurrence overlap counts duplicate named points with multiplicity. The
paper keeps that statistic separate from pointwise label overlap and from
distinct-point intersection. It also records linear orbit size 108 and affine
orbit size 5832; translations are geometric maps here and are not claimed to
preserve subgroup-generation semantics.

Entry points:

- `code/c74_named_core_affine_rigidity.py`: source-bound producer;
- `code/c74_named_core_affine_rigidity_checker.py`: independent checker;
- `code/c74_group_crosscheck.py`: alternate matrix/image cross-check;
- `code/c74_named_core_affine_rigidity_replay_checker.py`: clean replay;
- `code/c74_mutation_test.py`: hostile semantic mutations;
- `results/c74_named_core_affine_rigidity_evidence.json`: evidence;
- `paper/main.pdf`: manuscript.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`. No full Burnside ring,
arithmetic/local, Euler-factor, root-number, automorphy, or Hilbert--Polya
claim is made.
