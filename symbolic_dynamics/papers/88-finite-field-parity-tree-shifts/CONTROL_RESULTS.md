# Control Results

Command:

```text
python3 code/verify_parity_tree.py
```

Recorded two-round-audit output:

```text
finite-field parity tree exact controls
control scope: prime fields plus one exhaustive F_4 lane
F_2, d=2, c=(1, 1), h=3: leaves=8, blocks=256, rays=8, proper_subsets=255, restriction_fiber=16
F_2, d=3, c=(1, 1, 1), h=2: leaves=9, blocks=512, rays=9, proper_subsets=511, restriction_fiber=64
F_3, d=2, c=(1, 1), h=2: leaves=4, blocks=81, rays=4, proper_subsets=15, restriction_fiber=9
F_3, d=2, c=(1, 2), h=3: leaves=8, blocks=6561, rays=8, proper_subsets=0, restriction_fiber=81
F_5, d=2, c=(1, 2), h=2: leaves=4, blocks=625, rays=4, proper_subsets=15, restriction_fiber=25
F_2, d=2, c=(1, 1), h=2: leaves=4, blocks=16, rays=4, proper_subsets=0, restriction_fiber=4
F_2, d=3, c=(1, 1, 1), h=1: leaves=3, blocks=8, rays=3, proper_subsets=0, restriction_fiber=4
F_4, d=2, c=(1,a), h=2: leaves=4, blocks=256, rays=4, proper_subsets=15, restriction_fiber=16
negative controls: d=1 ray degeneracy; zero-coefficient deletion leak
rank F_2, d=2, c=(1, 1), h=4: constraint_rows=15, nullity=16, subset_certificates=49
rank F_2, d=3, c=(1, 1, 1), h=3: constraint_rows=13, nullity=27, subset_certificates=82
rank F_3, d=2, c=(1, 2), h=4: constraint_rows=15, nullity=16, subset_certificates=49
rank F_5, d=2, c=(2, 4), h=3: constraint_rows=7, nullity=8, subset_certificates=256
rank F_5, d=3, c=(1, 2, 4), h=3: constraint_rows=13, nullity=27, subset_certificates=82
rank F_7, d=2, c=(3, 5), h=4: constraint_rows=15, nullity=16, subset_certificates=49
ledger: enumerated_blocks=8315, exhaustive_proper_subsets=811, rank_constraint_rows=78, rank_subset_certificates=567, assertions=19764
ALL EXACT CONTROLS PASSED
```

## What was checked

The prime-field enumeration lane performs four definition-level tests:

1. generate every block from every leaf word and check every local equation;
2. compare generated and brute-force legal blocks in three small cases;
3. count every restriction fiber and every tested root-to-leaf ray word;
4. build the complete joint table of the root and every proper terminal
   subset in selected cases.

The independent `F_4` lane encodes `F_4 = F_2[a]/(a^2+a+1)`, checks its
field tables, exhausts all 256 terminal assignments for `d=2`, `h=2`, and
repeats legality, bijection, reconstruction, restriction, all-ray, and all
15 proper-subset joint-law tests. Two negative controls verify the stated
failure mechanisms at `d=1` and when one coefficient is zero.

The rank lane independently builds the local constraint matrix over prime
fields, computes rank and boundary nullity, constructs the
boundary-extension matrix, checks that the extension lies in the constraint
kernel, verifies the explicit root row, and checks root/subboundary
observation ranks. All arithmetic is exact; no floating point is used.

## Scope boundary

Enumeration covers `F_2`, `F_3`, `F_4`, and `F_5`; modular Gaussian
elimination covers `F_2`, `F_3`, `F_5`, and `F_7`. One extension-field
fixture is a regression test, not evidence for all prime powers. Universal
scope comes from the field-linear proofs: multiplication by a nonzero
coefficient is bijective, a nonzero linear functional has a codimension-one
kernel, and the displayed fiber arguments are independent of a particular
field representation.
