# Validation Report

## Material passport

- Candidate: `pcf_quadratic_prime_multiplier_obstruction_v1`
- Validation date: 2026-08-13
- Source-lock SHA-256:
  `aab59e6d97e919bd9f11f74cf45d8163fc320560dfa74bee85401bd184d37842`
- Verification status: `VERIFIED`
- Exact scope: frozen periods `n=1,2,3,4`; no numerical candidate runs
- All-period scope: analytic derivative-content theorem and its stated
  rational-multiplier consequences

## Verification decision

The required experiment package is verified.  Every source-lock, proof,
control, candidate, conjugacy, and branchwise symplectic gate passes; all 37
tests pass; and all required machine-readable artifacts were produced.  The
scientific result is a negative exact obstruction, not a finite-cutoff absence:

```text
No raw rational-prime multiplier occurs at any period.
No odd rational exponent-prime multiplier occurs at any period.
The rational p=2 exponent-prime case for n>=2 remains OPEN.
```

## Gate ledger

| Gate | Verification | Status |
|---|---|---|
| Source lock | Valid JSON; frozen pre-execution counts are zero; SHA-256 recorded. | PASS |
| Static isolation | 19 Python files and one executable configuration scanned; zero forbidden-access or post-hoc-tolerance finding. | PASS |
| Proof boundary | Twelve dependency/nonclaim checks, including the explicit `p=2` open residue. | PASS |
| Controls | `c=0`, `c=-2`, and `c=-3/4` recover every frozen exact outcome. | PASS |
| Parameter preflight | Rational isolating interval straddles the globally increasing cubic's unique real root. | PASS |
| Conjugacy preflight | `phi(f_u(x))=g(phi(x))` for `phi(x)=-ux`; `g'(z)=2z`. | PASS |
| Candidate algebra | Formal/exact degrees, cycle counts, chain identities, resultants, perfect powers, quotient annihilation, and rational-root certificates agree for `n<=4`. | PASS |
| Independent coordinate run | The separate `f_u` pipeline reproduces every normalized multiplier polynomial from `g`. | PASS |
| Symplectic bridge | One-form and determinant residuals vanish; reciprocal return spectrum and all negative geometry checks pass. | PASS |
| Test suite | 37 tests; 0 failures, 0 errors, 0 skipped. | PASS |

## Exact candidate certificates

| `n` | Formal/exact degree | Cycle count | Cycle multiplier polynomial | Rational candidates |
|---:|---:|---:|---|---|
| 1 | 2 / 2 | 2 | `L^2-2L-4u` | none |
| 2 | 2 / 2 | 1 | `L-4+4u` | none |
| 3 | 6 / 6 | 2 | `L^2+(-16+8u)L-64+64u` | none |
| 4 | 12 / 12 | 3 | `L^3+(-48+16u^2)L^2+(256+256u^2)L+4096` | none |

The point resultants have degrees `2,2,6,12` and are respectively the exact
`1st`, `2nd`, `3rd`, and `4th` powers of the per-cycle polynomials after cycle
grouping.  Rational candidates were certified by simultaneous vanishing of
the `1,u,u^2` coefficient polynomials, never by floating recognition.

## Independent and adversarial checks

- Direct chain-product multipliers equal derivatives of the complete iterate
  in all audited maps and periods.
- Substitution into the exact orbit quotient independently annihilates every
  multiplier with its cycle polynomial.
- The `f_u` and `g` dynatomic components, point resultants, cycle polynomials,
  and rational candidate lists agree period by period after exact conjugacy
  normalization.
- The `c=-3/4` control detects the exact odd raw-prime multiplier `3`, showing
  that the candidate null result is not hardcoded.
- Repeated saturation removes both copies of the fixed point with multiplier
  `-1` from the formal period-two polynomial of `c=-3/4`, leaving zero exact
  period-two degree.
- Adversarial tests verify that the protocol scanner rejects a suspicious
  `Path(...).read_text()` resource, process/subprocess access, and a post-hoc
  prime-tolerance configuration.
- A full CLI smoke test executes every gate in a temporary output directory
  and checks that all eleven expected JSON artifacts exist.

## Code-review closure

An independent pre-execution review found no mathematical error in the exact
algebra, but it did identify three implementation/integrity issues: a SymPy
Boolean JSON serialization crash in the official CLI, an underpowered static
forbidden-access scan, and two hardcoded negative symplectic flags.  Before
the official run, these were corrected by recursive JSON normalization plus
explicit native booleans, expanded AST/configuration scanning with adversarial
tests, and computed denominator/unbounded-domain witnesses.  The post-fix CLI
smoke test and official execution both complete successfully.

## Reproducibility and provenance

| Item | Record |
|---|---|
| Exact command | `python code/scripts/run_exact_audit.py --max-period 4` |
| Source lock | SHA-256 `aab59e6d97e919bd9f11f74cf45d8163fc320560dfa74bee85401bd184d37842` |
| Proof package | SHA-256 `6d01f26b5832bd88923d4f4ba0bb5ed7010a571f17f46a0e75b6247499034e17` |
| Python | 3.12.3 |
| SymPy | 1.14.0 |
| pytest | 9.0.3 |
| Platform | Linux 5.4.0-155-generic x86_64, glibc 2.35 |
| Peak RSS | 771,460 KiB (approximately 753 MiB) |
| GPU | Not used |
| External data | None |
| External prime/zero data | Explicitly false |

The exact polynomial index is `results/exact_polynomials.json`.  Complete
command/environment metadata is in `results/command_environment_manifest.json`;
the theorem boundary is separately frozen in
`results/negative_result_ledger.json`.

## Validity boundaries

### Internal validity

Internal validity is strong for the declared exact algebra.  The proof is
all-period, the finite computations audit rather than infer it, controls hit
both allowed and assumption-violating outcomes, the coordinate computation
is duplicated, and every equality is exact.

### Construct validity

The result concerns cycle multipliers themselves.  It does not infer prime
labels from approximate magnitudes, and it distinguishes a raw prime
`|lambda|=p` from an exponent-prime target `|lambda|=p^n`.  The symplectic
calculation only transports a regular one-dimensional multiplier to the
reciprocal pair `(lambda,lambda^{-1})`.

### External validity

The candidate-specific corollary applies to the frozen PCF quadratic and its
linear conjugate.  The elementary general theorem applies to monic
algebraic-integer polynomials with derivative content `m`, under the explicit
rationality hypothesis on the multiplier.  No modulus-only, arbitrary
rational-map, or global compact-symplectic conclusion follows.

### Open boundary

The theorem is compatible with a rational multiplier `lambda=+/-2^n`.
Accordingly, no amount of absence through the frozen period-four cutoff may
change the status of rational `p=2` exponent-prime multipliers for `n>=2`
from `OPEN`.  The conditional real-orbit ledger remained disabled and is not
needed for any verified claim.

## Final statement

The evidence is sufficient to close the frozen raw-prime candidate as an
all-period no-go result.  Further finite orbit sampling would add no logical
support.  Any attempt to resolve the residual `p=2` exponent-prime question,
or to replace the branchwise cotangent relation by a global compact carrier,
must begin as a separate source-locked project.
