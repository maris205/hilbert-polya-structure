---
name: route-b-evaluator
description: Audit a proposed Hilbert–Pólya operator, self-adjointness, arithmetic trace, or completed-xi determinant through Route B. Supports a requested limited early audit; not generic operator theory or routine paper work.
---

# Route B evaluator

Determine whether the user requests a formal Route B evaluation or a limited early question. Read [the rubric and schema](references/rubric.md) in full for either; its full-entry requirements apply to formal scoring, not to answering whether a missing operator construction might exist.

Formal scoring normally starts from `ROUTE_A_SUCCESS_ROUTE_B_READY`. If it is absent, report that limitation without using Route B to rescue an arithmetic fit. A user-requested limited audit may examine a natural Hilbert space, quantization, domain obstruction, or trace framework before full readiness. Answer that question, list open obligations, and do not award a layer PASS or full realization from partial inputs.

Keep the arithmetic, orbit, operator, domain, clock, trace and determinant in one compatible construction. Do not infer self-adjointness from symmetry, PT symmetry, real finite spectra or GUE statistics. Preserve the rubric's exact conditions for a Hilbert–Pólya realization, including the global divisor and exclusion of missing/extra zeros.

The warning about symmetry concerns insufficient assumptions: a real symmetric finite matrix on the standard full finite-dimensional domain is self-adjoint, but is not an infinite-dimensional arithmetic realization. Missing formal inputs support `ROUTE_B_NOT_TESTABLE`; separately report any failure already implied by the supplied construction. Unassessed fields may be `null`; never fill them with invented evidence.

Read the latest relevant Route A result if available, the proposed object, and the specific proof dependencies. Consult prior-work indexes and exact sources as needed rather than loading the archive. Verify literature benchmarks before use; a suggested Weil-form example is not an extra universal gate.

Bind inputs with existing locks or relevant hashes; commit fields may be `null` with a non-Git explanation. Use the v0.2.0 YAML schema for formal scoring; a scoped answer may be concise and state unavailable information without inventing it.

When saving is part of the requested work, write a new evaluation under `evaluations/route_b/<candidate_id>/` and update only changed candidate, obstruction or operator-obligation entries. Preserve previous reports. Review-only requests do not authorize experiments or registry writes.

User instructions take precedence over skill workflow guidance; claims still require the stated proof. If a skill instruction causes a pause, identify it and explain the concrete missing input or authority. Keep a cross-family idea as a clue and continue authorized in-family work.
