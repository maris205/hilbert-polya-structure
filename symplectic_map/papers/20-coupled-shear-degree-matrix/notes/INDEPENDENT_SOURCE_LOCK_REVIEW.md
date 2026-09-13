# Paper20 — Independent Source-Lock Review

Date: 2026-08-22 UTC

Project: `papers/20-coupled-shear-degree-matrix`

Role: independent source-lock auditor; read-only over all bound inputs

## Scope and authority boundary

This review reads `experiments/source_lock.json`, the ten bound author files,
and the excluded design-review artifact to EOF. No bound input was modified.
The only post-stop write is this reviewer-owned note, at the sole path allowed
by the lock's passing-review contract. This note is not part of the ten-file
author aggregate, the lock's source preimage, or any downstream publication
scope.

The lock remains a source/inventory gate. It does not authorize a manuscript,
paper plan, experiment, numerical or CAS run, code, build, transport, upload,
release, or priority claim.

## Lock identity and canonical JSON

The frozen lock is the regular 0644 file
`experiments/source_lock.json`, with:

- bytes: **11,847**;
- exactly one terminal LF (no CR, NUL, or BOM);
- SHA-256: `57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581`.

I parsed it with duplicate-key rejection and nonfinite-number rejection, then
recursively serialized string keys in Unicode code-point order with compact
JSON separators, UTF-8, and one LF. The canonical serialization is byte-exact
and has the same 11,847-byte SHA. The object has 23 unique top-level keys;
there are no duplicate keys, NaN/Infinity values, or unresolved JSON syntax.

The self-identity contract is correctly null and excluded:

```json
{"bytes":null,"path":"experiments/source_lock.json","self_excluded":true,"sha256":null}
```

The lock's own SHA and byte count occur zero times in its content, and
`author_aggregate.source_lock_included` is `false`.

## Author aggregate and file bindings

The declared ten-file allowlist is sorted, unique, and exactly equal to the
actual non-lock, non-reviewer source set. Every declared path, byte count, LF
count, and SHA-256 matches an independent read. Reapplying the declared
framing

`uint64_be(name_byte_length) || name_utf8 || uint64_be(content_byte_length) || content_bytes`

over byte-sorted relative POSIX names gives, independently:

- file count: **10**;
- total bytes: **45,416**;
- total LF: **873**;
- aggregate SHA-256:
  `3b27fe493832559e90ac5dcb059628492074574fe9492d12e500f7da107f7e90`.

The lock correctly excludes `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` from
that aggregate and binds it separately as provenance:

- bytes: 9,484;
- LF: 213;
- SHA-256:
  `c4f456c8d9aee5ac9364abf91dc140e9a0261b09cf1922491a773e8c7d87f2c5`;
- verdict: `SOURCE_DESIGN_PASS`;
- included in author aggregate: `false`.

The second reviewer is represented only by an out-of-band collaboration
receipt with null artifact identity, not by an invented local file or source
bytes. `source_lock.json` is likewise excluded from the author aggregate.

## Inventory and absence checks

At the author stop, the inventory counts are coherent: 11 regular project files
(the ten author files plus the design-review note), then 12 after adding the
source lock. The declared source-lock review path was absent at author stop.
There are no symlinks and no files or directories under the forbidden
`code`, `data`, `figures`, `manuscript`, `paper`, `results`, `transport`, or
`build` namespaces. The lock review note is the only expected post-stop
addition and is out of band.

The allowlist includes no reviewer note, source lock, PDF, TeX, transport, or
build artifact. Its path base and relative POSIX framing agree with the actual
project tree.

## Frozen theorem and proof contract

The lock's theorem object matches the bound source files and the independent
source-design review. Its literal scope is algebraically closed characteristic
zero, integer (g\ge5), the fixed four-dimensional word

\[
V=q_1^2q_2^2+q_1^g,\qquad W=p_1^2p_2^2+p_2^g,
\]

with (F_g=T_g\circ S_g), triangular symplectic inverses, the two phase rows

\[
A_g=\begin{pmatrix}g-1&0\\2&1\end{pmatrix},\qquad
B_g=\begin{pmatrix}1&2\\0&g-1\end{pmatrix},
\]

and complete-step matrix

\[
C_g=B_gA_g=\begin{pmatrix}g+3&2\\2(g-1)&g-1\end{pmatrix}.
\]

The frozen identities are the half-open cone selector, the phase recurrence
`v_(n+1)=A_g*u_n`, `u_(n+1)=C_g*u_n`,
`deg(F_g^n)=e_2^T C_g^n (1,1)^T`, and
`lambda_1(F_g)=rho(C_g)=(sqrt(g)+1)^2`, with the strict comparison to
`(g-1)^2`. The seven proof-contract lemmas cover symplecticity, both literal
selectors, cone invariance, no cancellation, visibility, and the Perron
calculation. `generic_newton_fan_claim` and all broader substitutions are
explicitly false.

## Citation, collision, and anti-claim locks

The citation lock binds `notes/CITATION_VERIFICATION.md` by its declared hash,
allows six primary sources plus one survey only for bounded context, forbids
using them as proof of the recurrence or symplecticity, and sets
`priority_claim_authorized=false` and `remote_bytes_binding=false`. The eight
P12–P19 collision rows are explicitly bounded `EMPTY` comparisons; the lock
also states that this is not an exhaustive priority search and leaves priority
unauthorized.

The anti-claim lock forbids arbitrary supports/words or coefficients, positive
characteristic, generic finite-fan or all-symplectic-map claims, entropy and
periodic/trace/torus claims, universal product non-conjugacy, numerical/CAS
proof certificates, and absolute novelty. Its seven selector, phase, leading
coefficient, visibility, coupling, and citation STOP rules agree with the
proof package.

## Permissions, zero-science, and downstream authority

All execution and downstream permissions are closed: build, code, manuscript,
paper plan, publication, experiment, CAS/symbolic execution, transport, upload,
and scientific-experiment flags are false. Scientific counts for runs,
datasets, figures, numerical runs, CAS runs, uploads, and results are zero or
false. Lifecycle fields keep paper-plan/publication/manuscript and
transport/build unlocks false, while `next_required_verdict` is exactly
`SOURCE_LOCK_PASS`.

The lock status is `SOURCE_LOCK_AUTHOR_STOP` / pending fresh review. The
`candidate_id` is only a bounded metadata label; no candidate payload,
downstream edge, or publication authority is present. The source-lock review
contract requires a fresh reviewer who authored none of the inputs, exact
rehashing, theorem/collision/citation/permission replay, inventory and
self-null checks, and names this note as the sole passing write path. All of
those checks pass.

SOURCE_LOCK_PASS
