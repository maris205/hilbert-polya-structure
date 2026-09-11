# P206 root's actual adverse-review replay pair

Executed 2026-09-06 UTC from the workspace root. Two separate physical
`python -B docs/papers204_208_sequence/reviews/p206_a/verify.py` producers
wrote `run1.stdout` and `run2.stdout` in this directory. Each exited zero;
each complete raw-byte comparison with the review's `CANONICAL.json`
exited zero. Each run computed 3,698,764 assertions. Both stderr files
are empty. These are new root executions, not relabelled reviewer runs.

Producer SHA-256:
`45fd54e08d271b2befdf53cbe2a11b8dc29cb7f3dd3ac24b39bfd353c31fc673`.

Canonical and both complete stdout SHA-256:
`6fee8997d694fd428b7b5d4594af57b72e44fbc1aa86bdbec4f702fc6b5dc8d9`.

Complete 23-entry review input pins, six-entry supplementary pins and
54-entry nonself package manifest passed. The original 22-file Round0
freeze remains unchanged. Successful mathematical/evidence checks do not
close the critical value finding or constitute an accepted delta.
