# Hostile audit

## Model confusion

The primary adversarial risk is replacing fatal collision attempts by rejected
moves.  That changes diagonal `-2k` to minus legal degree and produces a
reflecting exclusion chain.  Both theorem and checker freeze the former; a
model mutation is killed.

## Spectral and boundary attacks

Attacks alter the energy formula, Slater ground mode, trace, positivity,
normalization, gap, or full-occupancy null field.  Coordinate bool/float
aliases and appended states/cases are rejected.  Direct diagonalization of an
independently built integer generator prevents a producer/checker shared
spectral shortcut.

## Absorption and conditioning attacks

Mutated survival values, densities, time coordinates, QSD text, probe counts,
and detailed-balance residuals fail.  The paper separately checks that the
spectral coefficient signs need not be positive and does not promote the
finite sum to a simpler first-passage closed form.

## Serialization and provenance

Canonical JSON rejects duplicate keys, NaN, trailing objects, compact
reserialization, invalid UTF-8, and top-level lists.  Strict YAML rejects
duplicate/non-string keys, anchors, aliases, and merge keys.  Semantic JSON
mutations are rehashed before checking, while a separate stale-hash mutation
verifies binding.  The checker explicitly refuses `python -O`.

## Route and scope

The A4 entry is only `A4_FORMAL_HINT`; changing it to failure or pass is
rejected because both would misstate the frozen classification.  Overall
Route A remains rejected, Route B remains false, and all target-arithmetic
claim flags remain false.
