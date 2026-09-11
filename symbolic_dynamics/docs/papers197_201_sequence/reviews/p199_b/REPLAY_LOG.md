# P199 B fresh replay log

The final standalone endpoint verifier was first development-tested, then
run in two further fresh processes. Neither author nor A code is imported.

## Replay 1

`python3 -B docs/papers197_201_sequence/reviews/p199_b/verify_intervals.py`
exited zero. Its full stdout was captured and stored as CANONICAL.txt using
apply_patch. It contains 1,026,386 assertions, status=PASS, and explicit
critical/major/minor zero counts. This is the actual emitted output.

## Replay 2

```sh
set -o pipefail
python3 -B docs/papers197_201_sequence/reviews/p199_b/verify_intervals.py | cmp - docs/papers197_201_sequence/reviews/p199_b/CANONICAL.txt
```

The second fresh run and byte comparison exited zero. Both final runs
therefore match the complete canonical transcript, whose SHA256 is
b17db9368a6525af6d654cc40f4ab01dfaec34aee12f54d0562ff6fd94c7a89a.
Verifier SHA256 is
bea975860d99179872cbd210b71cde3589fde67b46358a58112ecc99dc04ef4f.
An additional terminal replay remains a separate batch action; these
repeatability checks are not extra independent experiments.
