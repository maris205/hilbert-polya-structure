# Paper 8 Phase-3 deterministic-controls independent audit

Audit date: **2026-08-14 (Asia/Shanghai)**  
Audit role: independent methodology, integrity, and reproducibility reviewer  
ARS basis: `academic-research-suite` v0.1.24; experiment `validate`,
methodology-review, and integrity-gate instructions were read before review  
Protected scope: `research_protocol.md`, `candidate_lock.md`,
`phase2_domain_amendment.md`, `code/`, `experiments/`, and `results/`  
Write boundary: **read and execute only; no code, result, protocol, or lock was
intentionally corrected by this review**

## 1. Verdict

**SCIENTIFIC/REPRODUCIBILITY PASS; RELEASE HOLD FOR ONE MINOR ARTIFACT-HYGIENE
FIX.**

There is no Critical or Major finding.  The shifted Floquet/Poisson sign, Haar
normalizations, finite-character cancellation, finite-corner witness,
clock/copy/composite controls, transverse-probability control, domain split,
active-lock hashes, implementation hashes, and two-fresh-directory byte
reproducibility all pass.  The package makes no theorem claim from its finite
controls and contains no target-zero or fitting input.

The sole release blocker is Minor finding `m1`: two generated `.pyc` files are
present under `code/__pycache__/`.  Their timestamp/size headers agree with the
current source files, so they are not stale by the CPython timestamp check;
nevertheless they are orphan release artifacts, are outside the frozen
implementation manifest, and would be copied by a whole-subtree release.
They must be removed and absence rechecked before the controls package is
called release-clean.  This review did not remove them.

## 2. Exact frozen-input hashes

The active tuple was re-hashed independently and agrees with both the hard
lock in the implementation and the generated manifest.

| Active record | Observed SHA-256 | Result |
|---|---|---|
| `notes/research_protocol.md` | `e1149ebd9609de24e0df00dcaeafdbcd31ee973e8ebe04b15cf86541f8084535` | PASS |
| `notes/candidate_lock.md` | `8a5a460bac51843e532c9894fcb99470247c7de7833449c3660813ccd183d64e` | PASS |
| `notes/phase2_domain_amendment.md` | `412e6d24c43ab5a995d135c6ecb207f5225414fac223fcf63080486af6fc3de3` | PASS |

The six-file implementation ledger also agrees exactly.

| Implementation record | Observed SHA-256 | Result |
|---|---|---|
| `code/isotropy_trace_controls.py` | `524884ef70eeaa8ace156f189c3aca4e2ca5574c091f48ed6d730e545a4cf926` | PASS |
| `code/test_isotropy_trace_controls.py` | `15ebd4a7330985d6ce432c76daf2020922a28ce36482624e52ee6700ed8c6b67` | PASS |
| `code/README.md` | `377060a53db657a508e8e7bf938c127bea17ed513f2cc9f83824593dafb3773a` | PASS |
| `experiments/reproduce.sh` | `9735b78945ed830280baaabd78ad1a2a835f1cc52944a71f284a89903fd5da26` | PASS |
| `experiments/README.md` | `2addb33c5c5038cdd4c434ae637121c7fa1b1c8c96ee0d91b687e0502a6461ae` | PASS |
| `results/README.md` | `703338a6fbacdf9ba1554b0de0280e64f8014f504acdc6e23f26b394606889b7` | PASS |

## 3. Reproduction receipt

I ran, from the Paper-8 workspace,

```text
./papers/8-isotropy-trace/experiments/reproduce.sh
```

Observed result:

- 18/18 unit tests passed;
- nine CSV artifacts regenerated successfully;
- artifact row counts, byte sizes, and SHA-256 values verified;
- all three active-tuple hashes verified;
- all six implementation-file hashes verified;
- two fresh generations in distinct `mktemp` directories compared byte for
  byte for all nine CSVs and the JSON manifest;
- the checked-in results hash inventory captured before the run was identical
  to the inventory captured afterward; and
- the manifest SHA-256 was
  `20801ebe4c927f939c462842e38569555f96f5fef78859755b6caa8cbcf38b07`.

The run used Python `3.10.12`, `LC_ALL=C`, and
`PYTHONDONTWRITEBYTECODE=1`.  The byte-identity verdict is therefore an exact
same-environment result; this audit does not infer cross-platform `libm` byte
identity from it.

