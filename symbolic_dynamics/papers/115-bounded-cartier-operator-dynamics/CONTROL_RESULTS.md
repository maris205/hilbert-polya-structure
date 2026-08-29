# Exact Control Results — P115

## Result

`python3 code/verify.py` completed with:

```text
PASS: 2,259,162 exact assertions
```

The complete deterministic stdout is stored in
`code/verification_output.txt`.

## Literal field lanes

| Field | Polynomial-basis modulus | Main degree bound | Phase size | Depth histogram | Core cycles by length | Component size by cycle length |
|---|---|---:|---:|---|---|---|
| `F_2` | `z` | 7 | 256 | `{0:2, 1:30, 2:96, 3:128}` | `{1:2}` | `{1:128}` |
| `F_3` | `z` | 5 | 729 | `{0:3, 1:240, 2:486}` | `{1:3}` | `{1:243}` |
| `F_4` | `z^2+z+1` | 5 | 4,096 | `{0:4, 1:252, 2:768, 3:3072}` | `{1:2, 2:1}` | `{1:1024, 2:2048}` |
| `F_8` | `z^3+z+1` | 4 | 32,768 | `{0:8, 1:504, 2:3584, 3:28672}` | `{1:2, 3:2}` | `{1:4096, 3:12288}` |
| `F_9` | `z^2+1` | 3 | 6,561 | `{0:9, 1:720, 2:5832}` | `{1:3, 2:3}` | `{1:729, 2:1458}` |
| `F_16` | `z^4+z+1` | 2 | 4,096 | `{0:16, 1:240, 2:3840}` | `{1:2, 2:1, 4:3}` | `{1:256, 2:512, 4:1024}` |

Each field also has a separate `n=0` exhaustive lane. The script verifies
the Frobenius identity, inverse-Frobenius identity, and nonzero field law
before testing the dynamical claims.

## Assertion families

1. Direct iterates equal the coefficient formula at every tested time and
   coordinate.
2. The index-chain coordinate transform and its inverse reconstruct every
   state exactly, including the empty positive-coordinate product at `n=0`.
3. Direct Cartier updates conjugate statewise to inverse Frobenius times the
   product of finite nilpotent shifts.
4. Weak-component sizes, per-periodic-root entry layers, tree cardinalities,
   and component totals agree with the structural theorem.
5. Literal depth equals the occupied-index valuation formula for every state.
6. Every CDF and shell count agrees with its closed form.
7. The literal image set equals the padded bounded-degree space.
8. Every target in the image has the predicted fibre size; a target outside
   the image has an empty fibre.
9. The deepest shell and top-chain multiplicity are exact.
10. Literal constant cycles equal Möbius-inverted cycle counts.
11. Full-map fixed counts through two Frobenius periods equal
   `p^gcd(a,m)`.
12. Zeta coefficients computed from the fixed-sequence exponential recurrence
   equal coefficients computed from the cycle Euler product.
13. Each temporal signature recovers the generating `(p,a,n)`.
14. Thirty-three rational lattice lanes for `p in {2,3,5}` and
    `a in {1,2,3}` verify exact floor stabilization through `L=9`.

The counter is the number of executed `check` calls. It includes repeated
statewise coordinate checks and aggregate identities and must not be read as
2,259,162 logically independent mathematical claims.

## Counterexample guards

- For every extension-field lane, a literal scalar witness rejects false
  `F_q`-linearity.
- Same-degree support witnesses reject the false claim that ordinary degree
  determines core-entry time.
- Extension-field cycle histograms reject the false fixed-core-only zeta.
- Explicit outside-image targets reject accidental assignment of a positive
  size to an empty fibre.
- Literal weak-component aggregation rejects a component size incompatible
  with its Frobenius cycle length.

The program uses only the Python standard library. It is finite evidence and
does not certify novelty, owner completeness, or external release.
