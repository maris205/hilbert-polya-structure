# Exact author checks

Date: 2026-09-05. Working directory:
`/root/autodl-tmp/hilbert-polya-structure`.

Command actually executed:

```text
python henon_dynamics/research_c399_c403/hyperbolic_trace/exact_check.py
```

Exit code: `0`. Result: `PASS`. SymPy version reported by the program: `1.14.0`.
The initial version ran once. After adding the self-adjoint finite-certificate
theorem and its checks, the affected script ran again successfully. The figures
below refer to this second, current-input execution, not an independent audit.

Script SHA256:
`6896f8fc6c989396c95c5d02ad19d4790b8e90bd639502806b8532f12b77efe3`.
Proof input snapshot SHA256:
`fd03fd7322d8d0f95f69756624a714fdd5e2abf78e2b4de01fdf28dfec103b40`.
The executable does not import the prose; its proof hash records the claimed
interpretation rather than a computational dependency.

Post-review proof snapshot, checked on 2026-09-05:
`b7184d2304131031c06facabcd9d719cac9e558b11dc0a38e1b65f230ff7660f`.
This proof-only revision explicitly strengthens the finite-prefix realization
to a real normal matrix (conjugate roots give real rotation-dilation blocks)
and states the `B^K` trace-class condition in the self-adjoint summary.
These are the independent review's own corrections/clarifications, recorded in
`../arithmetic_scout/HYPERBOLIC_TRACE_ADMISSION_REVIEW.md`, sections 7.2 and 7.4.
The script hash is unchanged. No new run is claimed for this prose revision;
the executed snapshot above is deliberately preserved. The review still holds
the material below independent-paper admission despite mathematical closure.

| Control | Actual result |
|---|---|
| Direct matrix determinant versus grouped exterior power sums | 96 equalities: eight matrices, repetitions 1–12 |
| Newton companion prefix realizations | 36 exact moment equalities: dimensions 1–8, all corresponding initial moments |
| Even-shifted Hankel inertia and explicit negative polynomial | 21 exact cases: seven real-spectrum matrices and three even offsets; Sturm counts match the signed coefficient counts |
| Small self-adjoint exclusion certificate | The 2-by-2 moment minor for diag(2,1/2) is exactly -47/8 |
| First later mismatch for each companion in the selected symplectic example | Exactly repetition N+1, for N=1–8 |
| Generic two-pair minimum graded size | 16, with parity dimensions 8 and 8 |
| Resonant two-pair minimum graded size | 12, with parity dimensions 6 and 6 |
| Assumption boundary controls | Singular zero matrix allows scalar trace 1; identity monodromy allows scalar trace 0 |

The eight matrices include stable and unstable real scalars, a negative
unstable scalar, a nontrivial stable Jordan block, a nonreal conjugate pair,
a negative symplectic pair, and independent/resonant positive symplectic pairs.

All arithmetic was exact. The finite controls neither prove the infinite
obstruction nor certify a natural graded dynamical operator. The all-tail
argument is in `PROOF_PACKAGE.md`. This receipt is a concise transcription of
the actual structured stdout, not a claim that the complete stdout was archived
as an additional canonical file. A release contract, if admitted, must define
and execute its own final evidence and manifest gates.