In addition to the shipped tests, I performed a read-only, field-by-field
semantic audit of every generated row.  Coverage was nine CSV files and 129
data rows.  The independent aggregate checks returned:

```text
max shifted-Poisson absolute error:       4.847302891456678e-16
min wrong-sign error for theta != 0:      0.057875408571292516
max finite-grid floating residual:        1.2246467991473533e-15
manifest/artifact/lock/implementation:    exact hash match
semantic audit:                           PASS
```

## 4. Artifact inventory and field audit

| Artifact | Rows | Bytes | Observed SHA-256 | Field-level verdict |
|---|---:|---:|---|---|
| `shifted_poisson_convention.csv` | 16 | 5159 | `d63eac37c1995137234e9d4d95af137c853bcc6cca6d37bfc897fbc30d592fbb` | PASS |
| `finite_character_grid.csv` | 75 | 9603 | `632a2a6d51b7d806e3d8c45f19d3706f1f41eda9ccef0d7d09b8a5d67109f676` | PASS |
| `nontrivial_character_phase.csv` | 14 | 1369 | `ef3a577b1a6306db97764ff29a9c844a2b8a3b98ba376ddc4a15c7558b70bfab` | PASS |
| `trace_scale_controls.csv` | 4 | 1205 | `0f4f2e151633646c7479246cd138ae949681a2d847111966175c9ad490437489` | PASS |
| `rank_one_corner_peaks.csv` | 7 | 833 | `20bc2ed07483cba0dd2c40f84b66edc40e6e298b89a9dc22b7cd7be3a8ea429e` | PASS |
| `linfinity_representatives.csv` | 2 | 255 | `b28113700fbab40f639bbc6e64919f3cdcaa5b9332adf67ba4d0df894cfaef69` | PASS |
| `clock_copy_composite_controls.csv` | 4 | 1004 | `5f8a65523417cf507be89a6b69084ba31826bf2ca75ea7118cdbcecd66562f1f` | PASS |
| `transverse_probability_controls.csv` | 4 | 564 | `333083dcb90027bae61ff6d9abce2980f8fabf997c6969e57f19718fb4668cd2` | PASS |
| `domain_boundary_controls.csv` | 3 | 735 | `17a03cc85dc32afaddc769dc5309e0afd9038a154271ddfe5e1b1cfe5931762e` | PASS |

### 4.1 Shifted sign and character phases

The source, tests, CSV headers, every Poisson row, and the manifest all use the
same convention:

```text
chi_theta(rL)=exp(+i r theta),
xi(u+rL)=exp(-i r theta)xi(u),
lambda_n=(2 pi n-theta)/L,
sum_n fhat(lambda_n)=L sum_r f(rL)exp(+i r theta).
```

This pairing is mathematically consistent: a Floquet mode `exp(i lambda u)`
satisfies the frozen quasiperiodicity exactly when
`lambda=(2 pi n-theta)/L`; `U_t xi(u)=xi(u-t)` then gives the Fourier
eigenvalue `fhat(lambda)`.  Scaled Poisson summation under the frozen inverse
Fourier convention produces the positive return phase.  The non-even shifted
Gaussian makes the sign identifiable rather than symmetry-blind.  Across the
12 nonzero-`theta` cases, the wrong minus-phase residual is at least
`0.057875408571292516`, while the correct-pair absolute residual never exceeds
`4.847302891456678e-16`.  The designated `r=1, theta=pi/2` phase has positive
imaginary part `+1`.

The Gaussian is consistently typed as a Schwartz convention control, not as
a numerical proof of the compactly supported P8-3 theorem.  No generated
field promotes it beyond that role.

### 4.2 Finite-grid cancellation and trace scales

All 75 finite-grid rows satisfy the exact modular rule

```text
(1/N) sum_(j=0)^(N-1) exp(2 pi i r j/N) = 1  iff N divides r,
                                             0  otherwise.
```

The `phase_sign` field is `+` in every row.  The floating regression is
consistent with the exact classification, but the exact modular field—not
the floating residual—is correctly used as the cancellation authority.

All four scale rows satisfy, with zero recorded residual,

```text
regular_length = L * regular_probability,
trivial_length = L * trivial_probability.
```

