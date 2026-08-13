# Implementation Notes

## Scope

The implementation executes preregistered blocks B1--B5 for the
tensor-factorization branch and the naive finite dual branch.  It remains
inside Symbolic Dynamics and reads no external dataset.

No existing `PREREGISTRATION.md`, `EXPERIMENT_PLAN.md`, or
`EXPERIMENT_TRACKER.md` file is modified by this implementation package.

## Main program

`code/intrinsic_grading_experiment.py` uses the Python standard library only.
The default run is `N=512`.

The main construction proceeds as follows:

1. Recover the proper tensor-divisor interval of each mass `n`.
2. Enumerate every strict chain in the open interval.
3. Construct the augmented signed simplicial boundary.
4. Verify `d^2=0` over the integers by explicit coefficient cancellation.
5. Compute exact boundary ranks over `F_2` with bitset Gaussian elimination.
6. Compute reduced Betti numbers, Euler characteristic, and homology
   supertrace.
7. Compare with an independently recursive incidence-Möbius ledger.
8. Assemble the odd-atom Berezinian and exterior-Fock supertrace prefixes.
9. Run all frozen parity, monoid, and free-mixing controls.
10. Run finite `R_P` and Schatten diagnostics without scalar zeta evaluation.

The `F_2` calculation is sufficient for the computational parity check.  The
integral sphere/acyclic statement is supported mathematically by the
shellability of products of finite chains; the program does not claim a
general Smith-normal-form computation for arbitrary posets.

## Candidate data versus verifier data

Candidate construction uses:

- tensor divisibility;
- the tensor unit;
- the entropy norm.

The `factorization()` helper is verifier-only.  It checks the predicted
squarefree sphere/non-squarefree acyclic pattern after the order complex and
its homology have already been computed.  It is not used to select atoms,
create simplices, construct boundaries, or assign parity.

No function reads a prime file or a zeta-zero file.  Tensor atoms are detected
as nonunit objects with empty open factorization intervals.

## Frozen deterministic controls

- random atom parity: seeds `500000,...,500063`;
- random simplex parity: seeds `900000,...,900031`;
- orientation gauges: seeds `1300000,...,1300015`;
- factor-count parity with multiplicity;
- shifted multiplication;
- additive monoid;
- 28 free-mixing pairs among the first eight recovered atoms.

## Dual-ratio grid

Atom mass cutoffs are:

```text
31, 127, 257, 509
```

The seven frozen points are:

```text
1/4 + 0.75 i
1/3 + 2 i
1/2
1/2 + i
1/2 + 7 i
2/3 + 2 i
3/4 + 0.75 i
```

The computation uses the finite product directly.  It does not call a zeta
implementation.  Reflection and critical-modulus residuals measure floating
implementation error only; neither is interpreted as infinite-cutoff
convergence.

## Schatten grid

The sectors are:

```text
T_s
T_(1-s)
T_s - T_(1-s)
T_(1-s) T_s^(-1) - I
```

Partial `S_q` norms are stored for `q=1,2,4` at:

```text
s = -1/4
s =  1/4
s =  1/2
s =  1/2 + i
s =  3/4
s =  5/4
```

The output keeps numerical partial norms separate from the analytic
convergence classification.  In particular, a bounded finite table is never
used as proof of trace-class convergence.

## Complexity and performance

At `N=512`:

- 511 factorization fibers;
- 15,629 simplices including one augmented empty simplex per fiber;
- largest fiber: `n=480`, 976 simplices;
- largest chain dimension: seven;
- one complete experiment: about three CPU seconds in the current runtime;
- no GPU and no network access.

Boundary matrices are generated fiber by fiber.  Full matrices and the large
opaque tensor registry are not persisted because they are exactly
regenerable.  The complete result package is compact.

## Test and reproducibility commands

From the Paper05 root:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest discover -s code -p 'test_*.py' -v
```

The five tests cover:

1. hand complexes `p`, `p^2`, `pq`, repeated composite, and `pqr`;
2. exact Möbius/homology agreement through 64;
3. finite dual identities;
4. Schatten-domain diagnostics;
5. the complete frozen `N=512` regression.

For an independent reproducibility check:

```bash
run_a=$(mktemp -d /tmp/paper05-run-a.XXXXXX)
run_b=$(mktemp -d /tmp/paper05-run-b.XXXXXX)

PYTHONDONTWRITEBYTECODE=1 \
  python code/intrinsic_grading_experiment.py --N 512 --output "$run_a"
PYTHONDONTWRITEBYTECODE=1 \
  python code/intrinsic_grading_experiment.py --N 512 --output "$run_b"

diff -qr "$run_a" "$run_b"
```

The committed result files were produced by this exact command path and two
fresh runs were byte-identical.

## Claim boundary

The code certifies a finite exact grading ledger and diagnoses the naive dual
operator.  It does not certify analytic continuation, a zeta functional
equation, a Gamma factor, a Weil form, Riemann zeros, or a Hilbert--Pólya
operator.
