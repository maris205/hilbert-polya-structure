# Exact symbolic check: execution and scope

The coordinator ran, from `/root/autodl-tmp/hilbert-polya-structure`,
at the 2026-09-06 19:45 UTC development check:

```sh
python -B henon_dynamics/continuation_c414_c418_round2/function_field/certify_symbol_graph.py
```

Actual exit status: **0**. The full returned text gave:

```text
ALL_DIRECTED_SIMPLE_CYCLES 19
LITERAL_RECONSTRUCTION_IDENTITIES 16
SHARP_F3_T_ORDINARY_CYCLES {4: 1, 5: 2}
SHARP_F3_T_DISTINCT_POLYNOMIAL_POINTS 14
FINITE_SYMBOLIC_AND_LITERAL_CHECKS_PASS
```

The output also listed all nineteen unrestricted cycles with their
integer polynomial labels and all fourteen polynomial points of the
sharp example. The script works literally in $\mathbb F_3[t]$, not
by evaluating functions on the three constant-field elements. It checks
all sixteen signed labels for injectivity and verifies actual image
membership if and only if the asserted graph edge exists in that
example. Its reconstruction coefficient identities use exact fractions.

The script has not changed since that run. Current read-only SHA256:

```text
d4299f081c9bc6cde52d3451c8718961bf387360eb8d67e17a89f85744a41b23
```

The same session's read-only environment check reports Python 3.12.3
and Linux 5.15.0-78-generic; the program uses only the standard library.
The source hash and environment are recorded now, not falsely represented
as having appeared in its earlier stdout. No historical stdout file/hash
was retained or invented. No files are written by the program and `-B`
prevents bytecode output. It was not rerun merely to manufacture a receipt.

Earlier exploratory algebra included one SymPy call that failed with
exit 1 due to passing a list of `Poly` objects to an unsuitable gcd API.
The corrected expression-based call exited zero and helped expose the
nineteen graph cycles. Neither exploratory call is the saved standard-
library certificate, and neither is the proof of positive-characteristic
exhaustion. A prior determinant-one finite-field sample also had a
narrower scope than the final atlas; it is not used as an all-field proof.

The all-field seven-cycle exhaustion, rational-to-polynomial reduction,
common-degree rigidity and every characteristic overlap are proved
analytically in [PROOF_PACKAGE.md](PROOF_PACKAGE.md). The
[independent review](REVIEW_SOURCE_AND_REDUCTION.md) checks those
arguments without executing or claiming to certify this program.
Thus there are distinct mathematical-review and executable-diagnostic
evidence roles, with no finite sample promoted to a universal theorem.