The zero-only bump exposes `L f(0)` and has no positive or negative return;
the positive-only bump excludes zero and negative time; the two-sided controls
separate the identity-time regular owner from the full trivial-character
ledger.  Thus no independent post-result rescaling or silent zero-time
deletion is present.

### 4.3 Finite rank-one corner and `L-infinity` boundary

For the peak indices `1,2,4,8,16,32,64`, the table is consistent with the
decreasing continuous circle peaks

```text
g_n(theta)=max(1-n*d_T(theta,0),0).
```

At normalized dual Haar scale, these have point value `1`, support probability
`1/(pi n)`, and integral `1/(2 pi n)`.  The seven rows reproduce those exact
formulas to the printed precision, the integrals decrease strictly, the
pointwise infimum at zero remains `1`, and the order infimum in the Haar
`L-infinity` quotient is the zero class.  Every row says
`corner_is_central=false` and `fixed_map_still_required=true`.

The separate two-row representative table correctly shows that the literal
zero function and a singleton spike have the same zero `L-infinity` class and
Haar integral but different point values.  It therefore witnesses why point
evaluation is not well-defined on the regular measurable quotient.  Neither
table claims to prove the image of `p`, existence of a singular state, the
normal-extension theorem, or packet transport; those proof obligations remain
visible in the READMEs and manifest.

### 4.4 Clock, copy, transverse, and domain controls

- All four clock systems use positive, fixed, target-free inputs and record
  `fitting_used=false`.
- The copied `L=1.1` system is exactly additive: its threefold ledger equals
  three times the single-clock reference with zero residual.
- Arbitrary clocks compile the same analytic ledger, while the composite
  augmentation explicitly records that rational-prime provenance fails.
- Each transverse model has exact total mass one.  Its time-only value is
  unchanged with zero residual, while the three non-singleton observable
  expectations are the distinct exact values `2/3`, `1`, and `4/3`.
  `full_trace_selected_canonically=false` and
  `packet_measure_theorem_claimed=false` occur in every row.
- The local two-sided, finite-prime positive, and all-prime positive-time
  scalar domains remain three separate rows.  Every row records
  `global_operator_asserted=false` and `cstar_trace_asserted=false`.  The
  all-prime row is locally finite on support `(0.25,4.75)`, has 30 contributing
  prime components and 40 return terms, and explicitly remains a scalar
  distribution rather than an all-prime operator.

These controls falsify arithmetic uniqueness of the analytic mechanism and
full-trace uniqueness under transverse choices.  They do not falsify the
source-owned statement that the actual prime clocks are `log p`; the output
keeps that provenance distinction explicit.

## 5. Integrity and overclaim scan

Source inspection found only Python standard-library imports and shell/Python
execution local to the Paper-8 package.  There is no network call, random
generator, external dataset, Riemann-zero ordinate, target Euler comparison,
parameter optimizer, fitted phase, fitted clock, fitted transverse measure,
determinant computation, or Route evaluator.  Prime labels and `log p` values
appear only as frozen source-clock/reference inputs and in the target-free
clock/domain controls.

The generated fields that state `PASS`, `true`, or `false` were checked against
the implementation and their relevant mathematical invariants rather than
accepted as self-authenticating metadata.  The manifest's interpretation
boundary is accurate: the package supplies deterministic convention,
falsification, and domain-regression witnesses, not proofs of P8-1--P8-9,
packet LCH topology, the regular von Neumann decomposition, trace
semifiniteness, no-normal-extension, packet transport, source-selected mass,
or any Route result.

No theorem overclaim was found in `code/`, `experiments/`, or `results/`.

## 6. Findings by severity

### Critical

**None.**

### Major

**None.**

### Minor m1 — orphan CPython bytecode is present in the release subtree

**Location.** `papers/8-isotropy-trace/code/__pycache__/`

| Orphan file | Observed SHA-256 |
|---|---|
| `isotropy_trace_controls.cpython-310.pyc` | `dcb1a445142be47c4deb435cf3c6231a629b10921f7915e88f9009247a8dc4a5` |
| `test_isotropy_trace_controls.cpython-310.pyc` | `75b1c158ad450a0a7b37d350ff7e8b228273ec894e9b7d0d47e30ff46b875fe3` |

