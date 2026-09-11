# Auxiliary receiver count clarification

The immutable RESULT.json reports whole_workspace_record_files=33. The
receiver computes that field before reading its own final source pin, so
the complete INPUTS.json includes 34 files: those 33 records plus the full
18,200-byte receive_phase.js. This is an auxiliary counter-label defect,
not a missing input or a changed scientific/native result. Root uses the
actual complete 34-row input set for closure and states that count explicitly.
The original result/source/native output are preserved without correction.
This receiver's same field must be interpreted at its pre-final-self point
if used for later phases; it is not an exact final input-census assertion.
