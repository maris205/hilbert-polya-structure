# Paper improvement log — C122

No external reviewer, acceptance prediction, or numeric review score was used.

## Round 0

The baseline derivation recorded the inverse and two-cycle but did not separate
the parameter contraction from the state-feedback gain.

## Round 1

Added the uniqueness calculation for gain `3`, offset `-1/2`, and the gain-zero
control.  The monodromy order was made explicitly chronological.

## Round 2

Added the neighboring gain `5/2` residual, exact scope labels, reproducibility
commands, and all nonclaims.  Both internal semantic passes preceded the final
release compile; the round-named release snapshots may therefore be
byte-identical and are not presented as an external-review history.