Both files use CPython's timestamp-based header.  Their embedded source epochs
and sizes are respectively `(1786695544, 39327)` and `(1786695472, 13124)`,
which exactly match the current `.py` files.  They are therefore not stale
under the timestamp/size invalidation rule.  That does not make them release
inputs: neither file is in `IMPLEMENTATION_RELATIVE_PATHS`, neither is hashed
by `isotropy_trace_manifest.json`, and no root `.gitignore` protects the
Paper-8 subtree from their accidental inclusion.

**Impact.** No mathematical or current-run reproducibility result changes.
The defect is artifact hygiene and provenance completeness: a whole-subtree
GitHub synchronization could publish untracked interpreter output whose bytes
depend on compilation path/runtime details.

**Severity.** Minor.  It does not alter a core claim, but it is a mechanical
release blocker because the requested release tree must have no orphan or
stale bytecode.

**Required fix.** Remove exactly `code/__pycache__/` before synchronization;
do not add the `.pyc` files to the manifest.  Then rerun the reproduction
script with `PYTHONDONTWRITEBYTECODE=1` and confirm that no `__pycache__`,
`*.pyc`, `*.pyo`, backup, or temporary artifact exists under `code/`,
`experiments/`, or `results/`.

## 7. Release conditions

The controls review may be mechanically promoted to an unconditional PASS
when all of the following are true on the exact release snapshot:

1. `papers/8-isotropy-trace/code/__pycache__/` and its two `.pyc` files are
   absent;
2. the forbidden-artifact scan over `code/`, `experiments/`, and `results/`
   is empty;
3. `./experiments/reproduce.sh` again reports 18/18 tests, manifest/lock/
   implementation verification PASS, and two byte-identical fresh
   generations; and
4. the protected active-tuple, six implementation, nine CSV, and manifest
   hashes above remain unchanged, unless a separately reviewed intentional
   source edit creates a new complete lock.

Because `.pyc` files are deliberately outside the implementation ledger,
closing `m1` should not alter any protected hash.  No scientific-code or
result correction is requested by this audit.

## 8. Narrow closure and exact-byte re-lock

Closure date: **2026-08-14 (Asia/Shanghai)**  
Closure scope: Minor finding `m1` only  
Pre-closure report SHA-256:
`35bf1e6c76e6c5a44b3e4537886f28f6759279a484b7a50a75cbebc83aa2bf4b`

The two orphan bytecode files and their containing `code/__pycache__/`
directory were moved, without changing a protected file, to the recoverable
temporary location
`/tmp/paper8-pycache-trash.9b3Pec/__pycache__/`.  This addendum records the
independent verification of that mechanical remediation; it does not treat
the temporary copy as a Paper-8 release input.

I independently repeated all four release conditions in Section 7:

1. recursive scans of `code/`, `experiments/`, and `results/` found no
   `__pycache__` directory and no `*.pyc`, `*.pyo`, `*~`, or `*.tmp` file;
2. `./experiments/reproduce.sh` passed all 18 unit tests, regenerated all nine
   CSV artifacts, verified the manifest, active tuple, and implementation
   hashes, and compared both fresh temporary generations byte for byte;
3. the manifest remained
   `20801ebe4c927f939c462842e38569555f96f5fef78859755b6caa8cbcf38b07`;
   and
4. complete protected-hash inventories captured immediately before and after
   the closure rerun were byte-identical.

The exact active tuple remains:

```text
research_protocol.md       e1149ebd9609de24e0df00dcaeafdbcd31ee973e8ebe04b15cf86541f8084535
candidate_lock.md          8a5a460bac51843e532c9894fcb99470247c7de7833449c3660813ccd183d64e
phase2_domain_amendment.md 412e6d24c43ab5a995d135c6ecb207f5225414fac223fcf63080486af6fc3de3
```

The six implementation hashes and all nine CSV hashes remain exactly those
listed in Sections 2 and 4.  No code, test, README, experiment script, result,
protocol, candidate lock, or typed amendment changed during closure.

**Finding status:** `m1` **CLOSED**.  The original finding remains above as the
audit trail; its release hold is superseded by this exact-byte closure.

**Final controls verdict: PASS.**  Open Critical findings: 0.  Open Major
findings: 0.  Open Minor findings: 0.  The deterministic controls package is
release-clean within the audited `code/` / `experiments/` / `results/` scope.
