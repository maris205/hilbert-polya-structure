# HCS-C68 defect--cokernel duality

Status: **PREFREEZE_COMPLETE_NOT_RELEASED**.

C68 identifies the embedded C65 saturation defect inside the C66 restricted
mark-map cokernel.  Let `M` be the frozen 16-by-16 C64 self-mark matrix and
let `u1,u2,u3` be the C65 saturation vectors.  The classes of these vectors
generate

```text
D ~= Z/8 + Z/2 + Z/2
```

inside `C = Z^16 / M Z^16`.  The quotient is

```text
C/D ~= (Z/2)^8 + (Z/4)^2 + Z/12 + Z/144
```

with invariant factors

```text
[1,1,1,1,2,2,2,2,2,2,2,2,4,4,12,144].
```

On the row side, the congruence lattice

```text
A = { y : z1.y = 0 mod 8, z2.y = 0 mod 2, z3.y = 0 mod 2 }
```

contains `M^T Z^16` with index quotient isomorphic to the dual of `C/D`.
Its quotient has the same invariant factors.  The result is restricted to
the frozen 16-type support and uses the scope firewall
`NO_BAD_EULER_OR_ROOT_NUMBER`.

Entry points:

- `code/c68_defect_duality.py`: source-bound exact producer;
- `code/c68_defect_duality_checker.py`: independent exact checker;
- `code/c68_defect_duality_replay_checker.py`: clean replay;
- `code/c68_snf_crosscheck.py`: SymPy Smith-form cross-check;
- `code/c68_mutation_test.py`: hostile semantic mutations;
- `results/c68_defect_duality_evidence.json`: canonical evidence;
- `paper/main.pdf`: compiled manuscript.

No full Burnside-ring, arithmetic/local, Euler-factor, root-number,
automorphy, or Hilbert--Polya claim is made.
