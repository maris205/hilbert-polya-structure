# Eleventh lane: closed without promotion

2026-09-06 UTC. **NO_PROMOTION / NO_ADMISSION / ZERO_RESERVES**.
Owner/proof contributor: `batch197_fosp_gate`.

Six desk proposals span four carriers, but four were excluded before
execution. Only **two literal rules on two carriers** were actually
piloted: WZS signed Walsh-zero feedback and ACP anchored critical-value
polynomials. The parent's permission to execute fewer nonduplicate slots
was used; this is not counted as six fresh attempts or three executed
carriers. HEP/BPF have direct or exact-factor primary-source collisions;
GFC/CRS are already occupied historical proposals/rules.

## Executed original boxes and outcome

| Rule | Original fixed full boxes | Finite result and disposition |
|---|---|---|
| WZS | Every subset of `F_2^d`, `d=0,1,2,3,4`; 65,814 states | At `d=4`: 1,027 images; 3 fixed points and 17 two-cycles; maximum tail 4; maximum fibre 33,664, uniquely at the empty target. The extra recurrent states are explained by a deducted orthogonal-complement subspace family. No all-d global recurrence/height or full-target inverse/extremal theorem. **NO_PROMOTION**. |
| ACP | All monic coefficient vectors at `(degree,prime)=(2,3),(2,5),(2,7),(2,11),(3,5),(3,7),(4,5)`; 1,297 states | Genuine four-cycles already at quadratic prime 11, including an off-anchor-zero cycle; cubic prime 7 and quartic prime 5 have tail 10. Quadratic every-target inverse and sharp fibre maximum are completely derived, but are elementary Vieta/square-character content. No full-carrier all-parameter temporal proof. **NO_PROMOTION**. |

No box was enlarged or added, no sampling replaced a full box, and no
literal was repaired after seeing its output. No candidate was numbered.

## Complete proof deductions and missing claims

The [proof/disposition note](PROOF_AND_DISPOSITION.md) is the controlling
mathematical original. It gives:

- WZS complement invariance, odd-weight forcing, exact small boundary
  dimensions, every affine-subspace image, and the interior-dimensional
  complementary-subspace fixed/two-cycle family. These use classical
  character orthogonality and polarity; they do not establish global
  convergence to that family.
- ACP quotient-algebra/resultant correctness including repeated and
  nonsplit critical points. For every odd prime its quadratic inverse is
  exactly two anchor-root square tests. The sharp maximum is two for
  `p=3 mod 4` and four for `p=1 mod 4`, with complete image/fibre census.
  The invariant zero-anchor line is ordinary field squaring. An explicit
  off-line four-cycle prevents a false universal collapse claim.
- Desk-only BPF strict-half normalization adapter to known Banzhaf
  reweighting, plus the generic squared-norm ascent proof for convergence.
  No BPF experiment or fresh value claim is attached to that deduction.

All-parameter proofs above are limited to their stated narrower claims.
No statement that WZS always has eventual period at most two, height d,
or the empty fibre as unique maximum is proved. No all-prime ACP full
orbit atlas is proved. These omissions are the rejection reasons, not
tasks silently converted to PASS. The two-cycle/four-cycle witnesses and
unproductive proof directions remain preserved.

## Actual execution evidence

[INTAKE.md](INTAKE.md) was written and SHA-pinned before pilot code and
before either execution. Its hash is
`ca2e42c1e41e722bc1bbaf545c15b4bae2a0e10dd308403e1587e9c0e01e7efd`.
[pilot.py](pilot.py) is standard-library-only and imports no old science.
[record.py](record.py) created separate immutable fresh execution folders.

| Execution | Actual UTC interval | Result |
|---|---|---|
| [01](execution_01/EXECUTION.json) | 09:22:49.628475--09:22:50.566685 | Child exit 0, empty stderr; three frozen input pins unchanged. |
| [02](execution_02/EXECUTION.json) | 09:22:56.198659--09:22:57.136486 | Child exit 0, empty stderr; three frozen input pins unchanged; actual raw `cmp` against 01 exit 0, empty comparison outputs. |

Each run covers **12 boxes, 67,111 states and 340,299 assertions**.
One provisional chat handoff mis-added the state total as 67,211 and
explicitly marked it pending audit; the immediately following correction
gave 67,111 = 65,814 + 1,297. The canonical outputs never contained that
typo and were not modified. This line preserves the communication error.
Complete stdout is 6,667 bytes with SHA-256
`5fbcc7276ee6a3ab7335339315d0e829da88d7da3cc789f6452745e5a41cdb89`.
It records all-cycle and depth/fibre histograms, transition-index digest,
explicit maximum-height orbits, longest-cycle witnesses and the first
maximum-fibre target. The byte-identical stdout is complete process
output; the digest of transitions is not mislabelled as a stored complete
transition table. Both [first](execution_01/stdout.jsonl) and
[second](execution_02/stdout.jsonl) raw outputs remain available.

The archived pair ran the direct-versus-butterfly Walsh comparison and
Parseval on every Boolean state, coefficient-level determinant checks
on ACP and the quadratic formula/every-target inverse on all four
quadratic boxes. The later closed deduction formulas were not given a
new theorem-check execution; no such execution is claimed.

## Source, audit and scope boundary

The [source/collision report](SOURCE_AND_COLLISION.md) records primary
body scopes, direct access failures, source-domain restrictions and
explicit adapters. The novelty-check skill's dedicated external review
interface is unavailable; no Phase C review or source/value PASS exists.
The project skill's rejection gate prevented a larger pilot or paper draft.
All work remains author-level and HOLD_EXTERNAL.

[check_package.py](check_package.py) verifies archived execution records,
byte comparisons, exact original box census, input pins, contextual
historical pins, all local Markdown links and complete nonself manifest.
This is an artifact audit, not a fresh mathematical execution or
independent manuscript review. `SHA256SUMS` covers every local file other
than itself; `CONTEXT_INPUTS.sha256` uses workspace-root-relative paths.

Only `scouting/finite_systems_eleventh/` was written. Tenth/OFS, P207,
central state, old manuscripts/reviews/frozen evidence and Git were not
modified. This lane is closed; no successor scope is assumed.
